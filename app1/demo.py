from flask import Flask
app = Flask(__name__)
  
@app.route('/')
def hello():
    return "This is demo app1 at 3000- > v1"
  
  
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 3000, debug = True) 
