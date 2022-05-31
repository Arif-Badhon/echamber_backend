"""family relation with

Revision ID: 078e6cd0db5b
Revises: 790ce274d248
Create Date: 2022-05-30 16:16:39.750184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '078e6cd0db5b'
down_revision = '790ce274d248'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient_families', sa.Column('relation_from', sa.String(length=100), nullable=True))
    op.add_column('patient_families', sa.Column('relation_to', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patient_families', 'relation_to')
    op.drop_column('patient_families', 'relation_from')
    # ### end Alembic commands ###
