"""added new notifications

Revision ID: 3ab6b90a032d
Revises: beb64a6db7e4
Create Date: 2024-12-27 11:39:03.593054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ab6b90a032d'
down_revision: Union[str, None] = 'beb64a6db7e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'new_notifications',
        sa.Column('message', sa.String(100), nullable=False),
      
        
    )
    op.add_column(
        'new_notifications',
        sa.Column('created_at',  sa.DateTime(), default=sa.func.now()),
      
        
    )


def downgrade() -> None:
    pass
