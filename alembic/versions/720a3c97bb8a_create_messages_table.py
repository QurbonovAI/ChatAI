"""create messages table

Revision ID: 720a3c97bb8a
Revises: 6d0ac9d8b4c9
Create Date: 2025-09-02 09:37:05.871060

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import  Column , VARCHAR , INTEGER , ForeignKey , TIMESTAMP , TEXT , DateTime ,  func


# revision identifiers, used by Alembic.
revision: str = '720a3c97bb8a'
down_revision: Union[str, Sequence[str], None] = '6d0ac9d8b4c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'messages',
        Column('id' , INTEGER , autoincrement=True , primary_key=True),
        Column('group_id' , INTEGER , ForeignKey('groups.id')),
        Column('user_id' , INTEGER  , ForeignKey('users.id')),
        Column('message' ,  TEXT , nullable=False),
        Column('created_at' , DateTime , server_default=func.now())
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('messages')
