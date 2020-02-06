# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import (
    Role,
    Collection,
    CollectionImport,
    Tag,
    CollectionVersion,
    AnsibleRemote,
    AnsibleRepository,
    CollectionRemote,
    AnsibleDistribution,
)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content_type', 'codename')
    raw_id_fields = ('content_type',)
    search_fields = ('name',)


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
    pass
    # list_display = (
    #     'pulp_id',
    #     'pulp_created',
    #     'pulp_last_updated',
    #     'namespace',
    #     'name',
    #     'deprecated',
    # )
    # list_filter = ('pulp_created', 'pulp_last_updated', 'deprecated')
    # search_fields = ('name',)
    # readonly_fields = ['namespace', 'name']


@admin.register(CollectionImport)
class CollectionImportAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'pulp_id', 'pulp_created', 'pulp_last_updated')
    list_filter = ('pulp_created', 'pulp_last_updated')
    search_fields = ('name',)
    readonly_fields = ['name', 'pulp_id', 'pulp_created', 'pulp_last_updated']
    fields = ('name', 'pulp_id', 'pulp_created', 'pulp_last_updated')


@admin.register(CollectionVersion)
class CollectionVersionAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'namespace',
        'name',
        'version',
        'description',
        'certification',
        'pulp_type',
        'is_highest',
        'pulp_last_updated',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'is_highest', 'certification')
    raw_id_fields = ('tags',)
    search_fields = ('namespace', 'name', 'pulp_id', 'certification', 'collection')
    readonly_fields = ('namespace',
                       'name',
                       'version',
                       'is_highest',
                       'collection',
                       'authors',
                       'contents',
                       'dependencies',
                       'description',
                       'homepage',
                       'issues',
                       'license',
                       'docs_blob',
                       'documentation',
                       'repository',
                       'pulp_id',
                       'pulp_created',
                       'pulp_last_updated',
                       )
    fields = (
        'pulp_id',
        'namespace',
        'name',
        'version',
        'is_highest',
        'description',
        'certification',
        'dependencies',
        'authors',
        'homepage',
        'issues',
        'repository',
        'license',
        'contents',
        'pulp_type',
        'documentation',
        'docs_blob',
        'search_vector',
        'pulp_created',
        'pulp_last_updated',
    )


@admin.register(AnsibleRemote)
class AnsibleRemoteAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'name',
        'url',
        'proxy_url',
        'username',
        'password',
        'download_concurrency',
        'policy',
    )
    list_filter = ('pulp_created', 'pulp_last_updated')
    search_fields = ('name',)


@admin.register(AnsibleRepository)
class AnsibleRepositoryAdmin(admin.ModelAdmin):
    pass


@admin.register(CollectionRemote)
class CollectionRemoteAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'name',
        'url',
        'proxy_url',
        'username',
        'password',
        'download_concurrency',
        'policy',
        'requirements_file',
    )
    list_filter = ('pulp_created', 'pulp_last_updated')
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
