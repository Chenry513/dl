# dl_tools_full


## first version


Web application (using Python Django library for the backend and Vue for the frontend) that lets users create an account (mock this for now -- to be added later).

The web app's homepage is a dashboard that displays known information about
AI models and their training data sources.

This dashboard should aim to concisely communicate model operating organization, use cases, and the practices of the operating organization.

Users can "save" specific preferences about models. For instance, they might save information that they do not want to support model X, or that they do want to support model Y. These preferences might later include conditional logic like,
"will only provide data if policy changes" or "will only provide data if paid z rate"

The interface of the web app should be modern.

In addition to a dashboard, there should also be pages (linked in navigation bar) for "search" and "profile".


## Updated Version (Current Pivot)
Change the platform to focus on making LLM information accessible to non-technical users by:

1. **Explaining Data Usage**: Clear breakdowns of how different LLMs use personal data
2. **Model Recommendations**: Helping users identify which models best fit their specific needs
3. **Transparency Features**: Disclosing training data sources and organizational practices

### The Markdown-to-Django Solution
To achieve these goals, we developed an automated Markdown processing system that:

- Allows users contribute through simple Markdown files
- Maintains schema validation 
- Serves as a reusable tool for other Django projects

This system solves two key problems:
1. **For Data Levers**: Allows easy expansion of model information while maintaining data integrity
2. **For Other Projects**: Provides a solution for Markdown-based content management

### Content Pipeline Implementation

1. **Content Creation**:
   - Users can add model information using simple Markdown files
   - Files follow standardized templates with a require schema to follow

2. **Automated Processing**:
   ```mermaid
   graph LR
       A[Markdown File] -->|GitHub Push| B(Linter Check)
       B --> C{Valid?}
       C -->|Yes| D[Convert to Django Models]
       C -->|No| E[Flag Errors]
       D --> F[Update Production Database]
   ```
   
   

