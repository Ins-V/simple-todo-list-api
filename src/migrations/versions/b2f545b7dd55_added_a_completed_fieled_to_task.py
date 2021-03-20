"""Added a completed fieled to task.

Revision ID: b2f545b7dd55
Revises: 577b8a105f71
Create Date: 2021-03-20 20:48:40.268290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2f545b7dd55'
down_revision = '577b8a105f71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'completed')
    # ### end Alembic commands ###
