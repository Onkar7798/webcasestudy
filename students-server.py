from flask import *
import csv

app = Flask(__name__)
app.secret_key = "wubbalubbadubdub"

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/add", methods=["POST", "GET"])
def add():
	if request.method == "POST":
		result = list(request.form.values());
		split = result[3].split('-')
		result[3] = split[2]+"-"+split[1]+"-"+split[0]
		with open('students.csv', 'a', newline='') as csv_file:
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow(result)
			flash("Student added to the Database!")
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
			flash(f"Student ID: {id[0]} not found, Please try again!", "info")
		else:	
			result = dict(zip(keys, details))
			return render_template("search-student.html", data=True, result=result)
	return render_template("search-student.html", data=False, result="")

@app.route("/display")
def display():
	with open('students.csv', 'r') as csv_file:
		csv_reader = list(csv.reader(csv_file))
		temp = csv_reader.copy()
		if len(list(temp)) == 0:
			flash("No Students to Display", "info")
			return render_template("display-student.html", result="")
		else:
			print(len(list(temp)))
			return render_template("display-student.html", result=csv_reader)

if __name__=="__main__":
<<<<<<< HEAD
	keys=[]
	with open('students.csv', 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		keys = csv_reader.fieldnames
		print(keys)
	app.run(debug=True)
=======
	app.run()
>>>>>>> c00cceabf18bca2f5dc772d234323bb4fae46c7a

