-- 3) SQL SELECT – realizando um cálculo simples

SELECT
    s.first_name,
    s.last_name,
    s.salary,
    s.salary * 1.05 AS new_salary
FROM
    hr.employees s;
