from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import session
from flask import Blueprint
from flask_login import LoginManager, logout_user, login_user, login_required

#from app import create
from flask import render_template, url_for, request, redirect, flash
from model import Role, User, Company, Student, database

#app=create()
# login maneger create
manager = LoginManager()
log=Blueprint('log','__name__')
manager.view='login'
@manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@log.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method=="POST":
            
            email = request.form["email_id"]
            password = request.form["pass"]
            info = User.query.filter_by(User_email_id=email).first()
            print(info)
            if info == None:
                flash('Wrong email')
                return render_template('login.html')
            else:
                print("not null")
                print(check_password_hash(info.user_password, password))
                if check_password_hash(info.user_password, password):
                    print("check pass")
                    user={"user_label":info.user_id,"email":info.User_email_id,"role":Role.query.get(info.role_id).role_name}
                    print(user)

                    if user["role"]=="admin":
                        print("hit")
                        print(session)
                        return redirect(url_for('admin.admin'))
                    elif str(user["role"]).upper=="COMPANY":
                        return redirect(url_for('company.company',idi=user["user_label"]))
                    elif str(user["role"]).upper=="STUDENT":
                        return redirect(url_for('student.student',idi=user["user_label"]))
                

                else:
                        flash('Wrong password')
                        return render_template('login.html')
@log.route('/log/out')
def logout():
    logout_user()
    session.clear()
    print(session)
    return redirect(url_for('log.login'))

@log.route('/registration/<int:user>', methods=['GET','POST'])
def registration(user):
    if request.method=='GET':
        return render_template('form.html')
    elif request.method=='POST':
        c=Company.query.filter_by(User_id=user).first()
        c.Name=request.form["Company_Name"]
        c.about=request.form["Company_about"]
        c.website=request.form["Company_website"]
        c.contact=request.form["Company_contact"]
        database.session.add(c)
        database.session.commit()
        return redirect(url_for('company.company',idi=user))

@log.route('/register',methods=['GET','POST'])
def Create():
    if request.method == "GET":
        return render_template('register.html')
    elif request.method == "POST":
        email = request.form["email"]
        create=request.form["pass"]
        confirm=request.form["Cpass"]
        
        pass_hash = generate_password_hash(request.form["pass"])
    
        use = request.form["Type"]
        print(use)
        # get userid
        idi = Role.query.filter_by(role_name=use).first()
        print(idi)
        id_new = idi.role_id

        # construct new User
        user = User(User_email_id=email, user_password=pass_hash, role_id=id_new)
        database.session.add(user)
        database.session.commit()
        stu = user.user_id
        print(id_new)
        if id_new == 1:
            candidate = Student(User_id=stu)
            database.session.add(candidate)
            database.session.commit()
        elif id_new == 2:
            print('hello')
            candidate = Company(User_id=stu)
            database.session.add(candidate)
            database.session.commit()
            return redirect(url_for('log.registration',user=stu))

