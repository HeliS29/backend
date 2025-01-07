"""QQQ

Revision ID: b95dc65b55ff
Revises: eba1b8e3a5ce
Create Date: 2024-12-15 14:14:41.561876

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b95dc65b55ff'
down_revision: Union[str, None] = 'eba1b8e3a5ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
