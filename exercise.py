"""
Day 03 실습: SQL 기초 - SELECT, 필터링, 집계

이 파일의 TODO 부분을 완성하세요.
각 함수는 SQLite 데이터베이스에서 데이터를 조회하는 SQL 쿼리를 작성합니다.
"""
import sqlite3
from typing import List, Tuple, Any, Optional


def create_connection(db_path: str = ':memory:') -> sqlite3.Connection:
    """데이터베이스 연결 생성

    Args:
        db_path: 데이터베이스 파일 경로 (기본값: 메모리 DB)

    Returns:
        sqlite3.Connection: 데이터베이스 연결 객체
    """
    # TODO: sqlite3.connect()를 사용하여 연결 생성
    # 힌트: sqlite3.connect(db_path)
    pass


def create_employees_table(conn: sqlite3.Connection) -> None:
    """직원 테이블 생성

    Args:
        conn: 데이터베이스 연결 객체

    테이블 구조:
        - emp_id: INTEGER, PRIMARY KEY
        - name: TEXT, NOT NULL
        - department: TEXT
        - position: TEXT
        - salary: INTEGER
        - hire_date: TEXT
    """
    # TODO: CREATE TABLE 문을 작성하여 employees 테이블 생성
    # 힌트: cursor.execute(sql)와 conn.commit() 사용
    pass


def insert_employee(conn: sqlite3.Connection, name: str, department: str,
                   position: str, salary: int, hire_date: str) -> int:
    """직원 데이터 삽입

    Args:
        conn: 데이터베이스 연결 객체
        name: 직원 이름
        department: 부서
        position: 직급
        salary: 급여
        hire_date: 입사일 (YYYY-MM-DD)

    Returns:
        int: 삽입된 행의 ID (lastrowid)
    """
    # TODO: INSERT INTO 문을 작성하여 데이터 삽입
    # 힌트: cursor.execute(sql, (값1, 값2, ...))
    # 힌트: cursor.lastrowid로 삽입된 ID 반환
    pass


def select_all_employees(conn: sqlite3.Connection) -> List[Tuple]:
    """모든 직원 조회

    Args:
        conn: 데이터베이스 연결 객체

    Returns:
        List[Tuple]: 모든 직원 데이터 리스트
    """
    # TODO: SELECT * FROM employees 쿼리 실행
    # 힌트: cursor.fetchall()로 결과 반환
    pass


def select_employees_by_department(conn: sqlite3.Connection,
                                   department: str) -> List[Tuple]:
    """특정 부서 직원 조회

    Args:
        conn: 데이터베이스 연결 객체
        department: 조회할 부서명

    Returns:
        List[Tuple]: 해당 부서 직원 리스트
    """
    # TODO: WHERE 절을 사용하여 특정 부서 직원 조회
    # 힌트: WHERE department = ?
    pass


def select_employees_salary_range(conn: sqlite3.Connection,
                                  min_salary: int,
                                  max_salary: int) -> List[Tuple]:
    """급여 범위로 직원 조회

    Args:
        conn: 데이터베이스 연결 객체
        min_salary: 최소 급여
        max_salary: 최대 급여

    Returns:
        List[Tuple]: 급여 범위에 해당하는 직원 리스트
    """
    # TODO: BETWEEN을 사용하여 급여 범위 조회
    # 힌트: WHERE salary BETWEEN ? AND ?
    pass


def select_employees_by_positions(conn: sqlite3.Connection,
                                  positions: List[str]) -> List[Tuple]:
    """특정 직급들에 해당하는 직원 조회

    Args:
        conn: 데이터베이스 연결 객체
        positions: 조회할 직급 리스트

    Returns:
        List[Tuple]: 해당 직급 직원 리스트
    """
    # TODO: IN 연산자를 사용하여 여러 직급 조회
    # 힌트: WHERE position IN (?, ?, ...)
    # 힌트: placeholders = ','.join(['?' for _ in positions])
    pass


