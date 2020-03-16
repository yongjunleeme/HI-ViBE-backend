# Generated by Django 3.0.4 on 2020-03-18 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.URLField(max_length=2000, null=True)),
                ('release_date', models.DateField(null=True)),
                ('description', models.TextField(null=True)),
                ('production_name', models.CharField(max_length=200, null=True)),
                ('agency_name', models.CharField(max_length=200, null=True)),
                ('is_regular', models.BooleanField(default=False)),
                ('like_count', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'albums',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField(max_length=2000, null=True)),
                ('debut_date', models.DateField(null=True)),
                ('birth_country', models.CharField(max_length=50, null=True)),
                ('nationality', models.CharField(max_length=50, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('is_group', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'artists',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge', models.URLField(max_length=2000, null=True)),
                ('thumbnail', models.URLField(max_length=2000)),
                ('release_date', models.DateField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'magazines',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.URLField(max_length=2000)),
                ('track_number', models.IntegerField(default=1)),
                ('writer', models.CharField(max_length=600, null=True)),
                ('composer', models.CharField(max_length=600, null=True)),
                ('arranger', models.CharField(max_length=600, null=True)),
                ('lyrics', models.TextField(null=True)),
                ('play_time', models.TimeField(null=True)),
                ('like_count', models.IntegerField(null=True)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Album')),
            ],
            options={
                'db_table': 'musics',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=100)),
                ('main_image', models.URLField(max_length=2000)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'recommendations',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'db_table': 'stations',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('creator', models.CharField(max_length=30)),
                ('charge', models.CharField(max_length=10)),
                ('main_image', models.URLField(max_length=2000, null=True)),
            ],
            options={
                'db_table': 'themes',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('main_image', models.URLField(max_length=2000)),
                ('content', models.URLField(max_length=2000, null=True)),
                ('release_date', models.DateField()),
                ('views', models.IntegerField(null=True)),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Music')),
            ],
            options={
                'db_table': 'videos',
            },
        ),
        migrations.CreateModel(
            name='StationTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=2000)),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Station')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Theme')),
            ],
            options={
                'db_table': 'station_themes',
            },
        ),
        migrations.CreateModel(
            name='StationMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Music')),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Station')),
            ],
            options={
                'db_table': 'station_musics',
            },
        ),
        migrations.AddField(
            model_name='station',
            name='music',
            field=models.ManyToManyField(through='music.StationMusic', to='music.Music'),
        ),
        migrations.AddField(
            model_name='station',
            name='theme',
            field=models.ManyToManyField(through='music.StationTheme', to='music.Theme'),
        ),
        migrations.CreateModel(
            name='SimilarArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='base_artist', to='music.Artist')),
                ('similar_artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar_artist', to='music.Artist')),
            ],
            options={
                'db_table': 'similar_artists',
                'unique_together': {('base_artist', 'similar_artist')},
            },
        ),
        migrations.CreateModel(
            name='RecommendationMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Music')),
                ('recommendation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Recommendation')),
            ],
            options={
                'db_table': 'recommendation_musics',
            },
        ),
        migrations.AddField(
            model_name='recommendation',
            name='music',
            field=models.ManyToManyField(through='music.RecommendationMusic', to='music.Music'),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.URLField(max_length=2000)),
                ('main_text', models.TextField()),
                ('news_link', models.URLField(max_length=2000)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Artist')),
            ],
            options={
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='MusicMagazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magazine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Magazine')),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Music')),
            ],
            options={
                'db_table': 'music_magazines',
            },
        ),
        migrations.AddField(
            model_name='magazine',
            name='music',
            field=models.ManyToManyField(through='music.MusicMagazine', to='music.Music'),
        ),
        migrations.CreateModel(
            name='GenreAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Album')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Genre')),
            ],
            options={
                'db_table': 'genre_albums',
            },
        ),
        migrations.CreateModel(
            name='ArtistVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Artist')),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Video')),
            ],
            options={
                'db_table': 'artist_videos',
            },
        ),
        migrations.CreateModel(
            name='ArtistMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Artist')),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Music')),
            ],
            options={
                'db_table': 'artist_musics',
            },
        ),
        migrations.CreateModel(
            name='ArtistGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Artist')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Genre')),
            ],
            options={
                'db_table': 'artist_genres',
            },
        ),
        migrations.CreateModel(
            name='ArtistAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Album')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Artist')),
            ],
            options={
                'db_table': 'artist_albums',
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='album',
            field=models.ManyToManyField(through='music.ArtistAlbum', to='music.Album'),
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ManyToManyField(through='music.ArtistGenre', to='music.Genre'),
        ),
        migrations.AddField(
            model_name='artist',
            name='music',
            field=models.ManyToManyField(through='music.ArtistMusic', to='music.Music'),
        ),
        migrations.AddField(
            model_name='artist',
            name='similar_ralation',
            field=models.ManyToManyField(through='music.SimilarArtist', to='music.Artist'),
        ),
        migrations.AddField(
            model_name='artist',
            name='video',
            field=models.ManyToManyField(through='music.ArtistVideo', to='music.Video'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(through='music.GenreAlbum', to='music.Genre'),
        ),
    ]
