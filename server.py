from models import User
from createDB import db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, flash
from createDB import db_init


app = Flask(__name__, static_folder='static/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event-web.db'


db_init(app=app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        email = request.form.get('email', '')
        phone_number = request.form.get('phone_number', '')
        job_title = request.form.get('job_title', '')
        department = request.form.get('department', '')

    # check = User.query.filter_by(first_name=first_name)

    # print(f'')

        print(
            f"First Name: {first_name}\n"
            f"Last Name: {last_name}\n"
            f"Email: {email}\n"
            f"Phone Number: {phone_number}\n"
            f"Job Title: {job_title}\n"
            f"Department: {department}"
        )
        try:
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                job_title=job_title,
                department=department
            )

        
            print(f'The user {new_user.department}')
            db.session.add(new_user)
            db.session.commit()
            print('db commited ###################################')
            flash('Registration Successful', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            db.session.rollback()
    
    return render_template('register.html')

@app.route('/admin', methods=['GET','POST'])
def admin_page():
    users = User.query.all()

    return render_template('admin.html', users=users)

if __name__=='__main__':
    app.run(debug=True)

    