"""all table for eprescriptions

Revision ID: 135d4b051afd
Revises: 06dc8af4fd8e
Create Date: 2022-08-02 16:10:05.608456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '135d4b051afd'
down_revision = '06dc8af4fd8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eprescriptions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('cause_of_consultation', sa.String(length=255), nullable=True),
    sa.Column('telemedicine_order_id', sa.Integer(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('current_address', sa.Text(), nullable=True),
    sa.Column('remarks', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_advices',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ep_id', sa.Integer(), nullable=True),
    sa.Column('advice', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['ep_id'], ['eprescriptions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_chief_complaints',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ep_id', sa.Integer(), nullable=True),
    sa.Column('chief_complaints', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['ep_id'], ['eprescriptions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_co_morbidity',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ep_id', sa.Integer(), nullable=True),
    sa.Column('cm_type', sa.String(length=255), nullable=False),
    sa.Column('remarks', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['ep_id'], ['eprescriptions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_diagnosis',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ep_id', sa.Integer(), nullable=True),
    sa.Column('diagnosis_type', sa.String(length=255), nullable=False),
    sa.Column('diagnosis', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['ep_id'], ['eprescriptions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_doctor_refer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ep_id', sa.Integer(), nullable=True),
    sa.Column('detail', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['ep_id'], ['eprescriptions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_histories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ep_id', sa.Integer(), nullable=True),
    sa.Column('history_type', sa.String(length=255), nullable=False),
    sa.Column('history', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['ep_id'], ['eprescriptions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_investigations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ep_id', sa.Integer(), nullable=True),
    sa.Column('investigation', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['ep_id'], ['eprescriptions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_medicines',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ep_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('generic', sa.String(length=255), nullable=False),
    sa.Column('form', sa.String(length=255), nullable=False),
    sa.Column('strength', sa.String(length=255), nullable=False),
    sa.Column('doses', sa.String(length=100), nullable=True),
    sa.Column('after_meal', sa.Boolean(), nullable=True),
    sa.Column('days', sa.Integer(), nullable=True),
    sa.Column('remarks', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['ep_id'], ['eprescriptions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_next_follow_up',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ep_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['ep_id'], ['eprescriptions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ep_on_examinations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ep_id', sa.Integer(), nullable=True),
    sa.Column('patient_indicator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ep_id'], ['eprescriptions.id'], ),
    sa.ForeignKeyConstraint(['patient_indicator_id'], ['patient_indicators.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ep_on_examinations')
    op.drop_table('ep_next_follow_up')
    op.drop_table('ep_medicines')
    op.drop_table('ep_investigations')
    op.drop_table('ep_histories')
    op.drop_table('ep_doctor_refer')
    op.drop_table('ep_diagnosis')
    op.drop_table('ep_co_morbidity')
    op.drop_table('ep_chief_complaints')
    op.drop_table('ep_advices')
    op.drop_table('eprescriptions')
    # ### end Alembic commands ###
