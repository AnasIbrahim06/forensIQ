from flask import*
from database import *
from public import public
from police import police
from court import court
from admin import admin
from staff import staff

a=Flask(__name__)
a.register_blueprint(public)
a.register_blueprint(police)
a.register_blueprint(court)
a.register_blueprint(admin)
a.register_blueprint(staff)

a.secret_key='kjhgfdz'
                
a.run(debug=True,port=5004)

