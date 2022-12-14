# Generated by Django 4.1.4 on 2022-12-08 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AmigoSecreto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao", models.CharField(max_length=50)),
                ("cod_amigosecreto", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Participante",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("id_amigo_sorteado", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Presente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao", models.CharField(max_length=20)),
                ("tamanho", models.CharField(blank=True, max_length=2)),
                ("observacao", models.TextField(blank=True)),
                (
                    "id_participante",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="amigosecreto.participante",
                    ),
                ),
            ],
        ),
    ]
