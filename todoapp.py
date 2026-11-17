
from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task', '').strip()
    email = request.form.get('email', '').strip()
    priority = request.form.get('priority', '')

    email_pattern = r'^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$'

    if not task or not re.fullmatch(email_pattern, email):
        return redirect(url_for('index'))

    if priority not in ['Low', 'Medium', 'High']:
        return redirect(url_for('index'))

    todo_list.append({
        'task': task,
        'email': email,
        'priority': priority
    })

    return redirect(url_for('index'))


@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
