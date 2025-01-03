"""added report content table

Revision ID: e07ed93984ff
Revises: eb8456e533c3
Create Date: 2024-12-19 14:14:55.700469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e07ed93984ff'
down_revision: Union[str, None] = 'eb8456e533c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'report_contents',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('report_version_id', sa.Integer(), sa.ForeignKey('report_versions.id', ondelete='CASCADE'), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), default=sa.func.now(), onupdate=sa.func.now()),
    
    ),


def downgrade() -> None:
    pass
