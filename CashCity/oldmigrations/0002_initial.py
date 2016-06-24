# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MapSettings'
        db.create_table(u'CashCity_mapsettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('zoom', self.gf('django.db.models.fields.IntegerField')()),
            ('MapLayer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('PawnShops', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('CheckCashing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('WireTransfer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Banks', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('McDonalds', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('SubwayLines', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Media', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['MapSettings'])

        # Adding model 'ExUserProfile'
        db.create_table(u'CashCity_exuserprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('teacherName', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('teacherOrStudent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('teacherId', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='teacher', null=True, to=orm['auth.User'])),
            ('section', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['ExUserProfile'])

        # Adding model 'MediaImage'
        db.create_table(u'CashCity_mediaimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('cropped_image', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cropped_image_w640_h480', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['MediaImage'])

        # Adding model 'MediaImageComments'
        db.create_table(u'CashCity_mediaimagecomments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('mediaImage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CashCity.MediaImage'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['MediaImageComments'])

        # Adding model 'MediaAudio'
        db.create_table(u'CashCity_mediaaudio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['MediaAudio'])

        # Adding model 'MediaAudioComments'
        db.create_table(u'CashCity_mediaaudiocomments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('mediaAudio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CashCity.MediaAudio'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['MediaAudioComments'])

        # Adding model 'MediaNote'
        db.create_table(u'CashCity_medianote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['MediaNote'])

        # Adding model 'MediaNoteComments'
        db.create_table(u'CashCity_medianotecomments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('mediaNote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CashCity.MediaNote'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['MediaNoteComments'])

        # Adding model 'MediaInterview'
        db.create_table(u'CashCity_mediainterview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('cropped_image', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cropped_image_w640_h480', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['MediaInterview'])

        # Adding model 'MediaInterviewComments'
        db.create_table(u'CashCity_mediainterviewcomments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('mediaInterview', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CashCity.MediaInterview'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['MediaInterviewComments'])

        # Adding model 'Opinions'
        db.create_table(u'CashCity_opinions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('teamImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('cropped_teamImage', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cropped_teamImage_w640_h480', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['Opinions'])

        # Adding model 'OpinionSections'
        db.create_table(u'CashCity_opinionsections', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opinion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CashCity.Opinions'])),
            ('sectionNumber', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CashCity.MediaImage'], null=True, blank=True)),
            ('audio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CashCity.MediaAudio'], null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CashCity.MediaNote'], null=True, blank=True)),
            ('interview', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CashCity.MediaInterview'], null=True, blank=True)),
            ('mapSnap', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CashCity.MapSettings'], null=True, blank=True)),
            ('uploadImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=10000, null=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['OpinionSections'])

        # Adding model 'OpinionComments'
        db.create_table(u'CashCity_opinioncomments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('opinion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CashCity.Opinions'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'CashCity', ['OpinionComments'])


    def backwards(self, orm):
        # Deleting model 'MapSettings'
        db.delete_table(u'CashCity_mapsettings')

        # Deleting model 'ExUserProfile'
        db.delete_table(u'CashCity_exuserprofile')

        # Deleting model 'MediaImage'
        db.delete_table(u'CashCity_mediaimage')

        # Deleting model 'MediaImageComments'
        db.delete_table(u'CashCity_mediaimagecomments')

        # Deleting model 'MediaAudio'
        db.delete_table(u'CashCity_mediaaudio')

        # Deleting model 'MediaAudioComments'
        db.delete_table(u'CashCity_mediaaudiocomments')

        # Deleting model 'MediaNote'
        db.delete_table(u'CashCity_medianote')

        # Deleting model 'MediaNoteComments'
        db.delete_table(u'CashCity_medianotecomments')

        # Deleting model 'MediaInterview'
        db.delete_table(u'CashCity_mediainterview')

        # Deleting model 'MediaInterviewComments'
        db.delete_table(u'CashCity_mediainterviewcomments')

        # Deleting model 'Opinions'
        db.delete_table(u'CashCity_opinions')

        # Deleting model 'OpinionSections'
        db.delete_table(u'CashCity_opinionsections')

        # Deleting model 'OpinionComments'
        db.delete_table(u'CashCity_opinioncomments')


    models = {
        u'CashCity.exuserprofile': {
            'Meta': {'object_name': 'ExUserProfile'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'teacherId': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teacher'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'teacherName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'teacherOrStudent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'CashCity.mapsettings': {
            'Banks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'CheckCashing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'MapLayer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'McDonalds': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Media': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'MapSettings'},
            'PawnShops': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'SubwayLines': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'WireTransfer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'zoom': ('django.db.models.fields.IntegerField', [], {})
        },
        u'CashCity.mediaaudio': {
            'Meta': {'object_name': 'MediaAudio'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'CashCity.mediaaudiocomments': {
            'Meta': {'object_name': 'MediaAudioComments'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediaAudio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaAudio']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'CashCity.mediaimage': {
            'Meta': {'object_name': 'MediaImage'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cropped_image': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cropped_image_w640_h480': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'CashCity.mediaimagecomments': {
            'Meta': {'object_name': 'MediaImageComments'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediaImage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaImage']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'CashCity.mediainterview': {
            'Meta': {'object_name': 'MediaInterview'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cropped_image': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cropped_image_w640_h480': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'CashCity.mediainterviewcomments': {
            'Meta': {'object_name': 'MediaInterviewComments'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediaInterview': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaInterview']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'CashCity.medianote': {
            'Meta': {'object_name': 'MediaNote'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'CashCity.medianotecomments': {
            'Meta': {'object_name': 'MediaNoteComments'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediaNote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaNote']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'CashCity.opinioncomments': {
            'Meta': {'object_name': 'OpinionComments'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opinion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.Opinions']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'CashCity.opinions': {
            'Meta': {'object_name': 'Opinions'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cropped_teamImage': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cropped_teamImage_w640_h480': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'teamImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'CashCity.opinionsections': {
            'Meta': {'object_name': 'OpinionSections'},
            'audio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaAudio']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaImage']", 'null': 'True', 'blank': 'True'}),
            'interview': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaInterview']", 'null': 'True', 'blank': 'True'}),
            'mapSnap': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MapSettings']", 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaNote']", 'null': 'True', 'blank': 'True'}),
            'opinion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.Opinions']"}),
            'sectionNumber': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'uploadImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['CashCity']