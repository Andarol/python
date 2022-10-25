/*#1
# write a query in SQL to display the first name,
# last name, department number, and department name
# for each employee*/
SELECT first_name.employee, last_name.employee, department_id.department,department_name.department
FROM department
INNER JOIN employee ON department.depatment_id=employees.employee_id;
/*#2write a query in SQL to display the first and last name,
# department, city, and state province for each employee*/
SELECT first_name.employee, last_name.employee, department_id.department,department_name.department
FROM department
INNER JOIN employee ON department.depatment_id=employees.employee_id;
/*#3write a query in SQL to display the first name,
# last name, department number, and department name,
# for all employees for departments 80 or 40*/
/*#4write a query in SQL to display all departments
# including those where does not have any employee*/
/*#5write a query in SQL to display the first name
# of all employees including the first name of their manager*/
/*#6write a query in SQL to display the job
# title, full name (first and last name )
# of the employee, and the difference between
# the maximum salary for the job and the salary of the employee*/
/*#7write a query in SQL to display the
# job title and the average salary of employees*/
/*#8write a query in SQL to display
# the full name (first and last name),
# and salary of those employees who work in
# any department located in London*/
/*#9 write a query in SQL to display the department
# name and the number of employees in each department*/