from flask import Flask   #Importing flask library

app = Flask(__name__)    #Creating our flask app to run

@app.route('/home/users/<string:name>/posts/<int:id>')   # Domain comes here  #<string:name> is variable
def hello(name,id):        #Function   --> name should be same as <string:name>
    return "Hello, "+ name + " your id is: " + str(id)

@app.route('/learnmethods',methods=['GET','POST'])  # here we can decalare both http methods
def getMethod():
    return "Hello It's Get Method"

if __name__ == '__main__':
    app.run(debug=True)    #running our function in debug mode
