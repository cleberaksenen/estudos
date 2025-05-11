# Tutorial sobre SQL - parte 02
## Conceitos
- SUBQUERY é uma QUERY que contém outra QUERY
- STORED PROCEDURE é uma QUERY que pode ser executada depois de um tempo por um nome, similar a funções
- VIEWS é uma tabela formada pro meio de uma QUERY
- TRIGGER é uma ação ativada com base em algum comportamento

### MIN, MAX, AVG, SUM
```
SELECT MIN(length) FROM film;
```
```
SELECT MAX(length) FROM film;
```
```
SELECT AVG(length) FROM film;
```
```
SELECT SUM(length) FROM film;
```

### Agrupando...
```
SELECT COUNT(amount) AS "Quantidade", 
	   SUM(amount) AS "Soma",
       AVG(amount) AS "Média" 
FROM payment;
```
```
SELECT 
	country.country AS "País",
	COUNT(city.city_id) AS "Quantidade de cidades" FROM city    
JOIN country ON city.country_id = country.country_id
GROUP BY country.country
ORDER BY COUNT(city.city_id) DESC;
```

### SUBQUERY
Isso aqui é um problema: WHERE length = MAX(length), para resolver isso:
```
SELECT title FROM film
WHERE
	length = (SELECT MAX(length) FROM film);
```

### STORED PROCEDURE
#### Sem argumento
- Criação da função:
```
DELIMITER //
CREATE PROCEDURE select_all_active_users()
BEGIN
    SELECT * FROM customer
    WHERE active = 1;
END//
DELIMITER ;
```

- Chamada da função:
```
select_all_active_users()
```

#### Com argumento
