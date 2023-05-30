import sys
import pyinputplus as pypi
import mysql.connector
from tabulate import tabulate

db = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password ='31Januari31',
    database = 'datasiswa'
)

def DataKelas():
        while True:
            prompt = f"\nList Menu\n\n"  
            choice = ['Data Kelas', 'Data Nilai','Back']
            response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
            if response == 'Data Kelas':
                prompt = f"\nList Menu\n\n"  
                choice = ['XII', 'XI', 'X','Back']
                response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
                if response == 'XII':
                    prompt = f"\nList Menu\n\n"  
                    choice = ['IPA', 'IPS', 'Bahasa','Back']
                    response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
                    if response == 'IPA':
                        datakelasXII_IPA = db.cursor()
                        queryKelasIPA = """
                        select * 
                        From ipa 
                        where kode_kelas = 'XII IPA'
                        """
                        datakelasXII_IPA.execute(queryKelasIPA)
                        Hasil = datakelasXII_IPA.fetchall()
                        print(tabulate(Hasil, headers=['Kode Kelas','ID Siswa','Nama Siswa'], tablefmt = 'psql' ))
                    elif response == 'IPS':
                        datakelasXII_IPS = db.cursor()
                        queryKelasIPS = """
                        select * 
                        From ips 
                        where kode_kelas = 'XII IPS'
                        """
                        datakelasXII_IPS.execute(queryKelasIPS)
                        Hasil = datakelasXII_IPS.fetchall()
                        print(tabulate(Hasil, headers=['Kode Kelas','ID Siswa','Nama Siswa'], tablefmt = 'psql' ))
                    elif response == 'Bahasa':
                        datakelasXII_BAHASA = db.cursor()
                        queryKelasBAHASA = """
                        select * 
                        From bahasa 
                        where kode_kelas = 'XII BAHASA'
                        """
                        datakelasXII_BAHASA.execute(queryKelasBAHASA)
                        Hasil = datakelasXII_BAHASA.fetchall()
                        print(tabulate(Hasil, headers=['Kode Kelas','ID Siswa','Nama Siswa'], tablefmt = 'psql' ))
                    elif response == 'Back':
                        DataKelas()
                elif response == 'XI':
                    prompt = f"\nList Menu\n\n"  
                    choice = ['IPA', 'IPS', 'Bahasa','Back']
                    response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
                    if response == 'IPA':
                        datakelasXI_IPA = db.cursor()
                        queryKelasIPA = """
                        select * 
                        From ipa 
                        where kode_kelas = 'XI IPA'
                        """
                        datakelasXI_IPA.execute(queryKelasIPA)
                        Hasil = datakelasXI_IPA.fetchall()
                        print(tabulate(Hasil, headers=['Kode Kelas','ID Siswa','Nama Siswa'], tablefmt = 'psql' ))
                    elif response == 'IPS':
                        datakelasXI_IPS = db.cursor()
                        queryKelasIPS = """
                        select * 
                        From ips 
                        where kode_kelas = 'XI IPS'
                        """
                        datakelasXI_IPS.execute(queryKelasIPS)
                        Hasil = datakelasXI_IPS.fetchall()
                        print(tabulate(Hasil, headers=['Kode Kelas','ID Siswa','Nama Siswa'], tablefmt = 'psql' ))
                    elif response == 'Bahasa':
                        datakelasXI_BAHASA = db.cursor()
                        queryKelasBAHASA = """
                        select * 
                        From bahasa 
                        where kode_kelas = 'XI BAHASA'
                        """
                        datakelasXI_BAHASA.execute(queryKelasBAHASA)
                        Hasil = datakelasXI_BAHASA.fetchall()
                        print(tabulate(Hasil, headers=['Kode Kelas','ID Siswa','Nama Siswa'], tablefmt = 'psql' ))
                    elif response == 'Back':
                        DataKelas()
                elif response == 'X':
                    prompt = f"\nList Menu\n\n"  
                    choice = ['IPA', 'IPS', 'Bahasa','Back']
                    response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
                    if response == 'IPA':
                        datakelasX_IPA = db.cursor()
                        queryKelasIPA = """
                        select * 
                        From ipa 
                        where kode_kelas = 'X IPA'
                        """
                        datakelasX_IPA.execute(queryKelasIPA)
                        Hasil = datakelasX_IPA.fetchall()
                        print(tabulate(Hasil, headers=['Kode Kelas','ID Siswa','Nama Siswa'], tablefmt = 'psql' ))
                    elif response == 'IPS':
                        datakelasX_IPS = db.cursor()
                        queryKelasIPS = """
                        select * 
                        From ips 
                        where kode_kelas = 'X IPS'
                        """
                        datakelasX_IPS.execute(queryKelasIPS)
                        Hasil = datakelasX_IPS.fetchall()
                        print(tabulate(Hasil, headers=['Kode Kelas','ID Siswa','Nama Siswa'], tablefmt = 'psql' ))
                    elif response == 'Bahasa':
                        datakelasX_BAHASA = db.cursor()
                        queryKelasBAHASA = """
                        select * 
                        From bahasa 
                        where kode_kelas = 'X BAHASA'
                        """
                        datakelasX_BAHASA.execute(queryKelasBAHASA)
                        Hasil = datakelasX_BAHASA.fetchall()
                        print(tabulate(Hasil, headers=['Kode Kelas','ID Siswa','Nama Siswa'], tablefmt = 'psql' ))
                    elif response == 'Back':
                        DataKelas()
                elif response == 'Back':
                    DataKelas()
            elif response == 'Data Nilai':
                prompt = f"\nList Menu\n\n"  
                choice = ['XII', 'XI', 'X','Back']
                response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
                if response == 'XII':
                    prompt = f"\nList Menu\n\n"  
                    choice = ['IPA', 'IPS', 'Bahasa','Back']
                    response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)

                    if response == 'IPA':
                        nilai_IPAXII = db.cursor()
                        qnilai_IPAXII = """
                        select i.Kode_kelas, n.Id_Siswa,i.Nama_Siswa,n.Matematika,n.Fisika,n.Kimia,n.biologi 
                        from ipa i 
                        join nilaiipa n on i.Id_Siswa = n.Id_Siswa 
                        where i.Kode_Kelas = 'XII IPA' 
                        """
                        nilai_IPAXII.execute(qnilai_IPAXII)
                        resnil_IPAXII = nilai_IPAXII.fetchall()
                        print(tabulate(resnil_IPAXII, headers = ['Kode Kelas','ID Siswa','Nama Siswa','Matematika','Fisika','Kimia','Biologi'] , tablefmt = 'psql'))
                    
                    elif response == 'IPS':
                        nilai_IPSXII = db.cursor()
                        qnilai_IPSXII= """
                        select i.Kode_kelas, n.Id_Siswa,i.Nama_Siswa,n.Geografi,n.Akuntansi,n.Sosiologi,n.Sejarah 
                        from ips i 
                        join nilaiips n on i.Id_Siswa = n.Id_Siswa 
                        where i.Kode_Kelas = 'XII IPS' 
                        """
                        nilai_IPSXII.execute(qnilai_IPSXII)
                        resnil_IPSXII = nilai_IPSXII.fetchall()
                        print(tabulate(resnil_IPSXII, headers = ['Kode Kelas','ID Siswa','Nama Siswa','Geografi','Akuntansi','Sosiologi','Sejarah'] , tablefmt = 'psql'))
                    
                    elif response == 'Bahasa':
                        nilai_BAHASAXII = db.cursor()
                        qnilai_BAHASAXII= """
                        select i.Kode_kelas, n.Id_Siswa,i.Nama_Siswa,n.Antropologi,n.Bahasa_Indonesia,n.Bahasa_Jepang,n.Bahasa_Inggris 
                        from bahasa i 
                        join nilaibahasa n on i.Id_Siswa = n.Id_Siswa 
                        where i.Kode_Kelas = 'XII BAHASA' 
                        """
                        nilai_BAHASAXII.execute(qnilai_BAHASAXII)
                        resnil_BAHASAXII = nilai_BAHASAXII.fetchall()
                        print(tabulate(resnil_BAHASAXII, headers = ['Kode Kelas','ID Siswa','Nama Siswa','Antropologi','Bahasa Indonesia','Bahasa Jepang','Bahasa Inggris'] , tablefmt = 'psql'))
                    
                    elif response == 'Back':
                        DataKelas()
            elif response == 'Back':
                main()
                
