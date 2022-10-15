# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os.path

from Comment import Comment
from MakePost import MakePost
from Photo import Photo
global photo_object
global comment_object
global MyphotoElement
global MycommentElement
def instantiate_both_classes():
    globals()['photo_object'] = Photo()
    globals()['MyphotoElement'] = MakePost(photo_object)
    globals()['comment_object'] = Comment()
    globals()['MycommentElement']=MakePost(comment_object)
def Read_Api_Insert_intoTable():
    MyphotoElement.ReadFromApi()
    MycommentElement.ReadFromApi()
def Insert_Input_to_table():
    ###Calling __Call__() method of Photo Class
    photo2 = photo_object(desc="THis is My new Photo", url=os.path.join('photos/ladybug.png'), thumurl="thumurl")
    MyphotoElement.CallInsert(photo2)
    comment_body = "This is new Comment"
    comment_name = "Sepehr"
    comment_email = "Sepehr@yhaoo.com"
    #calling __Call__() method of Comment Class
    comment2 = comment_object(comment_body, comment_name, comment_email)
    MycommentElement.CallInsert(comment2)
def Update_photo_comment():
    MyphotoElement.CallUpdate(id=1, title="Changing the title")
    MycommentElement.CallUpdate(id=2, name="SepehrSeifpour")

def Select_photo_comment():
    MycommentElement.CallSelect(id=2)
    MyphotoElement.CallSelect(id=1)
def Delete_photo_comment():
    MyphotoElement.CallDelte(id=3)
    MycommentElement.CallDelte(id=2)
if __name__=="__main__":
    instantiate_both_classes()
    Read_Api_Insert_intoTable()
    Insert_Input_to_table()
    Update_photo_comment()
    Select_photo_comment()
    Delete_photo_comment()




