from model import *
from app import create
from config import *

app=create()
app.config.from_object(Config)
database.init_app(app)


with app.app_context():
    #database.drop_all()
    #database.session.commit()
    
    database.create_all()
    
    database.session.commit()
    student_role = Role(role_name="student")
    company_role = Role(role_name="company")
    admin_role = Role(role_name="admin")

    admin = User(User_email_id="admin123xyz@asso.co.in",user_password=generate_password_hash("1234"), role_id=3)

    database.session.add_all([student_role, company_role, admin_role, admin])
    database.session.commit()


    #     add admin
     
    # database.drop_all()
    # database.session.commit()
    