def TambahSiswa():
    while True:
        prompt = f"\nList Menu\n\n"  
        choice = ['Tambah Siswa','Back']
        response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
        if response == 'Tambah Siswa':
            prompt = f"\nList Menu\n\n"  
            choice = ['IPA','IPS','BAHASA','Back']
            response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
            if response == 'IPA':
                print("""
NOTE
KODE ID KELAS :     XII = 1201**
                    XI  = 1101**
                    x   = 1001**
Ganti ** DENGAN ANGKA RANDOM

KODE KELAS
XII IPA
XI  IPA
X   IPA

GUNAKAN HURUF BESAR
                      """)
                
                IDSiswa = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                mycursor = db.cursor()
                query = 'select ID_Siswa from ipa'
                mycursor.execute(query)
                result = mycursor.fetchall()
                for i, val in enumerate(result):
                    if IDSiswa in val:
                        print("ID TELAH DIGUNAKAN")
                        break
                    elif i == len(result) - 1:
                        print(f"ID DAPAT DIGUNAKAN ID ={IDSiswa}")
                        
                        KodeKelasIPA = pypi.inputStr(prompt='Masukan Kode Kelas: ')
                        IDSiswaIPA = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                        NamaSisIPA = pypi.inputStr(prompt='Masukan Nama Siswa: ')
                        KodeNil = pypi.inputInt(prompt='Masukkan Kode Nilai: ')
                        ValIPA =[KodeKelasIPA,IDSiswaIPA,NamaSisIPA]
                        ValNil =[KodeNil,IDSiswaIPA]
                        print(f"KODE KELAS {KodeKelasIPA} ID SISWA {IDSiswaIPA} Nama Siswa {NamaSisIPA} ")
                        SaveIPA = pypi.inputYesNo(prompt='Apakah anda ingin menyimpan ? (ya/tidak):', yesVal='ya', noVal='tidak' )
                        if SaveIPA == 'ya':
                            penambahIPA = db.cursor()
                            querDataSiswa = "insert into IPA (Kode_Kelas,ID_Siswa,Nama_Siswa) values (%s,%s,%s)"
                            querNilSiswa = "insert into nilaiipa (Kode_Nilai,ID_Siswa,Matematika,Fisika,Kimia,Biologi) values (%s,%s,'0','0','0','0')"
                            penambahIPA.execute(querDataSiswa,ValIPA)
                            penambahIPA.execute(querNilSiswa, ValNil)
                            db.commit()
                            print("Data Berhasil disimpan")
                            break
                                
                        else:
                            break 
            elif response == 'IPS':
                print("""
NOTE
KODE ID KELAS :     XII = 1202**
                    XI  = 1102**
                    x   = 1002**
Ganti ** DENGAN ANGKA RANDOM

KODE KELAS
XII IPS
XI  IPS
X   IPS

GUNAKAN HURUF BESAR
                      """)
                
                IDSiswa = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                mycursor = db.cursor()
                query = 'select ID_Siswa from ips'
                mycursor.execute(query)
                result = mycursor.fetchall()
                for i, val in enumerate(result):
                    if IDSiswa in val:
                        print("ID TELAH DIGUNAKAN")
                        break
                    elif i == len(result) - 1:
                        print(f"ID DAPAT DIGUNAKAN ID ={IDSiswa}")
                        
                        KodeKelasIPS = pypi.inputStr(prompt='Masukan Kode Kelas: ')
                        IDSiswaIPS = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                        NamaSisIPS = pypi.inputStr(prompt='Masukan Nama Siswa: ')
                        KodeNilIPS = pypi.inputInt(prompt='Masukkan Kode Nilai: ')
                        ValIPS =[KodeKelasIPS,IDSiswaIPS,NamaSisIPS]
                        ValNilIPS =[KodeNilIPS,IDSiswaIPS]
                        print(f"KODE KELAS {KodeKelasIPS} ID SISWA {IDSiswaIPS} Nama Siswa {NamaSisIPS} ")
                        SaveIPS = pypi.inputYesNo(prompt='Apakah anda ingin menyimpan ? (ya/tidak):', yesVal='ya', noVal='tidak' )
                        if SaveIPS == 'ya':
                            penambahIPS = db.cursor()
                            querDataSiswaIPS = "insert into IPS (Kode_Kelas,ID_Siswa,Nama_Siswa) values (%s,%s,%s)"
                            querNilSiswaIPS = "insert into nilaiips (Kode_Nilai,ID_Siswa,Geografi,Akuntansi,Sosiologi,Sejarah) values (%s,%s,'0','0','0','0')"
                            penambahIPS.execute(querDataSiswaIPS,ValIPS)
                            penambahIPS.execute(querNilSiswaIPS, ValNilIPS)
                            db.commit()
                            print("Data Berhasil disimpan")
                            break
                                
                        else:
                            break
            elif response == 'BAHASA':
                print("""
NOTE
KODE ID KELAS :     XII = 1203**
                    XI  = 1103**
                    x   = 1003**
Ganti ** DENGAN ANGKA RANDOM

KODE KELAS
XII BAHASA
XI  BAHASA
X   BAHASA

GUNAKAN HURUF BESAR
                      """)
                
                IDSiswa = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                mycursor = db.cursor()
                query = 'select ID_Siswa from bahasa'
                mycursor.execute(query)
                result = mycursor.fetchall()
                for i, val in enumerate(result):
                    if IDSiswa in val:
                        print("ID TELAH DIGUNAKAN")
                        break
                    elif i == len(result) - 1:
                        print(f"ID DAPAT DIGUNAKAN ID ={IDSiswa}")
                        
                        KodeKelasBAHASA = pypi.inputStr(prompt='Masukan Kode Kelas: ')
                        IDSiswaBAHASA = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                        NamaSisBAHASA = pypi.inputStr(prompt='Masukan Nama Siswa: ')
                        KodeNilBAHASA = pypi.inputInt(prompt='Masukkan Kode Nilai: ')
                        ValBAHASA =[KodeKelasBAHASA,IDSiswaBAHASA,NamaSisBAHASA]
                        ValNilBAHASA =[KodeNilBAHASA,IDSiswaBAHASA]
                        print(f"KODE KELAS {KodeKelasBAHASA} ID SISWA {IDSiswaBAHASA} Nama Siswa {NamaSisBAHASA} ")
                        SaveBAHASA = pypi.inputYesNo(prompt='Apakah anda ingin menyimpan ? (ya/tidak):', yesVal='ya', noVal='tidak' )
                        if SaveBAHASA == 'ya':
                            penambahBAHASA = db.cursor()
                            querDataSiswaBAHASA = "insert into BAHASA (Kode_Kelas,ID_Siswa,Nama_Siswa) values (%s,%s,%s)"
                            querNilSiswaBAHASA = "insert into nilaibahasa (Kode_Nilai,ID_Siswa,Antropologi,Bahasa_Indonesia,Bahasa_Jepang,Bahasa_Inggris) values (%s,%s,'0','0','0','0')"
                            penambahBAHASA.execute(querDataSiswaBAHASA,ValBAHASA)
                            penambahBAHASA.execute(querNilSiswaBAHASA, ValNilBAHASA)
                            db.commit()
                            print("Data Berhasil disimpan")
                            break
                                
                        else:
                            break 
            elif response == 'Back':
                TambahSiswa()                                       
        elif response == 'Back':
            main()
            
