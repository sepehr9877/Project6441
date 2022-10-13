from PostControl import PostControl
from Post import Post
from ElementTDG import TDG
class MakePost(PostControl):
    Element=None
    Post_objects=[]
    description=None
    id=0
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
    def MakePost(self,comment,photo,description):
        self.description=description
        print("Myphotp")
        print(photo.get("title"))
        self.id=self.id +1
        item={"comment_id":comment.get("id"),"pohot_id":photo.get("id"),"description":self.description}
        self.Post_objects.append(item)
        return self.Post_objects
    def SelectPost(self,**kwargs):
        id=kwargs["id"]
        if id is not None:
            for index,item in enumerate(self.Post_objects):
                if item.get("id")==id:
                    return item
        else:
            return self.Post_objects



