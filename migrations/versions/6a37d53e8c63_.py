"""empty message

Revision ID: 6a37d53e8c63
Revises: a08dcb811e3b
Create Date: 2020-08-07 21:46:35.734121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a37d53e8c63'
down_revision = 'a08dcb811e3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portfolio', sa.Column('staff_username', sa.String(), nullable=True))
    op.create_foreign_key(None, 'portfolio', 'staff', ['staff_username'], ['username'])
    op.create_unique_constraint(None, 'staff', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'staff', type_='unique')
    op.drop_constraint(None, 'portfolio', type_='foreignkey')
    op.drop_column('portfolio', 'staff_username')
    # ### end Alembic commands ###
