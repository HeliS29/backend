"""added role in report

Revision ID: aaaf4706b8c7
Revises: 6147f3ef1d3e
Create Date: 2024-12-23 17:43:03.409423

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aaaf4706b8c7'
down_revision: Union[str, None] = '6147f3ef1d3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('reports', sa.Column('role', sa.String(50), nullable=False))


def downgrade() -> None:
    pass
