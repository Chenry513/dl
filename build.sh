#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Build Vue.js frontend
cd frontend
npm install
npm run build
cd ..

cd dl_tools
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py process_markdown

