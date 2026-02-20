#from app import app
from flask import render_template, url_for, request, redirect
from db import *
from flask import Blueprint,session
from flask_login import login_required
adm=Blueprint('admin','__name__')


#@login_required
@adm.route('/admin')
#@login_required
def admin():
    return render_template("admin.html")
   