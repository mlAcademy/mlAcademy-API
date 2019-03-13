# To run the server locally:

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

# To use the REST API

You can access the API through api.mlacademy.ml.

If you type `api.mlacademy.ml/admin` you can log into the admin portal and add new lessons to the database.

To send a **GET Request** for an existing lesson `api.mlacademy.ml/api/<LessonID>` (where LessonID is the unique ID for the lesson) will return a JSON file with the title, author and content.

To send a **POST Request** for a new lesson, the endpoint is `api.mlacademy.ml/api/`

`api.mlacademy.ml/api/compute/?input=print(1)` will return the output of the calculation in a JSON format: `{ "output": "1\n", "error", "" }` Similarly, you can replace print(1) with any script you want to execute as long as you take care of the special characters.

## Changes

Lessons are now organized in **Topics** - each topic has a name and a set of Lessons. Topics can be changes from the admin portal just like Lessons. Lesson now has a **code** text field and the difficulty field has been removed.

- `api.mlacademy.ml/api/topics` returns a list of all the available topics (their id-s and their names)
- To check the lessons in a specific topic, use `api.mlacademy.ml/api/lessons/?topic=<TOPIC_ID>`. This should return the number of lessons in that topic and their names.

## Changes 3rd March

### Student API

The student API can be accessed through `api.mlacademy.ml/api/students`.

#### GET Requests

- `api/students/uid=USER_ID` - returns `topics` (list of completed topics' ids) and `lessons` (list of completed lessons' ids) for the student with the corresponding UID.

#### POST Requests

Actions are specified by including an `action` parameter.

- **Creating a user** - `api/students/?uid=<NEW_USER_ID>&action=_create-user_`
- **Deleting a user** - `api/students/?uid=<DELETED_USER_ID>&action=_delete-user_`
- **Adding a completed lesson** - `api/students/?uid=<USER_ID>&action=_add-lesson_&lesson-id=<LESSON_ID>`
- **Removing a completed lesson** - `api/students/?uid=<USER_ID>&action=_remove-lesson_&lesson-id=<LESSON_ID>`
- **Adding a completed topic** - `api/students/?uid=<USER_ID>&action=_add-topic_&topic-id=<TOPIC_ID>`
- **Removing a topic** - `api/students/?uid=<USER_ID>&action=_remove-topic_&topic-id=<TOPIC_ID>`

### Changes to the computation API

The computation API parameters and url have been changed. To hand a computation task, use `api/compute` (and not the old `api/test`. The GET request parameter's name has been changed from `model_input` to `input`. The API returns an `output` and `error` field now, unlike the old version which only return output as `code_result`.
