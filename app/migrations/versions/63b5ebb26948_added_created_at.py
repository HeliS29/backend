"""added created at 

Revision ID: 63b5ebb26948
Revises: b40daae543c9
Create Date: 2024-12-18 16:23:24.260763

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63b5ebb26948'
down_revision: Union[str, None] = 'b40daae543c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.add_column('core_focus_areas', sa.Column('created_at', sa.DateTime, default=sa.func.now()))

    op.add_column('core_focus_areas', sa.Column('updated_at', sa.DateTime, default=sa.func.now(),onupdate=sa.func.now()))
    
    
    op.add_column('critical_activities', sa.Column('created_at',  sa.DateTime(), default=sa.func.now()))

    op.add_column('critical_activities', sa.Column('updated_at',  sa.DateTime(), default=sa.func.now(),onupdate=sa.func.now()))
    


def downgrade() -> None:
    pass
