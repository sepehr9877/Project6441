import json

from Post import Post
import requests
from ElementTDG import TDG
class Photo(Post):
    photodes = None
    url=None
    thumbnailUrl=None
    Photo_object=[]
    def __init__(self):
        self.__TDG_photo=TDG()
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
        for i in range(0, 6):
            thumbnailUrl_item, title_item, url_item = self.__set_api_item(Photo_data, i)
            Photo_elements={"url":url_item,"title":title_item,"thumbnailUrl":thumbnailUrl_item}
            self.Photo_object.append(Photo_elements)
        self.__TDG_photo.InsertPhoto(self.Photo_object)
        return True

    def __set_api_item(self, Photo_data, i):
        url_item = Photo_data[i].get("url")
        title_item = Photo_data[i].get("title")
        thumbnailUrl_item = Photo_data[i].get("thumbnailUrl")
        return thumbnailUrl_item, title_item, url_item

    def Insert_Element(self,object):
        self.__set_photo_object_element(object)
        photo_item={"title":self.photodes,"url":self.url,"thumbnailUrl":self.thumbnailUrl}
        item_list=[photo_item]
        self.__TDG_photo.InsertPhoto(item_list)
        print(self.Photo_object)
        print("Run Insert Query For Photo")
        return photo_item

    def __set_photo_object_element(self, object):
        self.setDescription(object["title"])
        self.photodes = self.title
        self.url = object["url"]
        self.thumbnailUrl = object["thumbnailUrl"]

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
        selected_photo=self.__TDG_photo.SelectPhoto(id=id)
        print("Select Query for Photo")
        return selected_photo
