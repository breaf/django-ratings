# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting model 'ScoreCorrelation'
        db.delete_table('djangoratings_scorecorrelation')

        # Adding model 'SimilarUser'
        db.create_table('djangoratings_similaruser', (
            ('to_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='similar_users_from', to=orm['auth.User'])),
            ('agrees', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disagrees', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='similar_users', to=orm['auth.User'])),
        ))
        db.send_create_signal('djangoratings', ['SimilarUser'])

        # Deleting field 'Score.stddev'
        db.delete_column('djangoratings_score', 'stddev')

        # Deleting field 'Score.mean'
        db.delete_column('djangoratings_score', 'mean')
    
    
    def backwards(self, orm):
        
        # Adding model 'ScoreCorrelation'
        db.create_table('djangoratings_scorecorrelation', (
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('to_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='djr_sc_2', to=orm['contenttypes.ContentType'])),
            ('rank', self.gf('django.db.models.fields.FloatField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='djr_sc_1', to=orm['contenttypes.ContentType'])),
            ('to_object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('djangoratings', ['ScoreCorrelation'])

        # Deleting model 'SimilarUser'
        db.delete_table('djangoratings_similaruser')

        # Adding field 'Score.stddev'
        db.add_column('djangoratings_score', 'stddev', self.gf('django.db.models.fields.FloatField')(default=0.0), keep_default=False)

        # Adding field 'Score.mean'
        db.add_column('djangoratings_score', 'mean', self.gf('django.db.models.fields.FloatField')(default=0.0), keep_default=False)
    
    
    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'djangoratings.score': {
            'Meta': {'unique_together': "(('content_type', 'object_id', 'key'),)", 'object_name': 'Score'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'djangoratings.similaruser': {
            'Meta': {'unique_together': "(('from_user', 'to_user'),)", 'object_name': 'SimilarUser'},
            'agrees': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'disagrees': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'similar_users'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'similar_users_from'", 'to': "orm['auth.User']"})
        },
        'djangoratings.vote': {
            'Meta': {'unique_together': "(('content_type', 'object_id', 'key', 'user', 'ip_address'),)", 'object_name': 'Vote'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votes'", 'to': "orm['contenttypes.ContentType']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'votes'", 'null': 'True', 'to': "orm['accounts.User']"})
        }
    }
    
    complete_apps = ['djangoratings']
