from abc import ABC, abstractmethod
import requests
import json
from Post import Post
class PostControl(ABC):
    post=Post()
    @abstractmethod
    def ReadFromApi(self):
        pass
    @abstractmethod
    def CallInsert(self,Element):
        pass

    @abstractmethod
    def CallUpdate(self,**kwargs):
        pass

    @abstractmethod
    def CallDelte(self,**kwargs):
        pass

    @abstractmethod
    def CallSelect(self,**kwargs):
        pass