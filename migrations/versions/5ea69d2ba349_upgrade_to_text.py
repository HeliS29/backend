"""upgrade to text

Revision ID: 5ea69d2ba349
Revises: 3dc4da3c0c35
Create Date: 2025-01-02 12:26:41.700854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ea69d2ba349'
down_revision: Union[str, None] = '3dc4da3c0c35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('email_queue', 'body', type_=sa.Text, existing_type=sa.String(100), existing_nullable=False)



def downgrade() -> None:
    pass
