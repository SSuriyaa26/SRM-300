
from fastapi import FastAPI,Response,status,HTTPException,Depends
from pydantic import BaseModel
from typing import  Optional,List
from random import randrange
import psycopg2#This makes it so we use SQL and we directly talk to SQL not ORM
from psycopg2.extras import RealDictCursor
import time
from . import models,schemas,utils
from sqlalchemy.orm import Session
from .database import engine,get_db
from .routers import  post,user,auth

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

while True:
    try:
        conn= psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='qwertyuiop',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connecting to Database Successful")
        break
    except Exception as error:
        print("Connecting to Database Failed")
        print("Error: ",error)
        time.sleep(2)
my_posts = [{"title":"title of post1","content":"content of post1","id":1},{"title":"favorite foods","content":"I like pizza","id":2}]

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
@app.get("/")
def root():
    return {"Message: Welcome to my api!!"}




