from abc import ABC,abstractmethod
class Post(ABC):
    title=None
    Element=None
    def setDescription(self,Description):
        self.title=Description
    def SetElement(self,Element):
        self.Element=Element

    @abstractmethod
    def Insert_Element(self):
        self.Element.insert()
    @abstractmethod
    def ReadApi(self):
        pass

    @abstractmethod
    def Delete_Element(self):
        self.Element.Delete()

    @abstractmethod
    def Update_Element(self):
        self.Element.Update()

    @abstractmethod
    def Select_Element(self):
        self.Element.Select()

