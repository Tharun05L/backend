students={
           '18PT01':{
                     'name':'name0',
                     'classs':'18pt'
                     },
           '18PD01':{
                     'name':'name1',
                     'classs':'18pd'
                     }
           }


from flask import Flask

app = Flask(__name__)

@app.route("/students")
def hello_world():
    return students

if __name__=="__main__":
    app.run() 