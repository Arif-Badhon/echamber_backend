"""am pm for doctor schedule

Revision ID: 88f2ea3921bb
Revises: 1d0a99498c9f
Create Date: 2022-09-18 11:33:25.920534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88f2ea3921bb'
down_revision = '1d0a99498c9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctor_schedules', sa.Column('am_pm', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('doctor_schedules', 'am_pm')
    # ### end Alembic commands ###
