# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-15 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rgbz', '0014_auto_20180511_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gemeentelijkeopenbareruimteobject',
            name='type_openbare_ruimte',
            field=models.CharField(blank=True, choices=[('weg', 'weg'), ('water', 'water'), ('spoorbaan', 'spoorbaan'), ('terrein', 'terrein'), ('kunstwerk', 'kunstwerk'), ('landschappelijk gebied', 'landschappelijk gebied'), ('functioneel gebied', 'functioneel gebied'), ('administratief gebied', 'administratief gebied')], help_text='De aard van de als zodanig benoemde OPENBARERUIMTE.', max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='huishoudenobject',
            name='huishoudensoort',
            field=models.CharField(blank=True, choices=[('1', 'institutioneel huishouden'), ('2', 'alleenstaand (inclusief andere personen die in hetzelfde object wonen, maar een eigen huishouding voeren)'), ('3', '2 personen, vaste partners, geen thuiswonende kinderen'), ('4', '2 personen, vaste partners, een of meer thuiswonende kinderen'), ('5', 'eenoudergezin, ouder met een of meer thuiswonende kinderen'), ('6', 'overig particulier huishouden (samenwoning van personen die geen partnerrelatie onderhouden of een ouder-kindrelatie hebben, maar wel gezamenlijk een huishouding voeren)')], help_text='Typering van het huishouden naar grootte en verbondenheid.', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='openbareruimteobject',
            name='type_openbare_ruimte',
            field=models.CharField(blank=True, choices=[('weg', 'weg'), ('water', 'water'), ('spoorbaan', 'spoorbaan'), ('terrein', 'terrein'), ('kunstwerk', 'kunstwerk'), ('landschappelijk gebied', 'landschappelijk gebied'), ('functioneel gebied', 'functioneel gebied'), ('administratief gebied', 'administratief gebied')], help_text='De aard van de als zodanig benoemde OPENBARERUIMTE.', max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='wozdeelobject',
            name='woz_objectnummer',
            field=models.CharField(blank=True, help_text='De unieke aanduiding van een WOZ-OBJECT.', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='wozobject',
            name='soortobjectcode',
            field=models.ForeignKey(help_text='Aanduiding van het soort object ten behoeve van een correcte bepaling van de waarde.', null=True, on_delete=django.db.models.deletion.CASCADE, to='rsgb.SoortWOZObject'),
        ),
        migrations.AlterField(
            model_name='wozwaardeobject',
            name='vastgestelde_waarde',
            field=models.CharField(blank=True, help_text='Waarde van het WOZ-object zoals deze in het kader van de Wet WOZ is vastgesteld.', max_length=11, null=True),
        ),
    ]