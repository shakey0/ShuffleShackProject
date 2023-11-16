"""Rooms added

Revision ID: 8eab8ddc5180
Revises: e84e5cf8428a
Create Date: 2023-11-16 21:48:54.225822

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8eab8ddc5180'
down_revision = 'e84e5cf8428a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=30), nullable=True))
        batch_op.add_column(sa.Column('last_name', sa.String(length=30), nullable=True))
        batch_op.add_column(sa.Column('user_name', sa.String(length=30), nullable=True))
        batch_op.add_column(sa.Column('phone_number', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('password', postgresql.BYTEA(), nullable=True))
        batch_op.add_column(sa.Column('d_o_b', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('nationality', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('t_bookings', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('no_shows', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('guest_complaints', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('host_complaints', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=60),
               existing_nullable=True)
        batch_op.drop_index('ix_users_email')
        batch_op.drop_index('ix_users_username')
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.create_unique_constraint(None, ['user_name'])
        batch_op.create_unique_constraint(None, ['phone_number'])
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_index('ix_users_username', ['username'], unique=False)
        batch_op.create_index('ix_users_email', ['email'], unique=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)
        batch_op.drop_column('is_admin')
        batch_op.drop_column('host_complaints')
        batch_op.drop_column('guest_complaints')
        batch_op.drop_column('no_shows')
        batch_op.drop_column('t_bookings')
        batch_op.drop_column('nationality')
        batch_op.drop_column('d_o_b')
        batch_op.drop_column('password')
        batch_op.drop_column('phone_number')
        batch_op.drop_column('user_name')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###
