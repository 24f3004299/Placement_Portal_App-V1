#from app import app
from flask import render_template, url_for, request, redirect
from model import *
from flask import Blueprint,session
from flask_login import login_required
stu=Blueprint('student','__name__')
import os # for file upload system
from dataSource import *
#####
os.makedirs("uploads",exist_ok=True)
# concept: make a new directory, no error if already exist

from datetime import datetime,date

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
        current.Department=request.form["dept"]
        current.student_Name=request.form["name"]

       
        database.session.commit()
        return render_template("view.html",link=current.resume)
@stu.route('/student/dash/drive/<int:idi>',methods=['GET','POST'])
def show_active(idi):
    active=get_drive_all()["active"]
    return render_template('studentXjobs.html',actives=active, idi=idi)

@stu.route('/apply/NOW/<int:idi>/<int:di>',methods=["GET","POST"])
def Applicant(idi,di):
    if request.method=="GET":

        app=Application.query.filter(Application.drive_id==di,Application.student_id==idi).all()
        about=getDriveByid(di)
        #print(about)
        if app:
            
            return render_template("Appllicant.html",about=about,idi=idi, di=di,button="applied", message="already applied , Go to 'My application' page ",user="student")
        else:
            return render_template("Appllicant.html",about=about,idi=idi, di=di,button="", message="",user="student")
            

@stu.route('/Apply/BUtton/Doit/<int:idi>/<int:di>')
def apply(idi,di):
    new_Applicant=Application(drive_id=di, student_id=idi,applied_on=date.today())
    database.session.add(new_Applicant)
    database.session.commit()
    return render_template("application_end_point.html",idi=idi)
#button For my applications
@stu.route('/view history/<int:idi>')
def History(idi):
    app=byStu(idi)
    return render_template("history.html",tot=app,idi=idi)
