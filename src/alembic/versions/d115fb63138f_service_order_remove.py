"""service order remove

Revision ID: d115fb63138f
Revises: a5f6af9e1aac
Create Date: 2022-06-08 13:13:31.868248

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd115fb63138f'
down_revision = 'a5f6af9e1aac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service_orders')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service_orders',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('service_name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('patient_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('order_placement', mysql.DATETIME(), nullable=False),
    sa.Column('order_completion', mysql.DATETIME(), nullable=False),
    sa.Column('order_value', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('discount_percent', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('payable_amount', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('payment_customer', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('payment_pending', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('payment_date', mysql.DATETIME(), nullable=False),
    sa.Column('payment_method', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('service_provider_type', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('service_provider_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('service_provider_fee', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('service_provider_fee_paid', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('service_provider_fee_pending', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('service_provider_fee_last_update', mysql.DATETIME(), nullable=True),
    sa.Column('service_provider_fee_status', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('referral_type', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('referral_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('referral_provider_fee', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('referral_provider_fee_paid', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('referral_provider_fee_pending', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('referral_provider_fee_last_update', mysql.DATETIME(), nullable=True),
    sa.Column('referral_provider_fee_status', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('current_address', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('remarks', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('payment_status', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
