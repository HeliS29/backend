"""profile data last datasss

Revision ID: bc8b3e81dc71
Revises: 06508d53798b
Create Date: 2024-12-15 12:51:29.524127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc8b3e81dc71'
down_revision: Union[str, None] = '06508d53798b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
