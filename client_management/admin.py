from django.contrib import admin
from . import models
from django import forms
import csv
import io
import bleach


# Create separate admin panel for the app
class ClientManagerAdminArea(admin.AdminSite):
    site_header = "Client Management"


client_manager = ClientManagerAdminArea(name="ClientManager")


# create costum form for clients
class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

    # add field to upload csv file
    csv_of_filterwords = forms.FileField(required=False)

    # read uploaded csv file without saving
    @staticmethod
    def read_csv(csv_field) -> dict:
        my_file = csv_field.read().decode("utf-8")
        my_file = bleach.clean(my_file, strip=True, strip_comments=True)
        delimiter = csv.Sniffer().sniff(my_file).delimiter
        reader = csv.DictReader(io.StringIO(my_file), delimiter=delimiter)
        read_data = dict()
        for d in reader:
            for key, value in d.items():
                if value == "":
                    value = None
                read_data.setdefault(key.casefold(), []).append(value)
        return read_data

    # save filterwords in filterwords table
    def save_filterwords(self, read_data, commit=True):
        for word, wordalias, subwordalias, stopword in zip(
            read_data["word"],
            read_data["wordalias"],
            read_data["subwordalias"],
            read_data["stopword"],
        ):
            models.Filterwords.objects.create(
                clientid=super(ClientForm, self).save(commit=commit),
                word=word,
                wordalias=wordalias,
                subwordalias=subwordalias,
                stopword=stopword,
            ).save()

    # override save method to parse csv file and save filterwords in filterwords table
    def save(self, commit=True):
        csv_field = self.cleaned_data.get("csv_of_filterwords", None)
        if csv_field:
            read_data = self.read_csv(csv_field)
            self.save_filterwords(read_data, commit=commit)

        return super(ClientForm, self).save(commit=commit)

    class Meta:
        model = models.Filterwords
        fields = "__all__"


# create different attributes for client in same form
class NotificationInline(admin.TabularInline):
    model = models.Notifications
    extra = 0


class FilterWordInline(admin.TabularInline):
    model = models.Filterwords
    extra = 0


class ArticleInline(admin.TabularInline):
    model = models.Articles
    extra = 0


# register client model with edited forms in admin panel
class ClientAdmin(admin.ModelAdmin):
    change_form_template = "admin/csv_view-2.html"
    form = ClientForm
    inlines = [NotificationInline, FilterWordInline, ArticleInline]


admin.site.register(models.Clients, ClientAdmin)


# register sites in admin panel
admin.site.register(models.Sites)
