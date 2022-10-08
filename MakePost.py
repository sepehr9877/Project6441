from PostControl import PostControl
from Post import Post
class MakePost(PostControl):
    Element=None
    def MakeELement(self,Element):
        self.Element=Element
    def CallInsert(self,Element):
        self.Element.Insert_Element(Element)
    def CallDelte(self,**kwargs):
        self.Element.Delete_Element(**kwargs)
    def CallUpdate(self,Element):
        self.Element.Update_Element()
    def callSelect(self,Element):
        self.Element.Select_Element()
    def MakePost(self,comment,photo):
        pass

