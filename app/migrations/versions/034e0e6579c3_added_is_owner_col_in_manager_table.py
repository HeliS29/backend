"""added is_owner col in manager table

Revision ID: 034e0e6579c3
Revises: d656dc470519
Create Date: 2025-02-13 12:54:26.727012

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '034e0e6579c3'
down_revision: Union[str, None] = 'd656dc470519'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("managers", sa.Column("is_owner", sa.Boolean(), nullable=False, server_default=sa.false()))



def downgrade() -> None:
    pass
