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
- **Install pipenv for super user with `sudo -H pip install -U pipenv`**
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

## Requests

### GET Requests

| Request                   | Endpoint                                       | Description                                                                                                                                                       | JSON Response Fields                    |
|---------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| Get all topics            | api.mlacademy.ml/api/topics                    | Get a list of all the website's topics (with all object fields exposed).                                                                                          | topics                                  |
| Get all lessons per topic | api.mlacademy.ml/api/lessons/?topic=<TOPIC_ID> | Returns a list of Lesson objects associated to the topic.                                                                                                         | number_of_lessons, lessons              |
| Get lesson by ID          | api.mlacademy.ml/api/students/<LESSON_ID>      | Retrieve a lesson by its absolute ID field.                                                                                                                       | id, name, date_published, content, code |
| Get student's details     | api.mlacademy.ml/api/students/?uid=<USER_ID>   | Returns the details of the student with user ID <USER_ID>. More specifically, it returns a list of completed Lesson objects and a lsit of completed Topic objects | topics, lessons, uid                    |
| Get computation output    | api.mlacademy.ml/api/compute/?input=print(1)   | The backend server executes the script and returns the output it generates.                                                                                       | output, error_output                    |

### POST Requests

| Request                     | Endpoint                                                                                | Description                                                                                     | Required JSON Fields   |
|-----------------------------|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|------------------------|
| Creating a user             | api.mlacademy.ml/api/students/?uid=<USER_ID>&action=create-user                         | Create a new user with user id USER_ID. UID needs to be unique.                                 | action, uid            |
| Deleting a user             | api.mlacademy.ml/api/students/?uid=<USER_ID>&action=delete-user                         | Delete user with user id USER_ID.                                                               | action, uid            |
| Adding a completed lesson   | api.mlacademy.ml/api/students/?uid=<USER_ID>&action=add-lesson&lesson-id=<LESSON_ID>    | Append lesson LESSON_ID to the list of completed lessons of the Student object with id USER_ID. | action, uid, lesson-id |
| Removing a completed lesson | api.mlacademy.ml/api/students/?uid=<USER_ID>&action=remove-lesson&lesson-id=<LESSON_ID> | Remove lesson LESSON_ID from the completed lessons list of the student with id USER_ID.         | action, uid, lesson-id |
| Adding a completed topic    | api.mlacademy.ml/api/students/?uid=<USER_ID>&action=add-topic&topic-id=<TOPIC_ID>       | Append topic TOPIC_ID to the list of completed topics of the Student object with id USER_ID.    | action, uid, topic-id  |
| Removing a topic            | api.mlacademy.ml/api/students/?uid=<USER_ID>&action=remove-topic&topic-id=<TOPIC_ID>    | Remove lesson LESSON_ID from the completed lessons list of the student with id USER_ID.         | action, uid, topic-id  |
