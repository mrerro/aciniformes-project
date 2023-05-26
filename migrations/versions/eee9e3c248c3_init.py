"""init

Revision ID: eee9e3c248c3
Revises:
Create Date: 2023-05-26 23:03:15.247266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eee9e3c248c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('fetcher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.Enum('GET', 'POST', 'PING', name='fetchertype', native_enum=False), nullable=False),
    sa.Column('settings', sa.JSON(), nullable=False),
    sa.Column('delay_sec', sa.Float(), nullable=False),
    sa.Column('result', sa.Enum('STATUS_CODE', 'CONTENT_LENGTH', 'AVAILABLE', name='resulttype', native_enum=False), nullable=False),
    sa.Column('create_ts', sa.DateTime(), nullable=False),
    sa.Column('modify_ts', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('metric',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('create_ts', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('metric')
    op.drop_table('fetcher')
