from django.contrib import admin
from apiapp.models import Media, Cluster, Article, \
        UserBlackList, Report, UserProfile


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'rss_list', 'political_view', 'icon')


@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    list_display = ('cluster_id',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'media', 'article_url', 'published_at')
    list_filter = ('media',)


@admin.register(UserBlackList)
class UserBlackListAdmin(admin.ModelAdmin):
    list_display = ('user', 'media')
    list_filter = ('user',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'article_a', 'article_b', 'content')
    list_filter = ('user',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'shown_news', 'clicked_news')

