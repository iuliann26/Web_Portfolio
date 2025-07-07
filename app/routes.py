from app.models import User
from app import db
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
#verifica dac este mail existent
        existing_user_email = User.query.filter_by(email=form.email.data).first()
        if existing_user_email:
            flash("Există deja un cont cu acest email.", "warning")
            return redirect(url_for('main.register'))

#verifica daca este cont cu user
        existing_user_username = User.query.filter_by(username=form.username.data).first()
        if existing_user_username:
            flash("Există deja un cont cu acest username.", "warning")
            return redirect(url_for('main.register'))

#creaza utilizator nou
        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_pw
        )

        db.session.add(new_user)
        db.session.commit()
        flash("Cont creat! Acum te poți loga.", "success")
        return redirect(url_for('main.login'))
    
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    return "Login page (în construcție)"
