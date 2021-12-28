from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
 return"Welcome to Yash's website!"

 app.run(host='0.0.0.0')
