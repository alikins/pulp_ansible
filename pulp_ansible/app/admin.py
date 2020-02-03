# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

from .models import Role, Collection, CollectionImport, Tag, CollectionVersion, AnsibleRemote, CollectionRemote, AnsibleDistribution

from pulpcore.plugin.models import \
    (
        ContentGuard,
        Publisher,
        Remote,
    )


from pulpcore.app.models import \
    (
        Artifact,
        Content,
        ContentArtifact,
        RemoteArtifact,

        ReservedResource,
        ReservedResourceRecord,
        TaskReservedResource,
        Worker,
        Task,
        CreatedResource,
        Repository,
        Exporter,

        Publication,
        PublishedArtifact,
        PublishedMetadata,

        RepositoryContent,
        RepositoryVersion,
        RepositoryVersionContentDetails,
        BaseDistribution,
        ContentAppStatus,
        Upload,
        UploadChunk,
        ProgressReport,
    )


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'file',
        'size',
        'md5',
        'sha1',
        'sha224',
        'sha256',
        'sha384',
        'sha512',
    )
    list_filter = ('pulp_created', 'pulp_last_updated')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
    )
    list_filter = ('pulp_created', 'pulp_last_updated')
    raw_id_fields = ('_artifacts',)


@admin.register(ContentArtifact)
class ContentArtifactAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'artifact',
        'content',
        'relative_path',
    )
    list_filter = ('pulp_created', 'pulp_last_updated')


@admin.register(RemoteArtifact)
class RemoteArtifactAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'url',
        'size',
        'md5',
        'sha1',
        'sha224',
        'sha256',
        'sha384',
        'sha512',
        'content_artifact',
        'remote',
    )
    list_filter = (
        'pulp_created',
        'pulp_last_updated',
        'content_artifact',
        'remote',
    )


@admin.register(ReservedResource)
class ReservedResourceAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'resource',
        'worker',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'worker')
    raw_id_fields = ('tasks',)


@admin.register(TaskReservedResource)
class TaskReservedResourceAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'resource',
        'task',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'resource', 'task')


@admin.register(ReservedResourceRecord)
class ReservedResourceRecordAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'resource',
    )
    list_filter = ('pulp_created', 'pulp_last_updated')
    raw_id_fields = ('tasks',)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'name',
        'last_heartbeat',
        'gracefully_stopped',
        'cleaned_up',
    )
    list_filter = (
        'pulp_created',
        'pulp_last_updated',
        'last_heartbeat',
        'gracefully_stopped',
        'cleaned_up',
    )
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'state',
        'name',
        'started_at',
        'finished_at',
        'error',
        'parent',
        'worker',
    )
    list_filter = (
        'pulp_created',
        'pulp_last_updated',
        'started_at',
        'finished_at',
    )
    search_fields = ('name',)


@admin.register(CreatedResource)
class CreatedResourceAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'content_type',
        'object_id',
        'task',
    )
    list_filter = ('pulp_created', 'pulp_last_updated')
    raw_id_fields = ('content_type', 'task')


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'name',
        'description',
        'last_version',
        'plugin_managed',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'plugin_managed')
    raw_id_fields = ('content',)
    search_fields = ('name',)


@admin.register(Remote)
class RemoteAdmin(admin.ModelAdmin):
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


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'name',
    )
    list_filter = ('pulp_created', 'pulp_last_updated')
    search_fields = ('name',)


@admin.register(Exporter)
class ExporterAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'name',
        'last_export',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'last_export')
    search_fields = ('name',)


@admin.register(RepositoryContent)
class RepositoryContentAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'content',
        'repository',
        'version_added',
        'version_removed',
    )
    list_filter = (
        'pulp_created',
        'pulp_last_updated',
        'content',
        'repository',
        'version_added',
        'version_removed',
    )


@admin.register(RepositoryVersion)
class RepositoryVersionAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'repository',
        'number',
        'complete',
        'base_version',
    )
    list_filter = (
        'pulp_created',
        'pulp_last_updated',
        'repository',
        'complete',
        'base_version',
    )


@admin.register(RepositoryVersionContentDetails)
class RepositoryVersionContentDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'count_type',
        'content_type',
        'repository_version',
        'count',
    )


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'complete',
        'pass_through',
        'publisher',
        'repository_version',
    )
    list_filter = (
        'pulp_created',
        'pulp_last_updated',
        'complete',
        'pass_through',
        'publisher',
        'repository_version',
    )


@admin.register(PublishedArtifact)
class PublishedArtifactAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'relative_path',
        'content_artifact',
        'publication',
    )
    list_filter = (
        'pulp_created',
        'pulp_last_updated',
        'content_artifact',
        'publication',
    )


@admin.register(PublishedMetadata)
class PublishedMetadataAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'relative_path',
        'publication',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'publication')


@admin.register(ContentGuard)
class ContentGuardAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'name',
        'description',
    )
    list_filter = ('pulp_created', 'pulp_last_updated')
    search_fields = ('name',)


@admin.register(BaseDistribution)
class BaseDistributionAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'pulp_type',
        'name',
        'base_path',
        'content_guard',
        'remote',
    )
    list_filter = (
        'pulp_created',
        'pulp_last_updated',
        'content_guard',
        'remote',
    )
    search_fields = ('name',)


@admin.register(ContentAppStatus)
class ContentAppStatusAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'name',
        'last_heartbeat',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'last_heartbeat')
    search_fields = ('name',)


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'file',
        'size',
    )
    list_filter = ('pulp_created', 'pulp_last_updated')


@admin.register(UploadChunk)
class UploadChunkAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'upload',
        'offset',
        'size',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'upload')


@admin.register(ProgressReport)
class ProgressReportAdmin(admin.ModelAdmin):
    list_display = (
        'pulp_id',
        'pulp_created',
        'pulp_last_updated',
        'message',
        'code',
        'state',
        'total',
        'done',
        'task',
        'suffix',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'task')


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
        'namespace',
        'name',
        'pulp_last_updated',
        'pulp_type',
        'description',
        'version',
        'is_highest',
        'certification',
    )
    list_filter = ('pulp_created', 'pulp_last_updated', 'is_highest', 'certification')
    raw_id_fields = ('tags',)
    search_fields = ('namespace', 'name', 'pulp_id', 'certification', 'collection')
    readonly_fields = ('namespace', 'name', 'version', 'is_highest', 'collection', 'authors', 'contents', 'dependencies', 'description',
                       'homepage', 'issues', 'license',
                       'docs_blob', 'documentation', 'pulp_id',
                       'repository',
                       'pulp_created', 'pulp_last_updated',
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
