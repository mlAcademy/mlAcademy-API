<h1>To run the server locally: </h1>

<ul>
<li>make sure you have python 3+ and django + django REST framework installed + django-cors-headers
<li>download the server folder on your local machine</li>
<li><code>cd</code> into mlacademy</li>
<li>run <code>python3 manage.py runserver</code> or <code>python3 manage.py runserver 0.0.0.0:80</code> if you want to run it non-locally</li> 
</ul> 

<h1>To use the REST API</h1>

<p>You can access the API through api.mlacademy.cf.</p>

If you type <code>api.mlacademy.cf/admin</code> you can log into the admin portal and add new lessons to the database.</p>
<p>To send a <b>GET Request</b> for an existing lesson <code>api.mlacademy.cf/api/&ltLessonID&gt</code> (where LessonID is the unique ID for the lesson) will return a JSON file with the title, author and content. </p>
<p>To send a <b>POST Request</b> for a new lesson, the endpoint is <code>api.mlacademy.cf/api/</code></p>
<p><code>api.mlacademy.cf/api/compute/?input=print(1)</code> will return the output of the calculation in a JSON format: <code> 
    {
    "output": "1\n", 
    "error", ""
    }
</code>
Similarly, you can replace print(1) with any script you want to execute as long as you take care of the special characters. 
</p>

<h2>Changes</h2> 
<p>Lessons are now organized in <b>Topics</b> - each topic has a name and a set of Lessons. Topics can be changes from the admin portal just like Lessons. Lesson now has a <b>code</b> text field and the difficulty field has been removed.</p>
<ul>
    <li><code>api.mlacademy.cf/api/topics</code> returns a list of all the available topics (their id-s and their names)</li>
    <li>To check the lessons in a specific topic, use <code>api.mlacademy.cf/api/lessons/?topic=&ltTOPIC_ID&gt</code>. This should return the number of lessons in that topic and their names.</li>
    <li>To retrieve a specific lesson from a specific topic, use <code>api.mlacademy.cf/api/search/?topic=&ltTOPIC_ID&gt&amplesson=&ltLESSON_NUMBER&gt</code>. Here &ltLESSON_NUMBER&gt is not the lesson id (or primary key) but the number in the topic it belongs to. For example if topic <i>Introduction</i> has topics <i>Topic 1</i>, <i>Topic 2</i> and <i>Topic 3</i>, those will have lesson numbers 1, 2 and 3, regardless of their id-s in the database.</li>
</ul>

<h2>Changes 3rd March</h2> 
<h3>Student API</h3> 
<p>The student API can be accessed through <code>api.mlacademy.cf/api/students</code>.</p> 
<h4>GET Requests</h4> 
    <ul>
        <li><code>api/students</code> - get a list of all students' UID-s.</li> 
        <li><code>api/students/uid=USER_ID</code> - returns <code>topics</code> (list of completed topics' ids) and <code>lessons</code> (list of completed lessons' ids) for the student with the corresponding UID.</li>
    </ul>
<h4>POST Requests</h4> 
<p>Actions are specified by including an <code>action</code> parameter.</p>
    <ul> 
        <li><b>Creating a user</b> - <code>api/students/?uid=&ltNEW_USER_ID&gt&action=<i>create-user</i></code></li>
        <li><b>Deleting a user</b> - <code>api/students/?uid=&ltDELETED_USER_ID&gt&action=<i>delete-user</i></code></li>
        <li><b>Adding a completed lesson</b> - <code>api/students/?uid=&ltUSER_ID&gt&action=<i>add-lesson</i>&lesson-id=&ltLESSON_ID&gt</code></li>
        <li><b>Removing a completed lesson</b> - <code>api/students/?uid=&ltUSER_ID&gt&action=<i>remove-lesson</i>&lesson-id=&ltLESSON_ID&gt</code></li>
        <li><b>Adding a completed topic</b> - <code>api/students/?uid=&ltUSER_ID&gt&action=<i>add-topic</i>&topic-id=&ltTOPIC_ID&gt</code></li>
        <li><b>Removing a topic</b> - <code>api/students/?uid=&ltUSER_ID&gt&action=<i>remove-topic</i>&topic-id=&ltTOPIC_ID&gt</code></li>
    </ul>
<h3>Changes to the computation API</h3>
<p>The computation API parameters and url have been changed. To hand a computation task, use <code>api/compute</code> (and not the old <code>api/test</code>. The GET request parameter's name has been changed from <code>model_input</code> to <code>input</code>. The API returns an <code>output</code> and <code>error</code> field now, unlike the old version which only return output as <code>code_result</code>.</p>
