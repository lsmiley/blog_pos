# Generated by Django 3.2.5 on 2021-12-10 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='administratortraining_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='administratortraining_transformationhours',
            field=models.FloatField(default='17.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='administratortraining_transformationhoursitem',
            field=models.FloatField(default='17.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='administratortraining_transitionhours',
            field=models.FloatField(default='20.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='administratortraining_transitionhoursitem',
            field=models.FloatField(default='20.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='createbestpracticecustom_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='createbestpracticecustom_transformationhours',
            field=models.FloatField(default='33.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='createbestpracticecustom_transformationhoursitem',
            field=models.FloatField(default='33.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='createbestpracticecustom_transitionhours',
            field=models.FloatField(default='40.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='createbestpracticecustom_transitionhoursitem',
            field=models.FloatField(default='40.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='customerreviewsignoff_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='customerreviewsignoff_transformationhours',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='customerreviewsignoff_transformationhoursitem',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='customerreviewsignoff_transitionhours',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='customerreviewsignoff_transitionhoursitem',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developprovideagentsoftware_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developprovideagentsoftware_transformationhours',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developprovideagentsoftware_transformationhoursitem',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developprovideagentsoftware_transitionhours',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developprovideagentsoftware_transitionhoursitem',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developserviceresponsibilitymatrix_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developserviceresponsibilitymatrix_transformationhours',
            field=models.FloatField(default='13.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developserviceresponsibilitymatrix_transformationhoursitem',
            field=models.FloatField(default='13.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developserviceresponsibilitymatrix_transitionhours',
            field=models.FloatField(default='16.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developserviceresponsibilitymatrix_transitionhoursitem',
            field=models.FloatField(default='16.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developworkflows_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developworkflows_transformationhours',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developworkflows_transformationhoursitem',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developworkflows_transitionhours',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='developworkflows_transitionhoursitem',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='establishanyneededserviceaccounts_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='establishanyneededserviceaccounts_transformationhours',
            field=models.FloatField(default='13.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='establishanyneededserviceaccounts_transformationhoursitem',
            field=models.FloatField(default='13.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='establishanyneededserviceaccounts_transitionhours',
            field=models.FloatField(default='16.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='establishanyneededserviceaccounts_transitionhoursitem',
            field=models.FloatField(default='16.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='establishhealthcheck_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='establishhealthcheck_transformationhours',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='establishhealthcheck_transformationhoursitem',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='establishhealthcheck_transitionhours',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='establishhealthcheck_transitionhoursitem',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='executetransitionplan_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='executetransitionplan_transformationhours',
            field=models.FloatField(default='250.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='executetransitionplan_transformationhoursitem',
            field=models.FloatField(default='250.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='executetransitionplan_transitionhours',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='executetransitionplan_transitionhoursitem',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='identifytestdocument_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='identifytestdocument_transformationhours',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='identifytestdocument_transformationhoursitem',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='identifytestdocument_transitionhours',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='identifytestdocument_transitionhoursitem',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigure_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigure_transformationhours',
            field=models.FloatField(default='33.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigure_transformationhoursitem',
            field=models.FloatField(default='33.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigure_transitionhours',
            field=models.FloatField(default='40.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigure_transitionhoursitem',
            field=models.FloatField(default='40.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigureodbc_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigureodbc_transformationhours',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigureodbc_transformationhoursitem',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigureodbc_transitionhours',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigureodbc_transitionhoursitem',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigureremoteconsoles_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigureremoteconsoles_transformationhours',
            field=models.FloatField(default='13.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigureremoteconsoles_transformationhoursitem',
            field=models.FloatField(default='13.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigureremoteconsoles_transitionhours',
            field=models.FloatField(default='16.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='installconfigureremoteconsoles_transitionhoursitem',
            field=models.FloatField(default='16.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='managementmod1stline',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='managementmod2ndline',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='numtransformationweeks',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='numtransitionweeks',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='obtainnetworkandosaccesswave1_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='obtainnetworkandosaccesswave1_transformationhours',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='obtainnetworkandosaccesswave1_transformationhoursitem',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='obtainnetworkandosaccesswave1_transitionhours',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='obtainnetworkandosaccesswave1_transitionhoursitem',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='obtainnetworkandosaccesswave2_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='obtainnetworkandosaccesswave2_transformationhours',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='obtainnetworkandosaccesswave2_transformationhoursitem',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='obtainnetworkandosaccesswave2_transitionhours',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='obtainnetworkandosaccesswave2_transitionhoursitem',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='operationaldocumentation_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='operationaldocumentation_transformationhours',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='operationaldocumentation_transformationhoursitem',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='operationaldocumentation_transitionhours',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='operationaldocumentation_transitionhoursitem',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='otherdetail_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='otherdetail_transformationhours',
            field=models.FloatField(default='208.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='otherdetail_transformationhoursitem',
            field=models.FloatField(default='208.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='otherdetail_transitionhours',
            field=models.FloatField(default='249.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='otherdetail_transitionhoursitem',
            field=models.FloatField(default='249.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='researchandsetupemailautomation_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='researchandsetupemailautomation_transformationhours',
            field=models.FloatField(default='13.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='researchandsetupemailautomation_transformationhoursitem',
            field=models.FloatField(default='13.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='researchandsetupemailautomation_transitionhours',
            field=models.FloatField(default='16.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='researchandsetupemailautomation_transitionhoursitem',
            field=models.FloatField(default='16.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='shadowestablishreviewallprocedures_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='shadowestablishreviewallprocedures_transformationhours',
            field=models.FloatField(default='50.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='shadowestablishreviewallprocedures_transformationhoursitem',
            field=models.FloatField(default='50.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='shadowestablishreviewallprocedures_transitionhours',
            field=models.FloatField(default='60.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='shadowestablishreviewallprocedures_transitionhoursitem',
            field=models.FloatField(default='60.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem1_count',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem1_transformationhours',
            field=models.FloatField(default='.0001'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem1_transformationhoursitem',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem1_transitionhours',
            field=models.FloatField(default='.0001'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem1_transitionhoursitem',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem2_count',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem2_transformationhours',
            field=models.FloatField(default='.0001'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem2_transformationhoursitem',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem2_transitionhours',
            field=models.FloatField(default='.0001'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem2_transitionhoursitem',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem3_count',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem3_transformationhours',
            field=models.FloatField(default='.0001'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem3_transformationhoursitem',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem3_transitionhours',
            field=models.FloatField(default='.0001'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem3_transitionhoursitem',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem4_count',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem4_transformationhours',
            field=models.FloatField(default='.0001'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem4_transformationhoursitem',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem4_transitionhours',
            field=models.FloatField(default='.0001'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem4_transitionhoursitem',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem5_count',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem5_transformationhours',
            field=models.FloatField(default='.0001'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem5_transformationhoursitem',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem5_transitionhours',
            field=models.FloatField(default='.0001'),
        ),
        migrations.AddField(
            model_name='order',
            name='specialitem5_transitionhoursitem',
            field=models.FloatField(default='.01'),
        ),
        migrations.AddField(
            model_name='order',
            name='staffingccoordinating_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='staffingccoordinating_transformationhours',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='staffingccoordinating_transformationhoursitem',
            field=models.FloatField(default='8.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='staffingccoordinating_transitionhours',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='staffingccoordinating_transitionhoursitem',
            field=models.FloatField(default='10.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='testinfrastructurepoc_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='testinfrastructurepoc_transformationhours',
            field=models.FloatField(default='33.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='testinfrastructurepoc_transformationhoursitem',
            field=models.FloatField(default='33.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='testinfrastructurepoc_transitionhours',
            field=models.FloatField(default='40.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='testinfrastructurepoc_transitionhoursitem',
            field=models.FloatField(default='40.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='tntdescription',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransformationhoursitem',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransformationtotal1stlinemgr',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransformationtotal2ndlinemgr',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransformationtotalband8',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransformationtotalfte',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransformationtotalhours',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransformationtotals',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransitionhoursitem',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransitiontotal1stlinemgr',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransitiontotal2ndlinemgr',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransitiontotalband8',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransitiontotalfte',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransitiontotalhours',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='totaltransitiontotals',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='tranformationsubtotalshours',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transformationfirstlinemanagementband8',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transformationfirstlinemanagementband8hours',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transformationfirstlinemanagementband8weeks',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transformationsecondlinemanagementband8',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transformationsecondlinemanagementband8weeks',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transformationsubtotalshoursitems',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transfortionhoursfte',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transitionfirstlinemanagementband8',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transitionfirstlinemanagementband8hours',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transitionfirstlinemanagementband8weeks',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transitionhoursfte',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transitionsecondlinemanagementband8',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transitionsecondlinemanagementband8weeks',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transitionsubtotalshours',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='transitionsubtotalshoursitems',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='troubleshoottune_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='troubleshoottune_transformationhours',
            field=models.FloatField(default='33.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='troubleshoottune_transformationhoursitem',
            field=models.FloatField(default='33.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='troubleshoottune_transitionhours',
            field=models.FloatField(default='40.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='troubleshoottune_transitionhoursitem',
            field=models.FloatField(default='40.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='workwithsecops_count',
            field=models.FloatField(default='1.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='workwithsecops_transformationhours',
            field=models.FloatField(default='13.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='workwithsecops_transformationhoursitem',
            field=models.FloatField(default='13.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='workwithsecops_transitionhours',
            field=models.FloatField(default='16.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='workwithsecops_transitionhoursitem',
            field=models.FloatField(default='16.0'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 12, 10, 15, 15, 21, 498311)),
        ),
    ]