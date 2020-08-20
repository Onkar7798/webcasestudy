from flask import *

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
	if request.method == "POST":
		req = list(request.form.values())
		print(req)
		if req[0] == "Add Student":
			return render_template("add-student.html")
		elif req[0] == "Search Student":
			return render_template("search-student.html")
		elif req[0] == "Display all Students":
			return render_template("display-student.html")
		else:
			return render_template("index.html")
	else:
		return render_template("index.html")

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

