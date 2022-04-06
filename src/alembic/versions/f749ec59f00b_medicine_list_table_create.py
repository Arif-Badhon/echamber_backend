"""medicine_list table create

Revision ID: f749ec59f00b
Revises: 6ca0f83d3545
Create Date: 2022-04-04 13:15:40.195689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f749ec59f00b'
down_revision = '6ca0f83d3545'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ep_medicine_list',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('generic', sa.String(length=255), nullable=False),
    sa.Column('form', sa.String(length=255), nullable=False),
    sa.Column('strength', sa.String(length=255), nullable=False),
    sa.Column('pharmaceuticals', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ep_medicine_list')
    # ### end Alembic commands ###