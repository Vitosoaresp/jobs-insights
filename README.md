# Jobs Insights

![sistema](https://user-images.githubusercontent.com/23152592/206872208-2d8e1fa3-758c-4f13-9ca5-7cfe95e19a01.png)


# Contexto
Esse projeto trata de análises a partir de um conjunto de dados sobre empregos(data/jobs.csv). As minhas implementações foram incorporadas a um aplicativo Web desenvolvido com Flask (feito pela Trybe). e também fiz alguns testes para a implementação de uma análise de dados. Por fim, como bônus, escrevi uma rota e view para um recurso novo usando Flask!

## Técnologias usadas

Back-end:
> Desenvolvido usando: [Python](https://docs.python.org/3/), [Pytest](https://docs.pytest.org/en/7.2.x/), Flake8, Black

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## Crie um ambiente virtual

```bash
 python3 -m venv .venv && source .venv/bin/activate
```


## Instale as dependências

```bash
 python3 -m pip install -r dev-requirements.txt
``` 
## Executando aplicação

- A aplicação rodará em http://localhost:5000

  ```
    flask run
  ```

## Executando Testes

* Para rodar todos os testes:

  ```
    python3 -m pytest
  ```
  
* Para rodar de um arquivo especifico:

  ```
   python3 -m pytest tests/nomedoarquivo.py
  ```
