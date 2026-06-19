import streamlit as st
import csv

def tampilkan_menu_layanan():
    st.header("Manajemen Layanan")
    
    data = []
    with open('layanan.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
            
    st.table(data)
    
    st.write("---")
    st.subheader("Tambah Layanan")
    nama_baru = st.text_input("Nama Layanan Baru")
    harga_baru = st.text_input("Harga Layanan Baru")
    
    if st.button("Simpan Baru"):
        data.append({'nama': nama_baru, 'harga': harga_baru})
        with open('layanan.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['nama', 'harga'])
            writer.writeheader()
            writer.writerows(data)
        st.success("Berhasil ditambah!")
        st.rerun()

    st.write("---")
    st.subheader("Ubah / Hapus Layanan")
    
    daftar_nama = []
    for d in data:
        daftar_nama.append(d['nama'])
        
    pilihan = st.selectbox("Pilih Layanan", daftar_nama)
    harga_ubah = st.text_input("Masukkan Harga Baru")
    
    if st.button("Ubah Harga"):
        for d in data:
            if d['nama'] == pilihan:
                d['harga'] = harga_ubah
                
        with open('layanan.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['nama', 'harga'])
            writer.writeheader()
            writer.writerows(data)
        st.success("Harga berhasil diubah!")
        st.rerun()
        
    if st.button("Hapus Layanan"):
        data_baru = []
        for d in data:
            if d['nama'] != pilihan:
                data_baru.append(d)
                
        with open('layanan.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['nama', 'harga'])
            writer.writeheader()
            writer.writerows(data_baru)
        st.success("Layanan berhasil dihapus!")
        st.rerun()