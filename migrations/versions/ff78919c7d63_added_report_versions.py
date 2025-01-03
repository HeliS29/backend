"""added report versions

Revision ID: ff78919c7d63
Revises: caccb47c6bbf
Create Date: 2024-12-19 10:21:38.849552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff78919c7d63'
down_revision: Union[str, None] = 'caccb47c6bbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'report_versions',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('report_id', sa.Integer(), sa.ForeignKey('reports.id', ondelete='CASCADE'), nullable=False),
        sa.Column('version_number', sa.Integer(), nullable=False),
        sa.Column('generated_at', sa.DateTime(), default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('pdf_path', sa.String(100), nullable=False)
    ),


def downgrade() -> None:
    pass
