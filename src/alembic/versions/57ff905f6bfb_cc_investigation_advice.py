"""cc_investigation_advice

Revision ID: 57ff905f6bfb
Revises: 28c53382e2c3
Create Date: 2022-03-19 21:55:03.008482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57ff905f6bfb'
down_revision = '28c53382e2c3'
branch_labels = None
depends_on = None

# fmt: off

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ep_advice_list',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('advice', sa.String(length=255), nullable=False),
    sa.Column('inserted_by', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_chief_complaints_list',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('cc', sa.String(length=255), nullable=False),
    sa.Column('inserted_by', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_investigation_list',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('investigation', sa.String(length=255), nullable=False),
    sa.Column('inserted_by', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ep_investigation_list')
    op.drop_table('ep_chief_complaints_list')
    op.drop_table('ep_advice_list')
    # ### end Alembic commands ###