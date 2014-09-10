from django.conf.urls import patterns, url

urlpatterns = patterns("forms_plus.views",
    url(r"^entries_list/$", "entries_list_view", name="entries_list"),
    url(r"^(?P<form_id>\d+)/entries/$", "entries_view", name="form_entries"),
    url(r"^file/(?P<field_entry_id>\d+)/$", "file_view", name="form_file"),
)
