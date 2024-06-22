from flask import Flask, Request, Response

app = Flask(__name__)
app.config['DEBUG']=False


@app.route('/')
def index():
    return "Breaker suspected, Hello!! "


@app.route('/')
def index():
    return "Breaker suspected, Hello!! "

@app.route('/v1/greet')
def greeter():
    return " Hello World OILLA!! "

if __name__ == "__main__":
    app.run(host='0.0.0.0')
