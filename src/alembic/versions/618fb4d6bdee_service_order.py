"""service order

Revision ID: 618fb4d6bdee
Revises: 38e4b0fd0e4a
Create Date: 2022-05-19 00:38:03.265816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '618fb4d6bdee'
down_revision = '38e4b0fd0e4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service_orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('service_name', sa.String(length=100), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('order_placement', sa.Date(), nullable=False),
    sa.Column('order_completion', sa.Date(), nullable=False),
    sa.Column('order_value', sa.Integer(), nullable=True),
    sa.Column('discount_percent', sa.Integer(), nullable=True),
    sa.Column('payable_amount', sa.Integer(), nullable=False),
    sa.Column('payment_customer', sa.Integer(), nullable=False),
    sa.Column('payment_pending', sa.Integer(), nullable=False),
    sa.Column('payment_date', sa.Date(), nullable=False),
    sa.Column('payment_method', sa.String(length=100), nullable=True),
    sa.Column('service_provider_type', sa.String(length=100), nullable=True),
    sa.Column('service_provider_id', sa.Integer(), nullable=True),
    sa.Column('service_provider_fee', sa.Integer(), nullable=True),
    sa.Column('service_provider_fee_paid', sa.Integer(), nullable=True),
    sa.Column('service_provider_fee_pending', sa.Integer(), nullable=True),
    sa.Column('service_provider_fee_status', sa.String(length=100), nullable=True),
    sa.Column('referral_type', sa.String(length=100), nullable=True),
    sa.Column('referral_id', sa.Integer(), nullable=True),
    sa.Column('referral_provider_fee', sa.Integer(), nullable=True),
    sa.Column('referral_provider_fee_paid', sa.Integer(), nullable=True),
    sa.Column('referral_provider_fee_pending', sa.Integer(), nullable=True),
    sa.Column('referral_provider_fee_status', sa.String(length=100), nullable=True),
    sa.Column('current_address', sa.String(length=255), nullable=True),
    sa.Column('remarks', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service_orders')
    # ### end Alembic commands ###