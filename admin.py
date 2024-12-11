from flask import* 
from database import*

admin=Blueprint("admin",__name__)

@admin.route("/admin_home")
def admin_homepage():
    return render_template("admin_home.html")


@admin.route("/manage_staff",methods=['get','post'])
def manage_staff():
     if 'submit' in request.form:
        f_name=request.form['f_n']
        l_name=request.form['l_n']
        gender=request.form['gen']
        dob=request.form['dob']
        state=request.form['s_t']
        district=request.form['d_t']
        city=request.form['c_y']
        address=request.form['a_s']
        pin=request.form['p_e']
        phno=request.form['p_r']
        altph=request.form['alt_ph']
        email=request.form['e_l']
        doj=request.form['doj']
        photo=request.form['p_o']
        uname=request.form['uname']
        psw=request.form['psw']

        a="insert into login values(null,'%s','%s','staff')"%(uname,psw)
        id=insert(a)

        b="insert into add_forensic_staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,f_name,l_name,gender,dob,state,district,city,address,pin,phno,altph,email,doj,photo)
        insert(b)

        return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registration Success</title>
        <style>
            /* Full-page container to center the alert */
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
            }

            /* Alert box styling */
            .alert-box {
                position: fixed;
                top: 20px;
                right: 20px;
                width: 300px;
                padding: 15px 20px;
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                animation: slideIn 0.5s ease-out;
            }

            /* Close button styling */
            .close-button {
                position: absolute;
                top: 8px;
                right: 8px;
                background: none;
                border: none;
                font-size: 18px;
                color: white;
                cursor: pointer;
            }

            .close-button:hover {
                color: #ddd;
            }

            /* Slide-in animation */
            @keyframes slideIn {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
        </style>
    </head>
    <body>
        <div class="alert-box">
            <button class="close-button" onclick="closeAlert()">×</button>
            <h3>Staff Succesfully Added</h3>
           
        </div>

        <script>
            // Close the alert box
            function closeAlert() {
                document.querySelector('.alert-box').style.display = 'none';
            }

            // Automatic redirect after 5 seconds
            setTimeout(() => {
                window.location = "/login";
            }, 5000);
        </script>
    </body>
    </html>
    ''')

     return render_template("staff_registration(A).html")    




@admin.route("/view_registered_police")
def view_registered_police():
    data={}
    qry="select * from police_station"
    res=select(qry)
    if res:
        data['view']=res
    return render_template("view_reg_police(A).html",data=data)


@admin.route("/view_court")
def view_court():
    data={}
    qry="select * from court"
    res=select(qry)
    if res:
        data['view']=res
    return render_template("view_court(A).html",data=data)

@admin.route("/view_crime(A)")
def view_crime():
    data={}
    qry="select * from add_crime"
    res=select(qry)
    if res:
        data['view']=res
    return render_template("view_crime(A).html",data=data)

@admin.route("/assign_staff(A)",methods=['get','post'])
def assign_staff():
    c_num=request.args['cnum']
    if 'submit' in request.form:
        forensic_id=request.form['fs_id']

        
        a="insert into assign_staff values(null,'%s','%s','pending')"%(forensic_id,c_num)
        insert(a)

        return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registration Success</title>
        <style>
            /* Full-page container to center the alert */
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
            }

            /* Alert box styling */
            .alert-box {
                position: fixed;
                top: 20px;
                right: 20px;
                width: 300px;
                padding: 15px 20px;
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                animation: slideIn 0.5s ease-out;
            }

            /* Close button styling */
            .close-button {
                position: absolute;
                top: 8px;
                right: 8px;
                background: none;
                border: none;
                font-size: 18px;
                color: white;
                cursor: pointer;
            }

            .close-button:hover {
                color: #ddd;
            }

            /* Slide-in animation */
            @keyframes slideIn {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
        </style>
    </head>
    <body>
        <div class="alert-box">
            <button class="close-button" onclick="closeAlert()">×</button>
            <h3>Assign Staff Successful!</h3>
           

        <script>
            // Close the alert box
            function closeAlert() {
                document.querySelector('.alert-box').style.display = 'none';
            }

            // Automatic redirect after 5 seconds
            setTimeout(() => {
                window.location = "/login";
            }, 5000);
        </script>
    </body>
    </html>
    ''')
    
    data={}
    qry="select * from add_forensic_staff"
    res=select(qry)
    if res:
        data['view']=res
    return render_template("assign_staff(A).html",data=data)