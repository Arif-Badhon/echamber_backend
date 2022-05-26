"""payment status

Revision ID: 875619d22aaa
Revises: 1db275a0cf1c
Create Date: 2022-05-21 14:09:48.583825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '875619d22aaa'
down_revision = '1db275a0cf1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service_orders', sa.Column('payment_status', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service_orders', 'payment_status')
    # ### end Alembic commands ###