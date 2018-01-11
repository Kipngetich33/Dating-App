"""add user_id column to messages

Revision ID: e46f3a4cdfcd
Revises: d3a581644a4d
Create Date: 2018-01-11 12:43:37.592727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e46f3a4cdfcd'
down_revision = 'd3a581644a4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('sender_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'sender_id')
    # ### end Alembic commands ###