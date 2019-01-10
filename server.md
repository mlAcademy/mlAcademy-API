<h1>To run the server locally: </h1>

<ul>
<li>make sure you have python 3+ and django + django REST framework installed
<li>download the server folder on your local machine</li>
<li><code>cd</code> into mlacademy</li>
<li>run <code>python3 manage.py runserver</code></li> 
</ul> 

<h1>To use the REST API</h1>

<p>The public IP of the VM is 18.224.107.58. If you type <code>18.224.107.58/admin</code> you can log into the admin portal and add new lessons to the database.</p>
<p>To send a <b>GET Request</b> for an existing lesson <code>18.224.107.58/api/&ltLessonID&gt</code> (where LessonID is the unique ID for the lesson) will return a JSON file with the title, author and content. </p>
<p>To send a <b>POST Request</b> for a new lesson, the enspoint is <code>18.224.107.58/api/</code></p>
<p><code>18.224.107.58/api/test/?model_input=print(1)</code> will return the output of the calculation in a JSON format: <code> 
    {
    "complex_result": "1\n"
    }
</code>
Similarly, you can replace print(1) with any script you want to execute as long as you take care of the special characters. 
</p>
