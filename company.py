#from app import app
from flask import render_template, url_for, request, redirect
from model import *
from flask import Blueprint,session
from flask_login import login_required
comp=Blueprint('company','__name__')


#@login_required
@comp.route('/company/<int:idi>')
#@login_required
def company(idi):
    c=Company.query.filter_by(User_id=idi).first()
    if c.status=="pending":
        return render_template("com_stat.html")
    else:
        return render_template("company.html")
@comp.route('/create/job/post<int: idi>')
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
            typeof=request.form["typeof"]

        )
        database.session.add(info)
    
   
