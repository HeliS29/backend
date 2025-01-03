"""hello mm

Revision ID: 30c75c32b1a5
Revises: 54199f015fb7
Create Date: 2024-12-15 14:06:54.378248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30c75c32b1a5'
down_revision: Union[str, None] = '54199f015fb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
