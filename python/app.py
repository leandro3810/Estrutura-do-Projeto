from flask import,render_template
app= flask(_ _name_ _)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

if _ _name_ _=='_ _main_ _':
      app.run(debug=True)
