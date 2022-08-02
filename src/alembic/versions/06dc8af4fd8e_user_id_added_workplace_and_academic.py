"""user id added workplace and academic

Revision ID: 06dc8af4fd8e
Revises: 5d3d1b728da8
Create Date: 2022-08-02 11:41:08.822559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06dc8af4fd8e'
down_revision = '5d3d1b728da8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctor_academic_info', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'doctor_academic_info', 'users', ['user_id'], ['id'])
    op.add_column('doctor_workplace', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'doctor_workplace', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'doctor_workplace', type_='foreignkey')
    op.drop_column('doctor_workplace', 'user_id')
    op.drop_constraint(None, 'doctor_academic_info', type_='foreignkey')
    op.drop_column('doctor_academic_info', 'user_id')
    # ### end Alembic commands ###
