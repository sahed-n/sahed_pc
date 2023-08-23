from flask import Flask, render_template, request
from forms import SignupForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eblict'

@app.route("/")
def home():
    return "hello world"

@app.route("/about")
def france():
    return "how about yes"

@app.route("/blog")
def blog():

    books = [{'name':'Hi Read','auth':'karen'},{'name':'Hi Smookes','auth':'feddy'}]

    return render_template('blog.html',authName="melox", sunny=False, books=books)

@app.route("/blog/<blog_id>")
def blogpost(blog_id):
    return "this is blog number "+ blog_id

@app.route("/signup", methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.is_submitted():
        result = request.form
        args = request.args
        return render_template('user.html', result=result, args = args)

    return render_template("signup.html",form=form)


if __name__ == '__main__':
    app.run()