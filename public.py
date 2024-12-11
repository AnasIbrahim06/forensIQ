from flask import *
from database import *



public=Blueprint("public",__name__)

@public.route("/")
def home():
    return render_template("home.html")


@public.route("/login",methods=['get','post'])
def login():
#police
    if'submit'in request.form:
        uname=request.form['uname']
        psw=request.form['psw']

        print(uname,psw)

        qry="select * from login where username='%s' and password='%s'"%(uname,psw)
        res=select(qry)
        if res:
            session['log']=res[0]['login_id']
        print(res)
        if res[0]['usertype']=='police':
            qry1="select * from police_station where login_id='%s'"%(session['log'])
            res1=select(qry1)
            if res1:
                session['police_station']=res1[0]['station_id']
            return redirect(url_for('police.police_homepage'))
        if res[0]['usertype']=='court':
            qry1="select * from court where login_id='%s'"%(session['log'])
            res1=select(qry1)
            if res1:
                session['court']=res1[0]['court_id']
            return redirect(url_for('court.court_homepage'))
        
        if res[0]['usertype']=='staff':
            qry1="select * from add_forensic_staff where login_id='%s'"%(session['log'])
            res1=select(qry1)
            if res1:
                session['staff']=res1[0]['forensic_id']
            return redirect(url_for('staff.staff_homepage'))
        
        if res[0]['usertype']=='admin':
            return redirect(url_for('admin.admin_homepage'))
        
        



   
        
    return render_template("login.html")

#police registration

@public.route("/police_register",methods=['get','post'])
def police_register():
    if 'submit' in request.form:
        register_number=request.form['sr_num']
        zone=request.form['zone']
        District=request.form['D_t']
        city=request.form['c_y']
        pincode=request.form['p_c']
        station_name=request.form['s_n']
        address=request.form['address']
        mail=request.form['e_m']
        phone=request.form['p_n']
        alt_phone=request.form['alt_p_n']
        uname=request.form['uname']
        psw=request.form['psw']
    
        print(register_number,zone,District,city,pincode,station_name,address,mail,phone,alt_phone,uname,psw)
        

        a="insert into login values(null,'%s','%s','police')"%(uname,psw)
        id=insert(a)

        b="insert into police_station values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,register_number,zone,District,city,pincode,station_name,address,mail,phone,alt_phone)
        insert(b)
         # Render success page with custom alert
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
            <h3>Registration Successful!</h3>
           
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
        



    return render_template("police_register.html")

#court registration

@public.route("/court_register",methods=['get','post'])
def court_register():
    if 'submit' in request.form:
        court_regno=request.form['crt_num']
        c_name=request.form['Cr_num']
        c_type=request.form['C_t']
        state=request.form['S_e']
        distr=request.form['D_t']
        address=request.form['A_d']
        pin=request.form['P_c']
        email=request.form['e_l']
        phno=request.form['p_n1']
        alt_phno=request.form['alt_p_n1']
        officer_name=request.form['O_n']
        uname=request.form['uname']
        psw=request.form['psw']


        print(court_regno,c_name,c_type,state,distr,address,pin,email,phno,alt_phno,officer_name,uname,psw)


        a="insert into login values(null,'%s','%s','court')"%(uname,psw)
        id=insert(a)

        b="insert into court values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,court_regno,c_name,c_type,state,distr,address,pin,email,phno,alt_phno,officer_name)
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
            <h3>Registration Successful!</h3>
            
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
    return render_template("court_register.html")
