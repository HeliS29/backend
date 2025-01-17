"""Change job_summary column type from String to Text

Revision ID: 64dc11093013
Revises: 4a28fc23527c
Create Date: 2025-01-10 11:20:58.434211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64dc11093013'
down_revision: Union[str, None] = '4a28fc23527c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('role_review', 'job_summary',
                    type_=sa.Text(),  # Set column type to Text
                    existing_type=sa.String(),  # Existing type is String
                    nullable=False)


def downgrade() -> None:
    pass
