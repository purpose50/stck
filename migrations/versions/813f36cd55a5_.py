"""empty message

Revision ID: 813f36cd55a5
Revises: 7f02c862b110
Create Date: 2018-09-11 17:43:29.648610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '813f36cd55a5'
down_revision = '7f02c862b110'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('body', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'body')
    # ### end Alembic commands ###
