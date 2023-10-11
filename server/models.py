from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    @validates("name")
    def valdate_names(self,key ,authors):
        if authors == '':
            raise ValueError("name is empty")
        elif authors in Author.name:
            raise ValueError("need a new name")
        else:
            return authors
    @validates("phone_number")
    def validate_number(self,key,authors):
        if len(authors)==10:
            return authors
        else:
            raise ValueError("incorrect phone_number length")
        

        




    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())



    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
    

    @validates("title")
    def validate_title(self,key,posts):
        if posts =="":
            raise ValueError("can't add empty field")
        else:
            return posts
    @validates("content")
    def validats_content(self,key,posts):
        if len(posts) <250:
            raise ValueError("the content length is less than 250")
        else:
            return posts    
    @validates("summary")  
    def validats_content(self,key,summary):
        if len(summary) ==250:
            return summary  
            
        else:
            raise ValueError("the content length is less than 250")
               