def select_employees_name_pattern(conn: sqlite3.Connection,
                                  pattern: str) -> List[Tuple]:
    """이름 패턴으로 직원 조회 (LIKE)

    Args:
        conn: 데이터베이스 연결 객체
        pattern: 검색 패턴 (예: '김%', '%수%')

    Returns:
        List[Tuple]: 패턴에 맞는 직원 리스트
    """
    # TODO: LIKE를 사용하여 패턴 검색
    # 힌트: WHERE name LIKE ?
    pass


def select_employees_ordered(conn: sqlite3.Connection,
                            order_by: str = 'salary',
                            desc: bool = True) -> List[Tuple]:
    """정렬된 직원 목록 조회

    Args:
        conn: 데이터베이스 연결 객체
        order_by: 정렬 기준 컬럼 (기본값: salary)
        desc: 내림차순 여부 (기본값: True)

    Returns:
        List[Tuple]: 정렬된 직원 리스트
    """
    # TODO: ORDER BY를 사용하여 정렬
    # 힌트: ORDER BY {컬럼} DESC 또는 ASC
    # 주의: 컬럼명은 파라미터 바인딩 불가, f-string 사용
    pass


def count_employees_by_department(conn: sqlite3.Connection) -> List[Tuple]:
    """부서별 직원 수 집계

    Args:
        conn: 데이터베이스 연결 객체

    Returns:
        List[Tuple]: (부서명, 직원수) 튜플 리스트
    """
    # TODO: GROUP BY와 COUNT를 사용하여 부서별 집계
    # 힌트: SELECT department, COUNT(*) FROM employees GROUP BY department
    pass


def get_salary_stats_by_department(conn: sqlite3.Connection) -> List[Tuple]:
    """부서별 급여 통계

    Args:
        conn: 데이터베이스 연결 객체

    Returns:
        List[Tuple]: (부서명, 직원수, 평균급여, 최소급여, 최대급여) 튜플 리스트
    """
    # TODO: GROUP BY와 집계 함수들 사용
    # 힌트: COUNT(*), AVG(salary), MIN(salary), MAX(salary)
    pass


def get_departments_with_min_employees(conn: sqlite3.Connection,
                                       min_count: int) -> List[Tuple]:
    """최소 인원 이상인 부서 조회

    Args:
        conn: 데이터베이스 연결 객체
        min_count: 최소 인원

    Returns:
        List[Tuple]: (부서명, 직원수) 튜플 리스트
    """
    # TODO: HAVING을 사용하여 그룹 필터링
    # 힌트: GROUP BY ... HAVING COUNT(*) >= ?
    pass


def complex_query(conn: sqlite3.Connection,
                  department: str,
                  min_salary: int) -> List[Tuple]:
    """복합 조건 쿼리

    특정 부서에서 급여가 min_salary 이상인 직원을
    급여 내림차순으로 조회

    Args:
        conn: 데이터베이스 연결 객체
        department: 부서명
        min_salary: 최소 급여

    Returns:
        List[Tuple]: (이름, 직급, 급여) 튜플 리스트
    """
    # TODO: WHERE, AND, ORDER BY 조합
    # 힌트: SELECT name, position, salary
    #       FROM employees
    #       WHERE department = ? AND salary >= ?
    #       ORDER BY salary DESC
    pass


# ============================================================
# 테스트용 헬퍼 함수 (수정하지 마세요)
# ============================================================

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


if __name__ == '__main__':
    # 간단한 테스트
    conn = create_connection()
    if conn:
        setup_test_data(conn)

        print("=== 전체 직원 ===")
        employees = select_all_employees(conn)
        if employees:
            for emp in employees:
                print(emp)

        print("\n=== 개발팀 직원 ===")
        dev_team = select_employees_by_department(conn, '개발팀')
        if dev_team:
            for emp in dev_team:
                print(emp)

        print("\n=== 부서별 직원 수 ===")
        dept_counts = count_employees_by_department(conn)
        if dept_counts:
            for dept, count in dept_counts:
                print(f"{dept}: {count}명")

        conn.close()
