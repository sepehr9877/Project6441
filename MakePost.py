import requests

from PostControl import PostControl
from Post import Post
from ElementTDG import TDG
class MakePost(PostControl):
    Element=None
    def __init__(self,Element):
        self.Element=Element
    def ReadFromApi(self):
        self.Element.ReadApi()
    def CallInsert(self,Element):
        return self.Element.Insert_Element(Element)
    def CallDelte(self,**kwargs):
        self.Element.Delete_Element(**kwargs)
    def CallUpdate(self,**kwargs):
        self.Element.Update_Element(**kwargs)
    def CallSelect(self,**kwargs):
        self.Element.Select_Element(**kwargs)
    def ChecktheCommentResponse(self):
        response_comment=requests.get('https://jsonplaceholder.typicode.com/comments')
        if response_comment.ok:
            print("True")
            return True
        else:
            return False
    def checkPhotoResponse(self):
        photo_response = requests.get('https://jsonplaceholder.typicode.com/photos')
        if photo_response.ok:
            print("True")
            return True
        else:
            return False




