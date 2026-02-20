from app import create
app=create()
from model import *
from config import *
from flask import session


from login import manager
from login import log
from student import stu
from admin import adm
from company import comp
app.config.from_object(Config)
manager.init_app(app)


app.register_blueprint(log)
app.register_blueprint(stu)
app.register_blueprint(comp)
app.register_blueprint(adm)
database.init_app(app)
#with app.app_context():
    #database.create_all()
    #database.session.commit()
    #student_role = Role(role_name="student")
    #company_role = Role(role_name="company")
    #admin_role = Role(role_name="admin")

    #admin = User(User_email_id="admin123xyz@asso.co.in",user_password=generate_password_hash("1234"), role_id=3)

    #database.session.add_all([student_role, company_role, admin_role, admin])
    #database.session.commit()


    #     add admin
     
    # database.drop_all()
    # database.session.commit()
    




if __name__=='__main__':
    app.run(debug=True)
