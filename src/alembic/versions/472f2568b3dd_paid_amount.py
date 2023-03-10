"""paid amount

Revision ID: 472f2568b3dd
Revises: ab98dc3782e2
Create Date: 2022-11-29 11:58:38.622453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '472f2568b3dd'
down_revision = 'ab98dc3782e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pharmacy_grn', sa.Column('discount_amount', sa.Float(), nullable=True))
    op.add_column('pharmacy_invoice', sa.Column('discount_amount', sa.Float(), nullable=True))
    op.add_column('pharmacy_purchase_order', sa.Column('discount_amount', sa.Float(), nullable=True))
    op.add_column('pharmacy_purchase_single_order', sa.Column('discount_amount', sa.Float(), nullable=True))
    op.add_column('pharmacy_single_grn', sa.Column('discount_amount', sa.Float(), nullable=True))
    op.add_column('pharmacy_single_invoice', sa.Column('discount_amount', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pharmacy_single_invoice', 'discount_amount')
    op.drop_column('pharmacy_single_grn', 'discount_amount')
    op.drop_column('pharmacy_purchase_single_order', 'discount_amount')
    op.drop_column('pharmacy_purchase_order', 'discount_amount')
    op.drop_column('pharmacy_invoice', 'discount_amount')
    op.drop_column('pharmacy_grn', 'discount_amount')
    # ### end Alembic commands ###
