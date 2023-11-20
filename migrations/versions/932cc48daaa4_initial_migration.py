"""Initial migration

Revision ID: 932cc48daaa4
Revises: b88f59a4e324
Create Date: 2023-11-20 16:18:22.308703

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '932cc48daaa4'
down_revision = 'b88f59a4e324'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rooms_bookings')
    op.drop_table('bookings')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookings',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('bookings_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('is_real', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('time_made', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('start_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('end_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('check_in', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('inclusions', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('guest_info', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('has_pets', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('room_info', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('property_info', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('status', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('seen_by_host', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('messages', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('review_ratings', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('review_reply', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('property_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['property_id'], ['properties.id'], name='bookings_property_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='bookings_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='bookings_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('rooms_bookings',
    sa.Column('room_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('booking_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['booking_id'], ['bookings.id'], name='rooms_bookings_booking_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], name='rooms_bookings_room_id_fkey', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('room_id', 'booking_id', name='rooms_bookings_pkey')
    )
    # ### end Alembic commands ###