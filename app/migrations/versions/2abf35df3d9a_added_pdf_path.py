"""added pdf path

Revision ID: 2abf35df3d9a
Revises: c541d48596f4
Create Date: 2024-12-21 13:18:30.926487

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2abf35df3d9a'
down_revision: Union[str, None] = 'c541d48596f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('reports', sa.Column('pdf_path', sa.String(100), nullable=False))


def downgrade() -> None:
    pass
