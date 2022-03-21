# meal-management-system
<h3>Step: 1</h3>
Git clone first:
<ul>
    <li>https://github.com/Rayhun/meal-management-system.git ( HTTPS )</li>
    <li>git@github.com:Rayhun/meal-management-system.git ( SSH )</li>
</ul>
<h3>Step: 2</h3>
Then change directory to the project folder and run the following command:
<ul>
    <li>cd MealManagementSystem</li>
</ul>
Then Create a virtual environment and activate it:
<ul>
    <li>python3 -m venv venv</li>
    <li>source venv/bin/activate ( for linux )</li>
    <li>venv\Scripts\activate ( for windows )</li>
</ul>
<h3>Step: 3</h3>
Install the required packages:
<ul>
    <li>pip install -r requirements.txt</li>
</ul>
<h3>Step: 4</h3>
Create a postgres user and database:
<ul>
    <li>sudo -u postgres psql</li>
    <li>create database mms_db;</li>
    <li>create user mms_user with encrypted password 'password';</li>
    <li>grant all privileges on database mms_db to mms_user;</li>
</ul>
<h3>Step: 5</h3>
Copy the local_settings and past it to the project folder:
<ul>
    <li>cp example/local_settings.example MealManagementSystem/local_settings.py</li>
</ul>
<h3>Step: 6</h3>
Update the postgres user and database and password to the local_settings.py:
<ul>
    <li>nano MealManagementSystem/local_settings.py</li>
</ul>
<h3>Step: 7</h3>
Run the server:
<ul>
    <li>python3 manage.py runserver</li>
</ul>