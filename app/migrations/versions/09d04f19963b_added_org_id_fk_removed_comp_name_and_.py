"""added org id fk,removed comp name and created admin table

Revision ID: 09d04f19963b
Revises: 64dc11093013
Create Date: 2025-01-21 10:45:24.419648

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09d04f19963b'
down_revision: Union[str, None] = '64dc11093013'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    

    # Drop company_name column from users table
    pass

    # Create admin table
    


def downgrade() -> None:
    pass
