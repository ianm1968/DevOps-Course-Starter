from flask import Flask,render_template,request,redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items,add_item,get_item,save_item,delete_item

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    sorted_items = sorted(get_items(), key=lambda item: item.get('status'), reverse=True)
    return render_template("index.html", to_do_list=sorted_items)
    
@app.route('/add', methods=['POST'])
def add_item_by_title():
    add_item(request.form.get('task_title'))
    return redirect('/')

@app.route('/complete', methods=['POST'])
def complete_item_by_title():
    item_to_complete = request.form.get('task_title')
    for item in get_items():
        if item['title'] == item_to_complete:
            item['status'] = 'Completed'
            save_item(item)
            break
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_item_by_title():
    item_to_delete = request.form.get('task_title')
    for item in get_items():
        if item['title'] == item_to_delete:
            delete_item(item['id'])
            break
    return redirect('/')

