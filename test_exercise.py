"""
Day 03 실습 테스트
SQL 기초 함수들을 테스트합니다.
"""
import pytest
import sqlite3
from exercise import (
    create_connection,
    create_employees_table,
    insert_employee,
    select_all_employees,
    select_employees_by_department,
    select_employees_salary_range,
    select_employees_by_positions,
    select_employees_name_pattern,
    select_employees_ordered,
    count_employees_by_department,
    get_salary_stats_by_department,
    get_departments_with_min_employees,
    complex_query,
)


@pytest.fixture
def db_connection():
    """테스트용 데이터베이스 연결"""
    conn = create_connection(':memory:')
    yield conn
    if conn:
        conn.close()


@pytest.fixture
def populated_db(db_connection):
    """테스트 데이터가 있는 DB"""
    create_employees_table(db_connection)

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
        insert_employee(db_connection, *emp)

    return db_connection


# ============================================================
# Part 1: 기본 연결 및 테이블 생성 테스트
# ============================================================

class TestCreateConnection:
    """데이터베이스 연결 테스트"""

    def test_create_connection_returns_connection(self):
        """연결 객체 반환 확인"""
        conn = create_connection(':memory:')
        assert conn is not None
        assert isinstance(conn, sqlite3.Connection)
        conn.close()

    def test_create_connection_memory_db(self):
        """메모리 DB 연결 확인"""
        conn = create_connection(':memory:')
        cursor = conn.cursor()
        cursor.execute("SELECT sqlite_version()")
        version = cursor.fetchone()[0]
        assert version is not None
        conn.close()


