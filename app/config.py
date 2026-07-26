from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL


class Settings(BaseSettings):
    app_name: str = "CRUD System"
    app_version: str = "1.0.0"
    server_name: str = "api-svc"
    server_ip: str = ""
    access_token_expire_minutes: int = 60
    cors_origins: str = "http://localhost:5173,http://localhost:8080"

    mysql_host: str = "db-svc"
    mysql_port: int = 3306
    mysql_database: str = "frodo"
    mysql_user: str = "frodo"
    mysql_password: str = "Frodo5020!!"

    redis_host: str = "redis-svc"
    redis_port: int = 6379
    redis_database: int = 0
    redis_password: str | None = None
    redis_session_prefix: str = "crud:session:"

    admin_username: str = "admin"
    admin_password: str = "frodo1234"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def database_url(self) -> URL:
        return URL.create(
            drivername="mysql+pymysql",
            username=self.mysql_user,
            password=self.mysql_password,
            host=self.mysql_host,
            port=self.mysql_port,
            database=self.mysql_database,
            query={"charset": "utf8mb4"},
        )

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
