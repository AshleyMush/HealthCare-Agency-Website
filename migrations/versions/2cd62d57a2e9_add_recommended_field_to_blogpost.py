"""Add recommended field to BlogPost

Revision ID: 2cd62d57a2e9
Revises: 0c47e7bd58a4
Create Date: 2024-10-06 18:24:37.995308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cd62d57a2e9'
down_revision = '0c47e7bd58a4'
branch_labels = None
depends_on = None



def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('BlogPost') as batch_op:
        batch_op.add_column(sa.Column('recommended', sa.Boolean(), nullable=False, server_default=sa.false()))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('BlogPost') as batch_op:
        batch_op.drop_column('recommended')
    # ### end Alembic commands ###