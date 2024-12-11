from flask import* 
from database import*

staff=Blueprint("staff",__name__)

#staff homepage
@staff.route("/staff_home")
def staff_homepage():
    return render_template("staff_home.html")

@staff.route("/view_profile",methods=['get','post'])
def view_crime():
    data={}
    qry="select * from add_forensic_staff where forensic_id='%s'"%(session['staff'])
    res=select(qry)
    if res:
        data['view']=res
    if "action" in request.args:
        a=request.args['action']
        b=request.args['id']
        if a =='update':
            c="select * from add_forensic_staff where forensic_id='%s'"%(b)
            res1=select(c)
            data['upd']=res1
            if 'update' in request.form:
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

                b="update add_forensic_staff set f_name='%s',l_name='%s',gender='%s',dob='%s',state='%s',district='%s',city='%s',address='%s',pincode='%s',phone='%s',alternative_phone='%s',email='%s',doj='%s',photo='%s' where forensic_id='%s'"%(f_name,l_name,gender,dob,state,district,city,address,pin,phno,altph,email,doj,photo,b)
                update(b)

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
                    <h3>Updated Successfully</h3>
                
                </div>

                <script>
                    // Close the alert box
                    function closeAlert() {
                        document.querySelector('.alert-box').style.display = 'none';
                    }

                    // Automatic redirect after 1.5 seconds
                    setTimeout(() => {
                        window.location = "/view_profile";
                    }, 1500);
                </script>
            </body>
            </html>
            ''')


    return render_template("view_profile(S).html",data=data)


@staff.route("/view_allocated_case")
def view_allocated_case():
    # group by add_crime.crime_num
    data={}
    # qry="SELECT * FROM assign_staff INNER JOIN add_forensic_staff INNER JOIN add_crime INNER JOIN police_station WHERE add_forensic_staff.forensic_id='%s' group by police_station.district "%(session['staff'])
    qry="SELECT * FROM assign_staff INNER JOIN add_forensic_staff USING(forensic_id) INNER JOIN add_crime USING(crime_num) INNER JOIN police_station USING(station_id) WHERE forensic_id='%s'"%(session['staff'])
    res=select(qry)
    if res:
        data['view']=res

    if "action" in request.args:
        action=request.args['action']
        b=request.args['id']
      
        if action=='verified':
            zy="update assign_staff set status='verified' where assign_id='%s'"%(b)
            update(zy)
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
            <h3>Assigned Case verified!</h3>
           
        </div>

        <script>
            // Close the alert box
            function closeAlert() {
                document.querySelector('.alert-box').style.display = 'none';
            }

            // Automatic redirect after 1.5 seconds
            setTimeout(() => {
                window.location = "/view_allocated_case";
            }, 1500);
        </script>
    </body>
    </html>
    ''')

            

              



    return render_template("view_allocated_case(S).html",data=data)

# @staff.route("/verify_staff(S)",methods=['get','post'])
# def verify_staff():
    

#         # return '''<script>alert(" verified successfully");window.location="/view_allocated_case"</script>'''
#     return render_template('')