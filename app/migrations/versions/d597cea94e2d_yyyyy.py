"""YYYYY

Revision ID: d597cea94e2d
Revises: b95dc65b55ff
Create Date: 2024-12-15 14:18:47.618111

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd597cea94e2d'
down_revision: Union[str, None] = 'b95dc65b55ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
