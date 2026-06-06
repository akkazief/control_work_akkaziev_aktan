from django.forms import Form, CharField



class SearchForm(Form):
    query = CharField(required=False, label="Поиск по имени")
