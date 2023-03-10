"""delivery fee

Revision ID: 7f49b1dbe8ef
Revises: 1db73cdab656
Create Date: 2022-12-30 21:19:51.877123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f49b1dbe8ef'
down_revision = '1db73cdab656'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service_orders', sa.Column('delivery_fee', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service_orders', 'delivery_fee')
    # ### end Alembic commands ###
