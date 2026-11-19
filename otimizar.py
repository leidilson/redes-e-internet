
from PIL import Image
import os

imagens = [
    "router.jpg",
    "switch.jpg",
    "access-point.jpg"
]

for nome in imagens:
    caminho = os.path.join("images", nome)

    imagem = Image.open(caminho)
    imagem.thumbnail((1400, 1400))

    novo_nome = nome.replace(".jpg", "-optimized.jpg")
    destino = os.path.join("images", novo_nome)

    imagem.save(
        destino,
        "JPEG",
        quality=78,
        optimize=True
    )

    print(f"Imagem otimizada: {destino}")
