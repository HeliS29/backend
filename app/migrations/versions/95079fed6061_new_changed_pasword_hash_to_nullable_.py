"""new changed pasword hash to nullable true

Revision ID: 95079fed6061
Revises: 2dfbc0ffdcfe
Create Date: 2025-01-21 15:33:44.156650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95079fed6061'
down_revision: Union[str, None] = '2dfbc0ffdcfe'
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
