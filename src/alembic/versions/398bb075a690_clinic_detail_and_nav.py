"""clinic detail and nav

Revision ID: 398bb075a690
Revises: 51ffe9c5872e
Create Date: 2022-10-19 17:08:33.425392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '398bb075a690'
down_revision = '51ffe9c5872e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clinic_details',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('clinic_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('sub_title', sa.Text(), nullable=True),
    sa.Column('title_bg_image_id', sa.Integer(), nullable=True),
    sa.Column('about', sa.Text(), nullable=False),
    sa.Column('about_image_id', sa.Integer(), nullable=True),
    sa.Column('contuct_us', sa.Text(), nullable=True),
    sa.Column('footer', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['clinic_id'], ['clinic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clinic_navbar',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('clinic_id', sa.Integer(), nullable=True),
    sa.Column('nav_text', sa.String(length=255), nullable=True),
    sa.Column('nav_href', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['clinic_id'], ['clinic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clinic_navbar')
    op.drop_table('clinic_details')
    # ### end Alembic commands ###