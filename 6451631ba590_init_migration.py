"""init migration

Revision ID: 6451631ba590
Revises: 57a9e7b8bafb
Create Date: 2024-10-20 15:53:24.601886

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6451631ba590'
down_revision: Union[str, None] = '57a9e7b8bafb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
