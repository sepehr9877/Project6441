import sqlite3
from sqlite3 import Error
class TDG():
    __cursor=None
    __conn=None
    #Implementing SingleTon Desing Pattern
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(TDG, cls).__new__(cls)
        return cls._instance
    def __init__(self):
        self.__conn=self.__ConnetToDB()
    def __checktable(self,TableName):
        tablename=self.__cursor.execute("SELECT name from sqlite_master where type='table' and name=?",(TableName,)).fetchall()
        if tablename ==[]:
            return False
        return True

    def __ConnetToDB(self):
        conn=sqlite3.connect('Test.db')
        cursor=conn.cursor()
        self.__cursor=cursor
        self.__conn=conn
        return self.__conn
    def CreatePhotTable(self):
        PhotoTable='''
        create table photo(
        PhotoID integer primary key autoincrement,
        title varchar(50),
        url varchar(100),
        thumbnailurl varchar(100)
        )
        '''
        self.__cursor.execute(PhotoTable)
    def InsertPhoto(self,photo_objects):
        if not self.__checktable("photo"):
            self.CreatePhotTable()
        for index ,item in enumerate(photo_objects):
            title=item.get("title")
            url=item.get("url")
            thumbnailurl=item.get("thumbnailUrl")
            self.__cursor.execute("insert into photo(title, url, thumbnailurl) values(?,?,?)",(title,url,thumbnailurl))
            self.__conn.commit()
        print("Insert Query For Photo")
        pass
    def CreateCommentTable(self):
        comment_table='''create table comment(
                        CommentID integer primary key autoincrement,
                        name varchar(40),
                        email varchar(40),
                        body varchar(500));
                            '''
        self.__cursor.execute(comment_table)

    def InsertComment(self,comment_object):
        if not self.__checktable("comment"):
            self.CreateCommentTable()
        for index,item in enumerate(comment_object):
            name=item.get("name")
            email=item.get("email")
            body=item.get("body")
            self.__cursor.execute('insert into comment(name, email, body) values(?,?,?)',(name,email,body))
            self.__conn.commit()

        print("Insert Query for Comment")
        pass
    def DeletePhoto(self,**kwargs):
        id = kwargs["id"]
        if self.__checktable("photo"):
            delete_query='delete from photo where PhotoID=?'
            self.__cursor.execute(delete_query,(id,))
            self.__conn.commit()
        print("Run Delete Photo Query")
        pass
    def DeleteComment(self,**kwargs):
        id=kwargs["id"]
        if self.__checktable("comment"):
            self.__cursor.execute("delete from comment where CommentID=?",(id,))
            self.__conn.commit()
        print("Run Delete Comment Query")
        pass
    def UpdateComment(self,**kwargs):
        id=kwargs["id"]
        name=kwargs["name"]
        self.__cursor.execute("update comment set name = ? where CommentID =?;",(name,id,))
        self.__conn.commit()
        print("Run Update Query for Comment")
        pass
    def UpdatePhoto(self,**kwargs):
        id=kwargs["id"]
        title=kwargs["title"]
        update_photo='update photo set title = ? where PhotoID =?;'
        self.__cursor.execute(update_photo,(title,id,))
        self.__conn.commit()
        print("Run Update Query for Photo")
        pass
    def SelectPhoto(self,id):
        if self.__checktable("photo"):
            selected_query='select * from photo  where PhotoID=?'
            selected_photo=self.__cursor.execute(selected_query,(id,)).fetchall()
            print("Selected Photo")
            print(selected_photo)
            return selected_photo
    def SelectComment(self,id):
        if self.__checktable("comment"):
            selected_comment=self.__cursor.execute("select * from comment where CommentID=?",(id,)).fetchall()
            print("Selected Comment")
            print(selected_comment)
            return selected_comment

