import shelve
import uuid
import socket
import os
import base64

class Handle:
    def __init__(self):
        if not os.path.exists("drive"):
            os.makedirs("drive")
    def add_file(self,filename=None,file=None):
        # file = file.encode()
        data_file = file
        f = open("drive/"+filename,"wb")
        f.write(data_file)
        return True

    def get_file(self,filename=None):
        temp = []
        f = open("drive/" +filename, "rb")
        hasil = f.read()
        f.close()
        hasil = str(hasil, "utf-8")
        return hasil

    def list_file(self):
        file_list = os.listdir("drive")
        return file_list

if __name__=='__main__':
    p = Handle()
    print(p.list_file())


