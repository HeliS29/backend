"""updated user table

Revision ID: 2edaa11a3514
Revises: e89b5013dc04
Create Date: 2024-12-17 13:18:20.024198

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2edaa11a3514'
down_revision: Union[str, None] = 'e89b5013dc04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', sa.Column('role_id', sa.Integer(), sa.ForeignKey('user_roles.id'), nullable=True))
    
    # Add organization_id column
    op.add_column('users', sa.Column('organization_id', sa.Integer(), sa.ForeignKey('organizations.id'), nullable=True))

    # Add job_title column
    op.add_column('users', sa.Column('job_title', sa.String(50), nullable=True))

    # Add manager_id column
    op.add_column('users', sa.Column('manager_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=True))


def downgrade() -> None:
    pass
