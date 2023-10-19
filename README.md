# Coletor de imagens do BING com Python

O projeto consiste no uso da biblioteca "bing_image_downloader", criando comandos de entrada para permitir que o usuário, através do CLI, possa decidir quais tipos de imagem quer pesquisar e baixar.


### Como executar o programa:

Para executar o projeto, você precisa ter instalado o Python 3.8+

- Clone o projeto para o local de sua escolha e entre na pasta do mesmo.
- Caso ainda não tenha, instale a biblioteca [bing-image-downloader](https://pypi.org/project/bing-image-downloader/), usando o comando "pip install bing-image-downloader" (outra forma de instalar está disponível no link da biblioteca).
- No CLI de sua preferência, execute o comando "python main.py" ou "python3 main.py" (a depender da sua instalação!).


### Instruções de uso:

Depois de executado, as opções de entrada são auto-explicativas e simples:

- "Digite o termo à ser pesquisado: " - Termo que usaria para pesquisar uma imagem direto no Bing, Ex: "cachorro" ou "gato preto".
- "Escolha um tipo: 1 - Foto, 2 - Clipart, 3 - Gif, 4 - Fundo transparente: " - Estes são os tipos de pesquisa que a biblioteca fornece. Basta digitar o número referente ao tipo desejado.
- "Digite a quantidade à ser baixada (Nº entre 1 e 500): " - Quantidade de fotos a serem baixadas. Apesar de ter um limite bem alto (500), em todos os meus testes, pesquisas com uma quantidade maior que 60 fotos, tendem a falhar após esse valor.


### Observações

- Notei que os resultados servidos pela pesquisa são mais adequados ao desejado se digitar o termo em inglês.
- Usar termos mais específicos gera resultados melhores e mais volumosos, por exemplo: Pesquisar "black cat" ao invés de "cat", retorna mais imagens de acordo com o termo. Já como "cat", acabam aparecendo muitas imagens que estão cassificadas de forma errada (em um caso, apareceu um poster de filme que não tem nada a ver com gatos por exemplo!).
- Usei o projeto para coletar imagens de vários animais diferentes, de cores e raças diferentes, para um treinamento de Machine Learning, somando mais de 120 imagens de vários animais e cores diferentes. Então mesmo que existam outras formas de se obter esse tipo de dataset, foi uma forma de estudar à respeito desse tipo de coleta.