def UpdateNilai():
    while True:
        prompt = f"\nList Menu\n\n"  
        choice = ['Update Nilai','Back']
        response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
        if response == 'Update Nilai':
            prompt = f"\nList Menu\n\n"  
            choice = ['IPA','IPS','BAHASA','Back']
            response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
            if response == 'IPA':
                IDSiswa = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                mycursor = db.cursor()
                query = 'select ID_Siswa from nilaiipa'
                mycursor.execute(query)
                result = mycursor.fetchall()
        
                for i, val in enumerate(result):
                    if IDSiswa in val:
                        print(f"ID Ditemukan {IDSiswa}")
                        IDNilSiswaIPA = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                        NilMat = pypi.inputInt(prompt='Masukkan Nilai Matematika: ', max = 100)
                        NilFis = pypi.inputInt(prompt='Masukkan Nilai Fisika: ', max = 100)
                        NilKim = pypi.inputInt(prompt='Masukkan Nilai Kimia: ', max= 100 )
                        NilBio = pypi.inputInt(prompt='Masukkan Biologi: ', max= 100)
                        valNilSiswaIPA = [NilMat,NilFis,NilKim,NilBio,IDNilSiswaIPA]
                        UpdateNilSiswaIPA = pypi.inputYesNo(prompt='Apakah anda ingin mengupdate nilai siswa ? (ya/tidak):', yesVal='ya', noVal='tidak' )
                        if UpdateNilSiswaIPA == "ya":    
                            UpdateNilIPA = db.cursor()
                            querUpdateNilIPA = """
                            UPDATE nilaiipa
                            SET Matematika = %s, Fisika = %s, Kimia = %s, Biologi = %s
                            WHERE ID_Siswa = %s
                            """
                            UpdateNilIPA.execute(querUpdateNilIPA, valNilSiswaIPA)
                            db.commit()
                            print("Nilai Berhasil diupdate")
                            break
                        else:
                            break
                    elif i == len(result) - 1:
                            print("ID tidak Ditemukan")
                            break
            elif response == 'IPS':
                IDSiswa = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                mycursor = db.cursor()
                query = 'select ID_Siswa from nilaiips'
                mycursor.execute(query)
                result = mycursor.fetchall()
        
                for i, val in enumerate(result):
                    if IDSiswa in val:
                        print(f"ID Ditemukan {IDSiswa}")
                        IDNilSiswaIPS = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                        NilGeo = pypi.inputInt(prompt='Masukkan Nilai Geografi: ', max = 100)
                        NilAku = pypi.inputInt(prompt='Masukkan Nilai Akuntansi: ', max = 100)
                        NilSos = pypi.inputInt(prompt='Masukkan Nilai Sosiologi: ', max= 100 )
                        NilSej = pypi.inputInt(prompt='Masukkan Nilai Sejarah: ', max= 100)
                        valNilSiswaIPS = [NilGeo,NilAku,NilSos,NilSej,IDNilSiswaIPS]
                        UpdateNilSiswaIPS = pypi.inputYesNo(prompt='Apakah anda ingin mengupdate nilai siswa ? (ya/tidak):', yesVal='ya', noVal='tidak' )
                        if UpdateNilSiswaIPS == "ya":    
                            UpdateNilIPS = db.cursor()
                            querUpdateNilIPS = """
                            UPDATE nilaiips
                            SET Geografi = %s, Akuntansi = %s, Sosiologi = %s, Sejarah = %s
                            WHERE ID_Siswa = %s
                            """
                            UpdateNilIPS.execute(querUpdateNilIPS, valNilSiswaIPS)
                            db.commit()
                            print("Nilai Berhasil diupdate")
                            break
                        else:
                            break
                    elif i == len(result) - 1:
                            print("ID tidak Ditemukan")
                            break
            elif response == 'BAHASA':
                IDSiswa = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                mycursor = db.cursor()
                query = 'select ID_Siswa from nilaibahasa'
                mycursor.execute(query)
                result = mycursor.fetchall()
        
                for i, val in enumerate(result):
                    if IDSiswa in val:
                        print(f"ID Ditemukan {IDSiswa}")
                        IDNilSiswaBahasa = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                        NilAnt = pypi.inputInt(prompt='Masukkan Nilai Antropologi: ', max = 100)
                        NilBI = pypi.inputInt(prompt='Masukkan Nilai Bahasa Indonesia: ', max = 100)
                        NilBJ = pypi.inputInt(prompt='Masukkan Nilai Bahasa Jepang: ', max= 100 )
                        NilBing = pypi.inputInt(prompt='Masukkan Nilai Bahasa Inggris: ', max= 100)
                        valNilSiswaBahasa = [NilAnt,NilBI,NilBJ,NilBing,IDNilSiswaBahasa]
                        UpdateNilSiswaBahasa = pypi.inputYesNo(prompt='Apakah anda ingin mengupdate nilai siswa ? (ya/tidak):', yesVal='ya', noVal='tidak' )
                        if UpdateNilSiswaBahasa == "ya":    
                            UpdateNilBahasa = db.cursor()
                            querUpdateNilBahasa = """
                            UPDATE nilaibahasa
                            SET Antropologi = %s, Bahasa_Indonesia = %s, Bahasa_jepang = %s, Bahasa_Inggris = %s
                            WHERE ID_Siswa = %s
                            """
                            UpdateNilBahasa.execute(querUpdateNilBahasa, valNilSiswaBahasa)
                            db.commit()
                            print("Nilai Berhasil diupdate")
                            break
                        else:
                            break
                    elif i == len(result) - 1:
                            print("ID tidak Ditemukan")
                            break
            elif response == 'Back':
                UpdateNilai()
            
        elif response == 'Back':
            main()
            
