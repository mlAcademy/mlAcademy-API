<h1>To run the server locally: </h1>

<ul>
<li>make sure you have python 3+ and django + django REST framework installed + django-cors-headers
<li>download the server folder on your local machine</li>
<li><code>cd</code> into mlacademy</li>
<li>run <code>python3 manage.py runserver</code> or <code>python3 manage.py runserver 0.0.0.0:80</code> if you want to run it non-locally</li> 
</ul> 

<h1>To use the REST API</h1>

<p>The public IP of the VM is <s>18.224.107.58</s>. (not deployed yet)</p>

If you type <code>PUBLICIP/admin</code> you can log into the admin portal and add new lessons to the database.</p>
<p>To send a <b>GET Request</b> for an existing lesson <code>PUBLICIP/api/&ltLessonID&gt</code> (where LessonID is the unique ID for the lesson) will return a JSON file with the title, author and content. </p>
<p>To send a <b>POST Request</b> for a new lesson, the endpoint is <code>PUBLICIP/api/</code></p>
<p><code>PUBLICIP/api/test/?model_input=print(1)</code> will return the output of the calculation in a JSON format: <code> 
    {
    "complex_result": "1\n"
    }
</code>
Similarly, you can replace print(1) with any script you want to execute as long as you take care of the special characters. 
</p>

<h2>Changes</h2> 
<p>Lessons are now organized in <b>Topics</b> - each topic has a name and a set of Lessons. Topics can be changes from the admin portal just like Lessons. Lesson now has a <b>code</b> text field and the difficulty field has been removed.</p>
<ul>
    <li><code>PUBLICIP/api/topics</code> returns a list of all the available topics (their id-s and their names)</li>
    <li>To check the lessons in a specific topic, use <code>PUBLICIP/api/lessons/?topic=&ltTOPIC_ID&gt</code>. This should return the number of lessons in that topic and their names.</li>
    <li>To retrieve a specific lesson from a specific topic, use <code>PUBLICIP/api/search/?topic=&ltTOPIC_ID&gt&amplesson=&ltLESSON_NUMBER&gt</code>. Here &ltLESSON_NUMBER&gt is not the lesson id (or primary key) but the number in the topic it belongs to. For example if topic <i>Introduction</i> has topics <i>Topic 1</i>, <i>Topic 2</i> and <i>Topic 3</i>, those will have lesson numbers 1, 2 and 3, regardless of their id-s in the database.</li>
</ul>
