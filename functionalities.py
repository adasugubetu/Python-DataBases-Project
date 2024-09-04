from functools import reduce
from DBmain import *

extract_salary_from_employee = lambda employee: employee.salary
extract_budget_from_project = lambda project: project.budget


def calculate_total_salary(employees):
    return sum(employee.salary for employee in employees)


def find_employee_with_min_salary(employees):
    return min(employees, key=extract_salary_from_employee)


def find_employee_with_max_salary(employees):
    return max(employees, key=extract_salary_from_employee)


def calculate_average_salary(employees):
    total_salary = calculate_total_salary(employees)
    employees_number = len(employees)
    if employees_number:
        return total_salary / employees_number
    return 0


def find_project_with_min_budget(projects):
    return min(projects, key=extract_budget_from_project)


def find_project_with_max_budget(projects):
    return max(projects, key=extract_budget_from_project)


def calculate_total_budget(projects):
    return sum(project.budget for project in projects)


def find_department_by_name(session, company, department_name):
    return session.query(Department).filter_by(name=department_name, company_id=company.id).first()


def find_team_by_name(session, department, team_name):
    return session.query(Team).filter_by(name=team_name, department_id=department.id).first()


def find_project_by_name(session, team, project_name):
    return session.query(Project).filter_by(name=project_name, team_id=team.id).first()


def find_task_by_title(session, project, task_title):
    return session.query(Task).filter_by(title=task_title, project_id=project.id).first()


def get_all_employees(company):
    all_employees = []
    for department in company.departments:
        for team in department.teams:
            all_employees.extend(team.employees)
    return all_employees

def get_all_projects(company):
    all_projects = []
    for department in company.departments:
        for team in department.teams:
            all_projects.extend(team.projects)
    return all_projects