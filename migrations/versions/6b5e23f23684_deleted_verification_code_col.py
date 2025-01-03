"""deleted verification code col

Revision ID: 6b5e23f23684
Revises: 4beeb8ffa85a
Create Date: 2024-12-17 14:13:14.420169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b5e23f23684'
down_revision: Union[str, None] = '4beeb8ffa85a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.drop_column('users', 'verification_code')

def downgrade() -> None:
    pass
