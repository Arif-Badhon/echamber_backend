"""invoice table and purchase order mrp added

Revision ID: 94a310b050ff
Revises: ba4d6da2d703
Create Date: 2022-10-06 16:24:42.138618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94a310b050ff'
down_revision = 'ba4d6da2d703'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pharmacy_invoice',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('subtotal_amount', sa.Float(), nullable=True),
    sa.Column('total_amount_mrp', sa.Float(), nullable=True),
    sa.Column('total_amount', sa.Float(), nullable=True),
    sa.Column('paid_amount', sa.Float(), nullable=True),
    sa.Column('due_amount', sa.Float(), nullable=True),
    sa.Column('remarks', sa.Text(), nullable=True),
    sa.Column('discount', sa.Float(), nullable=True),
    sa.Column('vat', sa.Float(), nullable=True),
    sa.Column('invoice_number', sa.String(length=100), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('pharmacy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['pharmacy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pharmacy_single_invoice',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('mrp', sa.Float(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('unit_prize', sa.Float(), nullable=True),
    sa.Column('discount', sa.Float(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('medicine_id', sa.Integer(), nullable=False),
    sa.Column('invoice_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['invoice_id'], ['pharmacy_invoice.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pharmacy_purchase_single_order', sa.Column('total_price_dp', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pharmacy_purchase_single_order', 'total_price_dp')
    op.drop_table('pharmacy_single_invoice')
    op.drop_table('pharmacy_invoice')
    # ### end Alembic commands ###
