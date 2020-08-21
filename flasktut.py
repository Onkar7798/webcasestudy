from flask import *
import csv


app = Flask(__name__)
app.secret_key = "qwerty"

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/add", methods=["POST", "GET"])
def add():
	if request.method == "POST":
		result = list(request.form.values());
		split = result[3].split('-')
		result[3] = split[2]+"-"+split[1]+"-"+split[0]
		with open('students.csv', 'a', newline='\n') as csv_file:
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow(result)
	return render_template("add-student.html")

@app.route("/search", methods=["POST", "GET"])
def search():
	if request.method == "POST":
		id = list(request.form.values())
		print(id[0])
		success = False
		with open('students.csv', 'r') as csv_file:
			csv_reader = csv.reader(csv_file)
			for line in csv_reader:
				if line[0] == id[0]:
					details = line
					success = True
		if not success:
			flash(f"Student id: {id} not found, Please try again!", "info")
		keys = ['Student ID', 'Student Name', 'Gender', 'Date of Birth', 'City', 'State', 'Email ID', 'Qualification', 'Stream']	
		result = dict(zip(keys, details))
		return render_template("search-student.html", data=True, result=result)
	return render_template("search-student.html", data=False, result="")

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

