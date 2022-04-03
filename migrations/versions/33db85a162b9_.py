"""empty message

Revision ID: 33db85a162b9
Revises: 
Create Date: 2022-04-01 16:29:31.249057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33db85a162b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('books',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('isbn_number', sa.String(), nullable=False),
    sa.Column('book_title', sa.String(length=150), nullable=True),
    sa.Column('book_length', sa.Integer(), nullable=True),
    sa.Column('author', sa.String(length=100), nullable=True),
    sa.Column('cover_type', sa.String(length=50), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('user')
    # ### end Alembic commands ###
