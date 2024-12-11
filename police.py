from flask import* 
from database import*

police=Blueprint("police",__name__)

@police.route("/police_home")
def police_homepage():
    return render_template("police_home.html")

@police.route("/add_crime",methods=['get','post'])
def add_crime():

    if 'submit' in request.form:
        f_name=request.form['F_name']
        l_name=request.form['L_name']
        designation=request.form['desig']
        case_num=request.form['case_num']
        t_Of_crime=request.form['ty_of_crime']
        latitude=request.form['lati']
        longitude=request.form['longi']
        status=request.form['sta']

        # print(crime_num,station_num,f_name,l_name,designation,case_num,t_Of_crime,latitude,longitude,status,date)

        a="insert into add_crime values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s',curdate())"%(session['police_station'],f_name,l_name,designation,case_num,t_Of_crime,latitude,longitude,status)
        add_crime=insert(a)

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
            <h3>Crime Added Successfully</h3>
           
        </div>

        <script>
            // Close the alert box
            function closeAlert() {
                document.querySelector('.alert-box').style.display = 'none';
            }

            // Automatic redirect after 5 seconds
            setTimeout(() => {
                window.location = "/add_crime";
            }, 5000);
        </script>
    </body>
    </html>
    ''')

    return render_template("add_crime(P).html")


@police.route("/view_crime")
def view_crime():
    data={}
    qry="select * from add_crime where station_id='%s'"%(session['police_station'])
    res=select(qry)
    if res:
        data['view']=res
    return render_template("view_crime(P).html",data=data)