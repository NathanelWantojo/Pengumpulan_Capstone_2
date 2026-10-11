
print('Selamat Datang di Hotel Nathan \nSilahkan Pilih Menu di Bawah ini!')
##### READ ##### --------------------------------------------------------------------------------------------
##### DATA UTAMA #####
data_reservasi = { 
    'KB01':{
        'Nama' : 'Budi',
        'Tipe Kamar' : 'Deluxe',
        'Tanggal Check In' : '12 Oktober 2026',
        'Lama Menginap' : '2 Hari'
        },
    'KB02':{
        'Nama' : 'Kevin',
        'Tipe Kamar' : 'Single',
        'Tanggal Check In' : '30 Oktober 2026',
        'Lama Menginap' : '5 Hari'
        }
}

def tampilkan_tabel():
    print(f"\n{'Kode':<10} {'Nama':<20} {'Tipe Kamar':<15} {'Check In':<22} {'Lama Menginap':<15}")
    print("-" * 90)

    for kode, detail in data_reservasi.items():
        print(f"{kode:<10} {detail['Nama']:<20} {detail['Tipe Kamar']:<15} {detail['Tanggal Check In']:<22} {detail['Lama Menginap']:<15}")

    print("-" * 90)

##### MENU UTAMA #####
while True:
    print('\n1. Lihat Reservasi yang Sudah Ada\n2. Jadwalkan Reservasi Hotel\n3. Ubah Jadwal Reservasi\n4. Batalkan Reservasi\n5. Keluar')
    pilih_menu=input('\nMasukkan Menu Pilihan Anda: ').strip()

    if pilih_menu == "1": 
        
        while True:
            print('\n1. Lihat Semua Reservasi')
            print('2. Cari Reservasi')
            print('3. Kembali ke Menu Utama')
    
            menu_1=input('Masukkan Menu Pilihan Anda: ').strip()
            
            if menu_1 == '1':
                
                if data_reservasi:
                    print('Berikut data semua reservasi\n')
                    tampilkan_tabel()
                else:
                    print('tidak ada data')
            
            elif menu_1 == '2':
                
                if data_reservasi:
                    kode_booking=input('\nMasukkan kode Booking yang ingin anda cari: ').strip().upper()
                    
                    if kode_booking in data_reservasi:
                        print(data_reservasi[kode_booking])
                    else:
                        print('Kode booking tidak ditemukan')
                
                else:
                    print('tidak ada data')
            
            elif menu_1 == '3':
                break
            else: 
                print ('Pilihan Anda Tidak Terdaftar')

