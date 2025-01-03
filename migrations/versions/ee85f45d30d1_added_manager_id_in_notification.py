"""added manager_id in notification

Revision ID: ee85f45d30d1
Revises: 1e1da45ae7b6
Create Date: 2024-12-20 17:18:51.071350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee85f45d30d1'
down_revision: Union[str, None] = '1e1da45ae7b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
