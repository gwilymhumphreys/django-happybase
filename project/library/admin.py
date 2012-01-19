from django.contrib import admin


class NamedModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class NamedModelInline(admin.TabularInline):
    prepopulated_fields = {'slug': ('name',)}
