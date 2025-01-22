"""remove token

Revision ID: 2ac5255182a4
Revises: c97862d7a6cb
Create Date: 2025-01-21 17:10:27.293537

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ac5255182a4'
down_revision: Union[str, None] = 'c97862d7a6cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('users','token')


def downgrade() -> None:
    pass
