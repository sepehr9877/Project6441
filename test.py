import unittest
from Photo import Photo
from Comment import Comment
from MakePost import MakePost
import os.path
from unittest.mock import patch
class Test(unittest.TestCase):
    def setUp(self):
        self.photo_object = Photo()
        self.comment_object = Comment()
        self.PhotoElement = MakePost(self.photo_object)
        self.CommentElement = MakePost(self.comment_object)
        self.assertIsInstance(obj=self.comment_object, cls=Comment)
        self.assertIsInstance(obj=self.photo_object, cls=Photo)
        self.assertIsInstance(obj=self.PhotoElement, cls=MakePost)
        self.assertIsInstance(obj=self.CommentElement, cls=MakePost)

    def test_connection(self):

        self.CommentElement.ReadFromApi()
        self.PhotoElement.ReadFromApi()
        fileDb=os.path.exists('Test.db')
        self.assertTrue(fileDb)
    def test_insert_element(self):
        comment_body = "This is new Comment"
        comment_name = "Sepehr"
        comment_email = "Sepehr@yhaoo.com"
        Comment=self.comment_object(comment_body,comment_name,comment_email)
        desc="THis is My new Photo"
        url=os.path.join('photos/ladybug.png')
        thumurl="url "
        photo=self.photo_object(desc=desc,url=url,thumurl=thumurl)
        self.CommentElement.CallInsert(Comment)
        self.PhotoElement.CallInsert(photo)
    def test_commentresponse(self):
        with patch('MakePost.requests.get') as mocked_get:
            mocked_get.return_value.ok=True
            mocked_get.return_value.test="Success"
            myResponse = self.CommentElement.ChecktheCommentResponse()
            mocked_get.assert_called_with('https://jsonplaceholder.typicode.com/comments')
            self.assertEqual(myResponse,True)
    def test_photoresponse(self):
        with patch('MakePost.requests.get') as mocked_get:
            mocked_get.return_value.ok=True
            mocked_get.return_value.test="Success"
            PhotoResponse=self.CommentElement.checkPhotoResponse()
            mocked_get.assert_called_with('https://jsonplaceholder.typicode.com/photos')
            self.assertEqual(PhotoResponse,True)



if __name__=='__main__':
    unittest.main()