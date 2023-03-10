import os
os.system("cls")
# membersihkan tampilan agar terlihat rapi

def fibosearch(arr, x): 
    n = len(arr) # untuk mendifinisikan panjang array
    n2 = 0 # fibonacci n-2
    n1 = 1 # fibonacci n-1
    fibM = n2 + n1 # rumus fibonacci

# mencari nilai dari fibonacci (n) mulai dari yang terbesar, yang terkecil atau yang sama dengan n
    while (fibM < n):
        n2 = n1
        n1 = fibM
        fibM = n2 + n1

# indeks untuk pencarian di awal 
    offset = -1

# mulai melakukan pencarian
    while (fibM > 1):

        # jika x disini lebih besar daripada elemen pada indeks i, maka akan dilakukan pencarian di sebelah kanan sub array
        i = min(offset + n2, n-1)
        if (arr[i] < x):
            fibM = n1
            n1 = n2
            n2 = fibM - n1
            offset = i

        # jika x disini lebih kecil daripada elemen pada indeks i, maka akan dilakukan pencarian di sebelah kiri sub array
        elif (arr[i] > x):
            fibM = n2
            n1 = n1 - n2
            n2 = fibM - n1
        
        #  jika x yang dicari ditemukan maka akan mengembalikan ke indeks i 
        else:
            return i

    # jika elemen tidak ditemukan, maka akan dilakukan pengembalian yakni pada -1
    if(n1 and arr[n-1] == x):
        return n-1

    # jika elemen tidak ditemukan, maka akan dilakukan pengembalian yakni pada -1
    return -1

arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
for i in range (10): 
    x = input("Input nama yang ingin dicari : ")

    for i in range(len(arr)):
        if type(arr[i]) == list:
            for a in range(len(arr[i])): #untuk mendapatkan index maka harus menghitung panjang array
                if arr[i][a] == x: # jika data berada dalam kolom
                    kolomdata = fibosearch(arr[i], x)
                    print(x, "berada di array index ke - ", i, "kolom", kolomdata)
        else : # jika elemen sama dengan elemen yang dicari maka ia akan mengembalikan nilai
            if arr[i] == x : 
                kolomdata = fibosearch(arr[i], x)
                print(x, "berada di array index ke - ", i)
