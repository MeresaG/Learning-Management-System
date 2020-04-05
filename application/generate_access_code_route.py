from application import app, db
from flask import redirect, render_template, flash, url_for
from application.generate_access_code import GenerateAccessCode
from flask_login import login_required
from application.access_code_model import AccessCode
from application.email import send_access_code_email
import random

@app.route('/generate_access_code', methods=['GET', 'POST'])
@login_required
def generate_access_code():

    form = GenerateAccessCode()
    if form.validate_on_submit():
        random_access_code = generate_random_access_code()
        while(AccessCode.query.filter_by(access_code = random_access_code).first()):
            random_access_code = generate_random_access_code()

        access_code = AccessCode(user_type=form.user_type.data, email=form.email.data, access_code=random_access_code)
        db.session.add(access_code)
        try:
            db.session.commit()
            send_access_code_email(access_code)
            flash('Congratulations, email sent to user!')
        except Exception as e:
            flash(str(e))
        return redirect(url_for('login'))
    return render_template('generate_access_code.html', title='Generate Access Code', form=form)


def generate_random_access_code():
    return ''.join(random.sample(app.config['ACCESS_CODE']*10, 10))