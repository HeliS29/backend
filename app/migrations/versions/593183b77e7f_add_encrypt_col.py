"""add encrypt col

Revision ID: 593183b77e7f
Revises: 7b3d6934454d
Create Date: 2025-03-05 11:26:52.996613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '593183b77e7f'
down_revision: Union[str, None] = '7b3d6934454d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('encrypted_password', sa.String(500), nullable=True))



def downgrade() -> None:
    pass
