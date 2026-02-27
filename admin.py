#from app import app
from flask import render_template, url_for, request, redirect
from model import *
from flask import Blueprint,session
from flask_login import login_required
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
@adm.route('/request')
#@login_required
def request_company():
    if request.method=="GET":
        c1=Company.query.filter_by(status="pending").all()
        c2=Company.query.filter_by(status="approved").all()
        c=c1+c2

        lis=[]
        for i in c:
            info={
                "sl":i.company_id,
                "Name":i.Name,
                "Website":i.website,
                "status":i.status,
                "Location":i.Location,
                "about":i.about,
                "user":i.User_id
            }
            lis.append(info)

        return render_template("pending_company.html",lis=lis)
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
        return redirect(url_for('admin.request_company'))