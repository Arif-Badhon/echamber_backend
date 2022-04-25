"""schedule doctor user foreign key

Revision ID: f06505c96a4a
Revises: ab382f38dac2
Create Date: 2022-04-25 12:21:02.666351

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f06505c96a4a'
down_revision = 'ab382f38dac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctor_schedules', sa.Column('doctor_user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'doctor_schedules', 'users', ['doctor_user_id'], ['id'])
    op.drop_column('doctor_schedules', 'doctor_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctor_schedules', sa.Column('doctor_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'doctor_schedules', type_='foreignkey')
    op.drop_column('doctor_schedules', 'doctor_user_id')
    # ### end Alembic commands ###
