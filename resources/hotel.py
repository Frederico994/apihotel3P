from flask_restful import Resource

lista_hoteis = [
    { "hotel_id": "sky", "nome": "Hotel Sky","estrelas":4.8,"diaria": 195.99,"Cidade":"Porto"},
    { "hotel_id": "Rei", "nome": "Hotel Rei","estrelas":4.9,"diaria": 199.99,"Cidade":"Lisboa"},
    { "hotel_id": "Paraiso", "nome": "Hotel Paraiso","estrelas":5.0,"diaria": 299.99,"Cidade":"famalicão"}
]

class Hoteis(Resource):
    def get (self):
        return { "hoteis": lista_hoteis }