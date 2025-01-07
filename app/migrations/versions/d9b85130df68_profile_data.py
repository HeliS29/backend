"""profile data

Revision ID: d9b85130df68
Revises: d88fb93e2539
Create Date: 2024-12-15 12:45:38.581802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9b85130df68'
down_revision: Union[str, None] = 'd88fb93e2539'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
