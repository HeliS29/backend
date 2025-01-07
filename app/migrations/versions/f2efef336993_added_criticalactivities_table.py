"""added criticalactivities table

Revision ID: f2efef336993
Revises: 840f7105b93c
Create Date: 2024-12-18 09:48:35.479253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2efef336993'
down_revision: Union[str, None] = '840f7105b93c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('critical_activities',
        sa.Column('core_focus_area_id',sa.Integer, sa.ForeignKey("core_focus_areas.id", ondelete="CASCADE"), nullable=False)
    )
        


def downgrade() -> None:
    pass
