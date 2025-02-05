"""Add WorkData model

Revision ID: fc47b3c21c28
Revises: 2ac5255182a4
Create Date: 2025-02-05 00:42:05.807933

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc47b3c21c28'
down_revision: Union[str, None] = '2ac5255182a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
