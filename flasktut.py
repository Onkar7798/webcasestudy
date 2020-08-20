from flask import *
import csv


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/add", methods=["POST", "GET"])
def add():
	if request.method == "POST":
		result = list(request.form.values());
		#return render_template("add-student.html", result=result)
		split = result[3].split('-')
		result[3] = split[2]+"-"+split[1]+"-"+split[0]
		with open('students.csv', 'a', newline='\n') as csv_file:
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow(result)
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

