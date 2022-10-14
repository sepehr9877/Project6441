# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os.path

from Comment import Comment
from MakePost import MakePost
from Photo import Photo

photo=Photo()
comment=Comment()
myphotoElement=MakePost(photo)
mycommentElement=MakePost(comment)
myphotoElement.ReadFromApi()
photo2=photo(desc="THis is My new Photo",url=os.path.join('photos/ladybug.png'),thumurl="thumurl")
photo3=photo(desc="THis is My new Photo",url=os.path.join('photos/pineapple_PNG2756.png'),thumurl="thumurl")
photo2=myphotoElement.CallInsert(photo2)
photo3=myphotoElement.CallInsert(photo3)
myphotoElement.CallUpdate(id=1,title="Changing the title")
myphotoElement.CallSelect(id=1)
mycommentElement.ReadFromApi()
comment_body="This is new Comment"
comment_name="Sepehr"
comment_email="Sepehr@yhaoo.com"
comment2=comment(comment_body,comment_name,comment_email)
comment3=comment(comment_body,comment_name,comment_email)
mycommentElement.CallInsert(comment2)
mycommentElement.CallInsert(comment3)
mycommentElement.CallUpdate(id=2,name="SepehrSeifpour")
mycommentElement.CallSelect(id=2)

