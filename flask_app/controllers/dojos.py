from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import ninja, dojo # import entire file, rather than class, to avoid circular imports

# Create Users Controller

@app.route("/dojos/create", methods=['POST'])
def create_dojo():
    dojo.Dojo.create_dojo(request.form)
    return redirect('/')


# Read Users Controller

@app.route('/')
def show_all_dojos():
    dojos_all = dojo.Dojo.get_all_dojos()
    return render_template('dojo.html', dojos_all = dojos_all)

@app.route('/ninja_list/<int:id>/dojo_location/')
def get_ninja_list_dojo_location(id):
    ninja_home = dojo.Dojo.get_dojos_with_ninjas(id)
    return render_template('dojo_show.html', ninja_home = ninja_home)


# Update Users Controller



# Delete Users Controller


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')
# def index(id):
#     user_info = user.User.get_user_by_id(id)
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.