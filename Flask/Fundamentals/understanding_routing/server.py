from flask import Flask  
app = Flask(__name__) 
@app.route('/')   
def hello_world():
    return 'Hello World!'  
    
@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>') 
def say(name):
    print(name)
    return "Hi " + name.capitalize() + "!"

@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"{word}"

    return output

if __name__=="__main__":    
    app.run(debug=True)   
    