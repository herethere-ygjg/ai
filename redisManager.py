import os
import redis
from dotenv import load_dotenv

# .env 환경볍수 로드
load_dotenv()

class RedisManager:
    """Redis 연결 및 데이터 업데이트/조회를 위한 클래스"""
    def __init__(self):
        self.client = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT")),
            db=int(os.getenv("REDIS_DATABASE")),
            password=os.getenv("REDIS_PASSWORD") or None,
            ssl=os.getenv("REDIS_SSL").lower() == "true"
        )
        print("[Redis] Connected")

    def close(self) -> None:
        self.client.close()
        print("[Redis] Disconnected")