import weaviate

client = weaviate.Client(
    url="https://njiyah3aqkrspt2dw1kaw.c0.asia-southeast1.gcp.weaviate.cloud",
    auth_client_secret=weaviate.AuthApiKey(
        api_key="cfzSw0lnUQ0YZ8N39qDjVVRf1GlbypwTm6Vx"  # Ganti dengan API Key Anda
    )
)
# Mendefinisikan schema untuk collection "buku"
schema = {
    "classes": [
        {
            "class": "Buku",  # Nama class
            "properties": [
                {
                    "name": "no_buku",  # Nama properti
                    "dataType": ["int"]  # Tipe data
                },
                {
                    "name": "judul",
                    "dataType": ["text"]
                },
                {
                    "name": "genre",
                    "dataType": ["text"]
                },
                {
                    "name": "penulis",
                    "dataType": ["text"]
                }
            ]
        }
    ]
}

# Membuat schema di Weaviate
client.schema.create(schema)
