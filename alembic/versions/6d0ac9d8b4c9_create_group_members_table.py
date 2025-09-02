"""create group_members table

Revision ID: 6d0ac9d8b4c9
Revises: 5e5a9d0391bd
Create Date: 2025-09-02 09:36:57.042866

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column , INTEGER , VARCHAR , TIMESTAMP , ForeignKey , DateTime ,  func


# revision identifiers, used by Alembic.
revision: str = '6d0ac9d8b4c9' 
down_revision: Union[str, Sequence[str], None] = '5e5a9d0391bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'group_members',
        Column('id' , INTEGER , autoincrement=True , primary_key=True , index=True),
        Column('group_id' , INTEGER  , ForeignKey('groups.id')),
        Column('user_id' , INTEGER , ForeignKey('users.id')),
        Column('joined_at' , DateTime , server_default=func.now())
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('group_members')
