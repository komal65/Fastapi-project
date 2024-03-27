
from fastapi  import FastAPI , Depends , status ,Response ,HTTPException
from .  import models
from .database import engine
from .routers import blog ,user , authentication





app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
# def get_db():
#     db = SessionLocal()
    
#     try:
#         yield db
    
#     finally:
#         db.close()



# #blog created
# @app.get("/blog",response_model=List[schemas.ShowBlog])
# def all(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

#show all blog
# @app.post("/blog" , status_code=status.HTTP_201_CREATED ,tags=['Blogs'])
# def create(request:schemas.Blog ,db:Session=Depends(get_db)):
#      new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
#      db.add(new_blog)
#      db.commit()
#      db.refresh(new_blog)
#      return new_blog

#access blog by specific id

# @app.get('/blog/{id}', status_code=200,response_model=schemas.ShowBlog ,tags=['Blogs'])
# def show(id,response:Response, db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id ==id).first()
#     if not blog:
#         # response.status_code= status.HTTP_404_NOT_FOUND
#         # return{'detail':f"Blog with the id  {id} is not found"}
#         raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id  {id} is not found")
    
#     return blog

# #delete blog
# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT ,tags=['Blogs'])
# def destroy(id,db:Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id ==id).delete(synchronize_session=False)
#     db.commit() 
#     return 'done '


# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED ,tags=['Blogs'])
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     # Check if the blog with the specified ID exists
#     existing_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if existing_blog is None:
#         # Blog with the specified ID does not exist, return a 404 HTTP error
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
#     # Get the data from the request and convert it to a dictionary
#     updated_data = request.model_dump(exclude_unset=True)
    
#     # Update the specified fields
#     db.query(models.Blog).filter(models.Blog.id == id).update(updated_data)
    
#     db.commit()
#     return "updated"

 
 
 
 
# @app.post('/user',response_model=schemas.ShowUser ,tags=['Users'])
# def create_user(request:schemas.User , db: Session = Depends(get_db)):
   
#     new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user



# @app.get('/user/{id}', response_model=schemas.ShowUser  , tags=["Users"])
# def get_user(id:int , db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id ==id).first()
#     if not user:
#         raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} is not available")
    
#     return user

