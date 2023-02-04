from flask import Flask
app = Flask(__name__)
  
@app.route('/')
def hello():
    return "This is demoapp at 5001- > v3"
  
  
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True) 
