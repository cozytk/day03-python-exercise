# Day 03 실습: SQL 기초 - SELECT, 필터링, 집계

## 🎯 이 실습을 완료하면?

이 실습을 통해 다음 역량을 갖추게 됩니다:

| 배우는 것 | 실무 활용 |
|----------|----------|
| `SELECT`, `WHERE` | 데이터 조회 및 필터링 |
| `BETWEEN`, `IN`, `LIKE` | 다양한 조건 검색 |
| `ORDER BY` | 데이터 정렬 |
| `GROUP BY`, `HAVING` | 데이터 집계 및 그룹 필터링 |
| `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` | 통계 계산 |

> 💡 **SQL이란?** Structured Query Language. 데이터베이스에서 데이터를 조회, 삽입, 수정, 삭제하는 표준 언어!

---

## 📚 사전 준비

Day01, Day02 실습을 완료했다면 Git과 Docker가 이미 설치되어 있습니다.

```bash
# 확인
git --version
docker --version
```

> ⚠️ **중요**: Docker Desktop이 **실행 중**이어야 합니다!

---

## 🚀 Step by Step 실습 가이드

### Step 1: 저장소 Fork & Clone

```bash
# YOUR_USERNAME을 본인의 GitHub 사용자명으로 변경
git clone https://github.com/YOUR_USERNAME/day03-python-exercise.git
cd day03-python-exercise
```

### Step 2: 현재 상태 확인

```bash
docker compose run --rm test
```

31개 테스트가 모두 **FAILED**로 나오는 것이 정상입니다!

### Step 3: Part 1 - 기본 연결 및 테이블 생성

먼저 데이터베이스 연결부터 시작합니다:

```python
def create_connection(db_path: str = ':memory:') -> sqlite3.Connection:
    # TODO: sqlite3.connect()를 사용하여 연결 생성
    conn = sqlite3.connect(db_path)
    return conn
```

테스트:
```bash
docker compose run --rm test pytest test_exercise.py::TestCreateConnection -v
```

### Step 4: 단계별 구현하기

| 순서 | 함수명 | 테스트 명령어 |
|------|--------|-------------|
| **Part 1: 기본 연결 및 테이블** | | |
| 1 | `create_connection` | `pytest test_exercise.py::TestCreateConnection -v` |
| 2 | `create_employees_table` | `pytest test_exercise.py::TestCreateEmployeesTable -v` |
| 3 | `insert_employee` | `pytest test_exercise.py::TestInsertEmployee -v` |
| **Part 2: SELECT 기본 조회** | | |
| 4 | `select_all_employees` | `pytest test_exercise.py::TestSelectAllEmployees -v` |
| 5 | `select_employees_by_department` | `pytest test_exercise.py::TestSelectByDepartment -v` |
| 6 | `select_employees_salary_range` | `pytest test_exercise.py::TestSelectSalaryRange -v` |
| 7 | `select_employees_by_positions` | `pytest test_exercise.py::TestSelectByPositions -v` |
| 8 | `select_employees_name_pattern` | `pytest test_exercise.py::TestSelectNamePattern -v` |
| 9 | `select_employees_ordered` | `pytest test_exercise.py::TestSelectOrdered -v` |
| **Part 3: 집계 함수** | | |
| 10 | `count_employees_by_department` | `pytest test_exercise.py::TestCountByDepartment -v` |
| 11 | `get_salary_stats_by_department` | `pytest test_exercise.py::TestSalaryStats -v` |
| 12 | `get_departments_with_min_employees` | `pytest test_exercise.py::TestDepartmentsWithMinEmployees -v` |
| **Part 4: 복합 쿼리** | | |
| 13 | `complex_query` | `pytest test_exercise.py::TestComplexQuery -v` |

> 💡 테스트 명령어 앞에 `docker compose run --rm test`를 붙여서 실행하세요!

### Step 5: 전체 테스트 통과 확인

```bash
docker compose run --rm test
```

**31 passed**가 나오면 성공!

### Step 6: GitHub에 Push

```bash
git add .
git commit -m "feat: 모든 함수 구현 완료"
git push origin main
```

---

## 💡 막혔을 때는?

각 단계별로 정답이 포함된 브랜치가 준비되어 있습니다:

| 브랜치 | 포함된 함수 |
|--------|-----------|
| `base` | 빈칸 상태 (시작점) |
| `step-1` | Part 1: 기본 연결 및 테이블 (3개) |
| `step-2` | + Part 2: SELECT 기본 조회 (6개) |
| `step-3` | + Part 3: 집계 함수 (3개) |
| `step-4` | + Part 4: 복합 쿼리 (1개) |
| `main` | 모든 함수 완성 |

### 정답 확인 방법

```bash
# step-1에서 추가된 코드 확인
git diff base step-1 -- exercise.py
```

---

## 📝 SQL 문법 힌트

### 기본 SELECT
```sql
SELECT * FROM employees;
SELECT name, salary FROM employees;
```

### WHERE 필터링
```sql
SELECT * FROM employees WHERE department = '개발팀';
SELECT * FROM employees WHERE salary BETWEEN 4000 AND 6000;
SELECT * FROM employees WHERE position IN ('시니어', '매니저');
SELECT * FROM employees WHERE name LIKE '김%';
```

### ORDER BY 정렬
```sql
SELECT * FROM employees ORDER BY salary DESC;
```

### GROUP BY 집계
```sql
SELECT department, COUNT(*) FROM employees GROUP BY department;
SELECT department, AVG(salary) FROM employees GROUP BY department;
```

### HAVING 그룹 필터링
```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) >= 3;
```

---

## 🐳 Docker 명령어 모음

| 명령어 | 설명 |
|--------|------|
| `docker compose run --rm test` | 전체 테스트 실행 |
| `docker compose run --rm test pytest test_exercise.py::TestXXX -v` | 특정 테스트만 실행 |
| `docker compose run --rm shell` | Python 대화형 셸 (디버깅용) |

---

## ⚠️ 자주 발생하는 오류

### "sqlite3.OperationalError: no such table"

**원인**: 테이블이 생성되지 않음

**해결**: `create_employees_table()` 함수가 제대로 구현되었는지 확인

### "TypeError: 'NoneType' object is not iterable"

**원인**: 함수에서 `return`이 빠짐

**해결**: `cursor.fetchall()` 결과를 반환하는지 확인

### 파라미터 바인딩 오류

**원인**: SQL 인젝션 방지를 위해 `?` 사용 필요

**해결**:
```python
# ❌ 잘못된 예
cursor.execute(f"SELECT * FROM employees WHERE department = '{dept}'")

# ✅ 올바른 예
cursor.execute("SELECT * FROM employees WHERE department = ?", (dept,))
```

---

## 📁 파일 구조

```
day03-python-exercise/
├── README.md              # 이 파일 (실습 가이드)
├── exercise.py            # 🎯 빈칸 채우기 대상
├── test_exercise.py       # 테스트 코드 (수정 금지)
├── requirements.txt       # Python 패키지 목록
├── Dockerfile             # Docker 이미지 설정
├── docker-compose.yml     # Docker 서비스 설정
└── .github/workflows/test.yml
```

---

## 🎉 실습 완료 체크리스트

- [ ] 모든 31개 테스트 통과
- [ ] GitHub에 Push 완료
- [ ] GitHub Actions에서 ✅ 확인

**Day 03 완료! 내일은 SQL 심화를 배웁니다.** 🚀