##### CREATE ##### -------------------------------------------------------------------------------------------------------------
    elif pilih_menu == "2":
        
        while True:
            print('\n1. Jadwalkan Reservasi\n2. Kembali ke Menu Utama')
            menu_2=input('Masukkan Menu Pilihan Anda: ').strip()
            
            if menu_2 == '1':
                
                kode_baru=input('\nMasukkan Kode Booking Baru: ').strip().upper()
                if kode_baru in data_reservasi:
                    print(f'Kode Booking {kode_baru} Sudah Terdaftar')
                else:
                    nama=input('Masukkan Nama Anda: ').strip().title()
                    tipe_kamar=input('Masukkan Tipe Kamar yang Anda Pilih (Single/Double/Deluxe/Diamond/Sapphire): ').strip().title()
                    tanggal_menginap=input('Masukkan Tanggal Anda Mulai Menginap (tanggal/bulan/tahun): ').strip().title()
                    lama_menginap=input('Masukkan Lama Waktu Anda Menginap (Jumlah Hari): ').strip() + ' Hari'
                    print('Simpan Reservasi Anda?\n\n1. Ya\n2. Tidak')
                    menu_reservasi = input('Masukkan Menu Pilihan Anda: ').strip()

                    if menu_reservasi == '1':
                        print('Menyimpan data...')

                        data_reservasi[kode_baru] = {
                            'Nama': nama,
                            'Tipe Kamar': tipe_kamar,
                            'Tanggal Check In': tanggal_menginap,
                            'Lama Menginap': lama_menginap
                            }

                        print('Reservasi berhasil disimpan')

                    elif menu_reservasi == '2':
                        print('Reservasi tidak disimpan')
                    else:
                        print('Pilihan Anda Tidak Terdaftar')
            
            elif menu_2 == '2':
                break
            else:
                print('Pilihan Anda Tidak Terdaftar')
    
    ##### UPDATE ##### --------------------------------------------------------------------------------------------
    elif pilih_menu == "3": 

        while True:
            print('\n1. Ubah Reservasi\n2. Kembali ke Menu Utama')
            menu_3=input('Masukkan Menu Pilihan Anda: ').strip()

            if menu_3 == '1':
               
                if data_reservasi:
                    tampilkan_tabel()
                    
                    kode_edit = input('Masukkan Kode yang akan Anda Ubah: ').strip().upper()
                    if kode_edit in data_reservasi:
                        print(data_reservasi[kode_edit])
                        print('\nUbah Data?\n1. Ya\n2. Batalkan')
                        
                        update_kode=input('Masukkan Menu Pilihan Anda: ').strip()
                        if update_kode =='1':
                            update_data = input('Masukkan Data yang ingin Anda Update: ').strip().title()
                            if update_data in data_reservasi[kode_edit]:
                                nilai_baru = input(f'Masukkan {update_data} terbaru: ').strip().title()
                                if update_data == 'Lama Menginap':
                                    nilai_baru = nilai_baru + ' Hari'
                                print('Simpan Perubahan?\n1. Ya\n2. Tidak')
                                nilai_berubah = input('Masukkan Menu Pilihan Anda: ').strip()
                                if nilai_berubah == '1':
                                    data_reservasi[kode_edit][update_data] = nilai_baru
                                    print(f'{update_data} berhasil diperbarui')
                                elif nilai_berubah =='2':
                                    print(f'Perubahan {update_data} Dibatalkan')
                                else:
                                    print('Pilihan Anda Tidak Terdaftar')
                            else:
                                print('Data yang Anda Masukkan Salah')
                            
                        elif update_kode =='2':
                            print('Perubahan Dibatalkan')
                        else:
                            print('Pilihan Anda Tidak Terdaftar')
                    else:
                        print('Data Tidak Ditemukan')
                
                else:
                    print('Tidak Ada Data')
                    
            elif menu_3 == '2':
                break
            else:
                print('Pilihan Anda Tidak Terdaftar')

        
    ##### DELETE ##### -----------------------------------------------------------------------------------------------------------------------
    elif pilih_menu == "4":
        while True:
            print('1. Hapus Reservasi\n2. Kembali Ke Menu Utama')
            menu_4=input('Masukkan Menu Pilihan Anda: ').strip()

            if menu_4 == '1':

                if data_reservasi:
                    print(data_reservasi)

                    hapus_data=input('Masukkan Kode Booking Reservasi yang ingin Dihapus: ').strip().upper()
                    if hapus_data in data_reservasi:
                        print(data_reservasi[hapus_data])
                        print('\n1. Hapus Data\n2. Batalkan')

                        delete_kode = input('Masukkan Menu Pilihan Anda: ').strip()

                        if delete_kode == '1':
                            del data_reservasi[hapus_data]
                            print(f'Kode {hapus_data} Berhasil di Hapus')
                        elif delete_kode == '2':
                            print(f'Batal Menghapus Kode {hapus_data}')
                        else:
                            print('Pilihan Anda Tidak Terdaftar')


                    else:
                        print('Kode Booking Tidak Terdaftar')

                else:
                    print('Tidak Ada Data')

            elif menu_4 == '2':
                break
            else:
                print('Pilihan Anda Tidak Terdaftar')
                

##### CLOSE #####------------------------------------------------------------------------------------------------------------------
    elif pilih_menu == "5" :
        print('\nKeluar dari Menu')
        break
    else :
        print('\nPilihan Menu Anda Tidak Terdaftar')
    

