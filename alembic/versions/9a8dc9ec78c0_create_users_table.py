"""create users table

Revision ID: 9a8dc9ec78c0
Revises: 
Create Date: 2025-09-02 09:36:08.890620

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column , VARCHAR , INTEGER , TIMESTAMP , func


# revision identifiers, used by Alembic.
revision: str = '9a8dc9ec78c0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        Column('id' , INTEGER , autoincrement=True , primary_key=True),
        Column('username' , VARCHAR(100) ,unique=True),
        Column('pasword' , VARCHAR(100)),
        Column("created_at" , TIMESTAMP , server_default=func.now())
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
