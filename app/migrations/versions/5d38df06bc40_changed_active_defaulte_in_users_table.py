"""changed active defaulte in users table

Revision ID: 5d38df06bc40
Revises: 62cdc1f69f67
Create Date: 2025-01-21 15:02:45.940954

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d38df06bc40'
down_revision: Union[str, None] = '62cdc1f69f67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users','active',
            existing_type=sa.Boolean(),
            server_default=sa.text('0') )


def downgrade() -> None:
    pass
