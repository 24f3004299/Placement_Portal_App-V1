from model import Role, Drive, User, Company, Student, database
def Drive_All(idi):
    Drives=Drive.query.filter_by(company=idi).all()
    All=[]
    History=[]
    Active=[]
    Rejected=[]
    Pending=[]
    

    for job in Drives:
        each={
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
            "status":job.status
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
            "status":job.status
            }
            lisd.append(each)
            if each["status"]=="active":
                active_drives.append(each)
            elif each["status"]=="closed":
                closed_drives.append(each)
                 
            elif each["status"]=="pending":
                pending_drives.append(each)
            
        return {"all":lisd, "closed":closed_drives, "pending":pending_drives, "active":active_drives }
           