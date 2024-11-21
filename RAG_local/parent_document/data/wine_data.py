class Document:
    def __init__(self, page_content, metadata):
        self.page_content = page_content
        self.metadata = metadata

docs = [
    Document(
        page_content="Complex, layered, rich red with dark fruit flavors",
        metadata={"name": "Opus One", "year": 2018, "rating": 96, "grape": "Cabernet Sauvignon", "color": "red", "country": "USA"},
    ),
    Document(
        page_content="Luxurious, sweet wine with flavors of honey, apricot, and peach",
        metadata={"name": "Château d'Yquem", "year": 2015, "rating": 98, "grape": "Sémillon", "color": "white", "country": "France"},
    ),
    # Add more documents as needed
]
