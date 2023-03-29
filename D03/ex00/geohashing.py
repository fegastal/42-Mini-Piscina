import sys
from antigravity import geohash
# Geohash: encodes a geographic location into a short string of letters and digits.
# https://docs.quadrant.io/quadrant-geohash-algorithm
# 37.421542 -122.085589 2005-05-26-10458.68


def test_geohash():
    if (len(sys.argv) != 4):
        return(print("Wrong Usage!! [geohashing.py <latitude> <longitude> <date>]"))
    try:
        lat = float(sys.argv[1])
    except:
        return print("latitude<float>")
    try:
        long = float(sys.argv[2])
    except:
        return print("longitude<float>")
    try:
        date = sys.argv[3].encode('utf-8')
    except:
        return print("datedow<string>")
    geohash(lat, long, date)


if __name__ == '__main__':
#!/usr/bin/python3

import sys
from antigravity import geohash

# Função para fazer o tratamento dos argumentos no terminal
def geohash_verify():

    # Se a quantidade de argumentos passados for diferente de 4
    if (len(sys.argv) != 4):
            # " No caso de um erro, o programa deve mostrar uma mensagem
            # relevante que você terá escolhido antes de dar quit corretamente. "
            return(print("Error. Use: [geohashing.py <latitude> <longitude> <date>]"))
        # se a quantidade estiver certa, tente:
    try:
        # lat receberá o argumento 1 passado(do tipo float)
        lat = float(sys.argv[1])
    except:
        # se não for passada a latitude (do tipo float)
        return print("latitude<float>")
    try:
        # long receberá o argumento 2 passado(do tipo float)
        long = float(sys.argv[2])
    except:
        # se não for passada a longitude (do tipo float)
        return print("longitude<float>")
    try:
        # data receberá o argumento 3 (no formato especificado de string)
        date = sys.argv[3].encode('utf-8')
    except:
        # se não for passada a data como string
        return print("datedow<string>")
    # se tudo estiver de acordo com o especificado, execute a função geohash!
    # parâmetros: latitude, longitude e data
    # which allows users to convert geographic coordinates
    # to short URLs which uniquely identify positions
    # on the Earth, so that referencing them in emails,
    # forums, and websites is more convenient.
    geohash(lat, long, date)

if __name__ == '__main__':
    geohash_verify()