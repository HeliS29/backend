"""added comments

Revision ID: 992170ced6e7
Revises: aaaf4706b8c7
Create Date: 2024-12-24 11:12:07.012104

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '992170ced6e7'
down_revision: Union[str, None] = 'aaaf4706b8c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('report_version_id', sa.Integer(), sa.ForeignKey('report_versions.id'), nullable=False),
        sa.Column('comment_text', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), default=sa.func.now())
        
    )


def downgrade() -> None:
    pass
