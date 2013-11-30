# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('snippets_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63, unique=True)),
        ))
        db.send_create_signal('snippets', ['Tag'])

        # Adding model 'Board'
        db.create_table('snippets_board', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='boards', to=orm['auth.User'])),
            ('read_public', self.gf('django.db.models.fields.BooleanField')()),
            ('write_public', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('snippets', ['Board'])

        # Adding M2M table for field read_users on 'Board'
        m2m_table_name = db.shorten_name('snippets_board_read_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('board', models.ForeignKey(orm['snippets.board'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['board_id', 'user_id'])

        # Adding M2M table for field write_users on 'Board'
        m2m_table_name = db.shorten_name('snippets_board_write_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('board', models.ForeignKey(orm['snippets.board'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['board_id', 'user_id'])

        # Adding model 'Snippet'
        db.create_table('snippets_snippet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_time', self.gf('django.db.models.fields.DateField')(blank=True, auto_now_add=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('board', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['snippets.Board'])),
            ('code', self.gf('django.db.models.fields.TextField')()),
            ('score', self.gf('django.db.models.fields.FloatField')()),
            ('score0', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('score1', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('score2', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('score3', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('score4', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('snippets', ['Snippet'])

        # Adding M2M table for field tags on 'Snippet'
        m2m_table_name = db.shorten_name('snippets_snippet_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('snippet', models.ForeignKey(orm['snippets.snippet'], null=False)),
            ('tag', models.ForeignKey(orm['snippets.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['snippet_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('snippets_tag')

        # Deleting model 'Board'
        db.delete_table('snippets_board')

        # Removing M2M table for field read_users on 'Board'
        db.delete_table(db.shorten_name('snippets_board_read_users'))

        # Removing M2M table for field write_users on 'Board'
        db.delete_table(db.shorten_name('snippets_board_write_users'))

        # Deleting model 'Snippet'
        db.delete_table('snippets_snippet')

        # Removing M2M table for field tags on 'Snippet'
        db.delete_table(db.shorten_name('snippets_snippet_tags'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'snippets.board': {
            'Meta': {'object_name': 'Board'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'boards'", 'to': "orm['auth.User']"}),
            'read_public': ('django.db.models.fields.BooleanField', [], {}),
            'read_users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'readable'", 'blank': 'True', 'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'write_public': ('django.db.models.fields.BooleanField', [], {}),
            'write_users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'writeable'", 'blank': 'True', 'to': "orm['auth.User']", 'symmetrical': 'False'})
        },
        'snippets.snippet': {
            'Meta': {'object_name': 'Snippet'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['snippets.Board']"}),
            'code': ('django.db.models.fields.TextField', [], {}),
            'creation_time': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.FloatField', [], {}),
            'score0': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'score1': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'score2': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'score3': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'score4': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['snippets.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'snippets.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63', 'unique': 'True'})
        }
    }

    complete_apps = ['snippets']