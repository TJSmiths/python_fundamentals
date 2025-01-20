from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from .models import Todo
from . import db

# new instance of the Flask class
my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    todo_list = Todo.query.all()
    error = request.args.get('error', None)
    success = request.args.get('success', None)
    return render_template("index.html", todo_list=todo_list, error=error, success=success)

@my_view.route("/add", methods=["POST"])
def add():
    try:
        task = request.form.get("task")
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
        success = "Task added successfully"
        return redirect(url_for("my_view.home", success=success))
    except:
        error = "There was an issue adding your task"
        return redirect(url_for("my_view.home", error=error))

@my_view.route("/update/<todo_id>")
def update(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.complete = not todo.complete
        db.session.commit()
        success = "Task updated successfully"
        return redirect(url_for("my_view.home", success=success))
    except:
        error = "There was an issue updating your task"
        return redirect(url_for("my_view.home", error=error))

@my_view.route("/delete/<todo_id>")
def delete(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        db.session.commit()
        success = "Task deleted successfully"
        return redirect(url_for("my_view.home", success=success))
    except:
        error = "There was an issue deleting your task"
        return redirect(url_for("my_view.home", error=error))