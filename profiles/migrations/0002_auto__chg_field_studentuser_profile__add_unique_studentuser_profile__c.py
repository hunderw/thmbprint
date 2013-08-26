# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'StudentUser.profile'
        db.alter_column(u'profiles_studentuser', 'profile_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.UserProfile'], unique=True, null=True))
        # Adding unique constraint on 'StudentUser', fields ['profile']
        db.create_unique(u'profiles_studentuser', ['profile_id'])


        # Changing field 'MentorUser.profile'
        db.alter_column(u'profiles_mentoruser', 'profile_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.UserProfile'], unique=True, null=True))
        # Adding unique constraint on 'MentorUser', fields ['profile']
        db.create_unique(u'profiles_mentoruser', ['profile_id'])


        # Changing field 'UserProfile.user'
        db.alter_column(u'profiles_userprofile', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))
        # Adding unique constraint on 'UserProfile', fields ['user']
        db.create_unique(u'profiles_userprofile', ['user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'UserProfile', fields ['user']
        db.delete_unique(u'profiles_userprofile', ['user_id'])

        # Removing unique constraint on 'MentorUser', fields ['profile']
        db.delete_unique(u'profiles_mentoruser', ['profile_id'])

        # Removing unique constraint on 'StudentUser', fields ['profile']
        db.delete_unique(u'profiles_studentuser', ['profile_id'])


        # User chose to not deal with backwards NULL issues for 'StudentUser.profile'
        raise RuntimeError("Cannot reverse this migration. 'StudentUser.profile' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'StudentUser.profile'
        db.alter_column(u'profiles_studentuser', 'profile_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.UserProfile']))

        # User chose to not deal with backwards NULL issues for 'MentorUser.profile'
        raise RuntimeError("Cannot reverse this migration. 'MentorUser.profile' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'MentorUser.profile'
        db.alter_column(u'profiles_mentoruser', 'profile_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.UserProfile']))

        # Changing field 'UserProfile.user'
        db.alter_column(u'profiles_userprofile', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    models = {
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
        u'profiles.mentoruser': {
            'Meta': {'object_name': 'MentorUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.UserProfile']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.UserProfile']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True'})
        },
        u'profiles.projectitem': {
            'Meta': {'object_name': 'ProjectItem'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.Project']"})
        },
        u'profiles.projectitemfile': {
            'Meta': {'object_name': 'ProjectItemFile'},
            'file_data': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.ProjectItem']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'profiles.projectitemimage': {
            'Meta': {'object_name': 'ProjectItemImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_data': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.ProjectItem']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'profiles.recommendation': {
            'Meta': {'object_name': 'Recommendation'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.MentorUser']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.StudentUser']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profiles.studentuser': {
            'Meta': {'object_name': 'StudentUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.UserProfile']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['profiles']