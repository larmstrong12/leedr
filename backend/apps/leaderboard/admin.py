from django.contrib import admin

from backend.apps.leaderboard.models import GameDetail
from backend.apps.leaderboard.models import UserProfile
from backend.apps.leaderboard.models import UserGameProfile


admin.site.register(GameDetail)
admin.site.register(UserProfile)
admin.site.register(UserGameProfile)


