"""droped dept col

Revision ID: 4e680038095e
Revises: ddfe6ce5d81f
Create Date: 2025-01-21 11:07:04.443800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e680038095e'
down_revision: Union[str, None] = 'ddfe6ce5d81f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('managers','dept')


def downgrade() -> None:
    pass
