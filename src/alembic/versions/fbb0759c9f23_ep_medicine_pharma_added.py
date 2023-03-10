"""ep medicine pharma added

Revision ID: fbb0759c9f23
Revises: 135d4b051afd
Create Date: 2022-08-03 14:51:01.075212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbb0759c9f23'
down_revision = '135d4b051afd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ep_medicines', sa.Column('pharmaceuticals', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ep_medicines', 'pharmaceuticals')
    # ### end Alembic commands ###