def HapusData():
        while True:
            prompt = f"\nList Menu\n"  
            choice = ['Hapus Data','Back']
            response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
            if response == 'Hapus Data':
                prompt = f"\nList Menu\n"  
                choice = ['IPA', 'IPS', 'Bahasa','Back']
                response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
                if response == 'IPA':
                    IDSiswa = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                    mycursor = db.cursor()
                    query = 'select ID_Siswa from ipa'
                    mycursor.execute(query)
                    result = mycursor.fetchall()
        
                    for i, val in enumerate(result):
                        if IDSiswa in val:
                            print("ID Ditemukan")
                            IDSiswaDel = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                            valDel = [IDSiswaDel]
                            valDel2 = [IDSiswaDel]
                            HapusIPA = pypi.inputYesNo(prompt='Apakah anda ingin menghapus ? (ya/tidak):', yesVal='ya', noVal='tidak' )
                            if HapusIPA == "ya":
    
                                penghapus = db.cursor()
                                querTableNilaiIpa = "DELETE FROM nilaiipa where ID_Siswa = %s"
                                querTableIPA = "DELETE FROM ipa WHERE ID_Siswa = %s"
                                penghapus.execute(querTableNilaiIpa,valDel2)
                                penghapus.execute(querTableIPA, valDel)
                                db.commit()
                                print("Data Berhasil dihapus")
                                break
                            else:
                                break
                        elif i == len(result) - 1:
                                print("ID tidak Ditemukan")
                                break
                elif response == 'IPS':
                    IDSiswaIPSDEL = pypi.inputInt(prompt='Masukkan ID Siswa: ')

                    mycursorIPSDEL = db.cursor()
                    queryIPSDEL = 'select ID_Siswa from ips'

                    mycursorIPSDEL.execute(queryIPSDEL)
                    resultIPSdel = mycursorIPSDEL.fetchall()
        
                    for i, valDelIPSs in enumerate(resultIPSdel):
                        if IDSiswaIPSDEL in valDelIPSs:
                            print("ID Ditemukan")
                            IDSiswaDelIPS21 = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                            valDeXipss = [IDSiswaDelIPS21]
                            valDeXips2 = [IDSiswaDelIPS21]
                            HapusIPs = pypi.inputYesNo(prompt='Apakah anda ingin menghapus ? (ya/tidak):', yesVal='ya', noVal='tidak' )
                            if HapusIPs == "ya":
    
                                penghapusIPSX = db.cursor()
                                querTableNilaiIpa = "DELETE FROM nilaiips where ID_Siswa = %s"
                                querTableIPA = "DELETE FROM ips WHERE ID_Siswa = %s"
                                penghapusIPSX.execute(querTableNilaiIpa,valDeXips2)
                                penghapusIPSX.execute(querTableIPA, valDeXipss)
                                db.commit()
                                print("Data Berhasil dihapus")
                                break
                            else:
                                break
                        elif i == len(resultIPSdel) - 1:
                                print("ID tidak Ditemukan")
                                break
                elif response == 'BAHASA':
                    IDSiswaBagasaX = pypi.inputInt(prompt='Masukkan ID Siswa: ')

                    mycursorBahasX = db.cursor()
                    queryBahasX = 'select ID_Siswa from bahasa'

                    mycursorBahasX.execute(queryBahasX)
                    resultBahasaX = mycursorBahasX.fetchall()
        
                    for i, val in enumerate(resultBahasaX):
                        if IDSiswaBagasaX in val:
                            print("ID Ditemukan")
                            IDSiswaDelBahasaX = pypi.inputInt(prompt='Masukkan ID Siswa: ')
                            valDel = [IDSiswaDelBahasaX]
                            valDel2 = [IDSiswaDelBahasaX]
                            HapusBAHASAX = pypi.inputYesNo(prompt='Apakah anda ingin menghapus ? (ya/tidak):', yesVal='ya', noVal='tidak' )
                            if HapusBAHASAX == "ya":
    
                                penghapusBahasaX = db.cursor()
                                querTableNilaiBahasa = "DELETE FROM nilaibahasa where ID_Siswa = %s"
                                querTableBAHASAXX = "DELETE FROM bahasa WHERE ID_Siswa = %s"
                                penghapusBahasaX.execute(querTableNilaiBahasa,valDel2)
                                penghapusBahasaX.execute(querTableBAHASAXX, valDel)
                                db.commit()
                                print("Data Berhasil dihapus")
                                break
                            else:
                                break
                        elif i == len(resultBahasaX) - 1:
                                print("ID tidak Ditemukan")
                                break
                elif response == 'Back':
                    HapusData()      
            elif response == 'Back':
                main()
                       
def main():
  
    while True:
        prompt = f"\nList Menu\n\n"  
        choice = ['Data Kelas', 'Tambah Siswa', 'Update Nilai', 'Hapus Data', 'Exit']
        response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
        if response == 'Data Kelas':
            DataKelas()
        elif response == 'Tambah Siswa' :
            TambahSiswa()        
        elif response == 'Update Nilai':
            UpdateNilai()
        elif response == 'Hapus Data':
            HapusData()
        elif response == 'Exit':
            response = pypi.inputYesNo(prompt='Apakah anda ingin keluar(ya/tidak):', yesVal='ya', noVal='tidak' )
            if response.lower() == "tidak":
                main()
            elif response.lower() == "ya":
                sys.exit()    

        
main()