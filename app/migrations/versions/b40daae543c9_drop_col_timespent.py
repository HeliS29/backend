"""drop col timespent

Revision ID: b40daae543c9
Revises: f2efef336993
Create Date: 2024-12-18 10:01:54.988929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b40daae543c9'
down_revision: Union[str, None] = 'f2efef336993'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('critical_activities', 'time_spent')


def downgrade() -> None:
    pass
