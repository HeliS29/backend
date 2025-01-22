"""Added organization_id to Manager table

Revision ID: ddfe6ce5d81f
Revises: 09d04f19963b
Create Date: 2025-01-21 11:02:50.930730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ddfe6ce5d81f'
down_revision: Union[str, None] = '09d04f19963b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass
    # Add the foreign key constraint to the 'organization_id' column
    
    


def downgrade() -> None:
    pass
