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

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


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

    def __str__(self):
        return f'{self.team_name} {self.team_id}'


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
    def __str__(self):
        return f'{self.first_name} {self.second_name}'


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

    def __str__(self):
        return f'{self.address_1} {self.country}'

class Pagedata(models.Model):
    page_data_id = models.AutoField(primary_key=True)
    page_name = models.CharField(max_length=25)
    page_title = models.CharField(max_length=25)
    page_description = models.CharField(max_length=150)
    page_picture = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PageData'

    def __str__(self):
        return f'{self.page_name}'
    
class UserInfo(models.Model):
    user_info_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    profile_bio = models.CharField(max_length=500, blank=True, null=True)
    profile_picture = models.CharField(max_length=100, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserInfo'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.profile_bio}'
    
class Phonetype(models.Model):
    phone_type_id = models.AutoField(primary_key=True)
    phone_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'PhoneType'

    def __str__(self):
        return f'{self.phone_type}'
    
class Userphone(models.Model):
    user_phone_id = models.AutoField(primary_key=True)
    phone_type = models.ForeignKey(Phonetype, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserPhone'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.phone_type.phone_type}'
    
class Addresstype(models.Model):
    address_type_id = models.AutoField(primary_key=True)
    address_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'AddressType'

    def __str__(self):
        return f'{self.address_type}'