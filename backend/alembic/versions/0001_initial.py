from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector
revision='0001'; down_revision=None; branch_labels=None; depends_on=None

def upgrade():
 op.execute('CREATE EXTENSION IF NOT EXISTS vector')
 op.create_table('users',sa.Column('id',sa.String(36),primary_key=True),sa.Column('created_at',sa.DateTime(),nullable=False))
 op.create_table('sessions',sa.Column('id',sa.String(36),primary_key=True),sa.Column('user_id',sa.String(36),sa.ForeignKey('users.id',ondelete='CASCADE'),nullable=False),sa.Column('title',sa.String(200),nullable=False),sa.Column('created_at',sa.DateTime(),nullable=False),sa.Column('updated_at',sa.DateTime(),nullable=False))
 op.create_table('messages',sa.Column('id',sa.String(36),primary_key=True),sa.Column('session_id',sa.String(36),sa.ForeignKey('sessions.id',ondelete='CASCADE'),nullable=False),sa.Column('role',sa.String(20),nullable=False),sa.Column('content',sa.Text(),nullable=False),sa.Column('metadata',sa.JSON(),nullable=False),sa.Column('created_at',sa.DateTime(),nullable=False))
 op.create_table('documents',sa.Column('id',sa.String(36),primary_key=True),sa.Column('title',sa.Text(),nullable=False),sa.Column('episode',sa.Text(),nullable=False),sa.Column('guest',sa.Text(),nullable=False),sa.Column('source_url',sa.Text(),nullable=False),sa.Column('transcript_path',sa.Text(),unique=True,nullable=False),sa.Column('publish_date',sa.String(20),nullable=False),sa.Column('content_hash',sa.String(64),nullable=False),sa.Column('created_at',sa.DateTime(),nullable=False))
 op.create_table('chunks',sa.Column('id',sa.String(36),primary_key=True),sa.Column('document_id',sa.String(36),sa.ForeignKey('documents.id',ondelete='CASCADE'),nullable=False),sa.Column('chunk_index',sa.Integer(),nullable=False),sa.Column('content',sa.Text(),nullable=False),sa.Column('embedding',Vector(768),nullable=False),sa.Column('token_start',sa.Integer()),sa.Column('token_end',sa.Integer()),sa.Column('metadata',sa.JSON(),nullable=False))
 op.create_table('artifacts',sa.Column('id',sa.String(36),primary_key=True),sa.Column('session_id',sa.String(36),sa.ForeignKey('sessions.id',ondelete='CASCADE'),nullable=False),sa.Column('type',sa.String(20),nullable=False),sa.Column('title',sa.String(300),nullable=False),sa.Column('content',sa.Text(),nullable=False),sa.Column('sources',sa.JSON(),nullable=False),sa.Column('created_at',sa.DateTime(),nullable=False))
 op.create_index('ix_chunks_document_index','chunks',['document_id','chunk_index']); op.create_index('ix_messages_session','messages',['session_id']); op.create_index('ix_documents_hash','documents',['content_hash'])
def downgrade():
 for t in ['artifacts','chunks','documents','messages','sessions','users']: op.drop_table(t)
