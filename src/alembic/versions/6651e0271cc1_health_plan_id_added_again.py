"""health plan id added again

Revision ID: 6651e0271cc1
Revises: e7bf635f187a
Create Date: 2022-06-25 16:56:33.654301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6651e0271cc1'
down_revision = 'e7bf635f187a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('health_plan_for_patient', sa.Column('health_plan_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('health_plan_for_patient', 'health_plan_id')
    # ### end Alembic commands ###
