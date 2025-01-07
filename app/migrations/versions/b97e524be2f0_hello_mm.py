"""hello mm

Revision ID: b97e524be2f0
Revises: 30c75c32b1a5
Create Date: 2024-12-15 14:07:39.677538

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b97e524be2f0'
down_revision: Union[str, None] = '30c75c32b1a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
