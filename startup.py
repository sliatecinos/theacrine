from utils.win_toaster import notaBaixaBateria
from utils.win_psutil import *


tempo = restatempo_Bateria()
carga = restacarga_Bateria()
situacao = situacao_Bateria()

if not situacao:
    notaBaixaBateria(porcentagem=carga, tempo=tempo)
