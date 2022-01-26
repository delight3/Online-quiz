from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True


@app.route('/login')
def login():
    return render_template('sign_in.html', sitetitle='Login')


@app.route('/register')
def register():
    return render_template('sign_up.html', sitetitle='register')


@app.route('/exam')
def exam():
    return render_template('exam.html')


@app.route('/question')
def question():
    return render_template('question.html')


if __name__ == '__main__':
    app.run()
