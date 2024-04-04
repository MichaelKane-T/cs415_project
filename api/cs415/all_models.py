# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=35, blank=True, null=True)
    second_name = models.CharField(max_length=35, blank=True, null=True)
    points_per_game = models.IntegerField(blank=True, null=True)
    total_points = models.IntegerField(blank=True, null=True)
    goals_scored = models.IntegerField(blank=True, null=True)
    team = models.ForeignKey('Team', models.DO_NOTHING)
    assists = models.IntegerField(blank=True, null=True)
    form = models.IntegerField(blank=True, null=True)
    clean_sheets = models.IntegerField(blank=True, null=True)
    chance_of_playing_next_round = models.IntegerField(blank=True, null=True)
    yellow_cards = models.IntegerField(blank=True, null=True)
    red_cards = models.IntegerField(blank=True, null=True)
    saves = models.IntegerField(blank=True, null=True)
    penalties_missed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Player'


class Team(models.Model):
    team_name = models.CharField(max_length=35, blank=True, null=True)
    team_points = models.IntegerField(blank=True, null=True)
    log_position = models.IntegerField(blank=True, null=True)
    team_form = models.FloatField(blank=True, null=True)
    strength_overall_home = models.FloatField(blank=True, null=True)
    strength_overall_away = models.FloatField(blank=True, null=True)
    win = models.IntegerField(blank=True, null=True)
    loss = models.IntegerField(blank=True, null=True)
    draw = models.IntegerField(blank=True, null=True)
    team_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Team'


class User(models.Model):
    first_name = models.CharField(max_length=35, blank=True, null=True)
    second_name = models.CharField(max_length=35, blank=True, null=True)
    pass_word = models.CharField(max_length=35, blank=True, null=True)
    recovery_key = models.CharField(max_length=35, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=35, blank=True, null=True)
    user_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'User'


class Useraddress(models.Model):
    address_1 = models.CharField(db_column='Address_1', max_length=35, blank=True, null=True)  # Field name made lowercase.
    address_2 = models.CharField(db_column='Address_2', max_length=35, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=35, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING)
    zip = models.CharField(db_column='Zip', max_length=35, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=35, blank=True, null=True)  # Field name made lowercase.
    last_date_updated = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=35, blank=True, null=True)
    user_address_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'UserAddress'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
