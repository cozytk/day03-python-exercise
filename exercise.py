"""
Day 03 실습: SQL 기초 - SELECT, 필터링, 집계
"""
import sqlite3
from typing import List, Tuple, Any, Optional


def create_connection(db_path: str = ':memory:') -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    return conn


def create_employees_table(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT,
            position TEXT,
            salary INTEGER,
            hire_date TEXT
        )
    """)
    conn.commit()


def insert_employee(conn: sqlite3.Connection, name: str, department: str,
                   position: str, salary: int, hire_date: str) -> int:
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employees (name, department, position, salary, hire_date)
        VALUES (?, ?, ?, ?, ?)
    """, (name, department, position, salary, hire_date))
    conn.commit()
    return cursor.lastrowid


def select_all_employees(conn: sqlite3.Connection) -> List[Tuple]:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    return cursor.fetchall()


def select_employees_by_department(conn: sqlite3.Connection,
                                   department: str) -> List[Tuple]:
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM employees
        WHERE department = ?
    """, (department,))
    return cursor.fetchall()


def select_employees_salary_range(conn: sqlite3.Connection,
                                  min_salary: int,
                                  max_salary: int) -> List[Tuple]:
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM employees
        WHERE salary BETWEEN ? AND ?
    """, (min_salary, max_salary))
    return cursor.fetchall()


def select_employees_by_positions(conn: sqlite3.Connection,
                                  positions: List[str]) -> List[Tuple]:
    cursor = conn.cursor()
    placeholders = ','.join(['?' for _ in positions])
    cursor.execute(f"""
        SELECT * FROM employees
        WHERE position IN ({placeholders})
    """, positions)
    return cursor.fetchall()


def select_employees_name_pattern(conn: sqlite3.Connection,
                                  pattern: str) -> List[Tuple]:
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM employees
        WHERE name LIKE ?
    """, (pattern,))
    return cursor.fetchall()


def select_employees_ordered(conn: sqlite3.Connection,
                            order_by: str = 'salary',
                            desc: bool = True) -> List[Tuple]:
    cursor = conn.cursor()
    direction = 'DESC' if desc else 'ASC'
    cursor.execute(f"""
        SELECT * FROM employees
        ORDER BY {order_by} {direction}
    """)
    return cursor.fetchall()


def count_employees_by_department(conn: sqlite3.Connection) -> List[Tuple]:
    cursor = conn.cursor()
    cursor.execute("""
        SELECT department, COUNT(*) AS count
        FROM employees
        GROUP BY department
    """)
    return cursor.fetchall()


def get_salary_stats_by_department(conn: sqlite3.Connection) -> List[Tuple]:
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            department,
            COUNT(*) AS count,
            AVG(salary) AS avg_salary,
            MIN(salary) AS min_salary,
            MAX(salary) AS max_salary
        FROM employees
        GROUP BY department
    """)
    return cursor.fetchall()


def get_departments_with_min_employees(conn: sqlite3.Connection,
                                       min_count: int) -> List[Tuple]:
    cursor = conn.cursor()
    cursor.execute("""
        SELECT department, COUNT(*) AS count
        FROM employees
        GROUP BY department
        HAVING COUNT(*) >= ?
    """, (min_count,))
    return cursor.fetchall()


def complex_query(conn: sqlite3.Connection,
                  department: str,
                  min_salary: int) -> List[Tuple]:
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, position, salary
        FROM employees
        WHERE department = ? AND salary >= ?
        ORDER BY salary DESC
    """, (department, min_salary))
    return cursor.fetchall()


def setup_test_data(conn: sqlite3.Connection) -> None:
    create_employees_table(conn)
    test_data = [
        ('김철수', '개발팀', '시니어', 6000, '2020-03-15'),
        ('이영희', '마케팅', '주니어', 4000, '2023-07-01'),
        ('박민수', '개발팀', '리드', 7500, '2018-01-10'),
        ('정수진', '인사팀', '매니저', 5500, '2019-02-20'),
        ('홍길동', '개발팀', '주니어', 4500, '2023-05-05'),
        ('강미영', '마케팅', '시니어', 5500, '2020-09-01'),
        ('조현우', '개발팀', '시니어', 6200, '2019-11-15'),
        ('윤서연', '인사팀', '주니어', 3800, '2024-01-01'),
        ('임재현', '영업팀', '매니저', 5800, '2019-08-20'),
        ('한소희', '영업팀', '시니어', 5200, '2021-03-10'),
    ]
    for emp in test_data:
        insert_employee(conn, *emp)
