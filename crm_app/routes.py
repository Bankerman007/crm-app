from flask import flash, redirect, render_template, request, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from crm_app import app, bcrypt, db
from crm_app.forms import LogInForm, NewContactForm, RegistrationForm
from crm_app.models import Contacts, User
from crm_app.treasury_rate import Api_Call


@app.route("/")
@app.route("/home")
def home():
    rate= Api_Call().rates()
    prime=Api_Call().prime_rate()
    dow_change = Api_Call().dow_price_change()
    dow_price = Api_Call().dow()
    image_file = url_for('static', filename= 'profile_pics/default.jpeg')
    return render_template('home.html', image_file=image_file,rate=rate, prime=prime,
                            dow_price=dow_price,dow_change = dow_change)

@app.route("/about")
def about():
    rate= Api_Call().rates()
    prime=Api_Call().prime_rate()
    dow_change = Api_Call().dow_price_change()
    dow_price = Api_Call().dow()
    return render_template('about.html', title= 'About', rate=rate, prime=prime,
                            dow_change=dow_change,dow_price=dow_price,)

@app.route("/base")
def base():
    rate= Api_Call().rates()
    prime=Api_Call().prime_rate()
    dow_change = Api_Call().dow_price_change()
    dow_price = Api_Call().dow()
    return render_template('base.html', title='Base', rate=rate, prime=prime, 
                            dow_price=dow_price, dow_change=dow_change,)

@app.route("/register", methods= ['GET','POST'])
def register():
    rate= Api_Call().rates()
    prime=Api_Call().prime_rate()
    dow_change = Api_Call().dow_price_change()
    dow_price = Api_Call().dow()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form= RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created, you are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form, rate=rate, prime=prime,
                            dow_price=dow_price, dow_change=dow_change,)

@app.route("/login", methods= ['GET', 'POST'])
def login():
    rate= Api_Call().rates()
    prime=Api_Call().prime_rate()
    dow_change = Api_Call().dow_price_change()
    dow_price = Api_Call().dow()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form= LogInForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('account'))
        else:
            flash('Unsuccessful login attempt, check email and password', 'danger')
    return render_template('login.html', tiltle= "Login", form=form, rate=rate, prime=prime,
                            dow_price=dow_price, dow_change=dow_change,)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    rate= Api_Call().rates()
    prime=Api_Call().prime_rate()
    dow_change = Api_Call().dow_price_change()
    dow_price = Api_Call().dow()
    id = current_user.id
    user = User.query.get(id)
    contacts = user.contacts
    image_file = url_for('static', filename= 'profile_pics/' + current_user.image_file)
    return render_template('account.html', tiltle= "Account", image_file=image_file, 
                            contacts=contacts, rate=rate, prime=prime, dow_change=dow_change,
                            dow_price=dow_price,)

@app.route("/new_contact", methods= ['GET', 'POST'])
@login_required
def new_contact():
    rate= Api_Call().rates()
    prime=Api_Call().prime_rate()
    dow_change = Api_Call().dow_price_change()
    dow_price = Api_Call().dow()
    form= NewContactForm()
    if form.validate_on_submit():
        contact =Contacts(name=form.name.data, phone=form.phone.data, email=form.email.data, notes=form.notes.data, username= current_user)
        db.session.add(contact)
        db.session.commit()
        flash('New Contact has been created', 'success')
        return redirect(url_for('account'))
    return render_template('new_contact.html', tiltle= "New Contact", form=form, rate=rate,
                            prime=prime,dow_price=dow_price, dow_change=dow_change,)

@app.route("/contact/<id>")
def contact(id):
    rate= Api_Call().rates()
    prime=Api_Call().prime_rate()
    dow_change = Api_Call().dow_price_change()
    dow_price = Api_Call().dow()
    contact=Contacts.query.get(id)
    image_file = url_for('static', filename= 'profile_pics/' + current_user.image_file)
    return render_template('contact.html', title=contact.name, contact=contact,
                             image_file=image_file, rate=rate, prime=prime,dow_price=dow_price,
                             dow_change=dow_change)

@app.route("/contact/<id>/update", methods=['GET', 'POST'])
@login_required
def update_contact(id):
    contact = Contacts.query.get_or_404(id)
    if contact.user_id != current_user.id:
        abort(403)
    form = NewContactForm()
    if form.validate_on_submit():
        contact.name = form.name.data
        contact.phone = form.phone.data
        contact.email=form.email.data
        contact.notes=form.notes.data
        db.session.commit()
        flash('Your contact has been updated!', 'success')
        return redirect(url_for('contact', id=contact.id))
    elif request.method == 'GET':
        form.name.data = contact.name
        form.phone.data = contact.phone
        form.email.data=contact.email
        form.notes.data=contact.notes
    return render_template('new_contact.html', title='Update Contact',
                           form=form, legend='Update Contact')


@app.route("/post/<id>/delete", methods=['POST'])
@login_required
def delete_contact(id):
    contact = Contacts.query.get_or_404(id)
    if contact.user_id != current_user.id:
        abort(403)
    db.session.delete(contact)
    db.session.commit()
    flash('Your contact has been deleted!', 'success')
    return redirect(url_for('account'))