# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Comment import Comment
from MakePost import MakePost
from Photo import Photo
myelement=MakePost()
photo=Photo()
comment=Comment()
photo.ReadApi()
comment.ReadApi()
comment_body="This is new Comment"
comment_name="Sepehr"
comment_email="Sepehr@yhaoo.com"
comment2=comment(comment_body,comment_name,comment_email)
comment3=comment(comment_body,comment_name,comment_email)
myelement.MakeELement(comment)
comment2=myelement.CallInsert(comment2)
comment3=myelement.CallInsert(comment3)
myelement.CallDelte(id=1)
myelement.CallUpdate(id=2,name="Sepehr")
myelement.CallSelect(id=2)
photo2=photo(desc="THis is My new Photo",url="this is the  url",thumurl="thumurl")
photo3=photo(desc="THis is My new Photo",url="this is the  url",thumurl="thumurl")
myelement.MakeELement(photo)
photo2=myelement.CallInsert(photo2)
photo3=myelement.CallInsert(photo3)
myelement.CallDelte(id=4)
myelement.CallUpdate(id=1,title="Updated photo")
myelement.CallSelect(id=1)
post1=myelement.MakePost(comment=comment2,photo=photo2,description="THis is the first Post")
print(post1)
post2=myelement.MakePost(comment=comment2,photo=photo2,description="THis is the first Post")
print(post2)
selected_post=myelement.SelectPost(id=None)
print(selected_post)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
