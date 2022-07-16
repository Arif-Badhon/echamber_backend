"""review visibility

Revision ID: 29d93a4016ac
Revises: b17f69db55ab
Create Date: 2022-07-16 17:55:30.616982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29d93a4016ac'
down_revision = 'b17f69db55ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('review', sa.Column('visible', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('review', 'visible')
    op.drop_column('review', 'user_id')
    # ### end Alembic commands ###
