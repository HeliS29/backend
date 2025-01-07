"""added rolereview table

Revision ID: 7507ff17eac2
Revises: 2b42ac206834
Create Date: 2024-12-17 10:37:54.892269

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7507ff17eac2'
down_revision: Union[str, None] = '2b42ac206834'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'role_review',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('purpose', sa.String(100), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('title', sa.String(100), nullable=False),
        sa.Column('organization', sa.String(100), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('prepared_by', sa.String(100), nullable=False),
        sa.Column('job_summary', sa.String(200), nullable=False),
        sa.Column('created_at', sa.DateTime(), default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), default=sa.func.now(), onupdate=sa.func.now())
    )


def downgrade() -> None:
    pass
