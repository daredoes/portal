"""Add public settings

Revision ID: 43cf0405718b
Revises: 
Create Date: 2017-10-24 21:44:19.403951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43cf0405718b'
down_revision = None
branch_labels = ('portal',)
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portal_category', sa.Column('public', sa.Boolean(), server_default='True', nullable=False))
    op.add_column('portal_item', sa.Column('public', sa.Boolean(), server_default='True', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('portal_item', 'public')
    op.drop_column('portal_category', 'public')
    # ### end Alembic commands ###
