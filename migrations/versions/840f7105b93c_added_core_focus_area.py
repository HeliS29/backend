"""added core focus area

Revision ID: 840f7105b93c
Revises: c211cb3a68f6
Create Date: 2024-12-17 16:38:20.588707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '840f7105b93c'
down_revision: Union[str, None] = 'c211cb3a68f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   
    op.add_column('core_focus_areas', sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=True))
        
    


def downgrade() -> None:
    pass
