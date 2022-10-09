import json

from Post import Post
import requests
from ElementTDG import TDG
class Photo(Post):
    id=0
    photodes = None
    url=None
    thumbnailUrl=None
    Photo_object=[]
    TDG_photo=TDG()
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
            id=i+1
            url_item=Photo_data[i].get("url")
            title_item=Photo_data[i].get("title")
            thumbnailUrl_item=Photo_data[i].get("thumbnailUrl")
            Photo_elements={"id":id,"url":url_item,"title":title_item,"thumbnailUrl":thumbnailUrl_item}
            self.Photo_object.append(Photo_elements)
    def Insert_Element(self,object):
        self.setDescription(object["title"])
        self.photodes=self.title
        self.url=object["url"]
        self.thumbnailUrl=object["thumbnailUrl"]
        photo_item={"id":len(self.Photo_object)+1,"title":self.photodes,"url":self.url,"thumbnailUrl":self.thumbnailUrl}
        self.Photo_object.append(photo_item)
        self.TDG_photo.InsertPhoto(title=self.photodes,url=self.url,thumbnailUrl=self.thumbnailUrl)
        print(self.Photo_object)
        print("Run Insert Query For Photo")
        return photo_item
    def Delete_Element(self,**kwargs):
        id = kwargs["id"]
        self.TDG_photo.DeletePhoto(id=id)
        for index, item in enumerate(self.Photo_object):
            if item.get("id") == id:
                del self.Photo_object[index]
        print(self.Photo_object)
        print("Delete Query for Photo")
    def Update_Element(self,**kwargs):
        id=kwargs["id"]
        title=kwargs["title"]
        self.TDG_photo.UpdatePhoto(id=id,title=title)
        for index,item in enumerate(self.Photo_object):
            if item.get("id")==id:
                item.update({"title":title})
        print(self.Photo_object)
        print("Update Query for Photo")
    def Select_Element(self,**kwargs):
        id = kwargs["id"]
        selected_item=None
        if id is not None:
            for index, item in enumerate(self.Photo_object):
                if item.get("id")==id:
                    selected_item=item
        else:
            selected_item=self.Photo_object
        print(selected_item)
        self.TDG_photo.SelectPhoto(id=id)
        print("Select Query for Photo")
        return selected_item