"""service and medicine order name hange

Revision ID: d4d29b8d5923
Revises: 27b558cf145c
Create Date: 2022-06-11 13:07:17.424242

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd4d29b8d5923'
down_revision = '27b558cf145c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medicine_orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service_orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('discount_percent', sa.Integer(), nullable=False),
    sa.Column('service_provider_type', sa.String(length=100), nullable=True),
    sa.Column('service_provider_id', sa.Integer(), nullable=True),
    sa.Column('service_provider_fee', sa.Integer(), nullable=True),
    sa.Column('service_provider_fee_paid', sa.Integer(), nullable=True),
    sa.Column('service_provider_fee_pending', sa.Integer(), nullable=True),
    sa.Column('service_provider_fee_last_update', sa.DateTime(), nullable=True),
    sa.Column('service_provider_fee_status', sa.String(length=100), nullable=True),
    sa.Column('referral_type', sa.String(length=100), nullable=True),
    sa.Column('referral_id', sa.Integer(), nullable=True),
    sa.Column('referral_provider_fee', sa.Integer(), nullable=True),
    sa.Column('referral_provider_fee_paid', sa.Integer(), nullable=True),
    sa.Column('referral_provider_fee_pending', sa.Integer(), nullable=True),
    sa.Column('referral_provider_fee_last_update', sa.DateTime(), nullable=True),
    sa.Column('referral_provider_fee_status', sa.String(length=100), nullable=True),
    sa.Column('current_address', sa.String(length=255), nullable=True),
    sa.Column('remarks', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('service_order')
    op.drop_table('medicine_order_list')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medicine_order_list',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('service_order',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('discount_percent', mysql.INTEGER(), autoincrement=False, nullable=False),
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
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('service_orders')
    op.drop_table('medicine_orders')
    # ### end Alembic commands ###
