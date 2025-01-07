"""deleted userid

Revision ID: c211cb3a68f6
Revises: d484ae2bd783
Create Date: 2024-12-17 14:31:35.754845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c211cb3a68f6'
down_revision: Union[str, None] = 'd484ae2bd783'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
    
    sa.Column('role', sa.String(50), nullable=False),
    sa.Column('created_at', sa.DateTime, default=sa.func.now()),
    sa.Column('updated_at', sa.DateTime, default=sa.func.now(), onupdate=sa.func.now()),


def downgrade() -> None:
    pass
