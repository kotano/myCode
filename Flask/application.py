from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import url_for

app = Flask(__name__)


@app.route('/index')
def get_urls():
    return render_template('index.html', urls=[
        url_for('hello'),
        url_for("bottles"),
        url_for("arguments"),
        url_for("text"),
        url_for("json"),
        url_for("html"),
        url_for("not_found"),
        url_for("foo"),
        url_for("badresponse")
    ])


@app.route('/', redirect_to='/index')
def hello_world():
    return 'Hi'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/99-bottles')
def bottles():
    return render_template('99-bottles.html')


@app.route('/args', methods=['get'])
def arguments():
    args = list(request.args.lists())
    return(render_template('arguments.html', args=args))


@app.route('/return/text')
def text():
    return "text"


@app.route('/return/json')
def json():
    return {'json': 42}


@app.route('/return/html')
def html():
    return render_template('99-bottles.html')


@app.route('/not_found')
def not_found():
    return 'Oops!', 404


# @app.errorhandler(404)
# def not_found(error):
#     return 'Oops!', 404


@app.route('/foo')
def foo():
    response = make_response('foo')
    # устанавливаем заголовок
    response.headers['X-Parachutes'] = 'parachutes are cool'
    # меняем тип ответа
    response.mimetype = 'text/plain'
    # задаём статус
    response.status_code = 418
    # устанавливаем cookie
    response.set_cookie('foo', 'bar')
    return response


@app.route('/dict_args')
def badresponse():
    res = dict(request.args.lists())
    return res
