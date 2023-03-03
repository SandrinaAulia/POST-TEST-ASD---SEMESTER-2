import os 
# membersihkan tampilan agar terlihat rapi
os.system ('cls')
import random # library yang berfungsi menghasilkan data dalam bentuk acak

print(95*"=")
print(" >>>>>>>>> MERGESORT <<<<<<<<< ".center(95,"-"))
print(95*"-")

def ms(sample) :
    if len(sample) <= 1 : # jika panjang data kurang dari atau sama dengan satu maka akan mengembalikan data
        return sample
    else :
        mid = len(sample) //2 # membagi elemen data menjadi 2 sub yakni sub kanan dan kiri 
        left = sample[:mid] # memanggil data yang ada disebelah kiri yang telah dibagi 2 tadi
        right = sample[mid:] # memanggil data yang ada disebelah kanan yang telah dibagi 2 tadi 

        ms(left) # memanggil data yang berada di sebelah kiri
        ms(right) # memanggil data yang berada di sebelah kanan 

        # u dan v merupakan index untuk elemen kanan dan kiri
        # sedangkan w ialah penggabungan antara kedua index
        u = v = w = 0 
        while u < len(left) and v < len(right):
        # jika elemen kiri jumlahnya kurang dari kanan maka elemen kiri bisa ditambahkan ke output
            if left[u] < right [v]:
                sample[w] = left[u]
                u = u + 1 # bertugas menambahkan elemen ke awal
            else : # bila u tidak berlaku maka akan berlanjut ke v
                sample[w] = right[v]
                v = v + 1
            w = w+1 #perpindahan ke dalam slot berikutnya

        # elemen sisa
        while u < len(left):
            sample[w] = left[u]
            u = u+1
            w = w+1

        while v < len(right):
            sample[w] = right[v]
            v = v+1
            w = w+1
    return sample # mengembalikan data 



sample = [random.randint(1,49) for u in range(12)] 
print(f" Merge sort sebelum di Sorting : ", sample)
ms(sample) # menjalankan proses sorting 
print(f" Merge sort setelah di Sorting : ", sample) 


print(95*"=")
print(" >>>>>>>>> QUICK SORT <<<<<<<<< ".center(95,"-"))
print(95*"-")

def partition(arr, low, high):
    # pilih elemen ujung kanan sebagai pivot
    pivot = arr[high]
    # pointer untuk elemen yang lebih besar 
    i = low - 1
    # membandingkan elemen elemen dengan pivot 
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1 # i berfungsi untuk menukar elemen yang lebih kecil dari pivot ke elemen yang lebih besar
            (arr[i], arr[j]) = (arr[j], arr[i]) # penukaran elemen i dan j 
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1]) # penukaran pivot dengan elemen yang lebih besar oleh i tadi
    return i + 1 # mengembalikan kepada posisi partisi 

# proses sorting 
def quickSort(array, low, high): # mencari pivot, elemen yang lebih kecil berada disebelah kiri dari pivot
    if low < high:               # begitu juga sebaliknya, elemen lebih besar berada disebelah knan pivot
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1) # memanggil elemen kiri
        quickSort(array, pi + 1, high) # memanggil elemen kanan


sample =  [random.randint(50,94) for i in range(12)]
print(f" Quick sort sebelum di Sorting : ", sample) 
size = len(sample) # menampilkan elemen dalam list
quickSort(sample, 0, size - 1) # menjalankan proses sorting 
print(f" Quick sort setelah di Sorting : ", sample)


print(95*"=")
print(" >>>>>>>>> SHELL SORT <<<<<<<<< ".center(95,"-"))
print(95*"-")

def shell(sample):
    L = len(sample)
    gap = int(L/2) # menentukan jarak lompatan index berdasarkan pembagian panjang data

    while gap > 0:
        for u in range (gap, L):
            value = sample[u] # mengmbil value dari index u 
            v = u # menginisiasi index v
            while v >= gap and sample [v-gap] > value:
                sample[v] = sample[v-gap] # menginisiasi value index v dengan value index (v-gap)
                v -= gap  # untuk menghentikan perulangan 
            sample [v] = value # menginisiasi value index v dengan value index u
        gap //= 2 # memperkecil gap
    return sample # mengembalikan data

sample = [random.randint(95,150) for u in range(12)]
print(f" Shell sort sebelum di Sorting : {sample}")
shell(sample) # menampilkan elemen dalam list
print(f" Shell sort setelah di Sorting : {sample}")
print (95*"=")