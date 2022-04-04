# WebScrapingDino

WebScrapinDino é um scraping/crawler de dados sobre dinossauros. Essa aplicação é escrita com base no framework Scrapy 2.6.1, utilizando recursos da classe Spiders oferecida pelo framework.
Esta aplicação foi desenvolvida como parte de um estudo sobre o framework Scrapy e para gerar uma pequena base de informações sobre 309 espécies de dinossuaros catalogadas, até o momento, pelo Museu de História Natural de Londres.

![dino](https://user-images.githubusercontent.com/16140969/161632527-111ee9fd-a8a9-4fd6-bc43-898b4b031f35.gif)

## Funcionalidade
A aplicação é composta por duas partes distintas, a primeira parte é responsável por coletar as URL's referentes a cada perfil de dinosauro catalogado no site do museu.

![Url2](https://user-images.githubusercontent.com/16140969/161632284-5eeb9711-a7c3-4dd8-997f-009f9f3a9d34.gif)

Com base nas URL's obtidas, a segunda parte é responsável por coletar e armazenar em um arquivo JSON, às informações de cada dinossauro identificado.

![dinoDB](https://user-images.githubusercontent.com/16140969/161632532-11b41a8c-a472-4b6d-b23d-251c5e76d509.gif)

## Instalação

Para a execução da aplicação é preciso que o ambiente de execução contenha as seguintes configurações

```sh
Python: "^3.10"
Scrapy: "^2.6"
```
## Execução

A aplicação é executada via terminal, através do comando scrapy que inicializa a execução do framework Scrapy

```sh
scrapy runspider [arquivo].py
```
