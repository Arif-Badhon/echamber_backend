"""add: blood_group in ep table

Revision ID: 4292b7f37caf
Revises: 408364b6a3fa
Create Date: 2023-01-11 13:38:09.664654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4292b7f37caf'
down_revision = '408364b6a3fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('eprescriptions', sa.Column('blood_group', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('eprescriptions', 'blood_group')
    # ### end Alembic commands ###
