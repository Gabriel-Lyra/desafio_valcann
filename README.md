# desafio_valcann

## Passos para instalação e setup:

### 1. Faça download e instale Python e PostgreSQL.
### 2. Instale as libraries beautifulsoup4, selenium e webdriver-manager através dos seguintes comandos no anaconda prompt: 
- pip install beautifulsoup4, pip install selenium e pip install webdriver-manager
- caso necessario também instale a library psycopg2 com o comando pip install psycopg2-binary
### 3. Copie ou faça download deste repositório
### 4. Abra o file create_update_csv e substitua todos os paths de diretório de acordo com sua máquina.
- (e.g.: troque C:\Users\gabri\Desktop\atividade_valcann\books_update_temp.csv por C:\Users\seu_nome\Downloads\atividade_valcann\books_update_temp.csv)

### 5. Crie uma database com nome "books_database" no PostgreSQL.
### 6. Crie uma tabela com nome "books" dentro do database criado anteriormente. Ela deve possuir as seguintes colunas com tipo "text": Title, Category, Stock, Stars e Price.

### 7. Abra o file update_database e substitua os paths de diretório de acordo com sua máquina. Também atualize os campos user e password de acordo com seu setup.

## Como os scripts funcionam:
1. Ao rodar o scrapping_script será gerado um file chamado books.csv, o qual conterá todo o conteúdo da página do books.toscrape.com
2. Ao rodar o create_update_csv será gerado um file chamado books_update.csv, o qual conterá todo o conteúdo de books.csv que não já está presente em books_complete.csv
3. Ao rodar o update_database será inserido o conteudo do file books_update.csv à tabela "books" anteriormente gerada no setup
## Passos para uso:

### 1. Abra o anaconda prompt e entre no diretório contendo o projeto.
### 2. Rode as seguintes linhas em ordem:
- python scrapping_script.py
- python create_update_csv.py
- python update_database.py
