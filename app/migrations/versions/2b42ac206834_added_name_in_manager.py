"""added name in manager

Revision ID: 2b42ac206834
Revises: 317ff54c9b5e
Create Date: 2024-12-16 10:32:05.948408

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b42ac206834'
down_revision: Union[str, None] = '317ff54c9b5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.add_column('managers',
        sa.Column("name", sa.String(100), nullable=False)
    )



def downgrade() -> None:
    pass
