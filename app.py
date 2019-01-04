from flask import Flask, request, render_template

from data import Articles

app = Flask(__name__)

Articles = Articles()


@app.route('/')
def index():
    # return 'Hello World! {}'.format(request.method)
    return render_template('index.html', name="Hello World | Привет Мир")


@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return 'Method used was POST'
    else:
        return 'Method was GET'


@app.route('/cars/<name>')
def cars(name):
    return render_template('cars.html', name=name)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/articles')
def articles():
    articles = Articles
    return render_template('articles.html', articles=articles)


@app.route('/article/<int:id>/')
def article(id):
    return render_template('article.html', id=id)


@app.route('/info/<topic>')
def info(topic):
    return '<html><head><title>About</title></head><body><h1>Information {}</h1></body></html>'.format(topic)


@app.route('/post/<int:id>')
def post(id):
    return '<html><head><title>About</title></head><body><h1>Information {}</h1></body></html>'.format(id)


@app.route('/user')
@app.route('/user/<username>')
def user(username=None):
    return render_template('user.html', username=username)


@app.route('/shopping')
def shopping():
    food = ['cheese', 'tomato', 'ham', 'bread']
    return render_template('shopping.html', food=food)


if __name__ == '__main__':
    app.run(debug=True)
