import time
import redis
import sys
from flask import Flask, render_template, flash, redirect
from forms import TodoAddForm, TodoRemoveForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b5c4b72eb9b0600296ad6f083fc44942'

cache = redis.Redis(host='redis', port=6379,db=1)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/todo-list', methods=['GET', 'POST'])
def todolist():
    form = TodoAddForm()
    formRm = TodoRemoveForm()
    if form.validate_on_submit():
        cache.rpush('todos',form.label.data)
        
    if formRm.validate_on_submit():
        cache.lrem('todos',-1,formRm.value.data)

    todos = cache.lrange('todos',0,-1)
    return render_template('todo-list.html', todos=todos, form=form, formRm=formRm)
