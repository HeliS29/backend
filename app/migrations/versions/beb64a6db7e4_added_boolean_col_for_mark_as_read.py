"""added boolean col for mark as read

Revision ID: beb64a6db7e4
Revises: 8a2d30ae33cf
Create Date: 2024-12-26 11:50:54.103201

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'beb64a6db7e4'
down_revision: Union[str, None] = '8a2d30ae33cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('notifications', sa.Column('is_read_by_user', sa.Boolean(), default=False))
    op.add_column('notifications', sa.Column('is_read_by_manager', sa.Boolean(), default=False))


def downgrade() -> None:
    pass
