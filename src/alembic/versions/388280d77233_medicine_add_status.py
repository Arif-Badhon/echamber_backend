"""medicine add status

Revision ID: 388280d77233
Revises: fbb0759c9f23
Create Date: 2022-08-06 10:05:55.357128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '388280d77233'
down_revision = 'fbb0759c9f23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ep_medicine_list', sa.Column('add_status', sa.String(length=100), nullable=True))
    op.add_column('ep_medicine_list', sa.Column('added_by_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ep_medicine_list', 'added_by_id')
    op.drop_column('ep_medicine_list', 'add_status')
    # ### end Alembic commands ###
