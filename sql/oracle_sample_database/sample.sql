// employee id, full name, and job title
SELECT employee_id, first_name, last_name, job_title FROM employees;

// employee id and full name of accountants
SELECT * FROM employees
WHERE job_title='Accountant';

// products worth less than 20usd
SELECT * FROM products
where list_price <= 20

(query result)
/// products from lowest to highest
// product_id, product_name, description, list_price,
SELECT product_id, product_name, description, list_price FROM products
ORDER BY list_price ASC;

// orders that have been shipped past jan 1 2017
SELECT * FROM orders
WHERE status = 'Shipped' AND order_date > '01-JAN-17'

// select product id, name, desc, list price that are less than 20 and more than 100. order by lowest to highest
SELECT product_id, product_name, description, list_price
FROM products
WHERE list_price < 20 OR list_price > 100
ORDER BY list_price ASC;