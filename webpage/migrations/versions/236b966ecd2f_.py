"""empty message

Revision ID: 236b966ecd2f
Revises: 
Create Date: 2017-05-03 14:27:37.853971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '236b966ecd2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chatbot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('dataset', sa.String(length=64), nullable=True),
    sa.Column('base_cell', sa.String(length=64), nullable=True),
    sa.Column('encoder', sa.String(length=64), nullable=True),
    sa.Column('decoder', sa.String(length=64), nullable=True),
    sa.Column('learning_rate', sa.Float(), nullable=True),
    sa.Column('num_layers', sa.Integer(), nullable=True),
    sa.Column('state_size', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chatbot_name'), 'chatbot', ['name'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=True)
    op.create_table('conversation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('chatbot_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chatbot_id'], ['chatbot.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_conversation_start_time'), 'conversation', ['start_time'], unique=True)
    op.create_table('turn',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_message', sa.Text(), nullable=True),
    sa.Column('chatbot_message', sa.Text(), nullable=True),
    sa.Column('conversation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('turn')
    op.drop_index(op.f('ix_conversation_start_time'), table_name='conversation')
    op.drop_table('conversation')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_chatbot_name'), table_name='chatbot')
    op.drop_table('chatbot')
    # ### end Alembic commands ###