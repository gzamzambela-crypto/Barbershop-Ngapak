import streamlit as st
import csv

def tampilkan_menu_pelanggan():
    st.header("Data Pelanggan")
    
    data_plg = []
    with open('pelanggan.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_plg.append(row)
            
    st.table(data_plg)
    
    st.subheader("Registrasi Pelanggan Baru")
    nama_baru = st.text_input("Nama Lengkap")
    hp_baru = st.text_input("Nomor HP")
    
    if st.button("Daftarkan Pelanggan"):
        if nama_baru and hp_baru:
            id_baru = f"PLG{len(data_plg) + 1:03d}"
            data_plg.append({'id_pelanggan': id_baru, 'nama': nama_baru, 'no_hp': hp_baru})
            
            with open('pelanggan.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['id_pelanggan', 'nama', 'no_hp'])
                writer.writeheader()
                writer.writerows(data_plg)
                
            st.success(f"Pendaftaran Berhasil! ID Pelanggan Anda: {id_baru}")
        else:
            st.error("Nama dan nomor HP tidak boleh kosong!")