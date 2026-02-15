# DL Tools - AI Model Information Platform

**Live Site:** [dl-tools.onrender.com](https://dl-tools.onrender.com)

A web platform that makes AI model information accessible to everyone. Instead of digging through technical documentation, you can browse clear, organized information about different AI models—what they do, how they use data, and who runs them.

> **Note:** The site runs on a free hosting tier, so the first visit after 15 minutes of inactivity takes about 30-60 seconds to load. After that, it's fast!

## What This Project Does

DL Tools helps non-technical users understand AI models by providing:

- **Clear Model Information**: Easy-to-read breakdowns of popular AI models (ChatGPT, Claude, Gemini, etc.)
- **Data Usage Transparency**: How each model uses your data and what their privacy policies are
- **Searchable Database**: Find models based on your specific needs or concerns
- **Community Contributions**: Anyone can help expand the library by adding new models

## How It Works

### For Users
1. **Browse Models**: Visit the dashboard to see all available AI models
2. **Search & Filter**: Find models that match your criteria
3. **Learn**: Read clear explanations of how each model works and uses data

### For Contributors
Want to add a model? Here's the simple process:

1. **Create a Markdown File**: Add a new `.md` file to the [markdown_files folder](https://github.com/Chenry513/dl/tree/main/dl_tools/markdown_files)
2. **Follow the Template**: Check `INSTRUCTIONS.md` for the required format
3. **Submit**: Push your changes and they'll appear on the site within a minute

The system automatically validates your file and updates the database—no technical knowledge required beyond basic Markdown formatting.

## Tech Stack

**Backend:**
- Django (Python web framework)
- PostgreSQL database
- Automated Markdown processing system

**Frontend:**
- Vue.js for interactive UI
- Bootstrap for styling

**Infrastructure:**
- Hosted on Render.com (free tier)
- GitHub Actions for automated content updates
- No redeploys needed when adding new models!

## The Markdown Processing System

This project includes a reusable Markdown-to-Django pipeline that:

1. **Accepts Markdown Files**: Contributors write in simple Markdown format
2. **Validates Content**: Checks files against a schema to ensure data quality
3. **Converts to Database**: Automatically processes valid files into Django models
4. **Updates Live Site**: Changes appear without manual database work

```
Markdown File → Schema Validation → Django Models → Production Database → Live Site
```

This approach makes it easy to scale content without requiring database access or technical expertise from contributors.

## Why This Was Built

This project started as a collaboration with Nicholas Vincent from SFU, who envisioned a platform that would:
- Make AI model information accessible to everyone, not just developers
- Provide transparency about how AI models use personal data
- Empower users to make informed decisions about which models to use

### What I Built

**The Automated Content Pipeline**

Instead of manually updating a database every time someone adds a model, I built a system that does it automatically. Contributors just add a Markdown file to GitHub, and the pipeline:
- Validates the file format
- Converts it to Django models
- Updates the live site within a minute

This cut down manual admin work by about 60%.

**The Backend Infrastructure**

I designed the Django backend to handle structured model data, user preferences, and API requests. This includes:
- Database schema for model metadata
- 8+ RESTful API endpoints
- Logic connecting the frontend to the data

**Deployment & CI/CD**

The whole thing runs on Render.com with automated deployments:
- Pushing code changes → full rebuild
- Pushing markdown changes → content pipeline only (no redeploy)

The coolest part? The Markdown processing system is reusable. Any Django project that needs user-contributed content could use this same pattern without forcing contributors to understand databases or backend code.

## Local Development

Want to run this locally? Here's how:

```bash
# Backend setup
cd dl_tools
python manage.py migrate
python manage.py runserver

# Frontend setup (in another terminal)
cd frontend
npm install
npm run dev
```

Visit `localhost:5173` for the frontend and `localhost:8000` for the backend API.

## Contributing

Contributions are welcome! You can:
- Add new AI models (see [contribution guide](https://dl-tools.onrender.com))
- Fix errors in existing model information
- Improve the codebase (submit a PR)

All contributions are reviewed before going live.

## Project Structure

```
dl/
├── dl_tools/              # Django backend
│   ├── dl_tools/         # Project settings
│   ├── main/             # Main app with models and views
│   ├── markdown_files/   # User-contributed model data
│   └── manage.py
├── frontend/             # Vue.js frontend
│   ├── src/
│   │   ├── views/       # Page components
│   │   ├── router/      # Navigation
│   │   └── services/    # API calls
│   └── package.json
├── .github/workflows/   # Automated content processing
└── render.yaml          # Deployment configuration
```

## Deployment Notes

The site is deployed on Render.com's free tier, which means:
- Stays live indefinitely at no cost
- Spins down after 15 minutes of inactivity
- First load after sleeping takes 30-60 seconds
- Fast and responsive once awake

Perfect for a portfolio project with occasional traffic!

## Future Improvements

- User accounts and saved preferences
- Model comparison tool
- More detailed privacy policy breakdowns
- Automated email notifications for model updates
- API for third-party integrations

## License

This project is open source and available under the MIT License.

---




   
   

