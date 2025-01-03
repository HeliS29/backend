"""hello

Revision ID: 54199f015fb7
Revises: bc8b3e81dc71
Create Date: 2024-12-15 14:03:07.355294

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54199f015fb7'
down_revision: Union[str, None] = 'bc8b3e81dc71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
