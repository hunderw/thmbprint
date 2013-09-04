from django.conf.urls import patterns, include, url

urlpatterns = patterns('profiles.views',
        url(r'dashboard/$', 'dashboard', name='dashboard'),
        url(
            r'(?P<user_id>\d+)/project/$', 
            'list_user_projects',
            name='list_user_projects'
        ),
        url(
            r'(?P<user_id>\d+)/project/create/$',
            'create_project',
            name='create_project'
        ),
        url(
            r'(?P<user_id>\d+)/project/(?P<project_id>\d+)/$',
            'project_detail',
            name='project_detail'
        ),
        url(
            r'(?P<user_id>\d+)/project/(?P<project_id>\d+)/edit/$',
            'edit_project',
            name='edit_project'
        ),
)
