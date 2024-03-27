from typing import Optional
from fastapi import FastAPI
from blog import schemas
from  pydantic import BaseModel
#instance created
app=FastAPI()

#decorate
@app.get('/')
def index():
    return  {'data' :'blog list'}





@app.get('/blog')
def index(limit=10 ,published:bool =True , sort:Optional[str]=None):
    
    if published:
        return  {'data' :f'{limit} published blogs from the db'}
    
    else:
        return  {'data' :f'{limit} unpublished  blogs from the db'}
        




@app.get('/blog/unpublished')
def unpublished():
    return  {'data': 'This is an Unpublished blog post'}



@app.get('/blog/{id}')
def about(id:int):
    return  {'data': id}




@app.get('/blog/{id}/comments')
def comments(id):
    return  {'data': {'amazing':id}}



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]=None
    
 

@app.post('/blog')
def create_blog(blog:schemas.Blog):
   
    return {'data':f"Blog is created with {blog.title}"}
   