from flask import Flask, request,render_template, Response# loading in Flask
import json
import os
import subprocess
from subprocess import PIPE, Popen

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

# creating a Flask application
app = Flask(__name__,template_folder="template")


# creating user url and only allowing post requests.
@app.route('/newUser', methods=['GET','POST'])
def new():
    if request.method == 'POST':
        os.system('python3 request.py '+str(request.form.get('name')))

        return render_template('index.html', status="User Created")
    
    return render_template('index.html', status='')

@app.route('/', methods=['GET'])
def inex():
    return render_template('index.html', status='')

@app.route('/auth', methods=['POST'])
def auth():
    print(" ---------- [AUTH-START] ---------- ")

    user_name = request.form.get('name')
    out = subprocess.run(['python3','compare.py','-u',user_name],stdout=subprocess.PIPE)
    print("OUT ------ ");print(out)
    result = str(out).split('###')[7] #[1] is MSE , [3],TRUE OR FALSE
    print(" RESULT ----- ");print("-",result,"-")
    
    print(" ---------- [AUTH-END] ----------")

    if result == ' True ':
        return render_template('welcome.html', status=user_name)
    else:
        return render_template('index.html', status="Unrecognized face!")

if __name__ == '__main__':
    app.run(port=3000, debug=True)