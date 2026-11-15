from fastapi import Depends,status,APIRouter,HTTPException  ,Response
from sqlalchemy.orm import Session
from typing import List
from .. import schemas,models
from ..database import get_db
router=APIRouter(prefix='/posts',tags=['posts'])


# @app.get("/sqlalchemy")
# def test_posts(db:Session = Depends(get_db)):
#     posts=db.query(models.Post).all()
#     return {"data":posts}

@router.get('/',response_model=List[schemas.Post])
def get_posts(db:Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts""")
    # posts= cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts

@router.post('/',status_code=201,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db:Session = Depends(get_db)):
    # #print(Post)
    # #return {"new_post": f"title {P['Title']} content:{payLoad['Content']}"}
    # print (post.title)
    # print(post.published)
    # print(post.rating)
    # print(post.model_dump())
    # post_dict=post.model_dump()
    # post_dict['id']=randrange(0,1000000)
    # my_posts.append(post_dict)
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    # new_post=cursor.fetchone()
    # conn.commit()#saves the data
    new_post=models.Post(title=post.title,content=post.content,published=post.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# @app.get('/posts/latest')
# def get_latest_post():
#     post=my_posts[len(my_posts)-1]
#     return  post

@router.get('/{id}',response_model=schemas.Post)
def get_post(id :int,db:Session =Depends(get_db)):

    # print(id)
    # post=find_post(id)
    # cursor.execute("""SELECT * FROM posts WHERE id=%s""",(str(id)))
    # post=cursor.fetchone()
    post =db.query(models.Post).filter(models.Post.id==id).first()#all will search fully
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} was not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
    #     # return {"message":f"post with id:{id} was not found"}
    # print(post)
    return  post

#The below doesnt work since its placed below the get posts by id and it things '/latest' is an id and gives an error as its a string
# @app.get('/posts/latest')
# def get_latest_post():
#     post=my_posts[len(my_posts)-1]
#     return  {"detail":post}

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session =Depends(get_db)):
    # index=find_index_post(id)
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post=db.query(models.Post).filter(models.Post.id==id)
    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with index {id} does not exist")
    # my_posts.pop(index)
    # return {'message':'post was successfully deleted'}
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}',response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db:Session =Depends(get_db)):
    # print(post)
    # return {"message:"update_post""}
    # index=find_index_post(id)
    # cursor.execute("""UPDATE posts SET title=%s,content=%s,published=%s WHERE id =%s RETURNING *""",(post.title,post.content,post.published,str(id)))
    # updated_post=cursor.fetchone()
    # conn.commit()
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} does not exists")
    # post_dict =post.model_dump()
    # post_dict['id']=id
    # my_posts[index]=post_dict
    post_query.update(updated_post.model_dump(),synchronize_session=False)
    db.commit()
    db.refresh(post)
    return post_query.first()