#from app import app
from flask import render_template, url_for, request, redirect
from model import *
from flask import Blueprint,session
from flask_login import login_required
compn=Blueprint('company','__name__')
from model import Role, User, Company, Student, database

#@login_required
@compn.route('/company/<int:idi>', methods=['GET','POST'])
#@login_required
def company(idi):
    c=Company.query.filter_by(User_id=idi).first()
    if c.status=="pending":
        return render_template("com_stat.html")
    else:
        return render_template("company.html",idi=idi)
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
            policy=request.form["policy"]

        )
        database.session.add(info)
    return redirect(url_for('company.company',idi=idi))
@compn.route('/create/job/rifder<int:idi>', methods=['GET','POST'])
def manage(){
   pass
}
   
