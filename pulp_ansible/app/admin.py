# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

from .models import Role, Collection, CollectionImport, Tag, CollectionVersion, AnsibleRemote, CollectionRemote, AnsibleDistribution


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content_type', 'codename')
    raw_id_fields = ('content_type',)
    search_fields = ('name',)


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_label', 'model')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'namespace',
        'name',
        'version',
    )
    list_filter = ('pulp_created', 'pulp_last_updated')
    search_fields = ('name',)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'namespace',
        'name',
        'deprecated',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'deprecated')
    search_fields = ('name',)


@admin.register(CollectionImport)
class CollectionImportAdmin(admin.ModelAdmin):
    list_display = ('task', 'messages')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pulp_id', 'pulp_created', 'pulp_last_updated', 'name')
    list_filter = ('pulp_created', 'pulp_last_updated')
    search_fields = ('name',)


@admin.register(CollectionVersion)
class CollectionVersionAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'authors',
        'contents',
        'dependencies',
        'description',
        'docs_blob',
        'documentation',
        'homepage',
        'issues',
        'license',
        'name',
        'namespace',
        'repository',
        'version',
        'is_highest',
        'certification',
        'collection',
        'search_vector',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'is_highest')
    raw_id_fields = ('tags',)
    search_fields = ('name',)


@admin.register(AnsibleRemote)
class AnsibleRemoteAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'name',
        'url',
        'ssl_ca_certificate',
        'ssl_client_certificate',
        'ssl_client_key',
        'ssl_validation',
        'proxy_url',
        'username',
        'password',
        'download_concurrency',
        'policy',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'ssl_validation')
    search_fields = ('name',)


@admin.register(CollectionRemote)
class CollectionRemoteAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'name',
        'url',
        'ssl_ca_certificate',
        'ssl_client_certificate',
        'ssl_client_key',
        'ssl_validation',
        'proxy_url',
        'username',
        'password',
        'download_concurrency',
        'policy',
        'requirements_file',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'ssl_validation')
    search_fields = ('name',)


@admin.register(AnsibleDistribution)
class AnsibleDistributionAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'name',
        'base_path',
        'content_guard',
        'remote',
        'repository',
        'repository_version',
    )
    list_filter = (
        'pulp_created',
        'pulp_last_updated',
        'content_guard',
        'remote',
        'repository',
        'repository_version',
    )
    search_fields = ('name',)
