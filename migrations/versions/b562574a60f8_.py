"""empty message

Revision ID: b562574a60f8
Revises: 2c5b323deb59
Create Date: 2017-03-11 14:34:10.788139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b562574a60f8'
down_revision = '2c5b323deb59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('subject', sa.String(), nullable=True))
    op.drop_column('tasks', 'data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('data', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('tasks', 'subject')
    # ### end Alembic commands ###