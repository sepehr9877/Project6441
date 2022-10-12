import json

from Post import Post
import requests
from ElementTDG import TDG
class Photo(Post):
    photodes = None
    url=None
    thumbnailUrl=None
    Photo_object=[]
    __TDG_photo=TDG()
    def __call__(self,desc,url,thumurl):
        self.setDescription(desc)
        self.photodes=self.title
        self.url=url
        self.thumbnailUrl=thumurl
        photo_object={"url":self.url,"title":self.photodes,"thumbnailUrl":self.thumbnailUrl}
        return photo_object
    def ReadApi(self):
        Photo_response = requests.get("https://jsonplaceholder.typicode.com/photos")
        Photo_data = json.loads(Photo_response.text)
        for i in range(0, 3):
            url_item=Photo_data[i].get("url")
            title_item=Photo_data[i].get("title")
            thumbnailUrl_item=Photo_data[i].get("thumbnailUrl")
            Photo_elements={"url":url_item,"title":title_item,"thumbnailUrl":thumbnailUrl_item}
            self.Photo_object.append(Photo_elements)
        self.__TDG_photo.InsertPhoto(self.Photo_object)
        return True
    def Insert_Element(self,object):
        self.setDescription(object["title"])
        self.photodes=self.title
        self.url=object["url"]
        self.thumbnailUrl=object["thumbnailUrl"]
        photo_item={"title":self.photodes,"url":self.url,"thumbnailUrl":self.thumbnailUrl}
        item_list=[photo_item]
        self.__TDG_photo.InsertPhoto(item_list)
        print(self.Photo_object)
        print("Run Insert Query For Photo")
        return photo_item
    def Delete_Element(self,**kwargs):
        id = kwargs["id"]
        self.__TDG_photo.DeletePhoto(id=id)
        print("Delete Query for Photo")
    def Update_Element(self,**kwargs):
        id=kwargs["id"]
        title=kwargs["title"]
        self.__TDG_photo.UpdatePhoto(id=id,title=title)
        print("Update Query for Photo")
    def Select_Element(self,**kwargs):
        id = kwargs["id"]
        self.__TDG_photo.SelectPhoto(id=id)
        print("Select Query for Photo")
