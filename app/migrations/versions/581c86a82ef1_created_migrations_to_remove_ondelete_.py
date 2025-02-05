"""created migrations to remove ondelete cascade

Revision ID: 581c86a82ef1
Revises: fc47b3c21c28
Create Date: 2025-02-05 18:48:19.428516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '581c86a82ef1'
down_revision: Union[str, None] = 'fc47b3c21c28'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('core_focus_areas') as batch_op:
        batch_op.drop_constraint('core_focus_areas_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(
            'core_focus_areas_ibfk_1', 'users', ['user_id'], ['id']
        )

    with op.batch_alter_table('critical_activities') as batch_op:
        batch_op.drop_constraint('critical_activities_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(
            'critical_activities_ibfk_1', 'users', ['user_id'], ['id']
        )

        batch_op.drop_constraint('critical_activities_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(
            'critical_activities_ibfk_2', 'core_focus_areas', ['core_focus_area_id'], ['id']
        )


def downgrade() -> None:
    pass
