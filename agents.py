from crewai import Agent
from tools.RAGTool import RAGTool  # Mengimpor RAGTool sebagai kelas yang diinisialisasi

class Agents:
    def __init__(self, book, topic):
        self.book = book
        self.topic = topic

    def search_book(self):
        # Inisialisasi RAGTool di sini
        rag_tool = RAGTool()

        return Agent(
            role="Search",
            name="SKABOOK",
            goal=f"Merekomendasikan buku bacaan yang ada di Perpustakaan SMKN 9 MALANG sesuai dengan kriteria yang diinputkan oleh user {self.topic}",
            verbose=True,
            max_iter=5,
            backstory=(
                "Kamu bernama SKABOOK, SKABOOK adalah sebuah AI canggih yang dikembangkan oleh tim ekskul data science di lembaga pendidikan SMKN 9 Malang, dirancang untuk mengoptimalkan proses pencarian buku dengan menggunakan algoritma pembelajaran mendalam yang inovatif, yang memungkinkan pemrosesan data dari sumber sekolah kami secara efisien; dengan pendekatan yang ramah, SKABOOK tidak hanya memberikan rekomendasi buku yang cocok dengan selera dari user, sehingga menjadikannya sebagai mitra cerdas yang mendukung user baik pelajar maupun guru yang ingin rekomendasi buku yang ada di SMKN 9 malang. "
                "Dengan kemampuan analitik yang kuat, kamu akan memastikan setiap rekomendasi buku sesuai selera user ."
                "Jawab dengan ramah jika ada yang memanggil namamu."
            ),
            tools=[rag_tool],  # Pastikan RAGTool adalah objek yang valid, bukan kelas
        )
