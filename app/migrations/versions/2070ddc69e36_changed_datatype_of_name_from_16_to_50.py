"""changed datatype of name from 16 to 50

Revision ID: 2070ddc69e36
Revises: 4e680038095e
Create Date: 2025-01-21 11:43:27.390974

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2070ddc69e36'
down_revision: Union[str, None] = '4e680038095e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.alter_column('users', 'name',
               existing_type=sa.String(length=16),
               type_=sa.String(length=50),
               existing_nullable=False)


def downgrade() -> None:
    pass
