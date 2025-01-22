"""added token col with big data

Revision ID: c97862d7a6cb
Revises: 197c76c98532
Create Date: 2025-01-21 16:52:10.572436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c97862d7a6cb'
down_revision: Union[str, None] = '197c76c98532'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'token', type_=sa.String(length=255))


def downgrade() -> None:
    pass
