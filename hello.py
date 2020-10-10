from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameEmailForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email address?', validators=[DataRequired()], render_kw={'type':'email'})
    submit = SubmitField('Submit')


def UofT_email_check(field):
    if "utoronto" not in field.data.split('@')[-1]:
        return False
    return True

@app.errorhandler(404)
def page_not_found(e):
    session.clear()
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/clear_session', methods=['GET'])
def clear_session():
    session.clear()
    return "Session cleared"

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameEmailForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        old_email = session.get('email')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['is_uoft_email'] = UofT_email_check(form.email)
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'), is_uoft_email=session.get('is_uoft_email'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
