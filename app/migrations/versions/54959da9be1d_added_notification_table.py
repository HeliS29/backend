"""added notification table

Revision ID: 54959da9be1d
Revises: e07ed93984ff
Create Date: 2024-12-19 17:38:17.263982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54959da9be1d'
down_revision: Union[str, None] = 'e07ed93984ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'notifications',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('message', sa.String(100), nullable=False),
        sa.Column('is_read', sa.Boolean(), default=False),
        sa.Column('created_at', sa.DateTime(), default=sa.func.now())
    )



def downgrade() -> None:
    pass
