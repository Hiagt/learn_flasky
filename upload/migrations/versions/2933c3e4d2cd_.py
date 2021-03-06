"""empty message

Revision ID: 2933c3e4d2cd
Revises: 
Create Date: 2017-07-05 00:11:19.725000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2933c3e4d2cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('time', sa.DATETIME(), nullable=True),
    sa.Column('filename', sa.String(length=120), nullable=True),
    sa.Column('category', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_data')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('user_data',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('time', mysql.DATETIME(), nullable=True),
    sa.Column('filename', mysql.VARCHAR(length=120), nullable=True),
    sa.Column('category', mysql.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('users')
    # ### end Alembic commands ###
