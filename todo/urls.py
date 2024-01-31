from django.urls import path
from .views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagDetailView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskToggleDoneView,
)


urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

    path("toggle-task-done/<int:pk>/",
         TaskToggleDoneView.as_view(), name="toggle-task-done"),
]
