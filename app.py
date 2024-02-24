from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from events import Events
from course_info import main
from resourcesAPI import getTextBookLinks

app = Flask(__name__)
app.secret_key = "secretKey4us"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def home():
    if "discipline" in session:
        return render_template("index.html", courses=session["courses"], discipline=session["discipline"])
    else:
        return redirect(url_for("login"))

@app.route("/user/", methods=["POST", "GET"])
def user():
    discipline = None
    if "discipline" in session:
        if request.method == "POST":
            discipline = request.form["discipline"]
            courses = request.form['courses']
            session["discipline"] = discipline
            session["courses"] = courses.split(',')
            
        else:
            if "discipline" in session:
                discipline = session["discipline"]
                
        return render_template("user.html", discipline=session["discipline"], courses=session["courses"])
    else:
        return redirect(url_for("login"))

@app.route("/resources/")
def resources():
    books_list = {} # Dictionary of dictionaries of links with title as key for each course as the main key
    if "discipline" in session:
        for course in session["courses"]:
            book_links = getTextBookLinks(main(course)) # Dictionary of links with title as key
            books_list[course] = book_links
        #return books_list
        return render_template("resources.html", booksByCourses=books_list, courses=session["courses"])
        
    else:
        return redirect(url_for("login"))

@app.route("/events/", methods=["POST", "GET"])
def events():
    if "discipline" in session:
        res = Events(session["discipline"])
        return render_template("events.html", content=res)
        
    else:
        return redirect(url_for("login"))
    
@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        discipline = request.form["discipline"]
        courses = request.form['courses']
        
        if discipline == "" or courses == "":
            return redirect(url_for("login"))
        
        courses = [course.strip() for course in courses.split(",")] #courses.split(',')
        #print(courses)
        
        session["discipline"] = discipline
        session["courses"] = courses
        #print(discipline, courses)
        
        return redirect(url_for("home"))
    else:
        return render_template("login.html")
    
@app.route("/logout/")
def logout():
    session.pop("discipline", None)
    session.pop("courses", None)
    return redirect(url_for("login"))

"""
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!!")) """

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000, threaded=True)