import random
import os
from PIL import Image, ImageDraw, ImageFont

def verificar_neumonia():
    # Genera un número aleatorio entre 0 y 1
    probabilidad = random.random()
    
    # Supongamos que hay un 30% de probabilidad de tener neumonía
    if probabilidad < 0.3:
        return "Tiene neumonía"
    else:
        return "No tiene neumonía"
