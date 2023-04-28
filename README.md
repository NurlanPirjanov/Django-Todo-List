# todo
A simple todo app built with django

![todo App](https://raw.githubusercontent.com/NurlanPirjanov/todo/main/static/screen_todo.png)
### Setup
To get this repository, run the following command inside your git enabled terminal
```bash
$ git clone "https://github.com/NurlanPirjanov/Django-Todo-List.git"
```

Create a virtual environment for this project.

```bash
python -m venv venv
```

Activate the virtual environment
```bash
venv\scripts\activate 
```

Now, navigate to the project directory
```bash
cd Django-Todo-List
```

Install the requirements for this project
```bash
pip install -r requirements.txt
```

Create this file .env
```bash
export SECRET_KEY=your_secret_key
export DEBUG=True
```

```bash
$ python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
$ python manage.py migrate
```

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
$ python manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```bash
$ python manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000/ for the App.

Cheers and Happy Coding :)
