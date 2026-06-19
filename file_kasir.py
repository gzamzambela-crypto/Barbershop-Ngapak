import streamlit as st
import csv
from datetime import datetime

def tampilkan_menu_kasir():
    st.header("Kasir Pembayaran")
    
    data_bkg = []
    with open('booking.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_bkg.append(row)
            
    opsi_bkg = []
    for b in data_bkg:
        if b['status'] == 'Aktif':
            opsi_bkg.append(b['id_booking'])
            
    data_lay = []
    with open('layanan.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_lay.append(row)
            
    opsi_lay = []
    for l in data_lay:
        opsi_lay.append(f"{l['nama']} - Rp {l['harga']}")
        
    if not opsi_bkg:
        st.info("Semua antrean booking sudah selesai dibayar!")
        return
        
    id_bkg_pilih = st.selectbox("Pilih ID Booking Antrean", opsi_bkg)
    lay_pilih = st.selectbox("Pilih Layanan Yang Diambil", opsi_lay)
    
    nama_layanan = lay_pilih.split(" - Rp ")[0]
    harga_layanan = int(lay_pilih.split(" - Rp ")[1])
    
    st.write(f"### Total Tagihan: **Rp {harga_layanan:,}**")
    uang_tunai = st.number_input("Masukkan Uang Tunai Pelanggan", min_value=0, step=5000)
    
    if st.button("Proses Bayar"):
        if uang_tunai < harga_layanan:
            st.error("Maaf, uang tunai pelanggan kurang!")
        else:
            kembalian = uang_tunai - harga_layanan
            st.success(f"Transaksi Berhasil! Kembalian: Rp {kembalian:,}")
            
            id_pelanggan_target = ""
            for b in data_bkg:
                if b['id_booking'] == id_bkg_pilih:
                    b['status'] = 'Selesai'
                    id_pelanggan_target = b['id_pelanggan']
                    
            with open('booking.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['id_booking', 'id_pelanggan', 'jam_booking', 'status'])
                writer.writeheader()
                writer.writerows(data_bkg)
                
            data_trx = []
            with open('transaksi.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data_trx.append(row)
                    
            id_trx_baru = f"TRX{len(data_trx) + 1:03d}"
            tanggal_hari_ini = datetime.now().strftime("%Y-%m-%d")
            
            data_trx.append({
                'id_transaksi': id_trx_baru,
                'tanggal': tanggal_hari_ini,
                'id_pelanggan': id_pelanggan_target,
                'layanan': nama_layanan,
                'total': str(harga_layanan)
            })
            
            with open('transaksi.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['id_transaksi', 'tanggal', 'id_pelanggan', 'layanan', 'total'])
                writer.writeheader()
                writer.writerows(data_trx)