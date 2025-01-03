"""added body col

Revision ID: c541d48596f4
Revises: aefeb853b207
Create Date: 2024-12-20 17:39:22.074266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c541d48596f4'
down_revision: Union[str, None] = 'aefeb853b207'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'email_queue',
    
        sa.Column('body', sa.String(100), nullable=False)
    )


def downgrade() -> None:
    pass
