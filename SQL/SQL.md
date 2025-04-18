# Tutorial sobre SQL
## 🛢️ O que é um banco de dados?
- Entidade utilizada para gerenciar os dados de uma aplicação.
- As tabelas categorizam os cados, separando-os de acordo com seu contexto.
- Colunas: campos das tabelas
- Linhas: entidades
- Outros elementos importantes - queries (ações), views, stored procedures...

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

## 🚀 Utilização

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
