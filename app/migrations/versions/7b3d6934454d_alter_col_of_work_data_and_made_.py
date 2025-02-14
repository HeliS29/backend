"""alter col of work data and made nullable to true

Revision ID: 7b3d6934454d
Revises: 034e0e6579c3
Create Date: 2025-02-13 16:33:11.051569

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b3d6934454d'
down_revision: Union[str, None] = '034e0e6579c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('workdata') as batch_op:
        batch_op.alter_column('work_description', existing_type=sa.String(500), nullable=True)
        batch_op.alter_column('hours_description', existing_type=sa.String(500), nullable=True)


def downgrade() -> None:
    pass
