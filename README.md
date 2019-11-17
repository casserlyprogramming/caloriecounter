
# Calorie Counter Django App

  

This Project is a simple Django App for saving a bunch of workouts and seeing

a rough estimate how many calories you have burnt.

  

# Setup

  

The project uses Docker to make things easy. To run the project, simply clone

the repository then run the following commands:

`docker-compose up build`

This will build the docker images for the database and the website

Then either cancel that or in a different tab run:

`docker-compose run web python manage.py migrate`

This will migrate the database so you are up to date

  

# Tech used

  

This project uses 
- Django 2.2.7
- Postgres 
- Materialize CSS. 
- Docker
