SELECT * FROM actor;
-- Criar uma coluna para apresentar o nome completo
-- Utilização do comando concat(concatenar) para juntar as
-- colunas first_name com um espaço e a coluna last_name.
-- para apresentar um nome amigável para a coluna, usamos o
-- comando as(para criar um alias(apelido)) e chamamos de fullname.
SELECT *, concat(first_name," ",last_name) as fullname FROM actor;

-- exibir a quantidade de linhas da nossa tabela de atores
-- vamos usar comando count apontando para uma coluna que não
-- contenha valores nulos

SELECT count(actor_id) as "Qtd actor" FROM actor;
-- da pra saber quantos itens tem na tabela

-- Selecionar os 50 primeiros atores pelo ID
SELECT * FROM actor WHERE actor_id <= 50;

-- Selecionar os 20 primeiros e os 20 ultimos
-- SELECT * FROM actor WHERE actor_id <= 20 AND actor_id >= 180;
SELECT * FROM actor WHERE actor_id <= 20; 
SELECT * FROM actor WHERE actor_id >= 180;

-- selecionar todos os atores que tem o primeiro nome
-- nike
SELECT * FROM actor WHERE first_name="NICK";

SELECT * FROM actor WHERE last_name="DEAN";

-- vamos verificar a estrutura da tabela film
-- utilizaremos o comando desc(describe)
DESC film;

SELECT * FROM film;
SELECT title, description,release_year FROM film;

-- Obter a quantidade de films da tabela
SELECT COUNT(film_id) FROM film;

SELECT * FROM actor;

SELECT * FROM film_actor;

SELECT * FROM film_actor ORDER BY film_id;

-- Nome do autor, Filme que participou e Ano de lançamento.
-- actor(first_name, last_name)
-- films(title,release_year)
-- film_actor

-- Metodo incorreto
SELECT actor.actor_id,
		actor.first_name,
		actor.last_name,
		film.film_id,
		film.title,
		film.release_year
FROM actor,film;


-- Metodo correto
SELECT actor.actor_id,
		actor.first_name,
		actor.last_name,
		film.film_id,
		film.title,
		film.release_year
FROM actor,film, film_actor
WHERE actor.actor_id = film_actor.actor_id 
AND film.film_id = film_actor.film_id
ORDER BY film.film_id;


-- Select feito com INNER JOIN
SELECT actor.actor_id,
		actor.first_name,
		actor.last_name,
		film.film_id,
		film.title,
		film.release_year
FROM actor INNER JOIN film_actor 
ON actor.actor_id = film_actor.actor_id 
INNER JOIN film 
ON film_actor.film_id = film.film_id 
ORDER BY film.film_id;

-- Descrever a tabela category para ver sua estrutura 
DESC category;

SELECT * FROM category;
SELECT * FROM film;

SELECT f.film_id,
		f.title,
        f.description,
        f.release_year,
        c.category_id,
        c.name 
FROM film f INNER JOIN film_category fc 
ON f.film_id = fc.film_id 
INNER JOIN category c 
ON fc.category_id = c.category_id
ORDER BY f.film_id;

SELECT * FROM customer;
SELECT * FROM store;
SELECT * FROM payment;
SELECT * FROM rental;

SELECT c.first_name, c.last_name,
	r.rental_date, r.return_date,
    p.amount, p.payment_date
FROM  customer c INNER JOIN rental r 
ON c.customer_id = r.customer_id
INNER JOIN payment p 
ON p.rental_id = r.rental_id;

SELECT concat(c.first_name, c.last_name) AS fullname,
	r.rental_date, r.return_date,
    p.amount, p.payment_date, f.title
FROM  customer c INNER JOIN rental r 
ON c.customer_id = r.customer_id
INNER JOIN payment p 
ON p.rental_id = r.rental_id
INNER JOIN inventory i
ON r.inventory_id = i.inventory_id
INNER JOIN film f
ON i.film_id = f.film_id; 

SELECT concat(c.first_name, c.last_name) AS fullname,
	r.rental_date, r.return_date,
    p.amount, p.payment_date, f.title
FROM  customer c INNER JOIN rental r 
ON c.customer_id = r.customer_id
INNER JOIN payment p 
ON p.rental_id = r.rental_id
INNER JOIN inventory i
ON r.inventory_id = i.inventory_id
INNER JOIN film f
ON i.film_id = f.film_id WHERE f.title = "ALI FOREVER"; 

SELECT concat(c.first_name, c.last_name) AS fullname,
	r.rental_date, r.return_date,
    p.amount, p.payment_date, f.title
FROM  customer c INNER JOIN rental r 
ON c.customer_id = r.customer_id
INNER JOIN payment p 
ON p.rental_id = r.rental_id
INNER JOIN inventory i
ON r.inventory_id = i.inventory_id
INNER JOIN film f
ON i.film_id = f.film_id WHERE c.first_name = "BOB"; 

SELECT count(f.film_id) AS qtd
FROM  customer c INNER JOIN rental r 
ON c.customer_id = r.customer_id
INNER JOIN payment p 
ON p.rental_id = r.rental_id
INNER JOIN inventory i
ON r.inventory_id = i.inventory_id
INNER JOIN film f
ON i.film_id = f.film_id WHERE c.first_name = "BOB"; 

SELECT sum(p.amount) AS fullvalor
FROM  customer c INNER JOIN rental r 
ON c.customer_id = r.customer_id
INNER JOIN payment p 
ON p.rental_id = r.rental_id
INNER JOIN inventory i
ON r.inventory_id = i.inventory_id
INNER JOIN film f
ON i.film_id = f.film_id WHERE c.first_name = "BOB"; 

SELECT count(f.film_id) AS qtd, sum(p.amount) AS fullvalor
FROM  customer c INNER JOIN rental r 
ON c.customer_id = r.customer_id
INNER JOIN payment p 
ON p.rental_id = r.rental_id
INNER JOIN inventory i
ON r.inventory_id = i.inventory_id
INNER JOIN film f
ON i.film_id = f.film_id WHERE f.title = "ALI FOREVER"; 

SELECT * FROM address;

SELECT * FROM address WHERE district = "São Paulo";

SELECT a.*, c.*, p.* FROM address a 
INNER JOIN city c 
ON a.city_id = c.city_id
INNER JOIN country p
ON c.country_id = p.country_id
WHERE district = "São Paulo";