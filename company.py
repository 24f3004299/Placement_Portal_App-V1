#from app import app
from flask import render_template, url_for, request, redirect
from datetime import datetime
from model import *
from flask import Blueprint,session
from flask_login import login_required
compn=Blueprint('company','__name__')
from model import Role, User, Company, Student, database
from dataSource import *
#@login_required
@compn.route('/company/<int:idi>', methods=['GET','POST'])
#@login_required
def company(idi):
    c=Company.query.filter_by(User_id=idi).first()
    if c.status=="approved":
        return render_template("company.html",idi=idi)
        
    else:
        stat=Company.query.filter_by(User_id=idi).first().status
        return render_template("com_stat.html",stat=stat)
        
@compn.route('/create/job/post<int:idi>', methods=['GET','POST'])
def job(idi):
    if request.method=="GET":
        return render_template("Drive.html")
    if request.method=="POST":
        info=Drive(
            drive_name=request.form["drive_name"],
            company=idi,
            skill=request.form["skill"],
            eligibility=request.form["eligibility"],
            experience=request.form["experience"],
            typeof=request.form["typeof"],
            location=request.form["location"],
            role=request.form["role"],
            perk=request.form["perk"],
            policy=request.form["policy"],
            deadline=datetime.strptime(request.form["deadline"], "%Y-%m-%d"),
            salary=request.form["salary"]

        )
        database.session.add(info)
        database.session.commit()
        return redirect(url_for('company.company',idi=idi))
@compn.route('/create/job/rifder<int:idi>', methods=['GET','POST'])
def manage(idi):
   if request.method=="GET":
       jobs=Drive_All(idi)[0]
       print(Drive_All(idi))
       return render_template("allDrivec.html",jobs=jobs,idi=idi)
   if request.method=="POST":
       print("post")
       if request.form["filter"]=="All":
           print(request.form["filter"])
           jobs=Drive_All(idi)[0]
           print(jobs)
           return render_template("allDrivec.html",jobs=jobs)
       elif request.form["filter"]=="Active":
           jobs=Drive_All(idi)[-1]
           return render_template("allDrivec.html",jobs=jobs)
       elif request.form["filter"]=="History":
           jobs=Drive_All(idi)[-2]
           return render_template("allDrivec.html",jobs=jobs)
       elif request.form["filter"]=="Pending":
           jobs=Drive_All(idi)[2]
           return render_template("allDrivec.html",jobs=jobs)
       elif request.form["filter"]=="Rejected":
           jobs=Drive_All(idi)[1]
           return render_template("allDrivec.html",jobs=jobs)
       else:
           return "I dont know!"
       
           
   
   
   
   
   pass
# view active drive 
# shows applicants
@compn.route("/check/update/<int:di>")
def driveUpdate(di):
    All_stu=ApplicationDetails(di)
    company=Drive.query.get(di).company
    return render_template('showapplicant.html',all=All_stu,company=company)
@compn.route('/update/status/student/<int:sid>/<int:aid>',methods=['GET','POST'])
def update(aid,sid):
    return render_template("view.html")
