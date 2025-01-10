"""Added 1000 as string

Revision ID: 4a28fc23527c
Revises: 9e6420a3031f
Create Date: 2025-01-09 17:14:00.976263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a28fc23527c'
down_revision: Union[str, None] = '9e6420a3031f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Correct syntax to alter column size
    op.alter_column('role_review', 'job_summary', type_=sa.String(length=1000), nullable=False)



def downgrade() -> None:
    pass
