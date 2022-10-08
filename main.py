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
myelement.CallInsert(comment2)
myelement.CallInsert(comment3)
myelement.MakePost(comment.Comment_objects,photo.Photo_object)
myelement.CallDelte(id=1)
# comment(body="I am Sepehr",name="Sepehr",email="Sepehr@yahoo.com")
# print(comment.Comment_objects)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
