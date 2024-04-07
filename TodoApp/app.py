from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
completed_tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task']
    category = request.form['category']
    due_date = request.form['due_date']
    priority = request.form['priority']
    notes = request.form['notes']
    task = {
        'name': task_name,
        'category': category,
        'due_date': due_date,
        'priority': priority,
        'notes': notes
    }
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/remove/<int:index>', methods=['POST'])
def remove_task(index):
    if index < len(tasks):
        completed_task = tasks.pop(index)
        completed_tasks.append(completed_task)
    return redirect(url_for('index'))

@app.route('/completed')
def completed():
    return render_template('completed.html', completed_tasks=completed_tasks)

if __name__ == '__main__':
    app.run(debug=True)
