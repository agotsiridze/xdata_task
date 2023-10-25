# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# from typing_extensions import SupportsIndex
from django.db import models


class Articles(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    site_id = models.ForeignKey("Sites", on_delete=models.SET_NULL, null=True)
    clientid = models.ForeignKey(
        "Clients", on_delete=models.SET_NULL, db_column="clientid", null=True
    )
    insert_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    article_date = models.DateTimeField()

    class Meta:
        db_table = "articles"
        verbose_name_plural = "Articles"
        indexes = [
            models.Index(fields=["site_id"]),
            models.Index(fields=["insert_date"]),
            models.Index(fields=["article_date"]),
            models.Index(fields=["clientid"]),
        ]

    def __str__(self) -> str:
        return f"{self.id}"

    def __repr__(self) -> str:
        return super().__str__()


class Filterwords(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    clientid = models.ForeignKey(
        "Clients",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        db_column="clientid",
    )
    word = models.CharField(max_length=255, blank=True, null=True)
    wordalias = models.CharField(
        db_column="wordAlias", max_length=1022, blank=True, null=True
    )
    subwordalias = models.CharField(max_length=255, blank=True, null=True)
    stopword = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "filterwords"
        verbose_name_plural = "Filterwords"
        indexes = [
            models.Index(fields=["clientid"]),
            models.Index(fields=["word"]),
        ]

    def __str__(self) -> str:
        return self.word

    def __repr__(self) -> str:
        return super().__str__()


class Notifications(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    clientid = models.ForeignKey(
        "Clients",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        db_column="clientid",
    )
    sms = models.CharField(max_length=255, blank=True, null=True)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "notifications"
        verbose_name_plural = "Notifications"
        indexes = [
            models.Index(fields=["clientid"]),
        ]

    def __str__(self) -> str:
        return f"{self.id} to {self.clientid}"

    def __repr__(self) -> str:
        return super().__str__()


class Sites(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    sitename = models.CharField(unique=True, max_length=128)

    class Meta:
        db_table = "sites"
        verbose_name_plural = "Sites"

    def __str__(self) -> str:
        return self.sitename

    def __repr__(self) -> str:
        return super().__str__()


class Clients(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(unique=True, max_length=255, null=False, blank=False)
    tts_enabled = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        db_table = "clients"
        verbose_name_plural = "Clients"
        indexes = [
            models.Index(fields=["username"]),
        ]

    def __str__(self) -> str:
        return self.username

    def __repr__(self) -> str:
        return super().__str__()
