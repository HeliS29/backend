"""add_isEmail_VersionTable

Revision ID: d656dc470519
Revises: 581c86a82ef1
Create Date: 2025-02-07 10:12:41.238221

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd656dc470519'
down_revision: Union[str, None] = '581c86a82ef1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("report_versions", sa.Column("is_email", sa.Boolean(), nullable=False, server_default=sa.false()))


def downgrade() -> None:
    pass
