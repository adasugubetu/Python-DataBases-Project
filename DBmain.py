from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import pymysql


class ProjectNotFoundException(Exception):
    pass


class EmployeeNotFoundException(Exception):
    pass


class TaskNotFoundException(Exception):
    pass


class DepartmentNotFoundException(Exception):
    pass


class ResourceNotFoundException(Exception):
    pass


class TeamNotFoundException(Exception):
    pass


hostname = "127.0.0.1"
username = "root"
password = ""
port = 33061
database = "company_app"


conex = pymysql.connect(host=hostname, user=username, password=password, port=port)
cursor = conex.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
cursor.close()
conex.close()

DATABASE_URI = f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'
engine = create_engine(DATABASE_URI)

Base = declarative_base()


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    departments = relationship('Department', back_populates='company')

    def add_department(self, department):
        session.add(department)
        session.commit()

    def remove_department(self, department_name):
        department = session.query(Department).filter_by(name=department_name, company_id=self.id).first()
        if department:
            session.delete(department)
            session.commit()
        else:
            raise DepartmentNotFoundException(f"Department '{department_name}' not found.")

    def add_resource(self, resource):
        session.add(resource)
        session.commit()

    def remove_resource(self, resource_name):
        resource = session.query(Resource).filter_by(name=resource_name).first()
        if resource:
            session.delete(resource)
            session.commit()
        else:
            raise ResourceNotFoundException(f"Resource '{resource_name}' not found.")


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship('Company', back_populates='departments')
    teams = relationship('Team', back_populates='department')

    def __init__(self, name, company_id):
        self.name = name
        self.company_id = company_id

    def add_team(self, team):
        session.add(team)
        session.commit()

    def remove_team(self, team_name):
        team = session.query(Team).filter_by(name=team_name, department_id=self.id).first()
        if team:
            session.delete(team)
            session.commit()
        else:
            raise TeamNotFoundException(f"Team '{team_name}' not found.")


class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship('Department', back_populates='teams')
    employees = relationship('Employee', back_populates='team')
    projects = relationship('Project', back_populates='team')

    def __init__(self, name, department_id):
        self.name = name
        self.department_id = department_id

    def add_employee(self, employee):
        session.add(employee)
        session.commit()

    def remove_employee(self, employee_id):
        employee = session.query(Employee).filter_by(id=employee_id, team_id=self.id).first()
        if employee:
            session.delete(employee)
            session.commit()
        else:
            raise EmployeeNotFoundException(f"Employee with ID '{employee_id}' not found.")

    def add_project(self, project):
        session.add(project)
        session.commit()

    def remove_project(self, project_name):
        project = session.query(Project).filter_by(name=project_name, team_id=self.id).first()
        if project:
            session.delete(project)
            session.commit()
        else:
            raise ProjectNotFoundException(f"Project '{project_name}' not found.")


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)
    salary = Column(Float, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Team', back_populates='employees')

    def __init__(self, name, id, role, team_id, salary):
        self.name = name
        self.id = id
        self.role = role
        self.team_id = team_id
        self.salary = salary

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(50))
    start_date = Column(Date)
    end_date = Column(Date)
    budget = Column(Float, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Team', back_populates='projects')
    tasks = relationship('Task', back_populates='project')

    def __init__(self, name, description, start_date, end_date, budget, team_id):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.team_id = team_id

    def add_task(self, task):
        session.add(task)
        session.commit()

    def remove_task(self, task_title):
        task = session.query(Task).filter_by(title=task_title, project_id=self.id).first()
        if task:
            session.delete(task)
            session.commit()
        else:
            raise TaskNotFoundException(f"Task '{task_title}' not found.")


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(50))
    deadline = Column(Date)
    responsible = Column(String(50))
    status = Column(String(50))
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship('Project', back_populates='tasks')

    def __init__(self, title, description, deadline, responsible, status, project_id):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.responsible = responsible
        self.status = status
        self.project_id = project_id

class Resource(Base):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    type = Column(String(50))
    availability = Column(String(50))
    cost = Column(Float)

    def __init__(self, name, type, availability, cost):
        self.name = name
        self.type = type
        self.availability = availability
        self.cost = cost


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# new_company = Company(name="Tech Corp")
# session.add(new_company)
# session.commit()
# print("Company 'Tech Corp' has been added to the database.")