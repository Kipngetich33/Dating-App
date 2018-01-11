"""add messages to user model

Revision ID: 84265e2f333e
Revises: 24f3b7a553c0
Create Date: 2018-01-10 10:44:00.572895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84265e2f333e'
down_revision = '24f3b7a553c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('messages', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'messages')
    # ### end Alembic commands ###