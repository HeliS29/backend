"""added email tables

Revision ID: 1e1da45ae7b6
Revises: 54959da9be1d
Create Date: 2024-12-20 16:24:54.695351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e1da45ae7b6'
down_revision: Union[str, None] = '54959da9be1d'
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
