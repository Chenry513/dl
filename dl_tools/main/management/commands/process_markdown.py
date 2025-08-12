import os
import frontmatter
from django.core.management.base import BaseCommand
from django.conf import settings
from main.models import ModelInfo
from md_data_linter import MdDataLint  # Import the linter

class Command(BaseCommand):
    help = 'Validates and processes Markdown files into ModelInfo'

    def handle(self, *args, **options):
        # Path to markdown files (should be in project root/markdown_files)
        markdown_dir = os.path.join(settings.BASE_DIR, 'markdown_files')
        os.makedirs(markdown_dir, exist_ok=True)  # Create dir if it doesn't exist

        # Path to schema (in project root - same as manage.py)
        schema_path = os.path.join(settings.BASE_DIR, 'example-schema.json')
        
        if not os.path.exists(schema_path):
            self.stdout.write(self.style.ERROR(
                f"Schema file not found at {schema_path}. "
                "Please ensure example-schema.json is in your project root."
            ))
            return

        # Step 1: Validate files
        linter = MdDataLint(schema_path)
        results = linter.validate_directory(markdown_dir)

        # Step 2: Get names of all valid files (without .md extension)
        valid_names = [os.path.basename(r.file_path)[:-3] for r in results if r.is_valid]

        # Step 3: Delete records that aren't represented in current files
        stale_records = ModelInfo.objects.exclude(name__in=valid_names)
        stale_count = stale_records.count()
        if stale_count > 0:
            stale_records.delete()
            self.stdout.write(self.style.SUCCESS(
                f"Deleted {stale_count} stale records no longer present in markdown files"
            ))

        # Step 4: Process valid files
        processed_count = 0
        for result in results:
            if result.is_valid:
                self.process_file(result.file_path)
                processed_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"Processed {processed_count}/{len(results)} valid files. "
            f"Deleted {stale_count} stale records."
        ))

    def process_file(self, filepath):
        """Process a single Markdown file into the database."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            ModelInfo.objects.update_or_create(
                name=os.path.basename(filepath)[:-3],  # Remove '.md'
                defaults={
                    'organization': post.get('organization', ''),
                    'use_cases': '\n'.join(post.get('use_cases', [])),
                    'practices': '\n'.join(post.get('practices', [])),
                    'data_info': '\n'.join(post.get('data_info', [])) or None,
                    'concerning_practices': '\n'.join(post.get('concerning_practices', [])) or None,
                    'concerning_practices_urls': ','.join(post.get('concerning_practices_urls', [])) or None,
                    'severity': post.get('severity', '').lower() or None
                }
            )
            self.stdout.write(self.style.SUCCESS(
                f"Processed {os.path.basename(filepath)}"
            ))
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f"Error processing {os.path.basename(filepath)}: {str(e)}"
            ))