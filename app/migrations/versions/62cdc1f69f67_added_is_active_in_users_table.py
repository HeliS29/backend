"""added is_active in users table

Revision ID: 62cdc1f69f67
Revises: 2070ddc69e36
Create Date: 2025-01-21 14:59:37.982958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62cdc1f69f67'
down_revision: Union[str, None] = '2070ddc69e36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('active', sa.Boolean(), nullable=True, server_default=sa.text('1')))



def downgrade() -> None:
    pass
