"""empty message

Revision ID: 8580b596a1b9
Revises: 6a37d53e8c63
Create Date: 2020-08-07 21:54:09.409251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8580b596a1b9'
down_revision = '6a37d53e8c63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portfolio', sa.Column('staff_username', sa.String(), nullable=True))
    op.create_foreign_key(None, 'portfolio', 'staff', ['staff_username'], ['username'])
    op.create_unique_constraint('unique_username', 'staff', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_username', 'staff', type_='unique')
    op.drop_constraint(None, 'portfolio', type_='foreignkey')
    op.drop_column('portfolio', 'staff_username')
    # ### end Alembic commands ###
