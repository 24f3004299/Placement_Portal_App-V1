#from app import app
from flask import render_template, url_for, request, redirect
from model import *
from flask import Blueprint,session
from flask_login import login_required
from dataSource import *
adm=Blueprint('admin','__name__')

# dashboard
#@login_required
@adm.route('/admin')
#@login_required
def admin():
    count_comp=len(Company.query.filter_by(status="approved").all())
    count_stu=len(Student.query.all())
    count_drive=len(Drive.query.filter_by(status="active").all())
    return render_template("admin.html",count_comp=count_comp,count_stu=count_stu,count_drive=count_drive)
#manage company
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
            print(lisi)
            return render_template("pending_company.html",lisi=lisi,state="all")
           
           
       elif request.form["filter"]=="Approved":
           print('hit')
           lisi=get_company()["approved"]
           return render_template("pending_company.html",lisi=lisi,state="approved")
           
       elif request.form["filter"]=="Pending":
           lisi=get_company()["pending"]
           print(lisi)
           return render_template("pending_company.html",lisi=lisi,state="pending")

       elif request.form["filter"]=="Rejected":
           lisi=get_company()["rejected"]
           return render_template("pending_company.html",lisi=lisi,state="rejected")
       else:
           return "I dont know!"
       
       
# company status update 
        
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
       return render_template("adminXdrive.html",lisi=lisi,state="all")
    if request.method=="POST":
       print("post")
       if request.form["filter"]=="All":
            lisi=get_drive_all()["all"]
            return render_template("adminXdrive.html",lisi=lisi,state="all")
           
           
       elif request.form["filter"]=="Completed":
           print('hit')
           lisi=get_drive_all()["closed"]
           return render_template("adminXdrive.html",lisi=lisi,state="closed")
           
       elif request.form["filter"]=="Pending":
           lisi=get_drive_all()["pending"]
           return render_template("adminXdrive.html",lisi=lisi,state="pending")

       elif request.form["filter"]=="Ongoing":
           lisi=get_drive_all()["active"]
           return render_template("adminXdrive.html",lisi=lisi,state="ongoing")
       else:
           return "I dont know!"
       
#  update manage drive
@adm.route('/update/status/drive/<int:idid>')
def update_drive(idid):
    if Drive.query.get(idid).status=="pending":
        Drive.query.get(idid).status="active"
        database.session.commit()
        return redirect(url_for('admin.request_drive'))
    elif Drive.query.get(idid).status=="active":
        Drive.query.get(idid).status="closed"
        database.session.commit()
        return redirect(url_for('admin.request_drive'))
    


    pass
# view student
#@adm.route('/drive/to/applicants/<di=di>')
@adm.route('/drive/to/company/<int:di>')
def view_drive_com(di):
    if request.method=="GET":
        #app=Application.query.filter(Application.drive_id==di,Application.student_id==idi).all()
        about=all_incl_drive(di)
        return render_template("Appllicant.html",about=about, di=di,user="admin")
#update student
# search 
#view applicants
@adm.route('/reject/<int:di>')
def rejectD(di):
    Drive.query.get(di).status="Rejected"
    database.session.commit()
    return redirect(url_for('admin.request_drive'))
# view application by students for a drive
@adm.route('/view/applicant/application/<int:appli>',methods=["GET","POST"])
def applyView(appli):
    print("hit")

    info=getInfoDrive(appli)
    print(info)
    
    return render_template('view.html',user="admin",info=info)
@adm.route('/view/applicants/<int:di>',methods=['GET','POST'])
def driveSee(di):
    All_stu=ApplicationDetails(di)
    #company=Drive.query.get(di).company
    return render_template('showapplicant.html',all=All_stu,user="admin")

#manage student
@adm.route('/admin/manages/student')
def manageStu():
    stu=getStudent()
    return render_template('manage_stu.html',all=stu)
@adm.route('/del/<int:idi>')
def delStu(idi):
    stu=Student.query.get(idi)
    database.session.delete(User.query.filter_by(User_id=stu.User_id).first)
    database.session.commit()
    return render_template('manage_stu.html',all=stu)


