from django.contrib import admin
from .models import *

admin.site.register(Accountinggrouptable)

class AdminAccountstable(admin.ModelAdmin):
    list_display = ('accountname', 'accountcurrency')

admin.site.register(Accountstable, AdminAccountstable)
admin.site.register(Accounttypetable)
admin.site.register(Categorygrouptable)

class AdminChildcategorytable(admin.ModelAdmin):
    list_display = ('categorytableid', 'childcategoryname', 'parentcategoryid')
    list_editable = ('childcategoryname',)

admin.site.register(Childcategorytable, AdminChildcategorytable)
admin.site.register(Filterstable)

class AdminItemtable(admin.ModelAdmin):
    list_display = ('itemtableid', 'itemname', 'itemautofillvisibility')
    list_editable = ('itemautofillvisibility',)

admin.site.register(Itemtable, AdminItemtable)
admin.site.register(Labelstable)
admin.site.register(Notificationtable)
admin.site.register(Parentcategorytable)
admin.site.register(Picturetable)
admin.site.register(Settingstable)
admin.site.register(Smsstable)
admin.site.register(Trackingtable)

class AdminTransactionstable(admin.ModelAdmin):
    list_display = (
        'transactionstableid',
        'itemid',
        'amount',
        'transactioncurrency',
        'date',
        'transactiontypeid',
        'categoryid',
        'accountid',
        'accountpairid',
        'notes')
    search_fields = ('transactionstableid', 'date', 'notes', 'itemid__itemname')
    #list_editable = ('itemautofillvisibility',)

admin.site.register(Transactionstable, AdminTransactionstable)
admin.site.register(Transactiontypetable)
admin.site.register(AndroidMetadata)