class TestCreateEmployeesTable:
    """테이블 생성 테스트"""

    def test_create_table(self, db_connection):
        """테이블 생성 확인"""
        create_employees_table(db_connection)

        cursor = db_connection.cursor()
        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='employees'
        """)
        result = cursor.fetchone()
        assert result is not None
        assert result[0] == 'employees'

    def test_table_columns(self, db_connection):
        """테이블 컬럼 확인"""
        create_employees_table(db_connection)

        cursor = db_connection.cursor()
        cursor.execute("PRAGMA table_info(employees)")
        columns = {row[1] for row in cursor.fetchall()}

        expected_columns = {'emp_id', 'name', 'department', 'position', 'salary', 'hire_date'}
        assert expected_columns.issubset(columns)


class TestInsertEmployee:
    """데이터 삽입 테스트"""

    def test_insert_employee(self, db_connection):
        """직원 삽입 확인"""
        create_employees_table(db_connection)

        emp_id = insert_employee(
            db_connection, '테스트', '개발팀', '주니어', 4000, '2024-01-01'
        )
        assert emp_id is not None
        assert emp_id > 0

    def test_insert_multiple_employees(self, db_connection):
        """여러 직원 삽입 확인"""
        create_employees_table(db_connection)

        id1 = insert_employee(db_connection, '직원1', '개발팀', '주니어', 4000, '2024-01-01')
        id2 = insert_employee(db_connection, '직원2', '마케팅', '시니어', 5000, '2024-01-02')

        assert id1 != id2
        assert id2 > id1


# ============================================================
# Part 2: SELECT 기본 조회 테스트
# ============================================================

class TestSelectAllEmployees:
    """전체 조회 테스트"""

    def test_select_all(self, populated_db):
        """전체 직원 조회"""
        result = select_all_employees(populated_db)
        assert result is not None
        assert len(result) == 10

    def test_select_all_columns(self, populated_db):
        """모든 컬럼 포함 확인"""
        result = select_all_employees(populated_db)
        # emp_id, name, department, position, salary, hire_date
        assert len(result[0]) == 6


class TestSelectByDepartment:
    """부서별 조회 테스트"""

    def test_select_dev_team(self, populated_db):
        """개발팀 조회"""
        result = select_employees_by_department(populated_db, '개발팀')
        assert len(result) == 4

    def test_select_marketing(self, populated_db):
        """마케팅 조회"""
        result = select_employees_by_department(populated_db, '마케팅')
        assert len(result) == 2

    def test_select_nonexistent_department(self, populated_db):
        """존재하지 않는 부서"""
        result = select_employees_by_department(populated_db, '없는부서')
        assert len(result) == 0


class TestSelectSalaryRange:
    """급여 범위 조회 테스트"""

    def test_salary_range(self, populated_db):
        """급여 범위 조회"""
        result = select_employees_salary_range(populated_db, 5000, 6000)
        # 5000~6000: 김철수(6000), 정수진(5500), 강미영(5500), 임재현(5800), 한소희(5200)
        assert len(result) == 5

    def test_salary_range_boundaries(self, populated_db):
        """경계값 포함 확인 (BETWEEN은 양쪽 포함)"""
        result = select_employees_salary_range(populated_db, 6000, 6000)
        # 정확히 6000인 직원
        assert len(result) == 1


class TestSelectByPositions:
    """직급별 조회 테스트"""

    def test_select_single_position(self, populated_db):
        """단일 직급 조회"""
        result = select_employees_by_positions(populated_db, ['시니어'])
        assert len(result) == 4

    def test_select_multiple_positions(self, populated_db):
        """복수 직급 조회"""
        result = select_employees_by_positions(populated_db, ['시니어', '매니저'])
        # 시니어 4명 + 매니저 2명
        assert len(result) == 6


class TestSelectNamePattern:
    """이름 패턴 조회 테스트"""

    def test_name_starts_with(self, populated_db):
        """이름 시작 패턴"""
        result = select_employees_name_pattern(populated_db, '김%')
        # 김철수
        assert len(result) == 1

    def test_name_contains(self, populated_db):
        """이름 포함 패턴"""
        result = select_employees_name_pattern(populated_db, '%수%')
        # 김철수, 박민수, 정수진
        assert len(result) == 3


class TestSelectOrdered:
    """정렬 조회 테스트"""

    def test_order_by_salary_desc(self, populated_db):
        """급여 내림차순"""
        result = select_employees_ordered(populated_db, 'salary', desc=True)
        salaries = [emp[4] for emp in result]  # salary is 5th column (index 4)
        assert salaries == sorted(salaries, reverse=True)

    def test_order_by_salary_asc(self, populated_db):
        """급여 오름차순"""
        result = select_employees_ordered(populated_db, 'salary', desc=False)
        salaries = [emp[4] for emp in result]
        assert salaries == sorted(salaries)


# ============================================================
# Part 3: 집계 함수 테스트
# ============================================================

class TestCountByDepartment:
    """부서별 집계 테스트"""

    def test_count_departments(self, populated_db):
        """부서별 인원수"""
        result = count_employees_by_department(populated_db)
        result_dict = dict(result)

        assert result_dict['개발팀'] == 4
        assert result_dict['마케팅'] == 2
        assert result_dict['인사팀'] == 2
        assert result_dict['영업팀'] == 2


class TestSalaryStats:
    """급여 통계 테스트"""

    def test_salary_stats_columns(self, populated_db):
        """통계 컬럼 확인"""
        result = get_salary_stats_by_department(populated_db)
        # (부서, 직원수, 평균급여, 최소급여, 최대급여)
        assert len(result[0]) == 5

    def test_dev_team_stats(self, populated_db):
        """개발팀 통계 확인"""
        result = get_salary_stats_by_department(populated_db)
        dev_stats = [r for r in result if r[0] == '개발팀'][0]

        assert dev_stats[1] == 4  # 직원 수
        assert dev_stats[3] == 4500  # 최소급여 (홍길동)
        assert dev_stats[4] == 7500  # 최대급여 (박민수)


class TestDepartmentsWithMinEmployees:
    """최소 인원 부서 테스트"""

    def test_min_3_employees(self, populated_db):
        """3명 이상 부서"""
        result = get_departments_with_min_employees(populated_db, 3)
        departments = [r[0] for r in result]
        # 개발팀만 4명
        assert '개발팀' in departments
        assert len(result) == 1

    def test_min_2_employees(self, populated_db):
        """2명 이상 부서"""
        result = get_departments_with_min_employees(populated_db, 2)
        # 모든 부서가 2명 이상
        assert len(result) == 4


# ============================================================
# Part 4: 복합 쿼리 테스트
# ============================================================

class TestComplexQuery:
    """복합 조건 쿼리 테스트"""

    def test_complex_query_result(self, populated_db):
        """개발팀 5000 이상"""
        result = complex_query(populated_db, '개발팀', 5000)
        # 김철수(6000), 박민수(7500), 조현우(6200)
        assert len(result) == 3

    def test_complex_query_order(self, populated_db):
        """결과 정렬 확인"""
        result = complex_query(populated_db, '개발팀', 5000)
        salaries = [r[2] for r in result]  # salary is 3rd in (name, position, salary)
        assert salaries == sorted(salaries, reverse=True)

    def test_complex_query_columns(self, populated_db):
        """반환 컬럼 확인 (name, position, salary)"""
        result = complex_query(populated_db, '개발팀', 5000)
        assert len(result[0]) == 3


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
