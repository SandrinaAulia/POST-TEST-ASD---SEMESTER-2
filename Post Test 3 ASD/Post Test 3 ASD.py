# Nama : Sandrina Aulia
# NIM  : 2209116003
# Post Test 3 "Double Linked List"

import os
os.system("cls")
from prettytable import PrettyTable

class Node:
    def __init__(self, nik, nama, tanggal_lahir, riwayat_penyakit):
        self.next = None
        self.prev = None
        self.nik = nik
        self.nama = nama
        self.tanggal_lahir = tanggal_lahir
        self.riwayat_penyakit = riwayat_penyakit


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, nik, nama, tanggal_lahir, riwayat_penyakit):
        node = Node(nik, nama, tanggal_lahir, riwayat_penyakit)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.size -= 1

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.nik == value:
                self.__remove_node(node)
            node = node.next

    def display(self):
        tabel= PrettyTable(['NIK','Nama', 'Tanggal_Lahir', 'Riwayat_Penyakit']) 
        head = self.head
        while head is not None:

            tabel.add_row([head.nik, head.nama, head.tanggal_lahir, head.riwayat_penyakit])
            head = head.next
            
        print(tabel)

class historymasuk :
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    def add(self, nik, nama, tanggal_lahir, riwayat_penyakit):
        node = Node(nik, nama, tanggal_lahir, riwayat_penyakit)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def display2 (self):
        if self.head is None:
            print("Linked list kosong")
        else:
            tabel= PrettyTable(['No','NIK' ,'Nama', 'Tanggal_Lahir', 'Riwayat_Penyakit']) 
            head = self.head
            x2 = 1
            while head is not None:

                tabel.add_row([x2, head.nik, head.nama, head.tanggal_lahir, head.riwayat_penyakit])
                x2 +=1
                head = head.next    
        print(tabel)

  
listnya2 = historymasuk()
data = DoubleLinkedList()

while True :
    os.system('cls')
    menu = int(input("""
    ---------------------------------------------------
                1. Tambah Riwayat Pasien
                2. Lihat Riwayat Pasien
                3. Hapus Riwayat Pasien
                4. History
                5. Keluar
    ---------------------------------------------------
                Masukan pilihan anda :  """))
    
    if menu == 1 :
        ulang = "y"
        while (ulang == "y"):
            os.system('cls')
            nik = str(input("Masukan NIK : "))
            nama = str(input("Masukan Nama : "))
            tanggal = str(input("Masukan Tanggal Lahir : "))
            riwayat = str(input("Masukan Riwayat Penyakit: "))
            data.add(nik, nama, tanggal, riwayat)
            listnya2.add(nik, nama, tanggal, riwayat)
            data.display()
            ulang = input("Apakah anda ingin memasukan data lagi (y/n) : ")
            if ulang == "n":
                break
    elif menu == 2 :
        ulang = "y"
        while (ulang == "y"):
            os.system('cls')
            data.display()
            ulang = input("Apakah anda ingin menampilkan data lagi (y/n) : ")
            if ulang == "n":
                break
    elif menu == 3 :
        ulang = "y"
        while (ulang == "y"):
            os.system('cls')
            hapus = str(input("Masukan NIK yang akan dihapus : "))
            data.remove(hapus)
            data.display()
            ulang = input("Apakah anda ingin menghapus data lagi (y/n) : ")
            if ulang == "n":
                break
    elif menu == 4 :
        ulang = "y"
        os.system('cls')
        print(" Pastikan Anda Telah Menambahkan Data Sebelumnya Jika Ingin Melihat History ")
        while True :
            print('''
                       Menu History
        ------------------------------------------
            1. Pasien yang sudah terdaftar
            2. Keluar Menu History
        ------------------------------------------
            ''')
            inputhistory = input("Masukan Menu : ")
            os.system("cls")
            if inputhistory == "1":
                print("Berikut Data Pasien yang telah melakukan pendaftaran di Rumah sakit ini")
                listnya2.display2()
            elif inputhistory == "2":
                os.system('cls')
                break
            else:
                print('Input Salah')
                os.system('cls')
                ulang = input("Apakah anda ingin mengulang menu tersebut lagi (y/n) : ")
                if ulang == "n":
                    break       
    elif menu == 5:
        os.system('cls')
        print("Anda telah keluar dari program")
        break       