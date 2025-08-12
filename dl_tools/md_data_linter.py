#!/usr/bin/env python3
"""
md-data-lint: A linter for validating Markdown files used as structured data.

This script validates Markdown files with frontmatter against a defined schema,
ensuring they can be used consistently as a data backend for static sites,
databases, or other applications.
"""

import os
import re
import json
import argparse
import glob
import datetime
from typing import Dict, List, Any, Set, Optional, Tuple
import yaml
from pydantic import BaseModel, ValidationError, create_model, Field
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

# Regular expression to extract frontmatter from Markdown files
FRONTMATTER_REGEX = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

class SchemaDefinition(BaseModel):
    """Represents a schema definition for Markdown frontmatter."""
    name: str
    description: str
    fields: Dict[str, Dict[str, Any]]
    required: List[str] = []
    category_field: Optional[str] = None
    subdirectory: Optional[str] = None

class ValidationResult:
    """Represents the result of validating a Markdown file."""
    def __init__(self, file_path: str, schema_name: str):
        self.file_path = file_path
        self.schema_name = schema_name
        self.errors: List[str] = []
        self.warnings: List[str] = []
    
    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0

class MdDataLint:
    """Main class for the Markdown data linter."""
    
    def __init__(self, schema_path: str):
        """Initialize the linter with a schema file."""
        self.schemas: Dict[str, SchemaDefinition] = {}
        self.load_schema(schema_path)
        self.validation_models: Dict[str, Any] = {}
        self._create_validation_models()
    
    def load_schema(self, schema_path: str) -> None:
        """Load schema definitions from a JSON file."""
        try:
            with open(schema_path, 'r') as f:
                schema_data = json.load(f)
            
            # Parse schemas
            for schema_def in schema_data.get('schemas', []):
                schema = SchemaDefinition(**schema_def)
                self.schemas[schema.name] = schema
                
            console.print(f"Loaded {len(self.schemas)} schema definitions from {schema_path}")
        except Exception as e:
            console.print(f"[bold red]Error loading schema:[/bold red] {str(e)}")
            raise
    
    def _create_validation_models(self) -> None:
        """Create Pydantic models for validating frontmatter against schemas."""
        for name, schema in self.schemas.items():
            field_definitions = {}
            
            for field_name, field_def in schema.fields.items():
                field_type = self._get_python_type(field_def.get('type', 'string'))
                
                # Set up field parameters
                field_params = {}
                if field_name in schema.required:
                    field_params['default'] = ...  # This makes the field required
                else:
                    field_params['default'] = None
                
                # Add description if available
                if 'description' in field_def:
                    field_params['description'] = field_def['description']
                
                # Add other validations based on field_def
                if 'enum' in field_def:
                    field_params['enum'] = field_def['enum']
                
                # Create the field
                field_definitions[field_name] = (field_type, Field(**field_params))
            
            # Create the dynamic model for this schema
            self.validation_models[name] = create_model(
                f"{name}Model",
                **field_definitions
            )
    
    def _get_python_type(self, type_name: str) -> Any:
        """Convert schema type to Python type."""
        type_mapping = {
            'string': str,
            'number': float,
            'integer': int,
            'boolean': bool,
            'array': List[str],
            'object': Dict[str, Any],
            'date': datetime.date
        }
        
        if type_name in type_mapping:
            return type_mapping[type_name]
        
        # Default to string for unknown types
        return str
    
    def validate_file(self, file_path: str) -> Optional[ValidationResult]:
        """Validate a single Markdown file against appropriate schema."""
        try:
            # Determine which schema to use
            schema_name = self._determine_schema_for_file(file_path)
            if not schema_name:
                return None
            
            result = ValidationResult(file_path, schema_name)
            
            # Extract frontmatter
            frontmatter = self._extract_frontmatter(file_path)
            if not frontmatter:
                result.errors.append("No frontmatter found")
                return result
            
            # Parse frontmatter as YAML
            try:
                data = yaml.safe_load(frontmatter)
                if not isinstance(data, dict):
                    result.errors.append("Frontmatter is not a valid YAML object")
                    return result
            except yaml.YAMLError as e:
                result.errors.append(f"YAML parsing error: {str(e)}")
                return result
            
            # Validate against schema
            schema = self.schemas[schema_name]
            
            # Check for required fields
            for field in schema.required:
                if field not in data:
                    result.errors.append(f"Missing required field: '{field}'")
            
            # Check for unknown fields
            known_fields = set(schema.fields.keys())
            for field in data.keys():
                if field not in known_fields:
                    result.warnings.append(f"Unknown field: '{field}'")
            
            # Validate with Pydantic model
            try:
                self.validation_models[schema_name](**data)
            except ValidationError as e:
                for error in e.errors():
                    field = ".".join(str(loc) for loc in error["loc"])
                    result.errors.append(f"Field '{field}': {error['msg']}")
            
            return result
        
        except Exception as e:
            console.print(f"[bold red]Error validating {file_path}:[/bold red] {str(e)}")
            raise
    
    def _determine_schema_for_file(self, file_path: str) -> Optional[str]:
        """Determine which schema should be used for a file based on its path."""
        # First check subdirectory-based schemas
        rel_path = os.path.normpath(file_path)
        for name, schema in self.schemas.items():
            if schema.subdirectory:
                if schema.subdirectory in rel_path.split(os.sep):
                    return name
        
        # If no subdirectory match, check frontmatter for a type/category field
        frontmatter = self._extract_frontmatter(file_path)
        if frontmatter:
            try:
                data = yaml.safe_load(frontmatter)
                if isinstance(data, dict):
                    # Check if any schema's category_field matches
                    for name, schema in self.schemas.items():
                        if schema.category_field and schema.category_field in data:
                            if data[schema.category_field] == name:
                                return name
            except yaml.YAMLError:
                pass
        
        # If only one schema is defined, use that
        if len(self.schemas) == 1:
            return next(iter(self.schemas.keys()))
        
        return None
    
    def _extract_frontmatter(self, file_path: str) -> Optional[str]:
        """Extract frontmatter from a Markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            match = FRONTMATTER_REGEX.search(content)
            if match:
                return match.group(1)
            return None
        except Exception as e:
            console.print(f"[bold red]Error reading {file_path}:[/bold red] {str(e)}")
            return None
    
    def validate_directory(self, directory: str, patterns: List[str] = None) -> List[ValidationResult]:
        """Validate all Markdown files in a directory."""
        if patterns is None:
            patterns = ['**/*.md']
        
        results = []
        file_paths = set()
        
        for pattern in patterns:
            glob_pattern = os.path.join(directory, pattern)
            matching_files = glob.glob(glob_pattern, recursive=True)
            file_paths.update(matching_files)
        
        for file_path in sorted(file_paths):
            result = self.validate_file(file_path)
            if result:
                results.append(result)
        
        return results
    
    def print_summary(self, results: List[ValidationResult]) -> None:
        """Print a summary of validation results."""
        valid_count = sum(1 for r in results if r.is_valid)
        invalid_count = len(results) - valid_count
        
        console.print()
        console.print(f"[bold]Validation Summary:[/bold]")
        console.print(f"- Total files: {len(results)}")
        console.print(f"- Valid files: [green]{valid_count}[/green]")
        
        if invalid_count > 0:
            console.print(f"- Invalid files: [red]{invalid_count}[/red]")
        else:
            console.print(f"- Invalid files: {invalid_count}")
        
        # Print per-schema statistics
        schema_stats = {}
        for result in results:
            schema_name = result.schema_name
            if schema_name not in schema_stats:
                schema_stats[schema_name] = {'total': 0, 'valid': 0, 'invalid': 0}
            
            schema_stats[schema_name]['total'] += 1
            if result.is_valid:
                schema_stats[schema_name]['valid'] += 1
            else:
                schema_stats[schema_name]['invalid'] += 1
        
        console.print()
        console.print("[bold]Results by Schema:[/bold]")
        
        table = Table(show_header=True, header_style="bold", box=box.SIMPLE)
        table.add_column("Schema")
        table.add_column("Total", justify="right")
        table.add_column("Valid", justify="right")
        table.add_column("Invalid", justify="right")
        
        for schema_name, stats in schema_stats.items():
            table.add_row(
                schema_name,
                str(stats['total']),
                f"[green]{stats['valid']}[/green]",
                f"[red]{stats['invalid']}[/red]" if stats['invalid'] > 0 else "0"
            )
        
        console.print(table)
        
        # Print errors and warnings
        if invalid_count > 0:
            console.print()
            console.print("[bold red]Errors:[/bold red]")
            
            for result in results:
                if not result.is_valid:
                    rel_path = os.path.relpath(result.file_path)
                    console.print(f"[bold]{rel_path}[/bold] (schema: {result.schema_name}):")
                    for error in result.errors:
                        console.print(f"  - {error}")
        
        # Print warnings
        warning_results = [r for r in results if r.warnings]
        if warning_results:
            console.print()
            console.print("[bold yellow]Warnings:[/bold yellow]")
            
            for result in warning_results:
                rel_path = os.path.relpath(result.file_path)
                console.print(f"[bold]{rel_path}[/bold] (schema: {result.schema_name}):")
                for warning in result.warnings:
                    console.print(f"  - {warning}")

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Lint Markdown files against a schema')
    parser.add_argument('directory', help='Directory containing Markdown files')
    parser.add_argument('--schema', '-s', required=True, help='Path to schema definition file (JSON)')
    parser.add_argument('--pattern', '-p', action='append', help='Glob patterns for matching files (e.g., "**/*.md")')
    
    args = parser.parse_args()
    
    try:
        linter = MdDataLint(args.schema)
        results = linter.validate_directory(args.directory, args.pattern)
        linter.print_summary(results)
        
        # Exit with non-zero status if any files are invalid
        if any(not result.is_valid for result in results):
            exit(1)
    
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()