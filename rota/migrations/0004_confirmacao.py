# Generated by Django 5.1.6 on 2025-04-15 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rota', '0003_rota_veiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmada', models.BooleanField(default=False)),
                ('data_confirmacao', models.DateTimeField(auto_now_add=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rota.alunos')),
                ('rota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rota.rota')),
            ],
        ),
    ]
