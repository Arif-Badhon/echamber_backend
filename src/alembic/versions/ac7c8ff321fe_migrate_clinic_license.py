"""migrate clinic license

Revision ID: ac7c8ff321fe
Revises: def757c115ee
Create Date: 2022-11-19 13:37:58.295088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac7c8ff321fe'
down_revision = 'def757c115ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clinic', sa.Column('clinic_license', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clinic', 'clinic_license')
    # ### end Alembic commands ###
