from handler import Handle
import json
import logging

'''
------ PROTOCOL FORMAT ------

string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
Format : command *spasi* parameter *spasi* parameter

------ FITUR ------

a. Meletakkan File
   Untuk meletakkan file ke dalam folder "drive"
   Request : add
   Parameter : namafile *spasi* isi dari file
   Response : jika berhasil -> "File Added
              jika gagal -> "ERROR"

b. List File
   Untuk melihat list file di dalam folder 'drive'
   Request : list
   Parameter: -
   Response: list file yang ada dalam folder 'drive'

c. Mengambil File
   Untuk mengambil file berdasarkan nama file dari folder 'drive'
   Request : get
   Parameter : namafile yang ingin diambil
   Response: file ter download pada folder tempat script berada

d. Jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = Handle()

class Machine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='add'):
                print("add")
                filename = cstring[1].strip()
                file = cstring[2].strip()
                # print(file)
                print("Adding",filename)
                # print()
                p.add_file(filename,file.encode())
                return "File Added"

            elif (command=='get'):
                print("get")
                filename = cstring[1].strip()
                print("Retrieving", filename)
                hasil = p.get_file(filename)
                return hasil

            elif (command=='list'):
                logging.info("list")
                data = {}
                data['files'] = []
                hasil = p.list_file()
                for filename in hasil:
                    data['files'].append({"filename":filename})
                return json.dumps(data, indent=4)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    machine = Machine()