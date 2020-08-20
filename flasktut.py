from flask import *

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/add")
def add():
	return render_template("add-student.html")

@app.route("/search")
def search():
	return render_template("search-student.html")

@app.route("/display")
def display():
	return render_template("display-student.html")

# @app.route("/<param>")
# def say(param):
# 	return f"Hi {param}"

# @app.route("/admin")
# def admin():
# 	return redirect(url_for("say", param="admin!!"))
# content=[]
# for r in range(5):
# 	content.append(input("Enter a value"))
if __name__=="__main__":
	app.run(debug=True)

