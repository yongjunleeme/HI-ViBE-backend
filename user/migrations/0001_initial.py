# Generated by Django 3.0.4 on 2020-03-11 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'memberships',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'playlists',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naver_id', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('image', models.URLField(max_length=2000)),
                ('gender', models.CharField(max_length=5)),
                ('birthday', models.DateField()),
                ('expiry_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('membership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Membership')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='StationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Station')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'station_histories',
            },
        ),
        migrations.CreateModel(
            name='PlaylistMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Artist')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Genre')),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Music')),
                ('playlist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Playlist')),
            ],
            options={
                'db_table': 'playlist_musics',
            },
        ),
        migrations.AddField(
            model_name='playlist',
            name='music',
            field=models.ManyToManyField(through='user.PlaylistMusic', to='music.Music'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
        migrations.CreateModel(
            name='MusicLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Music')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'music_likes',
            },
        ),
        migrations.CreateModel(
            name='MusicHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Album')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Artist')),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Music')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'music_histories',
            },
        ),
        migrations.CreateModel(
            name='ArtistLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Artist')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'artist_likes',
            },
        ),
        migrations.CreateModel(
            name='AlbumLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Album')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'album_likes',
            },
        ),
    ]
