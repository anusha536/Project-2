"""
{{name}}-it is used to print something like name
you use {{_}}to display variable like form fields or values
*{%_%} --->it is used for do something (logic)
this is like running a command -like an if or loop
inside the HTML
**
###output value            {{something}}
Run logic               {%if%},{%for%},{%block%}
write a comment         {# comment here#}
# HTML comment            <!-->


"""
from wsgiref.validate import validator

from flask import Flask,render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired
app=Flask(__name__)
# app.secret_key='supersecretkey'
class NameForm(FlaskForm):
    username=StringField('Name')
    password=PasswordField('Password')

    submit=SubmitField('Submit')
    class Meta:
        csrf=False
@app.route('/',methods=['GET','POST'])
def index():
    form=NameForm()
    if form.validate_on_submit():
        name=form.username.data
        password=form.password.data

        return f"Hello ,{name} ,your password is {password}"
    return render_template('flask_wtf.html',form=form)
class Detail(FlaskForm):
    username=StringField('Name')
    password=PasswordField('Password')
    email=StringField('Email')
    message=StringField('Message')
    submit=SubmitField('Submit')
    class Meta:
        csrf=False
@app.route('/person',methods=['GET','POST'])
def details():
    form = Detail()
    if form.validate_on_submit():
        name = form.username.data
        password = form.password.data
        message=form.message.data
        email = form.email.data
        return f"Hello ,{name} ,your password is {password},{email},{message}"
    return render_template('contacts.html', form=form)
class HelloForm(FlaskForm):
    name = StringField("Enter your name",validators=[DataRequired])
    submit=SubmitField("Say Hello")
    class Meta:
        csf=False
@app.route('/',methods=['GET','POST'])
def index():
    form=HelloForm()
    if form.validate_on_submit():
        name=form.name.data
        return render_template("hello.html",name=name)
    return render_template("form.html",form=form)
if __name__=='__name__':
    app.run(debug=True)




