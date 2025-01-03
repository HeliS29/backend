"""zzzzz

Revision ID: 317ff54c9b5e
Revises: d597cea94e2d
Create Date: 2024-12-15 14:23:17.669327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '317ff54c9b5e'
down_revision: Union[str, None] = 'd597cea94e2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    

    op.create_table(
        'employees',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column('manager_id', sa.Integer, sa.ForeignKey("managers.id"), nullable=True),
        sa.Column('job_title', sa.String(100), nullable=False),
        sa.Column('organization_id', sa.Integer, sa.ForeignKey("organizations.id"), nullable=False),
        sa.Column('created_at', sa.DateTime, default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, default=sa.func.now(), onupdate=sa.func.now()),
    )
    


def downgrade() -> None:
    pass
