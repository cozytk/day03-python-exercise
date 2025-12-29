# Day 03 실습 테스트 환경
FROM python:3.10-slim

WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 테스트 실행
CMD ["pytest", "-v", "--tb=short"]
