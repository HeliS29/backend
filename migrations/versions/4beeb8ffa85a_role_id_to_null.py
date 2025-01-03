"""role id to null

Revision ID: 4beeb8ffa85a
Revises: 2edaa11a3514
Create Date: 2024-12-17 13:29:13.554740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4beeb8ffa85a'
down_revision: Union[str, None] = '2edaa11a3514'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




def upgrade() -> None:
    
  op.alter_column('users', sa.Column('role_id', sa.Integer(), sa.ForeignKey('user_roles.id'), nullable=True))