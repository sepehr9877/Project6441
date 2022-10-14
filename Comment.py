import json

import requests

from Post import Post
from ElementTDG import TDG
class Comment(Post):
    name=None
    email=None
    commentbody=None
    Comment_objects=[]
    def __init__(self):
        self.__comment_TDG=TDG()
    def __call__(self,body,name,email):
        self.setDescription(body)
        self.name=name
        self.email=email
        self.commentbody=self.title
        commentobject={"name":self.name,"email":self.email,"body":self.commentbody}
        return  commentobject
    def ReadApi(self):
        print("ff")
        Comment_response = requests.get("https://jsonplaceholder.typicode.com/comments")
        Comment_data = json.loads(Comment_response.text)
        for i in range(0,3):
            name_item=Comment_data[i].get("name")
            email_item=Comment_data[i].get("email")
            body_item=Comment_data[i].get("body")
            comment_item={"name":name_item,"email":email_item,"body":body_item}
            self.Comment_objects.append(comment_item)
        self.__comment_TDG.InsertComment(self.Comment_objects)

    def Insert_Element(self,object):
        self.setDescription(object["body"])
        self.name = object["name"]
        self.email = object["email"]
        self.id= len(self.Comment_objects)+1
        self.commentbody = self.title
        commentobject = { "name": self.name, "email": self.email,
                         "body": self.commentbody}
        comment_item=[commentobject]
        self.__comment_TDG.InsertComment(comment_item)
        return comment_item
    def Delete_Element(self,**kwargs):
        id=kwargs["id"]
        self.__comment_TDG.DeleteComment(id=id)
        print("Delete Query for Comment")
    def Update_Element(self,**kwargs):
        id=kwargs["id"]
        name=kwargs["name"]
        self.__comment_TDG.UpdateComment(id=id,name=name)
        print("Update Query for Comment")
    def Select_Element(self,**kwargs):
        id=kwargs["id"]
        selected_comment=self.__comment_TDG.SelectComment(id=id)
        print("Select Query for Comment")
        return selected_comment

