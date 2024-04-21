import psycopg2
from psycopg2 import sql
import random

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5431"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Define the number of rows you want to generate
districts = [
    "Aveiro", "Beja", "Braga", "Bragança", "Castelo Branco",
    "Coimbra", "Évora", "Faro", "Guarda", "Leiria",
    "Lisboa", "Portalegre", "Porto", "Santarém", "Setúbal",
    "Viana do Castelo", "Vila Real", "Viseu", "Açores", "Madeira"
]

municipalities = {
    "Aveiro": {
        "Oliveira de Azeméis": {"lat": (40.7, 41.0), "lng": (-8.8, -8.2)},
        "Ovar": {"lat": (40.7, 41.0), "lng": (-8.9, -8.3)},
        "Santa Maria da Feira": {"lat": (40.8, 41.1), "lng": (-8.8, -8.3)},
        "São João da Madeira": {"lat": (40.8, 41.1), "lng": (-8.8, -8.2)},
        "Albergaria-a-Velha": {"lat": (40.5, 40.9), "lng": (-8.6, -8.3)},
        "Anadia": {"lat": (40.2, 40.6), "lng": (-8.7, -8.2)},
        "Arouca": {"lat": (40.7, 41.1), "lng": (-8.5, -8.0)},
        "Castelo de Paiva": {"lat": (41.0, 41.2), "lng": (-8.5, -8.0)},
        "Estarreja": {"lat": (40.5, 40.9), "lng": (-8.7, -8.4)},
        "Ílhavo": {"lat": (40.4, 40.8), "lng": (-8.9, -8.4)},
        "Mealhada": {"lat": (40.1, 40.5), "lng": (-8.7, -8.2)},
        "Murtosa": {"lat": (40.5, 40.9), "lng": (-8.8, -8.5)},
        "Oliveira do Bairro": {"lat": (40.3, 40.7), "lng": (-8.7, -8.3)},
        "Sever do Vouga": {"lat": (40.6, 41.0), "lng": (-8.5, -8.2)},
        "Vagos": {"lat": (40.4, 40.8), "lng": (-8.8, -8.5)},
        "Vale de Cambra": {"lat": (40.8, 41.1), "lng": (-8.6, -8.2)},
    },
    "Beja": {
        "Aljustrel": {"lat": (37.7, 38.0), "lng": (-8.3, -7.9)},
        "Beja": {"lat": (37.8, 38.1), "lng": (-8.1, -7.6)},
        "Mértola": {"lat": (37.4, 37.8), "lng": (-7.8, -7.4)},
        "Serpa": {"lat": (37.7, 38.0), "lng": (-7.8, -7.5)},
        "Alvito": {"lat": (38.0, 38.3), "lng": (-8.2, -7.9)},
        "Barrancos": {"lat": (37.9, 38.2), "lng": (-7.6, -7.3)},
        "Cuba": {"lat": (38.0, 38.3), "lng": (-8.1, -7.7)},
        "Ferreira do Alentejo": {"lat": (37.9, 38.2), "lng": (-8.1, -7.8)},
        "Moura": {"lat": (38.0, 38.3), "lng": (-7.6, -7.3)},
        "Odemira": {"lat": (37.4, 37.8), "lng": (-8.7, -8.5)},
        "Ourique": {"lat": (37.5, 37.8), "lng": (-8.4, -8.1)},
        "Vidigueira": {"lat": (38.0, 38.3), "lng": (-8.0, -7.7)},
    },
    "Braga": {
        "Amares": {"lat": (41.5, 41.7), "lng": (-8.4, -8.2)},
        "Barcelos": {"lat": (41.4, 41.6), "lng": (-8.7, -8.5)},
        "Braga": {"lat": (41.4, 41.6), "lng": (-8.5, -8.3)},
        "Cabeceiras de Basto": {"lat": (41.4, 41.6), "lng": (-8.1, -7.9)},
        "Esposende": {"lat": (41.4, 41.6), "lng": (-8.9, -8.7)},
        "Fafe": {"lat": (41.3, 41.5), "lng": (-8.3, -8.1)},
        "Guimarães": {"lat": (41.3, 41.5), "lng": (-8.4, -8.2)},
        "Póvoa de Lanhoso": {"lat": (41.5, 41.7), "lng": (-8.3, -8.1)},
        "Terras de Bouro": {"lat": (41.5, 41.7), "lng": (-8.3, -8.1)},
        "Vieira do Minho": {"lat": (41.5, 41.7), "lng": (-8.2, -8.0)},
        "Vila Nova de Famalicão": {"lat": (41.3, 41.5), "lng": (-8.6, -8.4)},
        "Vila Verde": {"lat": (41.5, 41.7), "lng": (-8.5, -8.3)},
        "Celorico de Basto": {"lat": (41.3, 41.5), "lng": (-8.1, -7.9)},
    },
    "Bragança": {
        "Alfândega da Fé": {"lat": (41.2, 41.4), "lng": (-7.0, -6.8)},
        "Bragança": {"lat": (41.7, 41.9), "lng": (-6.9, -6.6)},
        "Mirandela": {"lat": (41.3, 41.5), "lng": (-7.3, -7.0)},
        "Vila Flor": {"lat": (41.1, 41.3), "lng": (-7.3, -7.0)},
        "Miranda do Douro": {"lat": (41.4, 41.6), "lng": (-6.4, -6.1)},
        "Mogadouro": {"lat": (41.2, 41.4), "lng": (-6.8, -6.5)},
        "Torre de Moncorvo": {"lat": (41.0, 41.2), "lng": (-7.1, -6.9)},
        "Vimioso": {"lat": (41.5, 41.7), "lng": (-6.7, -6.4)},
        "Vinhais": {"lat": (41.7, 41.9), "lng": (-7.1, -6.9)},
    },
    "Castelo Branco": {
        "Belmonte": {"lat": (40.2, 40.4), "lng": (-7.5, -7.2)},
        "Castelo Branco": {"lat": (39.7, 40.0), "lng": (-7.6, -7.4)},
        "Covilhã": {"lat": (40.1, 40.3), "lng": (-7.6, -7.4)},
        "Fundão": {"lat": (39.9, 40.2), "lng": (-7.6, -7.4)},
        "Oleiros": {"lat": (39.7, 40.0), "lng": (-8.0, -7.7)},
        "Penamacor": {"lat": (40.0, 40.2), "lng": (-7.3, -7.0)},
        "Proença-a-Nova": {"lat": (39.6, 39.8), "lng": (-8.0, -7.7)},
        "Sertã": {"lat": (39.7, 39.9), "lng": (-8.2, -7.9)},
        "Vila de Rei": {"lat": (39.5, 39.7), "lng": (-8.2, -7.9)},
        "Vila Velha de Ródão": {"lat": (39.6, 39.8), "lng": (-7.8, -7.5)},
    },
    "Coimbra": {
        "Arganil": {"lat": (40.1, 40.4), "lng": (-8.1, -7.9)},
        "Coimbra": {"lat": (40.1, 40.3), "lng": (-8.5, -8.3)},
        "Condeixa-a-Nova": {"lat": (40.0, 40.2), "lng": (-8.6, -8.4)},
        "Figueira da Foz": {"lat": (40.0, 40.3), "lng": (-8.9, -8.7)},
        "Góis": {"lat": (40.0, 40.3), "lng": (-8.2, -8.0)},
        "Lousã": {"lat": (40.0, 40.3), "lng": (-8.3, -8.1)},
        "Mira": {"lat": (40.3, 40.5), "lng": (-8.8, -8.6)},
        "Miranda do Corvo": {"lat": (40.0, 40.3), "lng": (-8.4, -8.2)},
        "Montemor-o-Velho": {"lat": (40.1, 40.4), "lng": (-8.7, -8.5)},
        "Oliveira do Hospital": {"lat": (40.3, 40.6), "lng": (-8.0, -7.8)},
        "Pampilhosa da Serra": {"lat": (40.0, 40.3), "lng": (-8.0, -7.7)},
        "Penacova": {"lat": (40.2, 40.5), "lng": (-8.3, -8.1)},
        "Penela": {"lat": (40.0, 40.3), "lng": (-8.4, -8.2)},
        "Soure": {"lat": (40.0, 40.3), "lng": (-8.7, -8.5)},
        "Tábua": {"lat": (40.3, 40.6), "lng": (-8.1, -7.9)},
        "Vila Nova de Poiares": {"lat": (40.1, 40.4), "lng": (-8.3, -8.1)},
    },
    "Évora": {
        "Arraiolos": {"lat": (38.6, 38.8), "lng": (-8.0, -7.8)},
        "Borba": {"lat": (38.7, 38.9), "lng": (-7.6, -7.4)},
        "Estremoz": {"lat": (38.7, 38.9), "lng": (-7.7, -7.4)},
        "Évora": {"lat": (38.4, 38.6), "lng": (-8.0, -7.7)},
        "Montemor-o-Novo": {"lat": (38.5, 38.7), "lng": (-8.3, -8.1)},
        "Mora": {"lat": (38.8, 39.0), "lng": (-8.2, -8.0)},
        "Mourão": {"lat": (38.1, 38.4), "lng": (-7.4, -7.2)},
        "Portel": {"lat": (38.1, 38.4), "lng": (-8.2, -7.9)},
        "Redondo": {"lat": (38.5, 38.7), "lng": (-7.6, -7.4)},
        "Reguengos de Monsaraz": {"lat": (38.3, 38.5), "lng": (-7.6, -7.4)},
        "Vendas Novas": {"lat": (38.5, 38.7), "lng": (-8.5, -8.3)},
        "Viana do Alentejo": {"lat": (38.2, 38.4), "lng": (-8.1, -7.9)},
        "Vila Viçosa": {"lat": (38.6, 38.8), "lng": (-7.5, -7.3)},
    },
    "Faro": {
        "Albufeira": {"lat": (37.0, 37.2), "lng": (-8.3, -8.1)},
        "Faro": {"lat": (36.9, 37.1), "lng": (-8.0, -7.8)},
        "Lagoa": {"lat": (37.1, 37.3), "lng": (-8.5, -8.3)},
        "Lagos": {"lat": (37.0, 37.2), "lng": (-8.7, -8.5)},
        "Loulé": {"lat": (37.1, 37.3), "lng": (-8.1, -7.9)},
        "Olhão": {"lat": (36.9, 37.1), "lng": (-7.9, -7.7)},
        "Portimão": {"lat": (37.1, 37.3), "lng": (-8.6, -8.4)},
        "São Brás de Alportel": {"lat": (37.1, 37.3), "lng": (-8.0, -7.8)},
        "Silves": {"lat": (37.1, 37.3), "lng": (-8.5, -8.3)},
        "Tavira": {"lat": (37.1, 37.3), "lng": (-7.7, -7.5)},
        "Vila do Bispo": {"lat": (37.0, 37.2), "lng": (-9.0, -8.7)},
        "Vila Real de Santo António": {"lat": (37.1, 37.3), "lng": (-7.5, -7.3)},
    },
    "Guarda": {
        "Aguiar da Beira": {"lat": (40.7, 40.9), "lng": (-7.7, -7.4)},
        "Almeida": {"lat": (40.6, 40.8), "lng": (-7.0, -6.7)},
        "Celorico da Beira": {"lat": (40.5, 40.7), "lng": (-7.5, -7.2)},
        "Figueira de Castelo Rodrigo": {"lat": (40.8, 41.0), "lng": (-7.0, -6.7)},
        "Fornos de Algodres": {"lat": (40.5, 40.7), "lng": (-7.7, -7.4)},
        "Gouveia": {"lat": (40.3, 40.5), "lng": (-7.7, -7.5)},
        "Guarda": {"lat": (40.4, 40.6), "lng": (-7.4, -7.1)},
        "Manteigas": {"lat": (40.3, 40.5), "lng": (-7.7, -7.4)},
        "Mêda": {"lat": (40.8, 41.0), "lng": (-7.4, -7.1)},
        "Pinhel": {"lat": (40.7, 40.9), "lng": (-7.2, -6.9)},
        "Sabugal": {"lat": (40.2, 40.5), "lng": (-7.2, -6.9)},
        "Seia": {"lat": (40.3, 40.5), "lng": (-7.8, -7.5)},
        "Trancoso": {"lat": (40.7, 40.9), "lng": (-7.5, -7.2)},
        "Vila Nova de Foz Côa": {"lat": (41.0, 41.2), "lng": (-7.3, -7.0)},
    },
    "Leiria": {
        "Alcobaça": {"lat": (39.4, 39.7), "lng": (-9.0, -8.7)},
        "Alvaiázere": {"lat": (39.6, 39.9), "lng": (-8.5, -8.1)},
        "Ansião": {"lat": (39.8, 40.0), "lng": (-8.6, -8.3)},
        "Batalha": {"lat": (39.6, 39.9), "lng": (-8.9, -8.6)},
        "Bombarral": {"lat": (39.2, 39.5), "lng": (-9.2, -8.9)},
        "Caldas da Rainha": {"lat": (39.3, 39.6), "lng": (-9.2, -8.9)},
        "Castanheira de Pera": {"lat": (39.8, 40.1), "lng": (-8.4, -8.0)},
        "Figueiró dos Vinhos": {"lat": (39.8, 40.1), "lng": (-8.4, -8.1)},
        "Leiria": {"lat": (39.5, 39.8), "lng": (-8.9, -8.6)},
        "Marinha Grande": {"lat": (39.6, 39.9), "lng": (-9.0, -8.7)},
        "Nazaré": {"lat": (39.4, 39.7), "lng": (-9.1, -8.9)},
        "Óbidos": {"lat": (39.2, 39.5), "lng": (-9.2, -8.9)},
        "Pedrógão Grande": {"lat": (39.8, 40.1), "lng": (-8.2, -7.9)},
        "Peniche": {"lat": (39.2, 39.5), "lng": (-9.4, -9.1)},
        "Pombal": {"lat": (39.8, 40.1), "lng": (-8.7, -8.4)},
        "Porto de Mós": {"lat": (39.4, 39.7), "lng": (-8.9, -8.6)}
    },
    "Lisboa": {
        "Alenquer": {"lat": (39.0, 39.1), "lng": (-9.1, -8.9)},
        "Amadora": {"lat": (38.7, 38.8), "lng": (-9.3, -9.2)},
        "Arruda dos Vinhos": {"lat": (38.9, 39.0), "lng": (-9.1, -9.0)},
        "Azambuja": {"lat": (39.0, 39.1), "lng": (-8.9, -8.7)},
        "Cadaval": {"lat": (39.2, 39.3), "lng": (-9.2, -9.0)},
        "Cascais": {"lat": (38.7, 38.8), "lng": (-9.4, -9.3)},
        "Lisboa": {"lat": (38.7, 38.8), "lng": (-9.2, -9.1)},
        "Loures": {"lat": (38.8, 38.9), "lng": (-9.2, -9.1)},
        "Lourinhã": {"lat": (39.2, 39.3), "lng": (-9.4, -9.3)},
        "Mafra": {"lat": (38.9, 39.0), "lng": (-9.4, -9.3)},
        "Odivelas": {"lat": (38.7, 38.8), "lng": (-9.3, -9.2)},
        "Oeiras": {"lat": (38.6, 38.7), "lng": (-9.4, -9.3)},
        "Sintra": {"lat": (38.8, 38.9), "lng": (-9.4, -9.3)},
        "Sobral de Monte Agraço": {"lat": (39.0, 39.1), "lng": (-9.2, -9.1)},
        "Torres Vedras": {"lat": (39.0, 39.1), "lng": (-9.3, -9.2)},
        "Vila Franca de Xira": {"lat": (38.9, 39.0), "lng": (-9.0, -8.9)},
    },
    "Portalegre": {
        "Alter do Chão": {"lat": (39.1, 39.2), "lng": (-7.7, -7.6)},
        "Arronches": {"lat": (39.1, 39.2), "lng": (-7.4, -7.2)},
        "Avis": {"lat": (39.0, 39.1), "lng": (-8.0, -7.8)},
        "Campo Maior": {"lat": (38.9, 39.1), "lng": (-7.2, -7.0)},
        "Castelo de Vide": {"lat": (39.3, 39.4), "lng": (-7.6, -7.4)},
        "Crato": {"lat": (39.2, 39.4), "lng": (-7.8, -7.5)},
        "Elvas": {"lat": (38.8, 39.0), "lng": (-7.3, -7.0)},
        "Fronteira": {"lat": (39.0, 39.1), "lng": (-7.8, -7.6)},
        "Gavião": {"lat": (39.4, 39.5), "lng": (-7.9, -7.8)},
        "Marvão": {"lat": (39.3, 39.4), "lng": (-7.5, -7.3)},
        "Monforte": {"lat": (39.0, 39.1), "lng": (-7.5, -7.4)},
        "Nisa": {"lat": (39.5, 39.6), "lng": (-7.7, -7.6)},
        "Ponte de Sor": {"lat": (39.2, 39.3), "lng": (-8.1, -8.0)},
        "Portalegre": {"lat": (39.2, 39.4), "lng": (-7.5, -7.4)},
        "Sousel": {"lat": (38.9, 39.0), "lng": (-7.7, -7.5)},
    },
    "Porto": {
        "Amarante": {"lat": (41.2, 41.3), "lng": (-8.2, -8.0)},
        "Baião": {"lat": (41.1, 41.2), "lng": (-8.1, -8.0)},
        "Felgueiras": {"lat": (41.4, 41.5), "lng": (-8.3, -8.1)},
        "Gondomar": {"lat": (41.1, 41.2), "lng": (-8.6, -8.5)},
        "Lousada": {"lat": (41.2, 41.3), "lng": (-8.3, -8.2)},
        "Maia": {"lat": (41.2, 41.3), "lng": (-8.7, -8.6)},
        "Marco de Canaveses": {"lat": (41.1, 41.2), "lng": (-8.2, -8.1)},
        "Matosinhos": {"lat": (41.1, 41.2), "lng": (-8.7, -8.6)},
        "Paços de Ferreira": {"lat": (41.2, 41.3), "lng": (-8.4, -8.3)},
        "Paredes": {"lat": (41.2, 41.3), "lng": (-8.4, -8.3)},
        "Penafiel": {"lat": (41.2, 41.3), "lng": (-8.3, -8.2)},
        "Porto": {"lat": (41.1, 41.2), "lng": (-8.7, -8.6)},
        "Póvoa de Varzim": {"lat": (41.3, 41.4), "lng": (-8.8, -8.7)},
        "Santo Tirso": {"lat": (41.3, 41.4), "lng": (-8.5, -8.4)},
        "Trofa": {"lat": (41.3, 41.4), "lng": (-8.6, -8.5)},
        "Valongo": {"lat": (41.1, 41.2), "lng": (-8.5, -8.4)},
        "Vila do Conde": {"lat": (41.3, 41.4), "lng": (-8.8, -8.7)},
        "Vila Nova de Gaia": {"lat": (41.1, 41.2), "lng": (-8.7, -8.6)},
    },
    "Santarém": {
        "Abrantes": {"lat": (39.4, 39.5), "lng": (-8.3, -8.1)},
        "Alcanena": {"lat": (39.4, 39.5), "lng": (-8.7, -8.6)},
        "Almeirim": {"lat": (39.1, 39.3), "lng": (-8.7, -8.6)},
        "Alpiarça": {"lat": (39.2, 39.3), "lng": (-8.6, -8.5)},
        "Benavente": {"lat": (38.9, 39.0), "lng": (-8.9, -8.7)},
        "Cartaxo": {"lat": (39.1, 39.2), "lng": (-8.8, -8.7)},
        "Chamusca": {"lat": (39.3, 39.4), "lng": (-8.5, -8.4)},
        "Constância": {"lat": (39.4, 39.5), "lng": (-8.4, -8.3)},
        "Coruche": {"lat": (38.9, 39.0), "lng": (-8.6, -8.5)},
        "Entroncamento": {"lat": (39.4, 39.5), "lng": (-8.5, -8.4)},
        "Ferreira do Zêzere": {"lat": (39.6, 39.7), "lng": (-8.4, -8.3)},
        "Golegã": {"lat": (39.3, 39.5), "lng": (-8.6, -8.5)},
        "Mação": {"lat": (39.5, 39.6), "lng": (-8.4, -8.3)},
        "Ourém": {"lat": (39.6, 39.7), "lng": (-8.6, -8.5)},
        "Rio Maior": {"lat": (39.3, 39.4), "lng": (-9.0, -8.9)},
        "Salvaterra de Magos": {"lat": (39.0, 39.1), "lng": (-8.8, -8.7)},
        "Santarém": {"lat": (39.2, 39.3), "lng": (-8.7, -8.6)},
        "Tomar": {"lat": (39.5, 39.7), "lng": (-8.5, -8.4)},
        "Torres Novas": {"lat": (39.4, 39.5), "lng": (-8.6, -8.5)},
        "Vila Nova da Barquinha": {"lat": (39.4, 39.5), "lng": (-8.4, -8.3)},
    },
    "Setúbal": {
        "Alcácer do Sal": {"lat": (38.3, 38.4), "lng": (-8.6, -8.5)},
        "Alcochete": {"lat": (38.7, 38.8), "lng": (-9.0, -8.9)},
        "Almada": {"lat": (38.6, 38.7), "lng": (-9.2, -9.1)},
        "Barreiro": {"lat": (38.6, 38.7), "lng": (-9.1, -9.0)},
        "Grândola": {"lat": (38.1, 38.2), "lng": (-8.6, -8.5)},
        "Moita": {"lat": (38.6, 38.7), "lng": (-9.0, -8.9)},
        "Montijo": {"lat": (38.6, 38.7), "lng": (-9.0, -8.9)},
        "Palmela": {"lat": (38.5, 38.6), "lng": (-9.0, -8.9)},
        "Santiago do Cacém": {"lat": (38.0, 38.1), "lng": (-8.7, -8.6)},
        "Seixal": {"lat": (38.6, 38.7), "lng": (-9.2, -9.1)},
        "Sesimbra": {"lat": (38.4, 38.5), "lng": (-9.2, -9.1)},
        "Setúbal": {"lat": (38.4, 38.6), "lng": (-8.9, -8.8)},
        "Sines": {"lat": (37.9, 38.0), "lng": (-8.9, -8.8)},
    },
    "Viana do Castelo": {
        "Arcos de Valdevez": {"lat": (41.8, 41.9), "lng": (-8.5, -8.3)},
        "Caminha": {"lat": (41.8, 41.9), "lng": (-8.9, -8.7)},
        "Melgaço": {"lat": (42.0, 42.2), "lng": (-8.3, -8.1)},
        "Monção": {"lat": (42.0, 42.1), "lng": (-8.6, -8.4)},
        "Paredes de Coura": {"lat": (41.9, 42.0), "lng": (-8.6, -8.4)},
        "Ponte da Barca": {"lat": (41.7, 41.9), "lng": (-8.5, -8.3)},
        "Ponte de Lima": {"lat": (41.7, 41.8), "lng": (-8.7, -8.5)},
        "Valença": {"lat": (42.0, 42.1), "lng": (-8.7, -8.5)},
        "Viana do Castelo": {"lat": (41.6, 41.8), "lng": (-8.9, -8.7)},
        "Vila Nova de Cerveira": {"lat": (41.9, 42.0), "lng": (-8.8, -8.6)},
    },
    "Vila Real": {
        "Alijó": {"lat": (41.2, 41.3), "lng": (-7.6, -7.4)},
        "Boticas": {"lat": (41.6, 41.7), "lng": (-7.8, -7.6)},
        "Chaves": {"lat": (41.7, 41.8), "lng": (-7.4, -7.2)},
        "Mesão Frio": {"lat": (41.1, 41.3), "lng": (-8.0, -7.8)},
        "Mondim de Basto": {"lat": (41.3, 41.5), "lng": (-8.0, -7.9)},
        "Montalegre": {"lat": (41.7, 41.9), "lng": (-7.9, -7.7)},
        "Murça": {"lat": (41.4, 41.6), "lng": (-7.6, -7.4)},
        "Peso da Régua": {"lat": (41.1, 41.2), "lng": (-7.8, -7.6)},
        "Ribeira de Pena": {"lat": (41.4, 41.6), "lng": (-7.9, -7.7)},
        "Sabrosa": {"lat": (41.2, 41.3), "lng": (-7.6, -7.4)},
        "Santa Marta de Penaguião": {"lat": (41.1, 41.3), "lng": (-7.9, -7.6)},
        "Valpaços": {"lat": (41.5, 41.7), "lng": (-7.4, -7.2)},
        "Vila Pouca de Aguiar": {"lat": (41.4, 41.6), "lng": (-7.7, -7.5)},
        "Vila Real": {"lat": (41.2, 41.4), "lng": (-7.8, -7.6)},
    },
    "Viseu": {
        "Armamar": {"lat": (41.1, 41.2), "lng": (-7.7, -7.6)},
        "Carregal do Sal": {"lat": (40.4, 40.5), "lng": (-8.0, -7.9)},
        "Castro Daire": {"lat": (40.9, 41.0), "lng": (-8.0, -7.9)},
        "Cinfães": {"lat": (41.0, 41.1), "lng": (-8.1, -8.0)},
        "Lamego": {"lat": (41.0, 41.1), "lng": (-7.9, -7.8)},
        "Mangualde": {"lat": (40.6, 40.7), "lng": (-7.8, -7.7)},
        "Moimenta da Beira": {"lat": (40.9, 41.0), "lng": (-7.7, -7.6)},
        "Mortágua": {"lat": (40.3, 40.4), "lng": (-8.3, -8.2)},
        "Nelas": {"lat": (40.5, 40.6), "lng": (-7.9, -7.8)},
        "Oliveira de Frades": {"lat": (40.7, 40.8), "lng": (-8.2, -8.1)},
        "Penalva do Castelo": {"lat": (40.6, 40.7), "lng": (-7.7, -7.6)},
        "Penedono": {"lat": (40.9, 41.0), "lng": (-7.4, -7.3)},
        "Resende": {"lat": (41.0, 41.1), "lng": (-8.0, -7.9)},
        "Santa Comba Dão": {"lat": (40.3, 40.4), "lng": (-8.1, -8.0)},
        "São João da Pesqueira": {"lat": (41.1, 41.2), "lng": (-7.5, -7.4)},
        "São Pedro do Sul": {"lat": (40.7, 40.8), "lng": (-8.1, -8.0)},
        "Sátão": {"lat": (40.7, 40.8), "lng": (-7.8, -7.7)},
        "Sernancelhe": {"lat": (40.9, 41.0), "lng": (-7.6, -7.5)},
        "Tabuaço": {"lat": (41.0, 41.1), "lng": (-7.6, -7.5)},
        "Tarouca": {"lat": (41.0, 41.1), "lng": (-7.8, -7.7)},
        "Tondela": {"lat": (40.5, 40.6), "lng": (-8.1, -8.0)},
        "Vila Nova de Paiva": {"lat": (40.8, 40.9), "lng": (-7.8, -7.7)},
        "Viseu": {"lat": (40.6, 40.7), "lng": (-7.9, -7.8)},
        "Vouzela": {"lat": (40.7, 40.8), "lng": (-8.2, -8.1)},
    }
}

