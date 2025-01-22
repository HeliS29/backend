"""added token col

Revision ID: 197c76c98532
Revises: 95079fed6061
Create Date: 2025-01-21 16:47:47.318202

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '197c76c98532'
down_revision: Union[str, None] = '95079fed6061'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('token', sa.String(length=100), nullable=True))


def downgrade() -> None:
    pass
