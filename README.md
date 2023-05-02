# reposicamera [api]

O **reposicamera** é um catálogo virtual em forma de API para cadastro de câmeras analógicas e digitais, com algumas categorias já pré-definidas. Com ele, o usuário consegue:

- Fazer controle patrimonial de câmeras
- Ver valores individuais
- Categorizar equipamentos

## Dando início

Primeiro, clone o projeto:
```bash
git clone https://github.com/brennofacasi/reposicamera-api.git
```
Para rodar o projeto, ative o ambiente virtual e instale os pacotes necessários:

```bash
source env/bin/activate
pip install -r requirements.txt
```
Para executar a aplicação, use o comando:

```bash
(env) flask run --host 0.0.0.0 --port 5050
```
Caso precise atualizar a cada atualização feita no código, utilize a flag `--reload` ao final do comando acima.

## Categorias

Ao rodar a API pela primeira vez na sua máquina, a tabela `categoria` já será populada automaticamente, logo não é preciso se preocupar em cadastrá-las. Caso precise adicionar, utilize a rota `/category` com método POST.

## Exemplos

Quer testar as rotas mas não conhece muito de câmeras? Fique tranquila(o), eu trouxe exemplos!

| Nome              | Marca      | Categoria     | Valor        |
| :---------------- | :--------- | :------------ | :----------- |
| MG-3              | Yashica    | [saboneteira] | R$ 160,00    |
| Fisheye 2         | Lomography | [lomo]        | R$ 311,00    |
| EOS 5000          | Canon      | [slr]         | R$ 250,00    |
| F3AF              | Nikon      | [slr]         | R$ 5.760,00  |
| A7C               | Sony       | [dslr]        | R$ 11.400,00 |
| Instax Mini 11    | Fujifilm   | [instant]     | R$ 429,00    |
| Cybershot DSC-h70 | Sony       | [digicam]     | R$ 680,00    |
