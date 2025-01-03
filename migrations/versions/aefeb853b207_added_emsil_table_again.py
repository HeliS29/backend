"""added emsil table again

Revision ID: aefeb853b207
Revises: ee85f45d30d1
Create Date: 2024-12-20 17:24:30.620730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aefeb853b207'
down_revision: Union[str, None] = 'ee85f45d30d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'email_queue',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('recipient_id', sa.Integer, nullable=False),
        sa.Column('recipient_type', sa.String(100), nullable=True),
        sa.Column('subject', sa.String(100), nullable=False),
        sa.Column('status', sa.String(100), default="pending"),
        sa.Column('sent_at', sa.DateTime,nullable=False),
        sa.Column('created_at', sa.DateTime, default=sa.func.now()),
    )


def downgrade() -> None:
    pass
