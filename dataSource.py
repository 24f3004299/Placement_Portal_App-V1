from model import Role, Drive, User, Company, Student, database, Application
from datetime import datetime
def Drive_All(idi):
    Drives=Drive.query.filter_by(company=idi).all()
    All=[]
    History=[]
    Active=[]
    Rejected=[]
    Pending=[]
    

    for job in Drives:
        each={"no":len(Application.query.filter_by(drive_id=job.drive_id).all()),
            "drive_id":job.drive_id,
            "drive_name": job.drive_name,
            "company_idi":idi,
            "company_name":Company.query.filter_by(User_id=idi).first().Name,
            "skill":job.skill,
            "eligibility":job.eligibility,
            "experience":job.experience,
            "typeof":job.typeof,
            "location":job.location,
            "role":job.role,
            "perk":job.perk,
            "policy":job.policy,
            "status":job.status, 
            "deadline":job.deadline,
            "salary":job.salary
            }
        All.append(each)
        if each["status"]=="active":
            Active.append(each)
        elif each["status"]=="closed":
            History.append(each)
        elif each["status"]=="pending":
            Pending.append(each)
        elif each["status"]=="rejected":
            Rejected.append(each)
    print([All,Rejected,Pending,History,Active])
    return [All,Rejected,Pending,History,Active]
def all(idi):
    return Drive_All(idi)[0]
    
def rejected(idi):
    return Drive_All(idi)[1]
   # print(Drive_All(idi)[1])
def pending(idi):
    return Drive_All(idi)[2]
    
def history(idi):
    return Drive_All(idi)[3]

def active(idi):
    return Drive_All(idi)[4]


#Get companies with status and shortlist by status    
def get_company():
        c=Company.query.all()


        lis=[]
        pending_companies=[]
        rejected_companies=[]
        approved_companies=[]

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
            if info["status"]=="pending":
                pending_companies.append(info)
            elif info["status"]=="rejected":
                rejected_companies.append(info)
            elif info["status"]=="approved":
                approved_companies.append(info)
        return {"all":lis,"pending":pending_companies,"approved":approved_companies,"rejected":rejected_companies}
        
#Drive for each
#   
def get_drive_all():
        c=Drive.query.all()

        lisd=[]
        pending_drives=[]
        closed_drives=[]
        active_drives=[]
        for job in c:
            each={
            "no":len(Application.query.filter_by(drive_id=job.drive_id).all()),
            "drive_id":job.drive_id,
            "drive_name": job.drive_name,
            "company_name":Company.query.filter_by(User_id=job.company).first().Name,
            "skill":job.skill,
            "eligibility":job.eligibility,
            "experience":job.experience,
            "typeof":job.typeof,
            "location":job.location,
            "role":job.role,
            "perk":job.perk,
            "policy":job.policy,
            "status":job.status,
            "company_status":Company.query.filter_by(User_id=job.company).first().status,
            "deadline":job.deadline,
            "salary":job.salary}
            if each["company_status"]=="approved":
                lisd.append(each)
                if each["status"]=="active":
                    active_drives.append(each)
                elif each["status"]=="closed":
                    closed_drives.append(each)
                 
                elif each["status"]=="pending":
                    pending_drives.append(each)
            
        return {"all":lisd, "closed":closed_drives, "pending":pending_drives, "active":active_drives }
def getDriveByid(idi):
     job=Drive.query.get(idi)

     each={ "no":len(Application.query.filter_by(drive_id=idi).all()),
            "drive_id":"DRIVE"+str(job.drive_id),
            "salary":job.salary,
            "drive_id":job.drive_id,
            "drive_name": job.drive_name,
            "company_name":Company.query.filter_by(User_id=job.company).first().Name,
            "skill":job.skill,
            "eligibility":job.eligibility,
            "experience":job.experience,
            "typeof":job.typeof,
            "location":job.location,
            "role":job.role,
            "perk":job.perk,
            "policy":job.policy,
            "status":job.status,
            "company_status":Company.query.filter_by(User_id=job.company).first().status,
            
            "deadline":job.deadline,
            "salary":job.salary
            }
     
     if each["status"]=="active":
         return each
     else:
         return {}


 # company show aplicant
 # algo:-info drive id
 #
def ApplicationDetails(idi):
    applications=Application.query.filter_by(drive_id=idi).all()
    students=[]
    for applicant in applications:
        stu=Student.query.filter_by(User_id=applicant.student_id).first()
        data={
            "applicationId":applicant.application_id,
            "cid":Drive.query.get(idi).company,
            "rono":stu.student_id,
            "student-id":applicant.student_id,
            "student_Name":Student.query.filter_by(User_id=applicant.student_id).first().student_Name,
            "Department/Major":stu.Department,
            "Resume":stu.resume,
            "Higher_qualification":stu.Higher_qualification,
            "Job Title":Drive.query.filter_by(drive_id=applicant.drive_id).first().drive_name,
            "Job Drive":"DRIVE"+str(applicant.drive_id),
            "Company":Company.query.filter_by(User_id=Drive.query.filter_by(drive_id=idi).first().company).first().Name,
            
         
        }
        students.append(data)
    return students
#def viewStudent(idi):
def all_incl_drive(idi):
    job=Drive.query.get(idi)

    each={"no":len(Application.query.filter_by(drive_id=job.drive_id).all()),
        "drive_id":"DRIVE"+str(job.drive_id),
            "salary":job.salary,
            "drive_id":job.drive_id,
            "drive_name": job.drive_name,
            "company_name":Company.query.filter_by(User_id=job.company).first().Name,
            "skill":job.skill,
            "eligibility":job.eligibility,
            "experience":job.experience,
            "typeof":job.typeof,
            "location":job.location,
            "role":job.role,
            "perk":job.perk,
            "policy":job.policy,
            "status":job.status,
            "company_status":Company.query.filter_by(User_id=job.company).first().status,
            
            "deadline":job.deadline,
            "salary":job.salary
            }
    return each
#application particiapants
def getInfoDrive(idi):
    appli=Application.query.get(idi)
    student=Student.query.filter_by(User_id=appli.student_id).first()
    drive=Drive.query.filter_by(drive_id=appli.drive_id).first()
    info={
        "student_Name":student.student_Name,
        "Drive Name":"DRIVE"+" "+str(drive.drive_id),
        "drive_id":drive.drive_id,
        "Job Title":drive.drive_name,
        "resume":student.resume,
        "Department":student.Department,
        "Higher Qualification":student.Higher_qualification,
        "company Name":Company.query.filter_by(User_id=drive.company).first().Name,
        "status":appli.status,
        "applied on":appli.applied_on
        
    }
    return info
