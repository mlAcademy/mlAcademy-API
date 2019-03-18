# mlAcademy API
Authored by:

- Samuil Stoychev [@samuil1998](https://github.com/samuil1998)
- Adam Peace [@adamnpeace](https://github.com/adamnpeace)
- Sotirios Vavaroutas [@svavaroutas](https://github.com/svavaroutas)

# Usage

## To run the server locally:

_Ensure you have python3 & **pipenv** installed_

- `pip --version`
- `python3 --version`
- Install pipenv for super user with `sudo -H pip install -U pipenv`
- `git clone https://github.com/mlacademy/backend.git mlacademy-backend`
- `cd mlacademy-backend`
- `pipenv install`
- `cp .env.example .env` and edit vars for your configuration
- Local development: `pipenv run python manage.py runserver`
- Deployment on port 80 `sudo pipenv run python3 manage.py runserver 0.0.0.0:80`

# Consuming the REST API

## Background

The API serves two main purposes. One is to make requests to the database and provide easy access to the website's content. Another is to compute Python scripts per request.

To use the API properly, it helps having basic of the database schema in the backend. The content in the website is structured into three main Django models - _Lessons, Topics and Students_.

Each **Lesson** consists of the following fields:

*   **id (or primary key)** - the object's unique identifier automatically assigned by Django.
*   **name** - the name of the lesson.
*   **date published** - the date and time of the lesson's creation.
*   **content** - the content accompanying the lesson.
*   **code** - the code filled in the interpreter for the student in advance.

A **Topic** is a thematic collection of ordered Lessons. It consists of:

*   **id** - unique identifier.
*   **name** - the name of the topic.
*   **description** - short description to go with the topic's tile.
*   **image url** _(optional)_\- a thumbnail for the topic's tile.
*   **prerequisites** - a list of Lessons needed to unlock the Topic.
*   **difficulty** - the topic's difficulty level (determines the order in which topic appears in the list of topics).
*   **colour** - field to store the topic's tile's colour.
*   **Lesson 1 to 10** - 10 fields to store the topic's lessons. Order matters as lessons are displayed in the respective order.

Each **Student** object represents a user. The model is used to store user preferences and progress and has the following fields:

*   **id** - unique identifier.
*   **uid** _(user ID)_ - a unique identifier provided with user authentication.
*   **completed lessons** - a list of Lessons completed by the Student.
*   **completed topics** - a list of Topic completed by the Student.
