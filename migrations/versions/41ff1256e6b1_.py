"""empty message

Revision ID: 41ff1256e6b1
Revises: 
Create Date: 2021-10-03 18:29:13.212752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41ff1256e6b1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diversity_submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('contact', sa.String(length=64), nullable=True),
    sa.Column('body', sa.String(length=2000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_diversity_submission_timestamp'), 'diversity_submission', ['timestamp'], unique=False)
    op.create_table('hazard_submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('contact', sa.String(length=64), nullable=True),
    sa.Column('body', sa.String(length=2000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hazard_submission_timestamp'), 'hazard_submission', ['timestamp'], unique=False)
    op.create_table('mental_submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('contact', sa.String(length=64), nullable=True),
    sa.Column('body', sa.String(length=2000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mental_submission_timestamp'), 'mental_submission', ['timestamp'], unique=False)
    op.create_table('misc_submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('contact', sa.String(length=64), nullable=True),
    sa.Column('body', sa.String(length=2000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_misc_submission_timestamp'), 'misc_submission', ['timestamp'], unique=False)
    op.create_table('physical_submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('contact', sa.String(length=64), nullable=True),
    sa.Column('body', sa.String(length=2000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_physical_submission_timestamp'), 'physical_submission', ['timestamp'], unique=False)
    op.create_table('resource_submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('contact', sa.String(length=64), nullable=True),
    sa.Column('body', sa.String(length=2000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_resource_submission_timestamp'), 'resource_submission', ['timestamp'], unique=False)
    op.create_table('resources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=64), nullable=True),
    sa.Column('desc', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('resources')
    op.drop_index(op.f('ix_resource_submission_timestamp'), table_name='resource_submission')
    op.drop_table('resource_submission')
    op.drop_index(op.f('ix_physical_submission_timestamp'), table_name='physical_submission')
    op.drop_table('physical_submission')
    op.drop_index(op.f('ix_misc_submission_timestamp'), table_name='misc_submission')
    op.drop_table('misc_submission')
    op.drop_index(op.f('ix_mental_submission_timestamp'), table_name='mental_submission')
    op.drop_table('mental_submission')
    op.drop_index(op.f('ix_hazard_submission_timestamp'), table_name='hazard_submission')
    op.drop_table('hazard_submission')
    op.drop_index(op.f('ix_diversity_submission_timestamp'), table_name='diversity_submission')
    op.drop_table('diversity_submission')
    # ### end Alembic commands ###