"""doctor speciality column add again 2

Revision ID: af22fb6a7080
Revises: 22f4aadcdb39
Create Date: 2022-08-31 10:36:21.260790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af22fb6a7080'
down_revision = '22f4aadcdb39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctor_specialities', sa.Column('speciality', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('doctor_specialities', 'speciality')
    # ### end Alembic commands ###
