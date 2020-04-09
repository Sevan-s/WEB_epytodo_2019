from app import app
from flask import render_template

@app.route('/', methods=['GET'])
def route_index():
    return render_template("index.html",
                           title="EPYTODO",
                           menu_url="http://127.0.0.1:5000/signin",
                           menu="signin",
                           myContent="Le meilleur outil de planification au monde")


@app.route('/register', methods=['GET', 'POST'])
def route_register():
    return render_template("register.html",
                           title="EPYTODO register",
                           menu_url="http://127.0.0.1:5000/signin",
                           menu="signin",
                           myContent="register a new user")


@app.route('/signin', methods=['GET', 'POST'])
def route_signin():
    return render_template("signin.html",
                           title="EPYTODO signout",
                           menu_url="http://127.0.0.1:5000/register",
                           menu="register",
                           myContent="connect user")


@app.route('/signout', methods=['GET', 'POST'])
def route_signout():
    return render_template("index.html",
                           title="EPYTODO signout",
                           menu_url="http://127.0.0.1:5000/user",
                           menu="user",
                           myContent="disconnect user")


@app.route('/user', methods=['GET'])
def route_user():
    return render_template("index.html",
                           title="EPYTODO user",
                           menu_url="http://127.0.0.1:5000/signout",
                           menu="signout",
                           myContent="view all user information")


@app.route('/task', methods=['GET'])
def route_task():
    return render_template("index.html",
                           title="EPYTODO task",
                           menu_url="http://127.0.0.1:5000/signout",
                           menu="signout",
                           myContent="view all user tasks")


@app.route('/task/id', methods=['GET', 'POST'])
def route_task_id():
    return render_template("index.html",
                           title="EPYTODO task id",
                           menu_url="http://127.0.0.1:5000/signout",
                           menu="signout",
                           myContent="view and update a specific task")


@app.route('/user/task/add', methods=['GET', 'POST'])
def route_task_add():
    return render_template("index.html",
                           title="EPYTODO task id",
                           menu_url="http://127.0.0.1:5000/signout",
                           menu="signout",
                           myContent="create a new task")


@app.route('/user/task/del/id', methods=['GET', 'POST'])
def route_task_del_id():
    return render_template("index.html",
                           title="EPYTODO task id",
                           menu_url="http://127.0.0.1:5000/signout",
                           menu="signout",
                           myContent="delete a specific task")

