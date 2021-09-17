# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accountinggrouptable(models.Model):
    accountinggrouptableid = models.AutoField(db_column='accountingGroupTableID', blank=True, primary_key=True)  # Field name made lowercase.
    accountgroupname = models.CharField(db_column='accountGroupName', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACCOUNTINGGROUPTABLE'
        verbose_name = 'Тип актива'
        verbose_name_plural = 'Тип актива'

    def __str__(self):
        return self.accountgroupname


class Accountstable(models.Model):
    accountstableid = models.AutoField(db_column='accountsTableID', blank=True, primary_key=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='accountName', max_length=63, blank=True, null=True)  # Field name made lowercase.

    #accounttypeid = models.IntegerField(db_column='accountTypeID', blank=True, null=True)  # Field name made lowercase.
    accounttypeid = models.ForeignKey('Accounttypetable', db_column='accountTypeID', db_index=True, blank=True, null=True, on_delete=models.DO_NOTHING)

    accounthidden = models.IntegerField(db_column='accountHidden', blank=True, null=True)  # Field name made lowercase.
    accountcurrency = models.CharField(db_column='accountCurrency', max_length=5, blank=True, null=True)  # Field name made lowercase.
    accountconversionrate = models.IntegerField(db_column='accountConversionRate', blank=True, null=True)  # Field name made lowercase.
    accountconversionratenew = models.FloatField(db_column='accountConversionRateNew', blank=True, null=True)  # Field name made lowercase.
    currencychanged = models.IntegerField(db_column='currencyChanged', blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.IntegerField(db_column='creditLimit', blank=True, null=True)  # Field name made lowercase.
    cutoffda = models.IntegerField(db_column='cutOffDa', blank=True, null=True)  # Field name made lowercase.
    creditcardduedate = models.IntegerField(db_column='creditCardDueDate', blank=True, null=True)  # Field name made lowercase.
    cashbasedaccounts = models.IntegerField(db_column='cashBasedAccounts', blank=True, null=True)  # Field name made lowercase.
    accountselectorvisibility = models.IntegerField(db_column='accountSelectorVisibility', blank=True, null=True)  # Field name made lowercase.
    accountsextracolumnstring1 = models.CharField(db_column='accountsExtraColumnString1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountsextracolumnstring2 = models.CharField(db_column='accountsExtraColumnString2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountsextracolumnint1 = models.CharField(db_column='accountsExtraColumnInt1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountsextracolumnint2 = models.CharField(db_column='accountsExtraColumnInt2', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACCOUNTSTABLE'
        verbose_name = 'Счета'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return self.accountname


class Accounttypetable(models.Model):
    accounttypetableid = models.AutoField(db_column='accountTypeTableID', blank=True, primary_key=True)  # Field name made lowercase.
    accounttypename = models.CharField(db_column='accountTypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #accountinggroupid = models.IntegerField(db_column='accountingGroupID', blank=True, null=True)  # Field name made lowercase.

    accountinggroupid = models.ForeignKey('Accountinggrouptable', db_column='accountingGroupID', db_index=True, blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ACCOUNTTYPETABLE'
        verbose_name = 'Тип счета'
        verbose_name_plural = 'Тип счета'

    def __str__(self):
        return self.accounttypename


class Categorygrouptable(models.Model):
    categorygrouptableid = models.AutoField(db_column='categoryGroupTableID', blank=True, primary_key=True)  # Field name made lowercase.
    categorygroupname = models.CharField(db_column='categoryGroupName', max_length=63, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATEGORYGROUPTABLE'

    def __str__(self):
        return self.categorygroupname


class Childcategorytable(models.Model):
    categorytableid = models.AutoField(db_column='categoryTableID', blank=True, primary_key=True)  # Field name made lowercase.
    childcategoryname = models.CharField(db_column='childCategoryName', max_length=63, blank=True, null=True)  # Field name made lowercase.

    #parentcategoryid = models.IntegerField(db_column='parentCategoryID', blank=True, null=True)  # Field name made lowercase.
    parentcategoryid = models.ForeignKey('Parentcategorytable', db_index=True, db_column='parentCategoryID', blank=True, null=True, on_delete=models.DO_NOTHING)


    budgetamount = models.IntegerField(db_column='budgetAmount', blank=True, null=True)  # Field name made lowercase.
    budgetperiod = models.IntegerField(db_column='budgetPeriod', blank=True, null=True)  # Field name made lowercase.
    budgetenabledcategorychild = models.IntegerField(db_column='budgetEnabledCategoryChild', blank=True, null=True)  # Field name made lowercase.
    childcategoryicon = models.CharField(db_column='childCategoryIcon', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryselectorvisibility = models.IntegerField(db_column='categorySelectorVisibility', blank=True, null=True)  # Field name made lowercase.
    budgetcustomsetup = models.CharField(db_column='budgetCustomSetup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryextracolumnstring1 = models.CharField(db_column='categoryExtraColumnString1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryextracolumnstring2 = models.CharField(db_column='categoryExtraColumnString2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryextracolumnint1 = models.CharField(db_column='categoryExtraColumnInt1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryextracolumnint2 = models.CharField(db_column='categoryExtraColumnInt2', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHILDCATEGORYTABLE'
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.childcategoryname


class Filterstable(models.Model):
    filterstableid = models.AutoField(db_column='filtersTableID', blank=True, primary_key=True)  # Field name made lowercase.
    filtername = models.CharField(max_length=255, blank=True, null=True)
    filterjson = models.CharField(db_column='filterJSON', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FILTERSTABLE'

    def __str__(self):
        return self.filtername


class Itemtable(models.Model):
    itemtableid = models.AutoField(db_column='itemTableID', blank=True, primary_key=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=63, blank=True, null=True)  # Field name made lowercase.
    itemautofillvisibility = models.IntegerField(db_column='itemAutoFillVisibility', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITEMTABLE'
        verbose_name = 'Ключевые слова'
        verbose_name_plural = 'Ключевые слова'

    def __str__(self):
        return self.itemname


class Labelstable(models.Model):
    labelstableid = models.AutoField(db_column='labelsTableID', blank=True, primary_key=True)  # Field name made lowercase.
    labelname = models.CharField(db_column='labelName', max_length=63, blank=True, null=True)  # Field name made lowercase.

    # transactionidlabels = models.IntegerField(db_column='transactionIDLabels', blank=True, null=True)  # Field name made lowercase.
    transactionidlabels = models.ForeignKey('Transactionstable', db_index=True, db_column='transactionIDLabels', blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'LABELSTABLE'

    def __str__(self):
        return self.labelname


class Notificationtable(models.Model):
    smstableid = models.AutoField(db_column='smsTableID', blank=True, primary_key=True)  # Field name made lowercase.
    notificationpackagename = models.CharField(db_column='notificationPackageName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notificationappname = models.CharField(db_column='notificationAppName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notificationdefaultname = models.CharField(db_column='notificationDefaultName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notificationsendercategoryid = models.IntegerField(db_column='notificationSenderCategoryID', blank=True, null=True)  # Field name made lowercase.
    notificationsenderaccountid = models.IntegerField(db_column='notificationSenderAccountID', blank=True, null=True)  # Field name made lowercase.
    notificationsenderamountorder = models.IntegerField(db_column='notificationSenderAmountOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTIFICATIONTABLE'



class Parentcategorytable(models.Model):
    parentcategorytableid = models.AutoField(db_column='parentCategoryTableID', blank=True, primary_key=True)  # Field name made lowercase.
    parentcategoryname = models.CharField(db_column='parentCategoryName', max_length=63, blank=True, null=True)  # Field name made lowercase.

    #categorygroupid = models.IntegerField(db_column='categoryGroupID', blank=True, null=True)  # Field name made lowercase.
    categorygroupid = models.ForeignKey('Categorygrouptable', db_index=True, db_column='categoryGroupID', blank=True, null=True, on_delete=models.DO_NOTHING)

    budgetamountcategoryparent = models.IntegerField(db_column='budgetAmountCategoryParent', blank=True, null=True)  # Field name made lowercase.
    budgetperiodcategoryparent = models.IntegerField(db_column='budgetPeriodCategoryParent', blank=True, null=True)  # Field name made lowercase.
    budgetenabledcategoryparent = models.IntegerField(db_column='budgetEnabledCategoryParent', blank=True, null=True)  # Field name made lowercase.
    budgetamountoverride = models.IntegerField(db_column='budgetAmountOverride', blank=True, null=True)  # Field name made lowercase.
    budgetcustomsetupparent = models.CharField(db_column='budgetCustomSetupParent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryparentextracolumnstring1 = models.CharField(db_column='categoryParentextraColumnString1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryparentextracolumnstring2 = models.CharField(db_column='categoryParentextraColumnString2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryparentextracolumnint1 = models.CharField(db_column='categoryParentextraColumnInt1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryparentextracolumnint2 = models.CharField(db_column='categoryParentextraColumnInt2', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PARENTCATEGORYTABLE'

    def __str__(self):
        return self.parentcategoryname


class Picturetable(models.Model):
    picturetableid = models.AutoField(db_column='pictureTableID', blank=True, primary_key=True)  # Field name made lowercase.
    picturefilename = models.CharField(db_column='pictureFileName', max_length=63, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.IntegerField(db_column='transactionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PICTURETABLE'

    def __str__(self):
        return self.picturefilename


class Settingstable(models.Model):
    settingstableid = models.AutoField(db_column='settingsTableID', blank=True, primary_key=True)  # Field name made lowercase.
    defaultsettings = models.CharField(db_column='defaultSettings', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SETTINGSTABLE'


class Smsstable(models.Model):
    smstableid = models.AutoField(db_column='smsTableID', blank=True, primary_key=True)  # Field name made lowercase.
    sendername = models.CharField(db_column='senderName', max_length=63, blank=True, null=True)  # Field name made lowercase.
    senderdefaultname = models.CharField(db_column='senderDefaultName', max_length=63, blank=True, null=True)  # Field name made lowercase.
    sendercategoryid = models.IntegerField(db_column='senderCategoryID', blank=True, null=True)  # Field name made lowercase.
    senderaccountid = models.IntegerField(db_column='senderAccountID', blank=True, null=True)  # Field name made lowercase.
    senderamountorder = models.IntegerField(db_column='senderAmountOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMSSTABLE'

    def __str__(self):
        return self.sendername


class Trackingtable(models.Model):
    trackingtableid = models.AutoField(db_column='trackingTableID', blank=True, primary_key=True)  # Field name made lowercase.
    trackingname = models.CharField(db_column='trackingName', max_length=63, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRACKINGTABLE'

    def __str__(self):
        return self.trackingname


class Transactionstable(models.Model):
    transactionstableid = models.AutoField(db_column='transactionsTableID', blank=True, primary_key=True)  # Field name made lowercase.

    #itemid = models.IntegerField(db_column='itemID', blank=True, null=True)  # Field name made lowercase.
    itemid = models.ForeignKey('Itemtable', db_index=True, db_column='itemID', blank=True, null=True, on_delete=models.DO_NOTHING)

    amount = models.IntegerField(blank=True, null=True)
    transactioncurrency = models.CharField(db_column='transactionCurrency', max_length=5, blank=True, null=True)  # Field name made lowercase.
    conversionrate = models.IntegerField(db_column='conversionRate', blank=True, null=True)  # Field name made lowercase.
    conversionratenew = models.FloatField(db_column='conversionRateNew', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)

    #transactiontypeid = models.IntegerField(db_column='transactionTypeID', blank=True, null=True)  # Field name made lowercase.
    transactiontypeid = models.ForeignKey('Transactiontypetable', db_column='transactionTypeID', blank=True, null=True, on_delete=models.DO_NOTHING)

    #categoryid = models.IntegerField(db_column='categoryID', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey('Childcategorytable', db_index=True, db_column='categoryID', blank=True, null=True, on_delete=models.DO_NOTHING)

    #accountid = models.IntegerField(db_column='accountID', blank=True, null=True)  # Field name made lowercase.
    accountid = models.ForeignKey('Accountstable', related_name='accountid', db_column='accountID', blank=True, null=True, on_delete=models.DO_NOTHING)  # Field name made lowercase.

    notes = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    accountreference = models.IntegerField(db_column='accountReference', blank=True, null=True)  # Field name made lowercase.

    #accountpairid = models.IntegerField(db_column='accountPairID', blank=True, null=True)  # Field name made lowercase.
    accountpairid = models.ForeignKey('Accountstable', related_name='accountpairid', db_column='accountPairID', blank=True, null=True, on_delete=models.DO_NOTHING)

    #uidpairid = models.IntegerField(db_column='uidPairID', blank=True, null=True)  # Field name made lowercase.
    uidpairid = models.ForeignKey('Transactionstable', related_name='uidpairid1', db_column='uidPairID', blank=True, null=True, on_delete=models.DO_NOTHING)

    deletedtransaction = models.IntegerField(db_column='deletedTransaction', blank=True, null=True)  # Field name made lowercase.
    newsplittransactionid = models.IntegerField(db_column='newSplitTransactionID', blank=True, null=True)  # Field name made lowercase.

    # transfergroupid = models.IntegerField(db_column='transferGroupID', blank=True, null=True)  # Field name made lowercase.
    transfergroupid = models.ForeignKey('Transactionstable', related_name='transfergroupid1', db_column='transferGroupID', blank=True, null=True, on_delete=models.DO_NOTHING)

    hasphoto = models.IntegerField(db_column='hasPhoto', blank=True, null=True)  # Field name made lowercase.
    labelcount = models.IntegerField(db_column='labelCount', blank=True, null=True)  # Field name made lowercase.
    remindertransaction = models.IntegerField(db_column='reminderTransaction', blank=True, null=True)  # Field name made lowercase.
    remindergroupid = models.IntegerField(db_column='reminderGroupID', blank=True, null=True)  # Field name made lowercase.
    reminderfrequency = models.IntegerField(db_column='reminderFrequency', blank=True, null=True)  # Field name made lowercase.
    reminderrepeatevery = models.IntegerField(db_column='reminderRepeatEvery', blank=True, null=True)  # Field name made lowercase.
    reminderendingtype = models.IntegerField(db_column='reminderEndingType', blank=True, null=True)  # Field name made lowercase.
    reminderstartdate = models.DateTimeField(db_column='reminderStartDate', blank=True, null=True)  # Field name made lowercase.
    reminderenddate = models.DateTimeField(db_column='reminderEndDate', blank=True, null=True)  # Field name made lowercase.
    reminderafternoofoccurences = models.IntegerField(db_column='reminderAfterNoOfOccurences', blank=True, null=True)  # Field name made lowercase.
    reminderautomaticlogtransaction = models.IntegerField(db_column='reminderAutomaticLogTransaction', blank=True, null=True)  # Field name made lowercase.
    reminderrepeating = models.IntegerField(db_column='reminderRepeating', blank=True, null=True)  # Field name made lowercase.
    reminderrepeatbydayofmonth = models.IntegerField(db_column='reminderRepeatByDayOfMonth', blank=True, null=True)  # Field name made lowercase.
    reminderexcludeweekend = models.IntegerField(db_column='reminderExcludeWeekend', blank=True, null=True)  # Field name made lowercase.
    reminderweekdaymovesetting = models.IntegerField(db_column='reminderWeekDayMoveSetting', blank=True, null=True)  # Field name made lowercase.
    reminderunbilled = models.IntegerField(db_column='reminderUnbilled', blank=True, null=True)  # Field name made lowercase.
    creditcardinstallment = models.IntegerField(db_column='creditCardInstallment', blank=True, null=True)  # Field name made lowercase.
    reminderversion = models.IntegerField(db_column='reminderVersion', blank=True, null=True)  # Field name made lowercase.
    dataextracolumnstring1 = models.CharField(db_column='dataExtraColumnString1', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRANSACTIONSTABLE'
        verbose_name = 'Транзакции'
        verbose_name_plural = 'Транзакции'
        ordering = ['-date']

    def __str__(self):
        return str(self.transactionstableid)


class Transactiontypetable(models.Model):
    transactiontypetableid = models.AutoField(db_column='transactionTypeTableID', blank=True, primary_key=True)  # Field name made lowercase.
    transactiontypename = models.CharField(db_column='transactionTypeName', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRANSACTIONTYPETABLE'

    def __str__(self):
        return self.transactiontypename


class AndroidMetadata(models.Model):
    locale = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'android_metadata'