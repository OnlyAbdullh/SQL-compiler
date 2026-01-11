SELECT
    employee_id,
    salary,
    bonus,
    tax_rate
FROM Employees
WHERE
(
    (salary + bonus * 2 - 1000) > (5000 / 2)
    AND
    (
        (salary - bonus) * tax_rate <= 3000
        OR
        (salary / (bonus + 1)) > 100
    )
)
OR
(
    ((salary + 200) / 2) - (bonus * 3) = 750
    AND
    (
        tax_rate + 0.05 > 0.3
        OR
        (salary - bonus * 4) / 2 < 1000
    )
);