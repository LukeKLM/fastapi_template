from sqlalchemy.orm import joinedload

from app.libs.base_repository import BaseRepository
from app.users.models.oauth_models import OAuthAccount
from core.db import SessionLocal


class OAuthRepository(BaseRepository):
    def __init__(self, db_session: SessionLocal):
        super().__init__(db_session)
        self.model = OAuthAccount

    async def get_by_identifier(self, identifier: str, oauth_type: str) -> OAuthAccount:
        detail = await self.db_session.execute(
            self._select()
            .options(
                joinedload(OAuthAccount.user),
            )
            .where(
                self.model.identifier == identifier,
                self.model.oauth_type == oauth_type,
            ),
        )
        return detail.scalars().first()
