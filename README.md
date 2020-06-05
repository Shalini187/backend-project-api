# Backend REST API PROJECT

In Django project, We could manage by executing some commands which could be invoked through the manage.py.

# API Created with admin/ page
http://127.0.0.1:8080/admin/backend_api/activitylog/

# API Viewed with api/ page
http://127.0.0.1:8080/api/members/

# Installation of apps
git clone https://github.com/Shalini187/backend-project-api.git

# Run Vagrant server
vagrant up ---> to the server

vagrant ssh ---> to start ubuntu server

# To execute

cd /Vagrant
workon backend_project_api

cd src/backend_project

python manage.py makemigrations ---> save custom user and activity models

python manage.py migrate

python manage.py createsuperuser ---> create su user

python manage.py runserver 0.0.0.0:8080

# On browser
# API Created with admin/ page
http://127.0.0.1:8080/admin/backend_api/activitylog/

# API Viewed with api/ page
http://127.0.0.1:8080/api/members/
