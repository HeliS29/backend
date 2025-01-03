"""added nullable true to tables

Revision ID: e89b5013dc04
Revises: 7507ff17eac2
Create Date: 2024-12-17 11:38:53.812770

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e89b5013dc04'
down_revision: Union[str, None] = '7507ff17eac2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('employees',
        sa.Column('job_title', sa.String(100), nullable=False)
    )
    op.add_column('employees',
        sa.Column('organisation_id', sa.String(100),sa.ForeignKey('organizations.id'), nullable=False)
    )


def downgrade() -> None:
    pass