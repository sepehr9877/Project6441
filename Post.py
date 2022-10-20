from abc import ABC,abstractmethod
class Post(ABC):
    title=None
    Element=None
    def setDescription(self,Description):
        self.title=Description
    def SetElement(self,Element):
        self.Element=Element

    def Insert_Element(self):
        pass

    def ReadApi(self):
        pass


    def Delete_Element(self):
        pass


    def Update_Element(self):
        pass


    def Select_Element(self):
        pass

