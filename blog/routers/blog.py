from typing import List
from fastapi import APIRouter , Depends, HTTPException, status ,Response
from sqlalchemy.orm import Session
from .. import schemas , database , models ,oauth2 
from ..repository import blog



router= APIRouter(
    prefix = "/blog",
    tags=[ 'Blogs']
)
get_db = database.get_db


#blog created
@router.get("/",response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(get_db), get_current_user:schemas.User =Depends(oauth2.get_current_user)):
    return blog.get_all(db)


#show all blog
@router.post("/" , status_code=status.HTTP_201_CREATED )
def create(request:schemas.Blog ,db:Session=Depends(get_db), get_current_user:schemas.User =Depends(oauth2.get_current_user)):
    return blog.create(request,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session = Depends(get_db), get_current_user:schemas.User =Depends(oauth2.get_current_user)):
    
    return blog.destroy(id,db)
 
@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog )
def show(id:int, db:Session = Depends(get_db), get_current_user:schemas.User =Depends(oauth2.get_current_user)):
    return blog.show(id,db )


#delete blog



#update blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED ,tags=['Blogs'])
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db), get_current_user:schemas.User =Depends(oauth2.get_current_user)):
    
    return blog.update(id,request,db)
    
    

