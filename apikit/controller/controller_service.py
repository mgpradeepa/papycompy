from flask import Flask, Request, Response, request

app = Flask(__name__)
app.config['DEBUG']=False


@app.route('/')
def index():
    return "Breaker suspected, Hello!! "

@app.route('/v1/tellme')
def consume_header():
    teller_header = request.headers.get("teller")
    print(teller_header)
    return Response('{"I know you were the teller:"'+ teller_header +' }', mimetype='application/json')
    

@app.route('/v1/greet')
def greeter():
    return " Hello World OILLA!! "

if __name__ == "__main__":
    app.run(host='0.0.0.0')
