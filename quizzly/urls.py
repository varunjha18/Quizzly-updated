from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quizzes.urls')),
    path('accounts/', include('accounts.urls')),
    path('leaderboard/', include('leaderboard.urls')),
    path('forums/', include('forums.urls'))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)