"""heli shah

Revision ID: eba1b8e3a5ce
Revises: b97e524be2f0
Create Date: 2024-12-15 14:10:11.131826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eba1b8e3a5ce'
down_revision: Union[str, None] = 'b97e524be2f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
