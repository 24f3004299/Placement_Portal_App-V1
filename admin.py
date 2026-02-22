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
   
