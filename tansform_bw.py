# para executar este comando, deve-se compilar o comando - pip install Pillow
from PIL import Image

imagem = Image.open("default.jpg")
imagem_transformada = imagem.convert("L")
imagem_transformada.save("default_transformada.jpg")
imagem_transformada.show()