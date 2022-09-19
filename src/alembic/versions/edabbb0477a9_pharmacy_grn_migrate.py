"""pharmacy grn migrate

Revision ID: edabbb0477a9
Revises: 88f2ea3921bb
Create Date: 2022-09-19 10:33:43.097348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edabbb0477a9'
down_revision = '88f2ea3921bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pharmacy_grn',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('total_amount_dp', sa.Float(), nullable=True),
    sa.Column('grn_number', sa.String(length=100), nullable=True),
    sa.Column('total_amount_mrp', sa.Float(), nullable=True),
    sa.Column('total_vat_mrp', sa.Float(), nullable=True),
    sa.Column('total_discount_mrp', sa.Float(), nullable=True),
    sa.Column('total_cost_mrp', sa.Float(), nullable=True),
    sa.Column('pharmaceuticals_name_id', sa.Integer(), nullable=True),
    sa.Column('purchase_order_id', sa.Integer(), nullable=True),
    sa.Column('pharmacy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['pharmacy.id'], ),
    sa.ForeignKeyConstraint(['purchase_order_id'], ['pharmacy_purchase_order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pharmacy_single_grn',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('dp_prize', sa.Float(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('mrp', sa.Float(), nullable=True),
    sa.Column('vat', sa.Float(), nullable=True),
    sa.Column('discount', sa.Float(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('expiry_date', sa.Date(), nullable=True),
    sa.Column('batch_number', sa.String(length=100), nullable=True),
    sa.Column('grn_id', sa.Integer(), nullable=True),
    sa.Column('medicine_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['grn_id'], ['pharmacy_grn.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pharmacy_single_grn')
    op.drop_table('pharmacy_grn')
    # ### end Alembic commands ###
