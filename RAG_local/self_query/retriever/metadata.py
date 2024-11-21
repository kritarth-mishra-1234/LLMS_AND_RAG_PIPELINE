#we made this class to remove langchain
class AttributeInfo:
    def __init__(self, name: str, description: str, type: str):
        self.name = name
        self.description = description
        self.type = type

metadata_field_info = [
    AttributeInfo(name="grape", description="The grape used to make the wine", type="string"),
    AttributeInfo(name="name", description="The name of the wine", type="string"),
    AttributeInfo(name="color", description="The color of the wine", type="string"),
    AttributeInfo(name="year", description="The year the wine was released", type="integer"),
    AttributeInfo(name="country", description="The country of origin", type="string"),
    AttributeInfo(name="rating", description="The wine rating (0-100)", type="integer"),
]