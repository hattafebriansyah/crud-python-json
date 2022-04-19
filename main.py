import os
import json
import uuid

def welcome():
    welcome_message= '''
    =======================================================================
    Selamat datang di aplikasi TODO List.
    Terdapat 4 command yang bisa dijalankan pada aplikasi ini:
    - add / a, untuk menambahkan todo
    - del / d, untuk menghapus todo
    - show/ s, untuk menampilkan daftar todo
    - quit/ q, untuk keluar dari aplikasi
    ========================================================================
    '''
    print(welcome_message)

    file_path = os.path.join(os.getcwd(), "todo.json")
    
    def start():
        command = input('Masukkan perintah: ')

        def add():
            print("-----Todo - Add------")
            title = input ("Masukkan Judul:")
            desc = input ("Masukkan Deskripsi:")
            date = input ("Masukkan Tanggal:")

            isi = {
                    "id": str(uuid.uuid4()),
                    "title" : title,
                    "desc" : desc,
                    "date" :  date
                }
            
            if os.path.exists(file_path):
                with open (file_path,"r+") as file:
                    data_json = json.load(file)
                    data_json.append(isi)
                    data_to_write = json.dumps(data_json, indent=2)
                    with open(file_path, "w") as file:
                        file.write(data_to_write)
                    print("Data berhasil ditambahkan!!\n")

            else:
                with open (file_path,"a") as file:
                    data_to_write = json.dumps([isi],indent =2)
                    file.write(data_to_write)
                    print("File baru telah dibuat dan data berhasil ditambahkan!!\n")

        def show():
            with open(file_path, 'r') as json_file:
                json_obj = json.load(json_file)

            print("-----Todo - Show-----")
            for data in json_obj:
                id = data['id']
                title = data['title']
                desc = data['desc']
                date = data['date']
                print(f'id:{id} |Judul:{title} | Deskripsi:{desc} |Tanggal:{date}')
            print("\n")

        def delete():
            print("-----Todo - Delete-----")
            del_id = input ("Masukkan id yang ingin dihapus:")

            json_obj = json.load(open(file_path))
            for i in range(len(json_obj)):
                if json_obj[i]["id"] == del_id:
                    json_obj.pop(i)
                    print ("Data berhasil dihapus\n")
                    break
                else:
                    print ("ID tidak ditemukan\n")
                    break
            open(file_path, "w").write(
                json.dumps(json_obj, indent=2, separators=(',', ': '))
            )


        def quit():
            print("Terima kasih sudah memakai aplikasi TODO\n")
            return      

        if command == "add" or command == "a":
            add()
            start()
        elif command == "del" or command == "d":
            delete()
            start()
        elif command == "show" or command == "s":
            show()
            start()
        elif command == "add" or command == "q":
            quit()
        else:
            print ("""
    ===========================================
    Perintah tidak dikenali, gunakan:
    -add / a 
    -delete / d
    -show / s
    -quit q
    ===========================================
            """)
            start()
    start()

welcome()