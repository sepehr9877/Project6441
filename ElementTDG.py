
class TDG:
    def ConnetToDB(self):
        pass
    def InsertPhoto(self,title,url,thumbnailUrl):
        print("Insert Query For Photo")
        pass
    def InsertComment(self,name,email,body):
        print(name)
        print(email)
        print(body)
        print("Insert Query for Comment")
        pass
    def DeletePhoto(self,**kwargs):
        id = kwargs["id"]
        print("Run Delete Query")
        pass
    def DeleteComment(self,id):

        print("Run Delete Query")
        pass
    def UpdateComment(self,id,name):
        print("Run Update Query for Comment")
        pass
    def UpdatePhoto(self,**kwargs):
        id=kwargs["id"]
        title=kwargs["title"]
        print(id,title)
        print("Update Query")
        pass
    def SelectPhoto(self,id):
        print("Run Select query for Photo")
        pass
    def SelectComment(self,id):
        print("Run select Query for Comment")
        pass