def generate_price(type_):
    # Define the maximum price
    max_price = 20000000
    
    # Define the price ranges and their corresponding percentages
    if type_ == 'arrendar':
        price_ranges = [(0, 5000) , (50001,100000),(100001,500000)]
        percentages = [0.99, 0.05, 0.05]
    else:
        price_ranges = [(0, 500000), (500001, 1000000), (1000001, 20000000)]
        percentages = [0.83, 0.11, 0.06]
    
    # Choose a price range based on the defined percentages
    price_range = random.choices(price_ranges, weights=percentages)[0]
    
    # Generate a random price within the selected price range
    price = random.randint(price_range[0], price_range[1])
    
    return round(price, 2)

# Assuming you have the rest of the code from your example...
num_rows = 53718
# Your code with price generation logic included
for i in range(num_rows):
    # Choose a random type
    type_ = random.choices(['venda', 'arrendar'], weights=[0.95, 0.05])[0]
    
    # Choose a random district
    district = random.choice(list(municipalities.keys()))
    
    # Choose a random municipality from the selected district
    municipality = random.choice(list(municipalities[district].keys()))
    
    # Generate a random coordinate within the bounds of the municipality
    min_lat, max_lat = municipalities[district][municipality]['lat']
    min_lng, max_lng = municipalities[district][municipality]['lng']
    latitude = round(random.uniform(min_lat, max_lat), 6)
    longitude = round(random.uniform(min_lng, max_lng), 6)

    name = f"Product {i + 1}"
    price = generate_price(type_)  # Using the generate_price function to get the price and change percentage
    location = district+", "+municipality
    coordinates = f"({latitude}, {longitude})"

    # Construct the SQL query
    query = sql.SQL("INSERT INTO RealEstateData (name, price, type, location, coordinates) VALUES (%s, %s, %s, %s, %s)").format(
        sql.Identifier("RealEstateData")
    )

    # Execute the SQL query with the data
    cur.execute(query, (name, price, type_, location, coordinates))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
