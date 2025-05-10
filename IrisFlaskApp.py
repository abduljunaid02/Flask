from flask import Flask, render_template, request, jsonify
import pickle

with open("myirismodel.pickle", "rb") as f:
    model_rf = pickle.load(f)

irisapp = Flask(__name__)


@irisapp.route("/")
def main():
    return "Hello World!"

@irisapp.route("/name")
def param_name():
    return "Hello Name"

@irisapp.route("/<name>")
def true_param_name(name):
    return f"Hello {name}"

@irisapp.route("/<name>/<age>")
def two_param_name(name, age):
    return f"Hello {name} Your age is {age}"


#http://127.0.0.1:5000/details?name=junaid&age=31&school=DPS
@irisapp.route("/details")
def details():
    print(request.args)
    name = request.args.get("name")
    age = request.args.get("age")
    school = request.args.get("school")
    return f"{name} is {age} years old and studies at {school}"

#To send a request from postman client

@irisapp.route("/postman", methods = ["POST"])
def postman():
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    school = data.get("school")
    return f"Messgae from postman client{name} studies at {school} and is {age} years old"


#Calling iris home page

@irisapp.route("/homepage")
def form():
    return render_template("homepage.html")

#prediction
@irisapp.route("/results", methods = ["GET","POST"])
def predict():
    sepal_length = float(request.form.get("sepal_length"))
    sepal_width = float(request.form.get("sepal_width"))
    petal_length = float(request.form.get("petal_length"))
    petal_width = float(request.form.get("petal_width"))
    prediction = model_rf.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return render_template("results.html", prediction= prediction[0])

#jasonify

@irisapp.route("/api", methods = ["GET", "POST"])
def jasonAPI():
    data = {
        "name" : "Robert Downey Jr",
        "Age" : 61,
        "School" : "Marvel"
    }
    return jsonify(data)


if __name__ == "__main__":
    irisapp.run()
