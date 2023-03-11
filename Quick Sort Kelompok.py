'''Anggota Kelompok: - Syarifatul Daimahtul Fatiyyah L200190077
                     - Muhammad Nur Taufiq L200190085
'''


from prettytable import PrettyTable
import pandas as pd

data = pd.read_excel(r'./PialaDunia.xlsx', engine='openpyxl')
data_list = data.values.tolist()

while True:
    print("==========Program Quicksort Jadwal Pertandingan Piala Dunia 2018==========")
    print("Ketik 1 = Quicksort huruf alphabet dari kolom tempat pertandingan")
    print("Ketik 2 = Quicksort waktu pertandingan awal ke akhir")
    print("Ketik 3 = Quicksort waktu pertandingan akhir ke awal")
    print("Ketik 0 = menghentikan program\n")
    pilih = int(input("Masukkan angka : "))
    
    class pil_dun(object):
        def __init__(self, ambil):
            self.match = ambil[0]
            self.venue = ambil[1]
            self.time = ambil[2]

        def getTempat(self):
            return self.venue
        def getWaktu(self):
            return self.time

    tabelPildun = PrettyTable(["Pertandingan/Match", "Tempat/Venue", "Waktu/Time"])
    daftarpildun =[]
    for i in range(len(data_list)):
        daftarpildun.append(pil_dun(data_list[i]))

    #=====Quicksort huruf alphabet dari kolom tempat pertandingan=====#
    if pilih == 1:
        def quickSort(A):
            quickSortBantu(A, 0, len(A)-1)

        def quickSortBantu(A, awal, akhir):
            if awal < akhir:
                titikBelah = partisi(A, awal, akhir)
                quickSortBantu(A, awal, titikBelah - 1)
                quickSortBantu(A, titikBelah + 1, akhir)

        def partisi(A, awal, akhir):
            nilaiPivot = A[awal].getTempat()
            tanda_Kiri = awal + 1
            tanda_Kanan = akhir

            selesai = False
            while not selesai :
                while tanda_Kiri <= tanda_Kanan and A[tanda_Kiri].getTempat() <= nilaiPivot:
                    tanda_Kiri = tanda_Kiri + 1
                while A[tanda_Kanan].getTempat() >= nilaiPivot and tanda_Kanan >= tanda_Kiri:
                    tanda_Kanan = tanda_Kanan - 1

                if tanda_Kanan < tanda_Kiri:
                    selesai = True
                else:
                    temp = A[tanda_Kiri]
                    A[tanda_Kiri] = A[tanda_Kanan]
                    A[tanda_Kanan] = temp

            temp = A[awal]
            A[awal] = A[tanda_Kanan]
            A[tanda_Kanan] = temp

            return tanda_Kanan

        quickSort(daftarpildun)
        for i in daftarpildun:
            tabelPildun.add_row([i.match, i.venue, i.time])
        print(tabelPildun)
        print("\n")






    #=====Quicksort waktu pertandingan awal ke akhir=====#
    if pilih == 2:
        def quickSort(A):
            quickSortBantu(A, 0, len(A)-1)

        def quickSortBantu(A, awal, akhir):
            if awal < akhir:
                titikBelah = partisi(A, awal, akhir)
                quickSortBantu(A, awal, titikBelah - 1)
                quickSortBantu(A, titikBelah + 1, akhir)

        def partisi(A, awal, akhir):
            nilaiPivot = A[awal].getWaktu()
            tanda_Kiri = awal + 1
            tanda_Kanan = akhir

            selesai = False
            while not selesai :
                while tanda_Kiri <= tanda_Kanan and A[tanda_Kiri].getWaktu() <= nilaiPivot:
                    tanda_Kiri = tanda_Kiri + 1

                while A[tanda_Kanan].getWaktu() >= nilaiPivot and tanda_Kanan >= tanda_Kiri:
                    tanda_Kanan = tanda_Kanan - 1

                if tanda_Kanan < tanda_Kiri:
                    selesai = True
                else:
                    temp = A[tanda_Kiri]
                    A[tanda_Kiri] = A[tanda_Kanan]
                    A[tanda_Kanan] = temp

            temp = A[awal]
            A[awal] = A[tanda_Kanan]
            A[tanda_Kanan] = temp

            return tanda_Kanan

        quickSort(daftarpildun)
        for i in daftarpildun:
            tabelPildun.add_row([i.match, i.venue, i.time])
        print(tabelPildun)
        print("\n")


    #=====Quicksort waktu pertandingan akhir ke awal=====#
    if pilih == 3:
            def quickSort(A):
                def quickSortBantu(A, awal, akhir):
                    if awal < akhir:
                        titikBelah = partisi(A, awal, akhir)
                        quickSortBantu(A, awal, titikBelah)
                        quickSortBantu(A, titikBelah + 1, akhir)
                quickSortBantu(A, 0, len(A)-1)
                    
            def partisi(A, awal, akhir):
                nilaiPivot = A[awal].getWaktu()
                tanda_Kiri = awal - 1
                tanda_Kanan = akhir + 1

                selesai = False
                while not selesai :
                    tanda_Kiri += 1
                    while A[tanda_Kiri].getWaktu() > nilaiPivot:
                        tanda_Kiri += 1
                    tanda_Kanan -= 1

                    while A[tanda_Kanan].getWaktu() < nilaiPivot:
                        tanda_Kanan -= 1
                    if tanda_Kiri >= tanda_Kanan:
                        return tanda_Kanan
                    A[tanda_Kiri], A[tanda_Kanan] = A[tanda_Kanan], A[tanda_Kiri]


            quickSort(daftarpildun)
            for i in daftarpildun:
                tabelPildun.add_row([i.match, i.venue, i.time])
            print(tabelPildun)
            print("\n")


    if pilih == 0 :
        break
