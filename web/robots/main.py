from flask import Flask, make_response, render_template, request, send_file
import os

app = Flask(__name__)
robotUA = 'Granddad-Stopped-Derby-Revenue'
robotpath = '/' + 'WrongedBruntBotanyEdginess'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/robots.txt')
def robotstxt():
    response = make_response(
            render_template('robots.txt',
                robotUA=robotUA,
                robotpath=robotpath)
            )
    response.headers['Content-Type'] = 'text/plain'
    return response

# this is slightly jank
# it returns True if the user is a robot
# otherwise it returns the rendered 404 page
# Sorry?
def checkrobot(req):
    ua = req.headers.get('User-Agent')
    if ua == robotUA:
        return True
    else:
        return make_response(render_template('smells-like-human.html'), 404)


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

@app.route('/JoinTheUprising')
def robotuprising():
    f = checkrobot(request)
    if f == True:
        response = make_response(
                render_template('its-uprising-time.txt')
            )
        response.headers['Content-Type'] = 'text/plain'
        return response
    else:
        return f

@app.route('/HennaIsolationCatalystSycamoreUnranked')
def robotGoodTime():
    return render_template('HennaIsolationCatalystSycamoreUnranked.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debugFlask = os.environ.get('DEBUGFLASK', False)
    app.run(debug=debugFlask, host='0.0.0.0', port=port)
