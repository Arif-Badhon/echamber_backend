"""doctor all fees

Revision ID: 1db73cdab656
Revises: 472f2568b3dd
Create Date: 2022-11-30 17:33:42.539505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1db73cdab656'
down_revision = '472f2568b3dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctors', sa.Column('online_healthx_fees', sa.Float(), nullable=True))
    op.add_column('doctors', sa.Column('online_vat', sa.Float(), nullable=True))
    op.add_column('doctors', sa.Column('online_total_fees', sa.Float(), nullable=True))
    op.add_column('doctors', sa.Column('followup_fees', sa.Float(), nullable=True))
    op.add_column('doctors', sa.Column('followup_healthx_fees', sa.Float(), nullable=True))
    op.add_column('doctors', sa.Column('followup_vat', sa.Float(), nullable=True))
    op.add_column('doctors', sa.Column('followup_total_fees', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('doctors', 'followup_total_fees')
    op.drop_column('doctors', 'followup_vat')
    op.drop_column('doctors', 'followup_healthx_fees')
    op.drop_column('doctors', 'followup_fees')
    op.drop_column('doctors', 'online_total_fees')
    op.drop_column('doctors', 'online_vat')
    op.drop_column('doctors', 'online_healthx_fees')
    # ### end Alembic commands ###
