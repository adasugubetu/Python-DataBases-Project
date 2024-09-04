from budget import Budget
from finance import Finance
from functionalities import *
from DBmain import *


def print_main_menu():
    print("\n*** Main Menu ***")
    print("1. Manage Departments")
    print("2. Manage Teams")
    print("3. Manage Employees")
    print("4. Manage Projects")
    print("5. Manage Tasks")
    print("6. Manage Resources")
    print("7. Generate Reports")
    print("8. Exit")
    print("**********************")


def print_department_menu():
    print("\n*** Manage Departments ***")
    print("1. Add Department")
    print("2. Remove Department")
    print("3. Back to Main Menu")
    print("*****************************")


def handle_departments(company):
    while True:
        print_department_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            try:
                name = input("Enter department name: ")
                department = Department(name, company.id)
                company.add_department(department)
                print(f"Department '{name}' has been added.")
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '2':
            try:
                name = input("Enter department name to remove: ")
                company.remove_department(name)
                print(f"Department '{name}' has been removed.")
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '3':
            break

        else:
            print("Invalid option. Please choose between 1 and 3.")


def print_team_menu():
    print("\n*** Manage Teams ***")
    print("1. Add Team")
    print("2. Remove Team")
    print("3. Back to Main Menu")
    print("********************")


def handle_teams(departament):
    while True:
        print_team_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            try:
                name = input("Enter team name: ")
                team = Team(name, department.id)
                departament.add_team(team)
                print(f"Team '{name}' has been added.")
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '2':
            try:
                name = input("Enter team name to remove: ")
                departament.remove_team(name)
                print(f"Team '{name}' has been removed.")
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '3':
            break

        else:
            print("Invalid option. Please choose between 1 and 3.")


def print_employee_menu():
    print("\n*** Manage Employees ***")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Back to Main Menu")
    print("*************************")


def handle_employees(team):
    while True:
        print_employee_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            try:
                name = input("Enter employee name: ")
                id = int(input("Enter employee ID: "))
                role = input("Enter employee role: ")
                team_name = input("Enter employee team name: ")
                salary = float(input("Enter employee salary: "))
                employee = Employee(name, id, role, team.id, salary)
                team.add_employee(employee)
                print(f"Employee '{name}' has been added.")
                finance.add_expense(salary)
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '2':
            try:
                id = int(input("Enter employee ID to remove: "))
                team.remove_employee(id)
                print(f"Employee with id '{id}' has been removed.")
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '3':
            break

        else:
            print("Invalid option. Please choose between 1 and 3.")


def print_project_menu():
    print("\n*** Manage Projects ***")
    print("1. Add Project")
    print("2. Remove Project")
    print("3. Back to Main Menu")
    print("*************************")


def handle_projects(team):
    while True:
        print_project_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            try:
                name = input("Enter project name: ")
                description = input("Enter project description: ")
                start_date = input("Enter project start date (YYYY-MM-DD): ")
                end_date = input("Enter project end date (YYYY-MM-DD): ")
                budget = float(input("Enter project budget: "))
                project = Project(name, description, start_date, end_date, budget, team.id)
                team.add_project(project)
                print(f"Project '{name}' has been added.")
                finance.add_expense(budget)
                company_budget.allocate(budget)
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '2':
            try:
                name = input("Enter project name to remove: ")
                team.remove_project(name)
                print(f"Project '{name}' has been removed.")
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '3':
            break

        else:
            print("Invalid option. Please choose between 1 and 3.")


def print_task_menu():
    print("\n*** Manage Projects ***")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Back to Main Menu")


def handle_tasks(project):
    while True:
        print_task_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            try:
                title = input("Enter project title: ")
                description = input("Enter project description: ")
                deadline = input("Enter project deadline (YYYY-MM-DD): ")
                responsible = input("Enter responsible name: ")
                status = input("Enter status name: ")
                task = Task(title, description, deadline, responsible, status, project.id)
                project.add_task(task)
                print(f"Task '{title}' has been added.")
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '2':
            try:
                title = input("Enter project title to remove: ")
                project.remove_task(title)
                print(f"Task '{title}' has been removed.")
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '3':
            break

        else:
            print("Invalid option. Please choose between 1 and 3.")


def print_resource_menu():
    print("\n*** Manage Resources ***")
    print("1. Add Resource")
    print("2. Remove Resource")
    print("3. Back to Main Menu")
    print("**************************")


def handle_resources(company):
    while True:
        print_resource_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            try:
                name = input("Enter resource name: ")
                resource_type = input("Enter resource type: ")
                availability = input("Enter resource availability: ")
                cost = float(input("Enter resource cost: "))
                resource = Resource(name, resource_type, availability, cost)
                company.add_resource(resource)
                print(f"Resource '{name}' has been added.")
                finance.add_expense(cost)
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '2':
            try:
                name = input("Enter resource name to remove: ")
                company.remove_resource(name)
                print(f"Resource '{name}' has been removed.")
                break
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

        elif choice == '3':
            break

        else:
            print("Invalid option. Please choose between 1 and 3.")


