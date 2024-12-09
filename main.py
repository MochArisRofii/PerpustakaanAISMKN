import streamlit as st
from crewai import Crew, Process
from static import Static
from agents import Agents
from tasks import Tasks
from database import saveSurvey

# Konfigurasi Halaman
Static.pageConfig()
Static.pageCss()
Static.logo()
Static.pageTitle()

# Input Data Pengguna
with st.container():
    # Bagian pertama: Input data pengguna
    name = st.text_input("Nama Lengkap : ", placeholder="Masukkan Nama Lengkap...")
    phone = st.text_input("Nomor Telepon : ", placeholder="Masukkan Nomor Telepon...")
    category = st.selectbox(
        "Kategori Identitas :",
        [
            "Pilih Kategori Identitas...",
            "Guru",
            "Siswa/Siswi",
            "Orang Tua/Wali",
            "Masyarakat Umum",
        ],
    )

    # Validasi Input Pengguna
    if not name or not phone or category == "Pilih Kategori Identitas...":
        st.warning("❕ Pastikan semua data pengguna telah diisi dengan benar.")
    else:
        st.success("✅ Data pengguna lengkap.")

        # Bagian kedua: Input untuk pencarian informasi
        st.header("Pencarian Informasi")
        book = st.text_input("Genre Buku : ", placeholder="Masukkan Genre Buku...")
        topic = st.text_input(
            "Masukkan kriteria yang ingin kamu cari:",
            placeholder="Contoh: Rekomendasi buku genre romansa dari penulis tere liye?",
        )
        language = st.selectbox(
            "Bahasa:",
            ["Pilih Bahasa...", "Bahasa Indonesia", "Bahasa Jawa", "Bahasa Inggris"],
        )

        search_button = st.button("🔍 Mulai Penelitian")

        if search_button:
            if not topic:
                st.error("❌ Tolong masukkan kriteria buku.")
            elif language == "Pilih Bahasa...":
                st.error("❌ Tolong pilih bahasa.")
            else:
                # Proses Pencarian
                try:
                    crew = Crew(
                        agents=[Agents(book ,topic).search_book()],
                        tasks=[Tasks(book ,topic, language).research_task()],
                        verbose=True,
                        process=Process.sequential,
                    )
                    with st.spinner("🔄 Sedang mencari informasi..."):
                        result = crew.kickoff()
                        saveSurvey(name, phone, category, topic, language)

                    # Tampilkan Hasil
                    st.subheader("Hasil Pencarian:")
                    st.markdown(result)

                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")
