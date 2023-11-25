from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample tasks for testing
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Build a task manager", "done": False},
    {"id": 3, "title": "Impress future interviewer", "done": False},
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        if title:
            new_task = {
                "id": len(tasks) + 1,
                "title": title,
                "done": False
            }
            tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>')
def update(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
