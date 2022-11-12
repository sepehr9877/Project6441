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
        self.__photo_TDG=TDG()
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
            thumbnailUrl_item, title_item, url_item = self.__set_api_item_photo(Photo_data, i)
            Photo_elements={"url":url_item,"title":title_item,"thumbnailUrl":thumbnailUrl_item}
            self.Photo_object.append(Photo_elements)
        self.__photo_TDG.InsertPhoto(self.Photo_object)
        return True

    def __set_api_item_photo(self, Photo_data, i):
        url_item = Photo_data[i].get("url")
        title_item = Photo_data[i].get("title")
        thumbnailUrl_item = Photo_data[i].get("thumbnailUrl")
        return thumbnailUrl_item, title_item, url_item

    def Insert_Element(self,object):
        self.__set_photo_object_element(object)
        photoobject={"title":self.photodes,"url":self.url,"thumbnailUrl":self.thumbnailUrl}
        photo_item=[photoobject]
        self.__photo_TDG.InsertPhoto(photo_item)
        print(self.Photo_object)
        print("Run Insert Query For Photo")
        return photoobject

    def __set_photo_object_element(self, object):
        self.setDescription(object["title"])
        self.photodes = self.title
        self.url = object["url"]
        self.thumbnailUrl = object["thumbnailUrl"]

    def Delete_Element(self,**kwargs):
        id = kwargs["id"]
        self.__photo_TDG.DeletePhoto(id=id)
        print("Delete Query for Photo")
    def Update_Element(self,**kwargs):
        id=kwargs["id"]
        title=kwargs["title"]
        self.__photo_TDG.UpdatePhoto(id=id, title=title)
        print("Update Query for Photo")
    def Select_Element(self,**kwargs):
        id = kwargs["id"]
        selected_photo=self.__photo_TDG.SelectPhoto(id=id)
        print("Select Query for Photo")
        return selected_photo
