from flask import render_template, current_app as app

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/about')
def about():
    return render_template('About.html')
