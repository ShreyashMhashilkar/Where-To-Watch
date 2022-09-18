from flask import Flask,redirect,url_for,render_template,request
from read_website import read_web

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/",methods=["POST","GET"])
def get_ott():
    if request.method == "POST":
        name = request.form["nm"]
        print(name)
        return redirect(url_for("display_ott_names",name = name))
    else:
        return render_template("index.html")

@app.route("/<name>")
def display_ott_names(name):
    print(name)
    result = read_web(name)
    print(result)
    return render_template("result.html",result = result)

if __name__=="__main__":
    app.run(debug=True)