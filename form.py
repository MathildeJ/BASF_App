from flask import Flask, request, make_response, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/landing_page')
def landing_page():
   return render_template('landing_page.html')

@app.route('/input_field')
def input_field():
   return render_template('input_field.html')

@app.route('/display_form')
def display_form():
   return render_template('display_form.html')
