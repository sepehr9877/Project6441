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
        self.Photo_object.append(photo_object)
        return photo_object
    def ReadApi(self):
        Photo_response = requests.get("https://jsonplaceholder.typicode.com/photos")
        Photo_data = json.loads(Photo_response.text)
        for i in range(0, 2):
            id=i+1
            url_item=Photo_data[i].get("url")
            title_item=Photo_data[i].get("title")
            thumbnailUrl_item=Photo_data[i].get("thumbnailUrl")
            Photo_elements={"id":id,"url":url_item,"title":title_item,"thumbnailUrl":thumbnailUrl_item}
            self.Photo_object.append(Photo_elements)
        return Photo_elements
    def Insert_Element(self,object,id):
        self.Photo_object.append(object)
        print("Run Insert Query For Photo")
    def Delete_Element(self,**kwargs):

        print("Delete Query for Photo")
    def Update_Element(self):
        print("Update Query for Photo")
    def Select_Element(self):
        print("Select Query for Photo")