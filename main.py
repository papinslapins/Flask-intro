from flask import Flask, render_template, request
from file_proc import read_file, write_file

app = Flask(__name__)

@app.route('/')
def index():
  return "<a href='/home'>HI!</a>"

@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = 22355704)

@app.route('/params')
def params():
  return render_template('params.html', args = request.args)

@app.route('/read_from_file')
def readFromFile():
  content = read_file()
  return content

@app.route('/write_to_file, methods = ['POST'])
def writeToFile():
  request_type = request.content_type
  if(request.type == 'application/json'):
    contentJSON = request.get_json()
    write_file(contentJSON['data'])

    return contentJSON

  else:

    return f"Request type '{request_type} not supported!"

  

@app.route('/file', methods = ['POST', 'GET'])

def fileWork():

  if request.method == 'GET':

    return readFromFile()

  elif request.method == 'POST':

    return writeToFile()
    
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 6211, threaded = True, debug = True)
