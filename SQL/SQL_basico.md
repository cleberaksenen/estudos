# Tutorial sobre SQL
## 🛢️ O que é um banco de dados?
- Entidade utilizada para gerenciar os dados de uma aplicação.
- As tabelas categorizam os cados, separando-os de acordo com seu contexto.
- Colunas: campos das tabelas
- Linhas: entidades
- Outros elementos importantes - queries (ações), views, stored procedures...

## 🧾 O que é uma tabela?
- Entidades que recebem a maioria das informações de um banco de dados (CRUD)
- Categorizam os dados, salvando-os em linhas
- Os tipos dos dados são salvos em colunas: TEXT, INT, FLOAT, VARCHAR, DATE...
- Criar corretamente as tabelas faz parte do DB Design
- Possuem características especiais (CONSTRAINTS): NOT NULL, AUTO_INCREMENT, UNIQUE, PRIMARY KEY, FOREIGN KEY, DEFAULT...

### -> Um banco de dados bem modelado representa o sucesso de uma aplicação

## 📦 Tipos de bancos de dados
- Relacionais (relação entre tabelas): MySQL
- Não relacionais (baseados em documentos): NoSQL, MongoDB
- Object Database (orientado a objetos): ObjectBox
- Cloud Database (servidores de alta escalabilidade)

---

## 🔧 Instalação
- Link para download do MySQL: https://dev.mysql.com/downloads/mysql/

(Servidor local MySQL e Workbench)

---

## 🛠️ Criação de um banco de dados
```
CREATE DATABASE banco_dados;
```

```
CREATE TABLE tabela01(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    coluna01 TEXT,
    coluna02 TEXT,
    coluna03 INT
);
```
```
CREATE TABLE tabela02(
	id2 INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id INT,
    coluna04 INT,
    coluna05 DATE,
    FOREIGN KEY (id) REFERENCES tabela01(id));
```

```
INSERT INTO tabela01(id, coluna01, coluna02, coluna03)
VALUES (1, XXX, XXX, XXX),
       (2, XXX, XXX, XXX),
       (3, XXX, XXX, XXX);
```

---

## 🚀 Utilização Parte 01

```
USE banco_dados;
```

### SELECT
```
SELECT * from tabela;
```

```
SELECT coluna1, coluna2 from tabela;
```

```
SELECT coluna AS Novo_nome;
```

### SELECT + WHERE (= | != | < | >)
```
SELECT *
FROM tabela
WHERE id = 10;
```

```
SELECT * FROM tabela
WHERE coluna < 60;    
```

### SELECT + ORDER BY
```
SELECT *
FROM tabela
ORDER BY coluna; #ASC ou DESC
```
```
SELECT * FROM film
ORDER BY length DESC
LIMIT 5; #Limite dos 5 maiores
```

### SELECT DISTINCT
```
SELECT DISTINCT nome;
```

### SELECT + AND OR NOT
#### -- AND (True, True)
#### -- OR (True, False)
#### -- NOT (Inverte)
```
SELECT * FROM tabela
WHERE coluna1 = "Opção 01" AND coluna2 > 90;
```

```
SELECT * FROM tabela
WHERE NOT coluna1 = "Opção 01";
```

#### OBS.
Isso:
```
SELECT * FROM film
WHERE length = 60
OR length = 90
OR length = 120;
```

Equivale a isso:
```
SELECT * FROM film
WHERE length IN(60, 90, 120);
```

### SELECT + BETWEEN + AND
Seleciona intervalos/faixas:
```
SELECT * FROM film
WHERE length BETWEEN 50 AND 55;
```
```
SELECT * FROM film
WHERE length BETWEEN 50 AND 55
ORDER BY rental_rate DESC;
```

### LIKE e REGEXP (operadores)
Procura se um texto se encontra presente na palavra.
```
SELECT * FROM film
WHERE title LIKE("%PHOBIA%"); #% --> entre essa coisa!
```
Pode substituir o LIKE, sem a porcentagem (sem regras):
```
SELECT * FROM film
WHERE title REGEXP("PHOBIA");
```

### COUNT
```
SELECT COUNT(*) AS "Filme com 7 dias de aluguel" FROM film
WHERE rental_duration = 7;
```

---

## 🚀🚀 Utilização Parte 02

### JOIN
Une os dados com outras tabelas.
- Forma direta:
```
SELECT * FROM customer
JOIN address;
```

- Linkando com chave-estrangeira:
```
SELECT * FROM customer
JOIN address
ON customer.address_id = address.address_id;
```

- Posso facilitar, chamando as tabelas por simbolos:
```
SELECT * FROM customer AS c
JOIN address AS a
ON c.address_id = a.address_id;
```

### JOIN com múltiplas tabelas
```
SELECT * FROM tabela_principal
JOIN tabela02
ON tabela_principal.id02 = tabela02.id02
JOIN tabela03
ON tabela_principal.id03 = tabela03.id03
JOIN tabela04
ON tabela_principal.id04 = tabela04.id04;
```