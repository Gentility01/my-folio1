from django.contrib import admin

from core.models import  *
# Register your models here.

# admin.site.register([ AboutMeModel, ServicesModel, ServiceRatingModel, NewsModel, Tags, Images, PotfolioModel])


@admin.register(AboutMeModel)
class AboutMeModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "thumbnail", "title", "location", "slug"]
    search_fields = ["name", "title"]


@admin.register(ServicesModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "i_class", "description", "description2"]
    search_fields = ["name", "title"]

@admin.register(ServiceRatingModel)
class ServiceRatingModelAdmin(admin.ModelAdmin):
    list_display = ["title", "pesentage"]
    search_fields = ["title", "pesentage"]

@admin.register(PotfolioModel)
class PotfolioAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "client", "firm_name"]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["title"]


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "slug",  "thumbnail"]
    search_fields = ["title"]


@admin.register(PotfolioQuestionModel)
class PotfolioQuestionModelAdmin(admin.ModelAdmin):
    list_display = ["questions", "answer"]

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ["id",  "image_tag", "potfolio", "news", "blogs"]

@admin.register(Experiences)
class ExperiencesAdmin(admin.ModelAdmin):
    list_display = ["id", "name_of_place", "work_as", "date_started", "date_stopped"]

@admin.register(Schools)
class SchoolsAdmin(admin.ModelAdmin):
    list_display = ["id", "name_of_school", "course", "place", "date_started", "date_stopped"]



@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(PortfolioBlogModel)
class PortfolioBlogModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name","category"]


@admin.register(CommentsModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "post", "body", "created"]


