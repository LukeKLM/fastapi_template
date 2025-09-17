from app.libs.base_repository import BaseRepository
from app.users.models.users_models import User
from core.db import SessionLocal


class UserRepository(BaseRepository):
    def __init__(self, db_session: SessionLocal):
        super().__init__(db_session)
        self.model = User

    async def get_by_email(self, email: str) -> User:
        detail = await self.db_session.execute(
            self._select().where(self.model.email == email),
        )
        return detail.scalars().first()
