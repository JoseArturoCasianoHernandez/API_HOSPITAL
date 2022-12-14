# Generated by Django 4.0.5 on 2022-06-12 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellidos')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumeroSeguro', models.DecimalField(decimal_places=4, max_digits=4, verbose_name='NumeroSeguro')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellidos')),
            ],
        ),
        migrations.CreateModel(
            name='VisitaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DiagnosticoEnfermedad', models.CharField(max_length=500, verbose_name='Diagnostico de Enfermedad')),
                ('FechadeVisita', models.DateTimeField(verbose_name='Fecha de visita')),
                ('Medico', models.CharField(max_length=100, verbose_name='Médico')),
                ('PacienteCama', models.DateField(verbose_name='Paciente Cama')),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('NumeroCamas', models.DateField(verbose_name='Número Camas')),
                ('IDPlanta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.planta', verbose_name='Planta')),
            ],
        ),
        migrations.CreateModel(
            name='PacienteCama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaAsignacion', models.DateTimeField(verbose_name='FechaAsignacion')),
                ('Cama', models.DateField(verbose_name='Cama')),
                ('IDPacienteCama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.pacientecama', verbose_name='ID Paciente Cama')),
            ],
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaEntrada', models.DateTimeField(verbose_name='FechaEntrada')),
                ('FechaSalida', models.DateTimeField(verbose_name='FechaSalida')),
                ('IDHistoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.historia', verbose_name='ID Historia')),
            ],
        ),
        migrations.CreateModel(
            name='Cama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Planta', models.DateField(verbose_name='Planta')),
                ('IDCama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.cama', verbose_name='Cama')),
            ],
        ),
    ]
