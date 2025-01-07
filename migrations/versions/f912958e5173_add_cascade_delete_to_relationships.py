"""Add cascade delete to relationships

Revision ID: f912958e5173
Revises: 5ea69d2ba349
Create Date: 2025-01-07 11:00:31.859498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f912958e5173'
down_revision: Union[str, None] = '5ea69d2ba349'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint('critical_activities_ibfk_2', 'critical_activities', type_='foreignkey')

    # Add a new foreign key constraint with ON DELETE CASCADE
    op.create_foreign_key(
        'critical_activities_ibfk_2',  # Name of the foreign key
        source_table='critical_activities',
        referent_table='core_focus_areas',
        local_cols=['core_focus_area_id'],  # Column in the source table
        remote_cols=['id'],  # Column in the target table
        ondelete='CASCADE'  # Add ON DELETE CASCADE behavior
    )


def downgrade() -> None:
    pass
