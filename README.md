# React + FastAPI + Redis CRUD System

React 프론트엔드, FastAPI API, MySQL 8.0 데이터베이스와 Redis 세션 저장소로 구성된 CRUD 애플리케이션입니다.

## 이미지

| 역할 | 이미지 |
| --- | --- |
| React + Nginx 프론트엔드 | `hifrodo/crud2-front:1.0` |
| FastAPI API | `hifrodo/crud2-api:1.0` |
| MySQL 데이터베이스 | `hifrodo/crud2-sql:1.0` |
| Redis 세션 저장소 | `hifrodo/crud2-redis:1.0` |

## 서비스 연결

- API → MySQL: `db-svc:3306`
- API → Redis: `redis-svc:6379`
- 프론트엔드 Nginx → API: `api-svc:8000`

로그인/회원가입 시 API가 opaque 세션 토큰을 발급하고 실제 세션은 Redis에 TTL과 함께 저장합니다. 프론트엔드는 토큰을 `Authorization: Bearer` 헤더로 전달하며 쿠키는 사용하지 않습니다. 로그아웃하면 Redis 세션이 즉시 삭제됩니다.

## 실행

```powershell
Copy-Item .env.example .env
docker compose up --build -d
```

- 프론트엔드: <http://localhost:8080>
- API 문서: <http://localhost:8000/docs>
- 상태 페이지: <http://localhost:8080/status>
- API 상태: <http://localhost:8000/health>
- 회원 API: `GET /api/members`
- 초기 아이디: `admin`
- 초기 비밀번호: `frodo1234`

MySQL 데이터는 `mysql_data`, Redis 데이터는 `redis_data` 볼륨에 보존됩니다.

## 개별 이미지 빌드 및 push

```powershell
docker build -f db/Dockerfile -t hifrodo/crud2-sql:1.0 db
docker build -f app/Dockerfile -t hifrodo/crud2-api:1.0 .
docker build -f frontend/Dockerfile -t hifrodo/crud2-front:1.0 frontend
docker build -f redis/Dockerfile -t hifrodo/crud2-redis:1.0 redis

docker push hifrodo/crud2-sql:1.0
docker push hifrodo/crud2-api:1.0
docker push hifrodo/crud2-front:1.0
docker push hifrodo/crud2-redis:1.0
```
