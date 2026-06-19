import streamlit as st
import csv

def tampilkan_menu_booking():
    st.header("Booking & Antrean")
    
    data_bkg = []
    with open('booking.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_bkg.append(row)
            
    st.subheader("Antrean Aktif Saat Ini")
    st.table(data_bkg)
    
    st.subheader("Ambil Antrean Baru")
    data_plg = []
    with open('pelanggan.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_plg.append(row)
            
    opsi_plg = []
    for p in data_plg:
        opsi_plg.append(f"{p['id_pelanggan']} - {p['nama']}")
        
    if not opsi_plg:
        st.warning("Silakan daftarkan pelanggan terlebih dahulu di menu Pelanggan!")
        return
        
    plg_terpilih = st.selectbox("Pilih Pelanggan", opsi_plg)
    id_plg = plg_terpilih.split(" - ")[0]
    
    jam = st.text_input("Masukkan Jam (atau ketik 'Antrean')", value="Antrean")
    
    if st.button("Konfirmasi Ambil Antrean"):
        id_bkg_baru = f"BKG{len(data_bkg) + 1:03d}"
        data_bkg.append({'id_booking': id_bkg_baru, 'id_pelanggan': id_plg, 'jam_booking': jam, 'status': 'Aktif'})
        
        with open('booking.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id_booking', 'id_pelanggan', 'jam_booking', 'status'])
            writer.writeheader()
            writer.writerows(data_bkg)
            
        st.success(f"Sukses Mencatat Antrean! ID Booking: {id_bkg_baru}")