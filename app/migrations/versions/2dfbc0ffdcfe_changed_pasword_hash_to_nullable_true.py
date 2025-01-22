"""changed pasword hash to nullable true

Revision ID: 2dfbc0ffdcfe
Revises: 5d38df06bc40
Create Date: 2025-01-21 15:32:20.419832

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2dfbc0ffdcfe'
down_revision: Union[str, None] = '5d38df06bc40'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users',
            'password_hash',
            existing_type=sa.String(length=100),
            nullable=True
        )


def downgrade() -> None:
    pass
