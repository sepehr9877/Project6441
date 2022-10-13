from abc import ABC, abstractmethod
import requests
import json
class PostControl(ABC):
    post_title=None
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