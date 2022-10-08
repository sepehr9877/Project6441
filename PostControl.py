from abc import ABC, abstractmethod
import requests
import json
class PostControl(ABC):
    post_title=None

    @abstractmethod
    def CallInsert(self):
        pass

    @abstractmethod
    def CallUpdate(self):
        pass

    @abstractmethod
    def CallDelte(self,**kwargs):
        pass

    @abstractmethod
    def CallSelect(self):
        pass