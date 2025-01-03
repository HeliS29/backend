"""added created at and updated at

Revision ID: 6148eab2ec6b
Revises: 63b5ebb26948
Create Date: 2024-12-18 16:28:57.097850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6148eab2ec6b'
down_revision: Union[str, None] = '63b5ebb26948'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('core_focus_areas', sa.Column('created_at', sa.DateTime, default=sa.func.now()))

    op.add_column('core_focus_areas', sa.Column('updated_at', sa.DateTime, default=sa.func.now(),onupdate=sa.func.now()))
    
    
    op.add_column('critical_activities', sa.Column('created_at',  sa.DateTime(), default=sa.func.now()))

    op.add_column('critical_activities', sa.Column('updated_at',  sa.DateTime(), default=sa.func.now(),onupdate=sa.func.now()))
    



def downgrade() -> None:
    pass
