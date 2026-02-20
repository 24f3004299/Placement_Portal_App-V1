#from app import app
from flask import render_template, url_for, request, redirect
from db import *
from flask import Blueprint,session
from flask_login import login_required
comp=Blueprint('company','__name__')


#@login_required
@comp.route('/company/<int:idi>')
#@login_required
def company(idi):
    return render_template("company.html")
   