"""medicine order with float

Revision ID: c9c808c4de7f
Revises: 08bc362a6c4e
Create Date: 2022-06-16 10:15:41.282581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9c808c4de7f'
down_revision = '08bc362a6c4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medicine_orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('service_order_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('generic', sa.String(length=100), nullable=True),
    sa.Column('form', sa.String(length=100), nullable=True),
    sa.Column('strength', sa.String(length=100), nullable=True),
    sa.Column('pharmaceuticals', sa.String(length=100), nullable=True),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('unit_price_tp', sa.Float(), nullable=True),
    sa.Column('unit_price_mrp', sa.Float(), nullable=False),
    sa.Column('unit_discount_percent', sa.Float(), nullable=False),
    sa.Column('total', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medicine_orders')
    # ### end Alembic commands ###
