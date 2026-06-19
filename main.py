import streamlit as st
from file_layanan import tampilkan_menu_layanan
from file_pelanggan import tampilkan_menu_pelanggan
from file_booking import tampilkan_menu_booking
from file_kasir import tampilkan_menu_kasir
from file_laporan import tampilkan_menu_laporan

st.title("Aplikasi Barbershop")

menu = st.sidebar.radio(
    "MENU",
    ["Daftar Layanan", "Data Pelanggan", "Booking & Antrean", "Kasir Pembayaran", "Laporan & Riwayat"]
)

if menu == "Daftar Layanan":
    tampilkan_menu_layanan()
elif menu == "Data Pelanggan":
    tampilkan_menu_pelanggan()
elif menu == "Booking & Antrean":
    tampilkan_menu_booking()
elif menu == "Kasir Pembayaran":
    tampilkan_menu_kasir()
elif menu == "Laporan & Riwayat":
    tampilkan_menu_laporan()