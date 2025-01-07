"""added manager comment in report version

Revision ID: 6147f3ef1d3e
Revises: 2abf35df3d9a
Create Date: 2024-12-23 12:04:58.093594

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6147f3ef1d3e'
down_revision: Union[str, None] = '2abf35df3d9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('report_versions', sa.Column('manager_comments', sa.Text(), nullable=True))
       


def downgrade() -> None:
    pass
