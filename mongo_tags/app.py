from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)

app.config.update(dict(
    SQLALCHEMY_DATABASE_URI='mysql://root:@localhost/shiyanlou',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ))

db = SQLAlchemy(app)
tags = MongoClient('127.0.0.1',27017).shiyanlou.tags 

class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),unique=True)
    created_time = db.Column(db.DateTime,nullable=False)
    category_id = db.Column(db.Integer,db.ForeignKey('categorys.id'))
    category = db.relationship('Category',uselist=False)
    content = db.Column(db.Text)

    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

    def add_tag(self,tag_name):
        tag = tags.find_one({'title':self.title})
        if not tag:
            tags.insert_one({'title':self.title,'value':[tag_name]})
        else:
            value = tag['value']
            if not tag_name in value:
                value.append(tag_name)
            tags.update_one({'title':self.title},{'$set':{'value':value}})

    def remove_tag(self,tag_name):
        tag = tags.find_one({'title':self.title})
        if tag_name in tag['value']:
            value = tag['value']
            value.remove(tag_name)
            tags.update_one({'title':self.title},{'$set':{'value':value}})

    @property
    def tags(self):
        return tags.find_one({'title':self.title})['value']

class Category(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File')

    def __init__(self,name):
        self.name = name

def main():
    db.create_all()
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java',datetime.utcnow(),java,
            'File Content - Java is cool!')
    file2 = File('Hello Python',datetime.utcnow(),python,
            'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()

    file1.add_tag('tech')
    file2.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')

@app.route('/')
def index():
    return render_template('index.html',files=File.query.all())

@app.route('/files/<int:file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id)
    return render_template('file.html',file_item=file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    main()
