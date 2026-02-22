#from app import app
from flask import render_template, url_for, request, redirect
from model import *
from flask import Blueprint,session
from flask_login import login_required
stu=Blueprint('student','__name__')
import os # for file upload system

#####
os.makedirs("uploads",exist_ok=True)
# concept: make a new directory, no error if already exist

from datetime import datetime

#@login_required
@stu.route('/student/<int:idi>',methods=['GET','POST'])
#@login_required
def student(idi):
    return  render_template("student.html",idi=idi)
@stu.route('/Update/<int:idi>',methods=['GET','POST'])
def Update(idi):
    if request.method=='GET':
        return render_template("student_update.html",idi=idi)
    if request.method=='POST':
        print(request.form)
        current=Student.query.filter_by(User_id=idi).first()
        current.Nationality=request.form["nation"]
        current.state=request.form["state"]
        current.location=request.form["area"]
        current.Dob=datetime.strptime(request.form["dob"], "%Y-%m-%d")
        # preprocess file
        resume=request.files["resume"]
        path=os.path.join("uploads",resume.filename)
        resume.save(path)
        current.resume=path

        current.Higher_qualification=request.form["qly"]
        current.contact=request.form["cont"]
       
        database.session.commit()
        return render_template("view.html",link=current.resume)

