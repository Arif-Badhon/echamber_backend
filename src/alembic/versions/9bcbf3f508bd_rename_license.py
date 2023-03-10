"""rename license

Revision ID: 9bcbf3f508bd
Revises: 38aa7af03632
Create Date: 2022-09-20 16:19:24.966512

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9bcbf3f508bd'
down_revision = '38aa7af03632'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pharmacy', sa.Column('trade_license', sa.String(length=255), nullable=False))
    op.add_column('pharmacy', sa.Column('drug_license', sa.String(length=255), nullable=True))
    op.drop_column('pharmacy', 'trade_lisence')
    op.drop_column('pharmacy', 'drug_lisence')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pharmacy', sa.Column('drug_lisence', mysql.VARCHAR(length=255), nullable=True))
    op.add_column('pharmacy', sa.Column('trade_lisence', mysql.VARCHAR(length=255), nullable=False))
    op.drop_column('pharmacy', 'drug_license')
    op.drop_column('pharmacy', 'trade_license')
    # ### end Alembic commands ###
