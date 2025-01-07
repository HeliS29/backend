"""added foreign key in report

Revision ID: eb8456e533c3
Revises: c73a7729da44
Create Date: 2024-12-19 10:24:28.565929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb8456e533c3'
down_revision: Union[str, None] = 'c73a7729da44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.add_column('reports', sa.Column('current_version_id', sa.Integer(), sa.ForeignKey('report_versions.id', ondelete='SET NULL'), nullable=True))

def downgrade() -> None:
    pass
