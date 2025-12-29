"""
Day 03 실습: SQL 기초 - SELECT, 필터링, 집계

이 파일의 TODO 부분을 완성하세요.
각 함수는 SQLite 데이터베이스에서 데이터를 조회하는 SQL 쿼리를 작성합니다.
"""
import sqlite3
from typing import List, Tuple, Any, Optional


def create_connection(db_path: str = ':memory:') -> sqlite3.Connection:
    """데이터베이스 연결 생성"""
    conn = sqlite3.connect(db_path)
    return conn


def create_employees_table(conn: sqlite3.Connection) -> None:
    """직원 테이블 생성"""
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
    """직원 데이터 삽입"""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employees (name, department, position, salary, hire_date)
        VALUES (?, ?, ?, ?, ?)
    """, (name, department, position, salary, hire_date))
    conn.commit()
    return cursor.lastrowid


def select_all_employees(conn: sqlite3.Connection) -> List[Tuple]:
    # TODO: SELECT * FROM employees 쿼리 실행
    pass


def select_employees_by_department(conn: sqlite3.Connection,
                                   department: str) -> List[Tuple]:
    # TODO: WHERE 절을 사용하여 특정 부서 직원 조회
    pass


def select_employees_salary_range(conn: sqlite3.Connection,
                                  min_salary: int,
                                  max_salary: int) -> List[Tuple]:
    # TODO: BETWEEN을 사용하여 급여 범위 조회
    pass


def select_employees_by_positions(conn: sqlite3.Connection,
                                  positions: List[str]) -> List[Tuple]:
    # TODO: IN 연산자를 사용하여 여러 직급 조회
    pass


def select_employees_name_pattern(conn: sqlite3.Connection,
                                  pattern: str) -> List[Tuple]:
    # TODO: LIKE를 사용하여 패턴 검색
    pass


def select_employees_ordered(conn: sqlite3.Connection,
                            order_by: str = 'salary',
                            desc: bool = True) -> List[Tuple]:
    # TODO: ORDER BY를 사용하여 정렬
    pass


def count_employees_by_department(conn: sqlite3.Connection) -> List[Tuple]:
    # TODO: GROUP BY와 COUNT를 사용하여 부서별 집계
    pass


def get_salary_stats_by_department(conn: sqlite3.Connection) -> List[Tuple]:
    # TODO: GROUP BY와 집계 함수들 사용
    pass


def get_departments_with_min_employees(conn: sqlite3.Connection,
                                       min_count: int) -> List[Tuple]:
    # TODO: HAVING을 사용하여 그룹 필터링
    pass


def complex_query(conn: sqlite3.Connection,
                  department: str,
                  min_salary: int) -> List[Tuple]:
    # TODO: WHERE, AND, ORDER BY 조합
    pass


def setup_test_data(conn: sqlite3.Connection) -> None:
    """테스트 데이터 설정"""
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
