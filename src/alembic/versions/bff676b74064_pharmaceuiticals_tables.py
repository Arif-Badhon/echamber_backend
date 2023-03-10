"""pharmaceuiticals tables

Revision ID: bff676b74064
Revises: 37f2938a95cb
Create Date: 2022-08-23 10:51:28.404809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bff676b74064'
down_revision = '37f2938a95cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pharmaceuticals',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('established', sa.String(length=255), nullable=True),
    sa.Column('details', sa.Text(), nullable=True),
    sa.Column('contact_phone', sa.String(length=255), nullable=True),
    sa.Column('contact_email', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('total_generics', sa.Integer(), nullable=True),
    sa.Column('total_brands', sa.Integer(), nullable=True),
    sa.Column('contact_person', sa.String(length=255), nullable=True),
    sa.Column('contact_person_phone', sa.String(length=255), nullable=True),
    sa.Column('contact_person_email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pharmavceuticals_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('phr_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['phr_id'], ['pharmaceuticals.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pharmavceuticals_user')
    op.drop_table('pharmaceuticals')
    # ### end Alembic commands ###
