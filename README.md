[![Coverage Status](https://coveralls.io/repos/github/andela-jngatia/Just-Do-It/badge.svg?branch=develop)](https://coveralls.io/github/andela-jngatia/Just-Do-It?branch=develop)
[![Build Status](https://travis-ci.org/andela-jngatia/Just-Do-It.svg?branch=develop)](https://travis-ci.org/andela-jngatia/Just-Do-It)

# Just-Do-It
A Django-powered Bucketlist application inspired by Shia LaBeouf's ["Just do it"](https://youtu.be/ZXsQAXx_ao0) motivational speech


## Getting Started
### Project Structure

This application has been divided into tow main parts:
- Apiv1 ,built on Django Rest Framework
- Bucketlist, built on native DjangoTEmplates and Views with Jquery and Material Design For Bootstrap in use to style the frontend.


The features attached to the service include:
* authenticating a user.
* creating new bucketlists and bucketlist items.
* updating and deleting the items, as well as marking them as done or not done.
* retrieving a list of all created bucket lists by a registered user.

### How it works on your local machine
1. Simply clone the repo by running ```git clone https://github.com/andela-jngatia/Just-Do-It.git```.
2. Install dependencies as per the requirements.txt file within your virtual environment. ```pip install -r requirements.txt```.
3. Initialize the database skeleton by running ```python manage.py makemigrations``` and ```python manage.py migrate```.
4. Run ```python manage.py collectstatic``` to copy all static files onto the staticfiles directory.
5. Access the API as well as the app by running ```python manage.py runserver```

Access to the API endpoints can be via [Postman](https://www.getpostman.com/) or through the Django Rest Framework browseable API accessed in this case by running ```localhost:8000/apiv1/<resource_targeted>/``` on your browser.
The App itself is accessed by running ```localhost:8000/```

### Running tests
1. Navigate to project directory.
3. Run ```python manage.py test``` to run the tests as well as check coverage report.

### API documentation
Django Rest Framework API endpoints were documented using Swagger.
This documentation can be accessed by running ```localhost:8000/docs```
