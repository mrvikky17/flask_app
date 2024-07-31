from flask import Flask, render_template, request, redirect, url_for, flash, Response,jsonify
import openai
app = Flask(__name__)

openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"




@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/nav")
def nav():
    return render_template('nav.html')


@app.route("/services")
def services():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contect")
def contect():
    return render_template('contect.html')


@app.route('/submit' , methods=["post"])
def index():
    
    data = request.form['abc']
        
    print(data)
    
    return render_template('after.html')
    
    
   
    

    


if __name__ == "__main__":
    app.run(debug=True)