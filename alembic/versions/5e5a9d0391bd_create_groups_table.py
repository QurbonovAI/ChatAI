"""create groups table

Revision ID: 5e5a9d0391bd
Revises: 9a8dc9ec78c0
Create Date: 2025-09-02 09:36:31.103835

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column , INTEGER , VARCHAR  , TIMESTAMP , func


# revision identifiers, used by Alembic.
revision: str = '5e5a9d0391bd'
down_revision: Union[str, Sequence[str], None] = '9a8dc9ec78c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'groups',
        Column('id' , INTEGER , primary_key=True , autoincrement=True),
        Column('name' , VARCHAR(100) , nullable=False),
        Column('token' , VARCHAR(255) , unique=True , index=True),
        Column("created_at" , TIMESTAMP , server_default=func.now())
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('groups')
