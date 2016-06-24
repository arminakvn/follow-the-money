# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MediaImage.shared'
        db.add_column(u'CashCity_mediaimage', 'shared',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'MapSettings.title'
        db.add_column(u'CashCity_mapsettings', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MapSettings.popup2Content'
        db.add_column(u'CashCity_mapsettings', 'popup2Content',
                      self.gf('django.db.models.fields.CharField')(max_length=10000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MapSettings.popup2LatLon'
        db.add_column(u'CashCity_mapsettings', 'popup2LatLon',
                      self.gf('django.db.models.fields.CharField')(max_length=10000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MapSettings.popup3Content'
        db.add_column(u'CashCity_mapsettings', 'popup3Content',
                      self.gf('django.db.models.fields.CharField')(max_length=10000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MapSettings.popup3LatLon'
        db.add_column(u'CashCity_mapsettings', 'popup3LatLon',
                      self.gf('django.db.models.fields.CharField')(max_length=10000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MapSettings.chartOn'
        db.add_column(u'CashCity_mapsettings', 'chartOn',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'MediaInterview.shared'
        db.add_column(u'CashCity_mediainterview', 'shared',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'OpinionSections.sectionTitle'
        db.add_column(u'CashCity_opinionsections', 'sectionTitle',
                      self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'OpinionSections.mediaTitle'
        db.add_column(u'CashCity_opinionsections', 'mediaTitle',
                      self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MediaAudio.shared'
        db.add_column(u'CashCity_mediaaudio', 'shared',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'MediaNote.shared'
        db.add_column(u'CashCity_medianote', 'shared',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MediaImage.shared'
        db.delete_column(u'CashCity_mediaimage', 'shared')

        # Deleting field 'MapSettings.title'
        db.delete_column(u'CashCity_mapsettings', 'title')

        # Deleting field 'MapSettings.popup2Content'
        db.delete_column(u'CashCity_mapsettings', 'popup2Content')

        # Deleting field 'MapSettings.popup2LatLon'
        db.delete_column(u'CashCity_mapsettings', 'popup2LatLon')

        # Deleting field 'MapSettings.popup3Content'
        db.delete_column(u'CashCity_mapsettings', 'popup3Content')

        # Deleting field 'MapSettings.popup3LatLon'
        db.delete_column(u'CashCity_mapsettings', 'popup3LatLon')

        # Deleting field 'MapSettings.chartOn'
        db.delete_column(u'CashCity_mapsettings', 'chartOn')

        # Deleting field 'MediaInterview.shared'
        db.delete_column(u'CashCity_mediainterview', 'shared')

        # Deleting field 'OpinionSections.sectionTitle'
        db.delete_column(u'CashCity_opinionsections', 'sectionTitle')

        # Deleting field 'OpinionSections.mediaTitle'
        db.delete_column(u'CashCity_opinionsections', 'mediaTitle')

        # Deleting field 'MediaAudio.shared'
        db.delete_column(u'CashCity_mediaaudio', 'shared')

        # Deleting field 'MediaNote.shared'
        db.delete_column(u'CashCity_medianote', 'shared')


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
            'chartOn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'popup2Content': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'popup2LatLon': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'popup3Content': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'popup3LatLon': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
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
            'shared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'shared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'shared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'coverPhoto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaImage']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cropped_teamImage': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cropped_teamImage_w640_h480': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'opinionText': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'teamImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'CashCity.opinionsections': {
            'Meta': {'object_name': 'OpinionSections'},
            'audio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaAudio']", 'null': 'True', 'blank': 'True'}),
            'cropped_uploadImage_w640_h480': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaImage']", 'null': 'True', 'blank': 'True'}),
            'interview': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaInterview']", 'null': 'True', 'blank': 'True'}),
            'mapSnap': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MapSettings']", 'null': 'True', 'blank': 'True'}),
            'mediaTitle': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.MediaNote']", 'null': 'True', 'blank': 'True'}),
            'opinion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CashCity.Opinions']"}),
            'sectionNumber': ('django.db.models.fields.IntegerField', [], {}),
            'sectionTitle': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
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