# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('snippets_tag')

        # Deleting field 'Snippet.score4'
        db.delete_column('snippets_snippet', 'score4')

        # Deleting field 'Snippet.score3'
        db.delete_column('snippets_snippet', 'score3')

        # Deleting field 'Snippet.score2'
        db.delete_column('snippets_snippet', 'score2')

        # Deleting field 'Snippet.score1'
        db.delete_column('snippets_snippet', 'score1')

        # Deleting field 'Snippet.score0'
        db.delete_column('snippets_snippet', 'score0')

        # Deleting field 'Snippet.score'
        db.delete_column('snippets_snippet', 'score')

        # Removing M2M table for field tags on 'Snippet'
        db.delete_table(db.shorten_name('snippets_snippet_tags'))


    def backwards(self, orm):
        # Adding model 'Tag'
        db.create_table('snippets_tag', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63, unique=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('snippets', ['Tag'])


        # User chose to not deal with backwards NULL issues for 'Snippet.score4'
        raise RuntimeError("Cannot reverse this migration. 'Snippet.score4' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Snippet.score4'
        db.add_column('snippets_snippet', 'score4',
                      self.gf('django.db.models.fields.PositiveIntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Snippet.score3'
        raise RuntimeError("Cannot reverse this migration. 'Snippet.score3' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Snippet.score3'
        db.add_column('snippets_snippet', 'score3',
                      self.gf('django.db.models.fields.PositiveIntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Snippet.score2'
        raise RuntimeError("Cannot reverse this migration. 'Snippet.score2' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Snippet.score2'
        db.add_column('snippets_snippet', 'score2',
                      self.gf('django.db.models.fields.PositiveIntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Snippet.score1'
        raise RuntimeError("Cannot reverse this migration. 'Snippet.score1' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Snippet.score1'
        db.add_column('snippets_snippet', 'score1',
                      self.gf('django.db.models.fields.PositiveIntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Snippet.score0'
        raise RuntimeError("Cannot reverse this migration. 'Snippet.score0' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Snippet.score0'
        db.add_column('snippets_snippet', 'score0',
                      self.gf('django.db.models.fields.PositiveIntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Snippet.score'
        raise RuntimeError("Cannot reverse this migration. 'Snippet.score' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Snippet.score'
        db.add_column('snippets_snippet', 'score',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)

        # Adding M2M table for field tags on 'Snippet'
        m2m_table_name = db.shorten_name('snippets_snippet_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('snippet', models.ForeignKey(orm['snippets.snippet'], null=False)),
            ('tag', models.ForeignKey(orm['snippets.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['snippet_id', 'tag_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
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
            'read_users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'readable'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'write_public': ('django.db.models.fields.BooleanField', [], {}),
            'write_users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'writeable'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"})
        },
        'snippets.snippet': {
            'Meta': {'object_name': 'Snippet'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'snippets'", 'to': "orm['snippets.Board']"}),
            'code': ('django.db.models.fields.TextField', [], {}),
            'creation_time': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['snippets']