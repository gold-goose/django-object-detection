# Generated by Django 3.2.12 on 2022-08-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InferrencedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('inf_image_path', models.CharField(blank=True, max_length=250, null=True)),
                ('detection_info', models.JSONField(blank=True, null=True)),
                ('yolo_model', models.CharField(blank=True, choices=[('yolov5s.pt', 'yolov5s.pt'), ('yolov5m.pt', 'yolov5m.pt'), ('yolov5l.pt', 'yolov5l.pt'), ('yolov5x.pt', 'yolov5x.pt')], help_text='Selected yolo model will download.                                  Requires an active internet connection.', max_length=250, null=True, verbose_name='YOLOV5 Models')),
                ('model_conf', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Model confidence')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]