"""add encrypt col in users table

Revision ID: effa44f50050
Revises: 593183b77e7f
Create Date: 2025-03-05 11:56:47.936137

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'effa44f50050'
down_revision: Union[str, None] = '593183b77e7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('encrypted_password', sa.String(500), nullable=True))


def downgrade() -> None:
    pass
