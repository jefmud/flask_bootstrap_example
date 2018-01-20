# flask_bootstrap_example
#
# documentation @ https://pythonhosted.org/Flask-Bootstrap/
#
# this add-on doesn't bring in that much, except a predefined template and blocks
# from which to pull the CDN resources into your project
#
# since bootstrap is wildly popular, you can find lots of examples/resources
# for design inspiration-- you can override the default jquery based scripts
# with something else (e.g. Angular)
# 
# one could just as easily used Materialize (inspired by Google's "Material Design"
# or Bulma (a pure CSS framework) to which you can add your own flavor of javascript
#
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app) # simple inclusion to the project

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=False)