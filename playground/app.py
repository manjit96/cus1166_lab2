from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/welcome/<string:name>")
def wel(name):
    return render_template("welcome.html", name=name)


@app.route("/roster/<string:grade_view>")
def roster(grade_view):
    class_roster = [("Jon", "A+", "Junior"), ("Sansa", "A", "Junior"), ("Arya", "B", "Sophomore"), ("Rhaegar", "A-", "Senior"), ("Ramsay", "F", "Junior"), ("Joffrey", "D+", "Freshman"), ("Robb", "B", "Senior"), ("Bran", "A-", "Sophomore")]
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)


if __name__ == '__main__':
    app.run(debug=True)
