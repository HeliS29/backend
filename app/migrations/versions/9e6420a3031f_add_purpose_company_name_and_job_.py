"""Add purpose, company_name, and job_summary to User table

Revision ID: 9e6420a3031f
Revises: f912958e5173
Create Date: 2025-01-09 16:53:22.175337

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e6420a3031f'
down_revision: Union[str, None] = 'f912958e5173'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint('users_ibfk_1', 'users', type_='foreignkey')
    op.drop_column('users', 'organization_id')
    op.add_column('users', sa.Column('purpose', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('company_name', sa.String(length=100), nullable=True))
    op.alter_column('role_review', sa.Column('job_summary', sa.String(length=1000), nullable=False))


def downgrade() -> None:
    pass
