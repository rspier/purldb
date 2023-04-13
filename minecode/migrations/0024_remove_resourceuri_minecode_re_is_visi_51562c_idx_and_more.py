# Generated by Django 4.1.2 on 2023-02-07 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "minecode",
            "0023_rename_minecode_r_is_visi_29fde2_idx_minecode_re_is_visi_51562c_idx_and_more",
        ),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="resourceuri",
            name="minecode_re_is_visi_51562c_idx",
        ),
        migrations.RemoveIndex(
            model_name="resourceuri",
            name="minecode_re_is_mapp_78700f_idx",
        ),
        migrations.AddField(
            model_name="resourceuri",
            name="has_map_error",
            field=models.BooleanField(
                db_index=True,
                default=False,
                help_text="When set to True (Yes), this field indicates that an error has occured when mapping this URI.",
            ),
        ),
        migrations.AddField(
            model_name="resourceuri",
            name="has_visit_error",
            field=models.BooleanField(
                db_index=True,
                default=False,
                help_text="When set to True (Yes), this field indicates that an error has occured when visiting this URI.",
            ),
        ),
        migrations.AddIndex(
            model_name="resourceuri",
            index=models.Index(
                fields=[
                    "is_visitable",
                    "last_visit_date",
                    "wip_date",
                    "has_visit_error",
                ],
                name="minecode_re_is_visi_5fc763_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="resourceuri",
            index=models.Index(
                fields=[
                    "is_mappable",
                    "last_visit_date",
                    "wip_date",
                    "last_map_date",
                    "has_visit_error",
                    "has_map_error",
                ],
                name="minecode_re_is_mapp_19780d_idx",
            ),
        ),
    ]