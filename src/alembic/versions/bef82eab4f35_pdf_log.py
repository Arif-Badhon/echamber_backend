"""pdf log

Revision ID: bef82eab4f35
Revises: b872b604b3e2
Create Date: 2022-05-31 17:56:07.040921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bef82eab4f35'
down_revision = 'b872b604b3e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pdf_log',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('service_name', sa.String(length=100), nullable=True),
    sa.Column('pdf_string', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pdf_log')
    # ### end Alembic commands ###