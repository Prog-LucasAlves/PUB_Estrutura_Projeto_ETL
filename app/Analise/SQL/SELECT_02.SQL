-- 2) SQL SELECT – selecionando dados de colunas específicas

SELECT
    s.employee_id,
    s.first_name,
    s.last_name,
    s.hire_date
FROM
    hr.employees s;
