#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/Shalini187/backend-project-api.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/backend-project-api

mkdir -p $VIRTUALENV_BASE_PATH
python3 -m venv $VIRTUALENV_BASE_PATH/backend_project_api

$VIRTUALENV_BASE_PATH/backend_project_api/bin/pip install -r $PROJECT_BASE_PATH/backend-project-api/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/backend-project-api/src

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/backend-project-api/deploy/supervisor_backend_api.conf /etc/supervisor/conf.d/backend_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart backend_api

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/backend-project-api/deploy/nginx_backend_api.conf /etc/nginx/sites-available/backend_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/backend_api.conf /etc/nginx/sites-enabled/backend_api.conf
systemctl restart nginx.service

echo "DONE! :)"
