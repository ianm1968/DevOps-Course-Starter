from flask import Flask,render_template,request,redirect
from todo_app.flask_config import Config
# import todo_app.data.session_items as to_do_session
from todo_app.data.session_items import get_items,add_item


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template("index.html", to_do_list=get_items())
    
@app.route('/add', methods=['POST'])
def add_item_by_title():
    add_item(request.form.get('task_title'))
    return redirect('/')

