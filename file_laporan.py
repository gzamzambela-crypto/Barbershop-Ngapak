import streamlit as st
import csv
from datetime import datetime

def tampilkan_menu_laporan():
    st.header("Laporan Pendapatan Harian")
    
    data_trx = []
    with open('transaksi.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_trx.append(row)
            
    hari_ini = datetime.now().strftime("%Y-%m-%d")
    total_pemasukan = 0
    transaksi_hari_ini = []
    
    for t in data_trx:
        if t['tanggal'] == hari_ini:
            transaksi_hari_ini.append(t)
            total_pemasukan = total_pemasukan + int(t['total'])
            
    st.write(f"Total Pemasukan Hari Ini ({hari_ini}): **Rp {total_pemasukan:,}**")
    st.table(transaksi_hari_ini)
    
    st.write("---")
    st.header("Riwayat Pelanggan")
    
    id_cari = st.text_input("Masukkan ID Pelanggan (Contoh: PLG001)")
    
    if st.button("Cari Riwayat"):
        riwayat_plg = []
        for t in data_trx:
            if t['id_pelanggan'].lower() == id_cari.strip().lower():
                riwayat_plg.append(t)
                
        if riwayat_plg:
            st.success(f"Ditemukan {len(riwayat_plg)} riwayat transaksi untuk {id_cari}")
            st.table(riwayat_plg)
        else:
            st.error("Tidak ada riwayat transaksi untuk ID pelanggan tersebut.")