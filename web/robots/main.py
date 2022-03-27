from flask import Flask, make_response, render_template, request
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

@app.route(robotpath)
def robotflag():
    ua = request.headers.get('User-Agent')
    if ua == robotUA:
        response = make_response(
            render_template('great-job-fellow-robot.txt')
            )
        response.headers['Content-Type'] = 'text/plain'
        return response
    else:
        return make_response(render_template('smells-like-human.html'), 404)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debugFlask = os.environ.get('DEBUGFLASK', False)
    app.run(debug=debugFlask, host='0.0.0.0', port=port)
