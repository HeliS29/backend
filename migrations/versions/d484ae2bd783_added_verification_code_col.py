"""added  verification code col

Revision ID: d484ae2bd783
Revises: 6b5e23f23684
Create Date: 2024-12-17 14:19:50.911386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd484ae2bd783'
down_revision: Union[str, None] = '6b5e23f23684'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('verification_code', sa.Integer(), nullable=True))


def downgrade() -> None:
    pass
