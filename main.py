from bing_image_downloader import downloader

# Considerações importantes:
# 1 - Bing não é Google, então alguns termos podem retornar uma quantidade de imagens bem menor do que a definida.
# 2 - Procure usar termos curtos e específicos ao invés de genéricos. Por exemplo: Ao invés de pesquisar por "pimentão", tente usar "pimentão verde" ou "pimentão vermelho".
# 3 - De preferência por pesquisar usando termos em inglês. Por exemplo: "black dog" ao invés de "cachorro preto".

def select_filter(value):
    options = {'1':'photo', '2':'clipart', '3':'gif', '4':'transparent'}

    if value not in options:
        return print("Digite uma opção válida!")
    else:
        return options[value]

def quantity(qtt):
    if qtt.isnumeric() == False:
        return print("Digite apenas números!")

    qtt = int(qtt)

    if (qtt < 1 or qtt > 500):
        return print("Digite um número entre 1 e 500!")
    else:
        return qtt

query_string = input("Digite o termo à ser pesquisado: ")
query_string = f"{query_string}"
input_filter = input("Escolha um tipo: 1 - Foto, 2 - Clipart, 3 - Gif, 4 - Fundo transparente: ")
selected = select_filter(input_filter)

img_limit = input("Digite a quantidade à ser baixada (Nº entre 1 e 500): ")
limit_downloads = quantity(img_limit)

directory = "./images"

downloader.download(query_string, limit=limit_downloads,  output_dir=directory, adult_filter_off=True, force_replace=False, timeout=60, verbose=True, filter=selected)