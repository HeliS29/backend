"""profile data latest

Revision ID: 06508d53798b
Revises: d9b85130df68
Create Date: 2024-12-15 12:47:35.258060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06508d53798b'
down_revision: Union[str, None] = 'd9b85130df68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
