/*#1
# write a query in SQL to display the first name,
# last name, department number, and department name
# for each employee*/
SELECT employees.first_name, employees.last_name, department.department_id,department.department_name
FROM department as department
INNER JOIN employees as employees ON department.depatment_id=employees.employee_id ORDER BY department.depatment_id;
/*#2write a query in SQL to display the first and last name,
# department, city, and state province for each employee*/
SELECT employees.first_name,employees.last_name,departments.depart_name,locations.state_province
FROM department as departments
LEFT OUTER JOIN employees as employees  ON employees .department_id=departments.department_id
LEFT OUTER JOIN locations as locations ON departments.location_id=locations.location_id
ORDER BY employees.department_id ASC;
/*#3write a query in SQL to display the first name,
# last name, department number, and department name,
# for all employees for departments 80 or 40*/
SELECT employees.first_name, employees.last_name, departments.department_id, departments.depart_name
FROM department as departments
LEFT OUTER JOIN employees as employees  ON employees.department_id=departments.department_id
WHERE employees.department_id=40 or employees.department_id=80
ORDER BY employees.department_id ASC;
/*#4write a query in SQL to display all departments
# including those where does not have any employee*/
SELECT * from departments;
/*#5write a query in SQL to display the first name
# of all employees including the first name of their manager*/
SELECT employees.first_name as 'employee',employees.first_name as 'manager' FROM employees
LEFT OUTER JOIN employees as employees ON employees.manager_id=employees.employee_id;
/*#6write a query in SQL to display the job
# title, full name (first and last name )
# of the employee, and the difference between
# the maximum salary for the job and the salary of the employee*/
SELECT employees.first_name,employees.last_name,j.job_title,(SELECT MAX(salary) FROM employees)-employees.salary as 'diff'
FROM employees as employees
LEFT OUTER JOIN jobs as jobs ON employees.job_id=jobs.job_id ORDER BY diff ASC;

/*#7write a query in SQL to display the
# job title and the average salary of employees*/
SELECT j.job_title,(SELECT SUM(salary)/COUNT(salary) FROM employees WHERE job_id=j.job_id) as 'average_salary'
FROM jobs as j
ORDER BY average_salary ASC;
/*#8write a query in SQL to display
# the full name (first and last name),
# and salary of those employees who work in
# any department located in London*/
SELECT e.first_name,e.last_name,e.salary FROM employees as e
INNER JOIN departments as d ON d.location_id=(SELECT location_id FROM locations WHERE city='London');
/*#9 write a query in SQL to display the department
# name and the number of employees in each department*/
SELECT department.depart_name /*а як дістати кількість робітників ,якщо такий параметр відсутній*/