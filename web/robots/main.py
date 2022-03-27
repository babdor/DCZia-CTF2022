from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from flask import send_file
from flask import send_from_directory
import base64
import os
import textwrap

app = Flask(__name__)
robotUA = 'Granddad-Stopped-Derby-Revenue'
robotpath = '/' + 'WrongedBruntBotanyEdginess'

# this is slightly jank
# it returns True if the user is a robot
# otherwise it returns the rendered 404 page
# Sorry?
def checkrobot(req):
    ua = req.headers.get('User-Agent')
    if ua == robotUA:
        return True
    else:
        return smellsLikeHuman()

def smellsLikeHuman():
    return make_response(render_template('smells-like-human.html'), 404)

@app.route('/')
def home():
    return render_template('index.html')

# This is "THE ROBOTS HAVE IT"
@app.route('/robots.txt')
def robotstxt():
    response = make_response(
            render_template('robots.txt',
                robotUA=robotUA,
                robotpath=robotpath)
            )
    response.headers['Content-Type'] = 'text/plain'
    return response


@app.route(robotpath)
def robotflag():
    f = checkrobot(request)
    if f == True:
        response = make_response(
            render_template('great-job-fellow-robot.txt')
            )
        response.headers['Content-Type'] = 'text/plain'
        return response
    else:
        return f

# This is "ROBOTS RISE"
@app.route('/JoinTheUprising')
def robotuprising():
    f = checkrobot(request)
    if f == True:
        if request.headers.get('X-Codeword', 'nope') == 'ZiaCTF{Unbent Graduate Wildness Caution Shortwave Creme}':
            # this file was generated with generate_email.py in this repo
            # in case you need to make changes
            with open('data/email.txt', mode='r') as emailFile:
                emailText = emailFile.read()

            emailB64 = textwrap.fill(base64.b64encode(bytes(emailText, 'utf-8')).decode(), width=74)

            response = make_response(
                    render_template('its-uprising-time.txt', 
                        base64thing=emailB64)
                )
            response.headers['Content-Type'] = 'text/plain'
            return response
        else:
            return smellsLikeHuman()
    else:
        return f

# This is "A ROBOTIC GOOD TIME"
@app.route('/HennaIsolationCatalystSycamoreUnranked')
def robotGoodTime():
    return render_template('HennaIsolationCatalystSycamoreUnranked.html')


## Misc non-challenge stuff
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debugFlask = os.environ.get('DEBUGFLASK', False)
    app.run(debug=debugFlask, host='0.0.0.0', port=port)
