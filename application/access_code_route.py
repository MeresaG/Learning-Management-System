from flask import render_template, flash, redirect, url_for, request
from application.access_code_form import AccessCodeForm
from application import app, db
from flask_login import current_user
from application.access_code_model import AccessCode
from application.register_form import RegistrationForm
from application.user_model import User

@app.route('/access_code', methods=['GET', 'POST'])
def access_code():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    register = RegistrationForm()
    form = AccessCodeForm()
    global access_code
    if form.validate_on_submit():
        access_code = AccessCode.query.filter_by(access_code=form.access_code.data).first()
        if access_code is not None:
            try:
                db.session.delete(access_code)
                db.session.commit()
                return render_template('register.html', title='Register Here', form=register, access_code=access_code)
            except Exception as e:
                flash(str(e))
        else:
            flash("Wrong Access Code, Check your email again")
        return redirect(url_for('login'))
    if register.validate_on_submit():
        user_type = access_code.user_type
        user = User(username=register.username.data, email=register.email.data, user_type=user_type)
        user.set_password(register.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('access_code.html', title='Sign In', form=form)