# Generated by Django 5.1.1 on 2024-10-11 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anexoaula',
            name='extensao',
            field=models.CharField(choices=[('PDF', 'PDF'), ('JPG', 'JPG'), ('WAV', 'WAV')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='anexoaula',
            name='tipo',
            field=models.CharField(choices=[('A', 'arquivo'), ('F', 'foto'), ('S', 'áudio')], max_length=1),
        ),
        migrations.AlterField(
            model_name='anexocomentario',
            name='extensao',
            field=models.CharField(choices=[('PDF', 'PDF'), ('JPG', 'JPG'), ('WAV', 'WAV')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='anexocomentario',
            name='tipo',
            field=models.CharField(choices=[('A', 'arquivo'), ('F', 'foto'), ('S', 'áudio')], max_length=1),
        ),
    ]
