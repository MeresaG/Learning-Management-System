from flask import render_template
from application import app
from flask_login import login_required
@app.route('/')
@app.route("/index")
@login_required
def index():
    courses = [
                {
                    'course_name' : "Introduction to Python Programming",
                    'expiration_date' : 'January 21, 2020'
                },

                {
                    'course_name' : 'Introduction to Ethical hacking',
                    'expiration_date' : 'August 18,2019'
                }
    ]
    return render_template('index.html',title="CADI", courses = courses)