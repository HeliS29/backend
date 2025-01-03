"""added id in comments

Revision ID: 8a2d30ae33cf
Revises: 992170ced6e7
Create Date: 2024-12-24 11:41:01.843101

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a2d30ae33cf'
down_revision: Union[str, None] = '992170ced6e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('comments', sa.Column('id', sa.Integer, primary_key=True, index=True))


def downgrade() -> None:
    pass
