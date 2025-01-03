"""added craeted at in new notifications

Revision ID: 329ae102831a
Revises: 3ab6b90a032d
Create Date: 2024-12-27 11:54:42.904074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '329ae102831a'
down_revision: Union[str, None] = '3ab6b90a032d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'new_notifications',
        sa.Column('created_at',  sa.DateTime(), default=sa.func.now()),
      
        
    )


def downgrade() -> None:
    pass
