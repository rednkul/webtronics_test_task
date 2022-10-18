<h2> Test task for Webtronics. </h2>

<h3> Instruction for deploy: </h3>
<ol>
<li> Install python 3 (3.9 used in project); </li>
<li> Create and activate new virtual environment on your host;</li>
<li> Clone this project to environment;</li>
<li> Open terminal and go to project directory;</li>
<li> Input 'pip install requirements.txt';</li>
<li> Input:
  python manage.py makemigrations
  python manage.py migrate
 </li>
<li> Input 'python manage.py createsuperuser'</li>
</ol>

<h3> Instruction for test with Postman: </h3>
<ul>
<li> Open terminal and input 'python manage.py runserver';</li>
<li> In postman input url 'localhost/api-auth/users/', add username, email and password to request body and do post-request to create user;</li>
<li> Input url 'localhost/api-auth/jwt/create/', add email and password from last point and do get-request to get JWT;</li>
<li> Copy access token and past it to authorization tab. So you are authorized for next requests;</li>
<li> Go to 'localhost/api/v1/posts/create/' with title and text in body and do post-request. New post was added. 
On 'localhost/api/v1/posts/' you can see list of posts with all fields and quantity of likes and dislikes;</li>
<li> Go to 'localhost/api/v1/posts/detail/{post_id}/' to see details of post or update/delete it if you are an admin or owner of post;</li>
<li> To like or dislike post go to 'localhost/api/v1/likes/create/' and add 'LIKE' or 'DISLIKE' to field like_or_dislike and post_id to field post to rate the post.
Only for authenticated users.</li>
<li> To change the rate of the post rate's owner can go to 'localhost/api/v1/likes/detail/{like_id}' and put value of like_or_dislike;</li>
</ul>

<h3> For better user experience we could use websockets for display likes/dislikes quantity changing in real-time. <h3>
