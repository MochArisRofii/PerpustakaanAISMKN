from crewai import Task
from agents import Agents
from tools.RAGTool import RAGTool  # Pastikan RAGTool diimpor dengan benar

class Tasks:
    def __init__(self, topic, language, book):
        self.topic = topic
        self.language = language
        self.book = book
        
    def research_task(self):
        # Inisialisasi RAGTool di sini
        rag_tool = RAGTool()

        # Membuat instance task
        return Task(
            description=(
                f"Hey! Mari kita cari tahu buku sesuai {self.book} di SMKN 9 Malang🔍 "
            ),
            expected_output=(
                f"""
                 ✨ Berikan ringkasan dalam bahasa {self.language} yang:
                
                🗣️ Menggunakan bahasa {self.language} yang gaul & kekinian yang sopan
                🎯 Fokus memberikan rekomendasi sesuai {self.book}
                ❌ Katakan Maaf jika tidak ada info valid
                
                Format jawaban:
                
                💡 [Judul Buku]
                
                📖[Genre Buku]
                🖋️[Penulis]
                
                🔍 Sumber: [link valid]
                """
            ),
            agent=Agents(self.topic, self.book).search_book(),  # Agent yang sudah disiapkan untuk mencari buku
            tools=[rag_tool],  # Pastikan kita memasukkan objek RAGTool
        )