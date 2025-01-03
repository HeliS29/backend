"""added added manager id 

Revision ID: 3dc4da3c0c35
Revises: 329ae102831a
Create Date: 2024-12-27 13:38:23.814812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3dc4da3c0c35'
down_revision: Union[str, None] = '329ae102831a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.add_column(
        'new_notifications',
        sa.Column('manager_id',sa.Integer(), sa.ForeignKey('managers.id'), nullable=True)),
      
        
  

def downgrade() -> None:
    pass
