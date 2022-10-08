import json

import requests

from Post import Post
class Comment(Post):
    id=0
    name=None
    email=None
    commentbody=None
    Comment_objects=[]
    def __call__(self,body,name,email):
        self.setDescription(body)
        self.name=name
        self.email=email
        self.commentbody=self.title
        commentobject={"name":self.name,"email":self.email,"body":self.commentbody}
        return  commentobject
    def ReadApi(self):
        Comment_response = requests.get("https://jsonplaceholder.typicode.com/comments")
        Comment_data = json.loads(Comment_response.text)
        for i in range(0,3):
            id=i+1
            name_item=Comment_data[i].get("name")
            email_item=Comment_data[i].get("email")
            body_item=Comment_data[i].get("body")
            comment_item={"id":id,"name":name_item,"email":email_item,"body":body_item}
            self.Comment_objects.append(comment_item)

    def Insert_Element(self,object):
        self.setDescription(object["body"])
        self.name = object["name"]
        self.email = object["email"]
        self.id= len(self.Comment_objects)+1
        self.commentbody = self.title
        commentobject = {"id":self.id, "name": self.name, "email": self.email,
                         "body": self.commentbody}


        self.Comment_objects.append(commentobject)
        print(self.Comment_objects)
        print("Run Insert Query For Comment")
    def Delete_Element(self,**kwargs):
        id=kwargs["id"]
        for index,item in enumerate(self.Comment_objects):
            if item.get("id")==id:
                del self.Comment_objects[index]
        print(self.Comment_objects)
        print("Delete Query for Comment")
    def Update_Element(self,**kwargs):
        id=kwargs["id"]
        name=kwargs["name"]
        for index,item in enumerate(self.Comment_objects):
            if item.get("id")==id:
                item.update({"name":name})
        print(self.Comment_objects)
        print("Update Query for Comment")
    def Select_Element(self,**kwargs):
        id=kwargs["id"]
        selected_comment=None
        if id is not None:
            for index, item in enumerate(self.Comment_objects):
                if item.get("id") == id:
                    selected_comment = item
        else:
            selected_comment=self.Comment_objects
        print(selected_comment)
        print("Select Query for Comment")
        return selected_comment

