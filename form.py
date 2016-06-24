from flask import Flask, request, make_response, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/landing_page')
def agents():
   return render_template('landing_page.html')

@app.route('/input')
def chat():
   return render_template('input.html')

