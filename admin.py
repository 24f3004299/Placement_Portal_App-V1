#from app import app
from flask import render_template, url_for, request, redirect
from model import *
from flask import Blueprint,session
from flask_login import login_required
from dataSource import *
adm=Blueprint('admin','__name__')


#@login_required
@adm.route('/admin')
#@login_required
def admin():
    count_comp=len(Company.query.filter_by(status="approved").all())
    count_stu=len(Student.query.all())
    count_drive=len(Drive.query.filter_by(status="active").all())
    return render_template("admin.html",count_comp=count_comp,count_stu=count_stu,count_drive=count_drive)
   
#@login_required
@adm.route('/request',methods=['GET','POST'])
#@login_required
def request_company():
    if request.method=="GET":
       lisi=get_company()["all"]
       return render_template("pending_company.html",lisi=lisi,state="all")
    if request.method=="POST":
       print("post")
       if request.form["filter"]=="All":
            lisi=get_company()["all"]
            return render_template("pending_company.html",lisi=lisi,state="all")
           
           
       elif request.form["filter"]=="Approved":
           print('hit')
           lisi=get_company()["approved"]
           return render_template("pending_company.html",lisi=lisi,state="approved")
           
       elif request.form["filter"]=="Pending":
           lisi=get_company()["pending"]
           return render_template("pending_company.html",lisi=lisi,state="pending")

       elif request.form["filter"]=="Rejected":
           lisi=get_company()["rejected"]
           return render_template("pending_company.html",lisi=lisi,state="rejected")
       else:
           return "I dont know!"
       
       

        
@adm.route("/update/staus/<int:idi>")
def update(idi):
    c=Company.query.get(idi)
    if c.status=="pending":
        c.status="approved"
        database.session.commit()
        return redirect(url_for('admin.request_company'))
    if c.status=="approved":
        c.status="rejected"
        database.session.commit()
    if c.status=="rejected":
        c.status="approved"
        database.session.commit()
        return redirect(url_for('admin.request_company'))
    
# admin and Drives 
@adm.route('/drives/request',methods=['GET','POST'])
#@login_required
def request_drive():
    if request.method=="GET":
       lisi=get_drive_all()["all"]
       return render_template("pending_company.html",lisi=lisi,state="all")
    if request.method=="POST":
       print("post")
       if request.form["filter"]=="All":
            lisi=get_company()["all"]
            return render_template("pending_company.html",lisi=lisi,state="all")
           
           
       elif request.form["filter"]=="Approved":
           print('hit')
           lisi=get_company()["approved"]
           return render_template("pending_company.html",lisi=lisi,state="approved")
           
       elif request.form["filter"]=="Pending":
           lisi=get_company()["pending"]
           return render_template("pending_company.html",lisi=lisi,state="pending")

       elif request.form["filter"]=="Rejected":
           lisi=get_company()["rejected"]
           return render_template("pending_company.html",lisi=lisi,state="rejected")
       else:
           return "I dont know!"
       
       


