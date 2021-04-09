from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename
import json

local_server = True

with open('config.json','r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['UPLOAD_FOLDER'] = params['file_path']
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

if (local_server):
    # Connecting the sqlalchemy.               mysql URI
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]
# initialzing the Sqlalchemy.
db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Post(db.Model):
    Sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20),nullable=False)
    slug = db.Column(db.String(25),nullable=False)
    content = db.Column(db.String(120),nullable=False)
    date = db.Column(db.String(20),nullable=False)
    img_file = db.Column(db.String(20),nullable=False)
    subheading = db.Column(db.String(25),nullable=True)


@app.route('/')
def Home():
    posts = Post.query.filter_by().all()[0:params["num_post"]]
    return render_template('index.html',params=params,posts=posts)

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_user']:
        posts = Post.query.all()
        return render_template('dashboard.html',params=params,posts=posts)
    if request.method == 'POST':
        uname = request.form.get('uname')
        password = request.form.get('password')
        if uname == params['admin_user'] and password == params['admin_pass']:
            session['user'] = uname
            posts = Post.query.all()
            return render_template('dashboard.html',params=params,posts=posts)
        else:
            return render_template('login.html',params=params)
    else:
            return render_template('login.html',params=params)

@app.route('/edit/<string:Sno>',methods=['GET','POST'])
def edit(Sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            '''Geting Data From, form'''
            title = request.form.get('title')
            subheading = request.form.get('subheading')
            content = request.form.get('content')
            slug = request.form.get('slug')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if Sno == '0':
                ''' Adding New Posts in the Database'''
                post = Post(title=title, slug=slug, content=content, img_file=img_file, subheading=subheading, date=date)
                db.session.add(post)
                db.session.commit()
            else:

                '''  Fetching Data Form the data base '''
                post = Post.query.filter_by(Sno=Sno).first()
                '''Getting Data From the form and Uploading to DataBase'''
                post.Sno = Sno
                post.title = title
                post.content = content
                post.subheading = subheading
                post.date = date
                post.img_file = img_file
                db.session.commit()
                '''Once the Data is Upgraded the user will redirect to upgraded Page.'''
                return redirect('/edit/'+ Sno)
        post = Post.query.filter_by(Sno=Sno).first()
        return render_template('edit.html',params=params,post=post)
    else:
        link = '<a href="/login">Login</a>'
        return f"Your are not Login, Plese login First + {link}" 

def check_exe(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods=['GET','POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            if 'file' not in request.files:
                return "Wrong File Selected"
            f = request.files['file']
            if f.filename == '':
                return "No File Selected"
            if f and check_exe(f.filename):
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
                return "Uploaded Secussfully..!"

@app.route('/delete/<string:Sno>')
def delete(Sno):
    if 'user' in session and session['user'] == params['admin_user']:
        post = Post.query.filter_by(Sno=Sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/dashboard')
    else:
        return redirect('/login')
        #return render_template('dashboard.html',params=params,post=post)

@app.route('/login',methods=['GET','POST'])
def login():

    return render_template('login.html',params=params)

@app.route('/logout')
def logout():
    session['user'] = None
    return redirect('/dashboard')

@app.route('/about')
def about():
    return render_template('about.html',params=params)

@app.route('/contact', methods=['GET','POST'])
def contect():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html',params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    # This means goto Post class and do query and filter the slug, and get the post_slug.
    # In This way the Post will be patched.
    post = Post.query.filter_by(slug=post_slug).first()


    return render_template('post.html',params=params, post=post)

