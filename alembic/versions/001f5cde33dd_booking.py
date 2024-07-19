"""booking

Revision ID: 001f5cde33dd
Revises: 1b4c19190cc2
Create Date: 2024-07-17 14:26:55.505775

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '001f5cde33dd'
down_revision: Union[str, None] = '1b4c19190cc2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('booking', sa.Column('total_price', sa.String(length=200), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('booking', 'total_price')
    # ### end Alembic commands ###
