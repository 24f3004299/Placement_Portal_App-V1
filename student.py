#from app import app
from flask import render_template, url_for, request, redirect
from db import *
from flask import Blueprint,session
from flask_login import login_required
stu=Blueprint('student','__name__')


#@login_required
@stu.route('/student/<int:idi>')
#@login_required
def student(idi):
    return  render_template("student.html",idi=idi)
   