currentEmployee = {1: 'Scott', 2: "Eric", 3:"Kelly"}
formerEmployee  = {2: 'Eric', 4: "Emma"}

allEmployee = {**currentEmployee, **formerEmployee}
print(allEmployee)