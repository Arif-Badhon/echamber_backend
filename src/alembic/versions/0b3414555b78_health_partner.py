"""health partner

Revision ID: 0b3414555b78
Revises: 90cd0a4dc37e
Create Date: 2022-05-17 16:28:27.565552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b3414555b78'
down_revision = '90cd0a4dc37e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('health_partner',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('district', sa.String(length=50), nullable=False),
    sa.Column('detail_address', sa.String(length=255), nullable=True),
    sa.Column('detail', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('contact_person', sa.String(length=255), nullable=False),
    sa.Column('contact_person_phone', sa.String(length=100), nullable=False),
    sa.Column('contact_person_email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('health_partner')
    # ### end Alembic commands ###
