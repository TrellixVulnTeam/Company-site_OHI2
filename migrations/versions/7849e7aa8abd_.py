"""empty message

Revision ID: 7849e7aa8abd
Revises: d01b13b4f4be
Create Date: 2020-08-07 20:50:50.938207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7849e7aa8abd'
down_revision = 'd01b13b4f4be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('staff', sa.Column('full_name', sa.String(), nullable=False))
    op.add_column('staff', sa.Column('image', sa.String(), nullable=False))
    op.add_column('staff', sa.Column('role', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('staff', 'role')
    op.drop_column('staff', 'image')
    op.drop_column('staff', 'full_name')
    # ### end Alembic commands ###
