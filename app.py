from flask import Flask , render_template , request , redirect , url_for , session
from flask_sqlalchemy import SQLAlchemy
from forms import TaskForm

app = Flask(__name__ , template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = 'SOME SECRETS'
db = SQLAlchemy(app)
from models import TaskData


@app.route('/' , methods=["GET" , "POST"])
def home():
    tasks = TaskData.query.all()
    return render_template("home.html", tasks=tasks)

    
@app.route('/add' , methods=["GET" , "POST"])
def add():
    form = TaskForm()
    if request.method == "GET":
        return render_template('add.html' , form=form)
    else:
        data = TaskData(
            title = form.title.data,
            task = form.task.data,
        )
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('home'))
    
    
@app.route('/delete/<int:id>' , methods=["POST"])
def delete(id):
    task = TaskData.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))
    
    
@app.route('/done/<int:id>')
def done(id):
    task = TaskData.query.get_or_404(id)
    task.done = True
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/undone/<int:id>')
def undone(id):
    task = TaskData.query.get_or_404(id)
    task.done = False
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/edit_session/<int:id>')
def edit_session(id):
    session['task'] = TaskData.query.get(id).task
    session['title'] = TaskData.query.get(id).title
    session['id'] = id
    return redirect(url_for('edit'))


@app.route('/edit', methods=["GET", "POST"])
def edit():
    form = TaskForm()
    if request.method == "GET":
        task = session.get('task' , '')
        title = session.get('title' , '')
        form.title.data = title
        form.task.data = task
        return render_template('add.html', form=form)
    elif request.method == "POST":
        data = TaskData.query.get_or_404(session['id'])
        data.title = form.title.data
        data.task = form.task.data
        db.session.commit()
    return redirect(url_for('home'))
    
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
