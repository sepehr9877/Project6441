import json

from Post import Post
import requests
class Photo(Post):
    id=0
    photodes = None
    url=None
    thumbnailUrl=None
    Photo_object=[]
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
        photo_item={"id":len(self.Photo_object)+1,"title":self.photodes,"thumbnailUrl":self.thumbnailUrl}
        self.Photo_object.append(photo_item)
        print(self.Photo_object)
        print("Run Insert Query For Photo")
    def Delete_Element(self,**kwargs):
        id = kwargs["id"]
        for index, item in enumerate(self.Photo_object):
            if item.get("id") == id:
                del self.Photo_object[index]
        print(self.Photo_object)
        print("Delete Query for Photo")
    def Update_Element(self):
        print("Update Query for Photo")
    def Select_Element(self):
        print("Select Query for Photo")