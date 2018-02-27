from flask import Flask
app = Falsk(__name__)

@app.route('/')
def hello():
  return "Hello Mr Go"