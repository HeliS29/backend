"""added report and report versions

Revision ID: caccb47c6bbf
Revises: 6148eab2ec6b
Create Date: 2024-12-19 10:16:35.049583

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'caccb47c6bbf'
down_revision: Union[str, None] = '6148eab2ec6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.create_table(
        'reports',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('manager_id', sa.Integer(), sa.ForeignKey('managers.id', ondelete='CASCADE'), nullable=False),
        sa.Column('created_at', sa.DateTime(), default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), default=sa.func.now(), onupdate=sa.func.now())
    )
    
    # Creating the ReportVersion table
    


def downgrade() -> None:
    pass
