from flask import Flask, request, jsonify, render_template
import ollama
import time
app = Flask(__name__)

modelfile='''
FROM llama2
SYSTEM You are a world class nutritionist. Respond in brief
'''
ollama.create(model='example', modelfile=modelfile)

resc="Error"
title="Title"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('ugh2.html')

@app.route('/receive_value', methods=['POST'])
def receive_value():
    global selected_value
    selected_value = request.json['selectedValue']
    print("Selected value received:", selected_value)
      
    response = ollama.chat(model='example', messages=[
    {
    'role': 'user',
    'content': selected_value,
    },
    ])
    global resc
    resc=response['message']['content']
    print(resc)
    return jsonify({"message": "Value received successfully"})



@app.route('/result')
def result():
    while resc=='Error':
        time.sleep(1)
    return render_template('result.html', dynamic_text=resc,title="Results")

if __name__ == '__main__':
    app.run(debug=True)