def print_report_menu():
    print("\n*** Generate Reports ***")
    print("1. Generate Project Report")
    print("2. Generate Finance Report")
    print("3. Back to Main Menu")
    print("**************************")


def generate_project_report(company):
    print("\n*** Project Report ***")
    for department in company.departments:
        print(f"Department: {department.name}")
        for team in department.teams:
            print(f"  Team: {team.name}")
            for employee in team.employees:
                print(f"    {employee}")
            for project in team.projects:
                print(f"    Project: {project.name}")
                print(f"    Description: {project.description}")
                print(f"    Start Date: {project.start_date}")
                print(f"    End Date: {project.end_date}")
                print(f"    Budget: ${project.budget}")
                print(f"    Tasks:")
                for task in project.tasks:
                    print(f"        - {task.title} (Status: {task.status})")
    print("**************************")


def generate_finance_report(finance, company_budget, company):
    print("\n*** Finance Report ***")
    print(f"Total Income: ${finance.income}")
    print(f"Total Expenses: ${finance.expenses}")
    print(f"Net Balance: ${finance.net_balance()}\n")
    print(f"Initial Budget for Projects: ${company_budget.initial_budget()}")
    print(f"Remaining Budget: ${company_budget.remaining_budget()}\n")

    employees = get_all_employees(company)
    if employees:
        min_salary_employee = find_employee_with_min_salary(employees)
        max_salary_employee = find_employee_with_max_salary(employees)

        total_salary = calculate_total_salary(employees)
        average_salary = calculate_average_salary(employees)

        print(f"Employee with minimum salary: {min_salary_employee}")

        print(f"Employee with maximum salary: {max_salary_employee.name}")

        print(f"Total salary paid to employees: ${total_salary}.")

        print(f"Average salary paid to employees: ${average_salary}.\n")
    else:
        print("No employees found.\n")

    projects = get_all_projects(company)
    if projects:
        project_with_min_budget = find_project_with_min_budget(projects)
        project_with_max_budget = find_project_with_max_budget(projects)
        total_budget = calculate_total_budget(projects)

        print(f"Project with minimum budget: {project_with_min_budget}")

        print(f"Project with maximum budget: {project_with_max_budget}")

        print(f"Total budget paid for projects: ${total_budget}.\n")
    else:
        print("No projects found.\n")
    print("**************************")


def handle_reports(company):
    while True:
        print_report_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            generate_project_report(company)
            break

        elif choice == '2':
            generate_finance_report(finance, company_budget, company)
            break

        elif choice == '3':
            break

        else:
            print("Invalid option. Please choose between 1 and 3.")


company = session.query(Company).first()

finance = Finance()
finance.add_income(1000000)
company_budget = Budget(finance.income * 0.5)

print("Welcome to the System")

while True:
    print_main_menu()
    choice = input("Choose an option (1-8): ")

    if choice == '1':
        try:
            handle_departments(company)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")

    elif choice == '2':
        department_name = input("Enter department name: ")
        department = find_department_by_name(session, company, department_name)
        if department:
            handle_teams(department)
        else:
            print(f"Department '{department_name}' not found.")

    elif choice == '3':
        department_name = input("Enter department name: ")
        department = find_department_by_name(session, company, department_name)
        if department:
            team_name = input("Enter team name: ")
            team = find_team_by_name(session, department, team_name)
            if team:
                handle_employees(team)
            else:
                print(f"Team '{team_name}' not found.")
        else:
            print(f"Department '{department_name}' not found.")

    elif choice == '4':
        department_name = input("Enter department name: ")
        department = find_department_by_name(session, company, department_name)
        if department:
            team_name = input("Enter team name: ")
            team = find_team_by_name(session, department, team_name)
            if team:
                handle_projects(team)
            else:
                print(f"Team '{team_name}' not found.")
        else:
            print(f"Department '{department_name}' not found.")

    elif choice == '5':
        department_name = input("Enter department name: ")
        department = find_department_by_name(session, company, department_name)
        if department:
            team_name = input("Enter team name: ")
            team = find_team_by_name(session, department, team_name)
            if team:
                project_name = input("Enter project name: ")
                project = find_project_by_name(session, team, project_name)
                if project:
                    handle_tasks(project)
                else:
                    print(f"Project '{project_name}' not found.")
            else:
                print(f"Team '{team_name}' not found.")
        else:
            print(f"Department '{department_name}' not found.")

    elif choice == '6':
        handle_resources(company)

    elif choice == '7':
        handle_reports(company)

    elif choice == '8':
        print("\nExiting the system...")
        break

    else:
        print("Invalid option. Please choose between 1 and 8.")
