from django.db import models
from utils.models import BaseModel
from users.models import User


class Stadium(BaseModel):
    title = models.CharField(max_length=31)
    country = models.ForeignKey('Country', on_delete=models.CASCADE,
                                related_name='stadiums')
    capacity = models.IntegerField()

    def __str__(self):
        return self.title


MAN, WOMAN = ("Goal", "Yellow Card")

class Player(BaseModel):
    GENDER_TYPE = (
        ('MAN', 'Man'),
        ('WOMAN', 'woman'),

    )

    name = models.CharField(max_length=31)
    number = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE,
                             related_name='players')
    gender = models.CharField(max_length=1, choices=GENDER_TYPE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE,
                                related_name='country_players')

    def __str__(self):
        return self.name


class Referee(BaseModel):
    GENDER_TYPE = (
        ('MAN', 'Man'),
        ('WOMAN', 'woman'),

    )

    name = models.CharField(max_length=31)
    gender = models.CharField(max_length=1, choices=GENDER_TYPE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE,
                                related_name='country_players')

    def __str__(self):
        return self.name


class Country(BaseModel):
    title = models.CharField(max_length=31)
    flag = models.ImageField(upload_to='images/countries/')

    def __str__(self):
        return self.title


class League(BaseModel):
    title = models.CharField(max_length=31)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name='countries', blank=True, null=True)
    image = models.ImageField(upload_to='images/leagues/')
    is_pin = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Team(BaseModel):
    title = models.CharField(max_length=31)
    image = models.ImageField(upload_to='images/teams/')
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name='teams')

    def __str__(self):
        return self.title


class Transfer(BaseModel):
    from_team = models.ForeignKey(Team, on_delete=models.CASCADE,
                              related_name='tf_team')
    to_team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                related_name='tf_team')
    player = models.ForeignKey(Player, on_delete=models.CASCADE,
                               related_name='tf_player')
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                  related_name='home_matches')
    guest_team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                  related_name='away_matches')
    league = models.ForeignKey(League, on_delete=models.CASCADE,
                               related_name='league_matches')
    date = models.DateTimeField()

    def __str__(self):
        return self.home_team.id


class News(BaseModel):
    title = models.TextField()
    image = models.ImageField(upload_to='images/news/')
    league = models.ForeignKey(League, on_delete=models.CASCADE,
                               related_name='news')
    content = models.TextField()
    related_articles = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.title


class MatchStatistics(BaseModel):
    yellow_card = models.ForeignKey('YellowCard', on_delete=models.CASCADE,
                                    related_name='ms_ycard')
    red_card = models.ForeignKey('RedCard', on_delete=models.CASCADE,
                                    related_name='ms_ccard')
    replace_player = models.ForeignKey('ReplacePlayer', on_delete=models.CASCADE,
                                       related_name='ms_rpplayer')
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE,
                                related_name='ms_referee')
    stadium = models.ManyToManyField(Stadium)
    attendance = models.IntegerField()
    round = models.IntegerField()
    result = models.ForeignKey('GoalsOfTeam', on_delete=models.CASCADE,
                               related_name='match_results')


class YellowCard(BaseModel):
    match = models.ForeignKey(Match, on_delete=models.CASCADE,
                              related_name='yc_match')
    player = models.ForeignKey(Player, on_delete=models.CASCADE,
                              related_name='yc_player')


class RedCard(BaseModel):
    match = models.ForeignKey(Match, on_delete=models.CASCADE,
                              related_name='rc_match')
    player = models.ForeignKey(Player, on_delete=models.CASCADE,
                              related_name='rc_player')


class ReplacePlayer(BaseModel):
    match = models.ForeignKey(Match, on_delete=models.CASCADE,
                              related_name='rp_match')
    from_player = models.ForeignKey(Player, on_delete=models.CASCADE,
                              related_name='rp_player')
    to_player = models.ForeignKey(Player, on_delete=models.CASCADE,
                                    related_name='rp2_player')


class FavoritesMatch(BaseModel):
    match = models.ForeignKey(Match, on_delete=models.CASCADE,
                              related_name='favorites_matches')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='FM_users')

    def __str__(self):
        return self.match.id


class MyTeams(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='MT_users')
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                             related_name='MT_teams')

    def __str__(self):
        return self.user


class Standings(BaseModel):
    league = models.ForeignKey(League, on_delete=models.CASCADE,
                               related_name='standings_league')
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                             related_name='standings_team')

    matches_played = models.ForeignKey('MatchesPlayed', on_delete=models.CASCADE,
                                       related_name='St_matches')
    wins = models.ForeignKey('Wins', on_delete=models.CASCADE,
                                       related_name='St_winners')
    draws = models.ForeignKey('Draws', on_delete=models.CASCADE,
                                       related_name='St_draws')

    losses = models.ForeignKey('Losses', on_delete=models.CASCADE,
                                       related_name='St_losses')
    goals = models.ForeignKey('GoalsOfTeam', on_delete=models.CASCADE,
                              related_name='standings_goal')

    antigoals = models.PositiveSmallIntegerField()
    points = models.ForeignKey('Points', on_delete=models.CASCADE,
                               related_name='ST_points')

    def __str__(self):
        return self.league.id


class MatchesPlayed(BaseModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                  related_name='MT_teams')
    amount = models.IntegerField()


class Points(BaseModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                  related_name='PT_teams')
    amount = models.IntegerField()


class Wins(BaseModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                  related_name='W_teams')
    amount = models.IntegerField()


class Draws(BaseModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                  related_name='D_teams')
    amount = models.IntegerField()


class Losses(BaseModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                                  related_name='L_teams')
    amount = models.IntegerField()


class GoalsOfTeam(BaseModel):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE,
                               related_name='GT_players')
    guest_team = models.ForeignKey(Team, on_delete=models.CASCADE,
                             related_name='GT2_players')
    league = models.ForeignKey(League, on_delete=models.CASCADE,
                               related_name='GT_leagues')
    amount = models.PositiveSmallIntegerField()


class GoalsOfPlayer(BaseModel):
    player = models.ForeignKey(Player, on_delete=models.CASCADE,
                               related_name='G_players')
    league = models.ForeignKey(League, on_delete=models.CASCADE,
                               related_name='G_leagues')
    amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.player.id


class AssistsOfPlayer(BaseModel):
    player = models.ForeignKey(Player, on_delete=models.CASCADE,
                               related_name='AS_players')
    league = models.ForeignKey(League, on_delete=models.CASCADE,
                               related_name='AS_leagues')
    goals = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.player.id


class MatchPlayers(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE,
                              related_name='MP_matches')
    player = models.ForeignKey(Player, on_delete=models.CASCADE,
                               related_name='MP_players')
    join_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['match', 'player']

    def __str__(self):
        return self.match.id


GOAL, YELLOW_CARD, RED_CARD, FOUL, AUTOGOAL, PENALTY, OUT_OF_MATCH = (
    "Goal", "Yellow Card", "Red Card", "Foul", "Autogoal", "Penalty", "Out of the match"
)


class MatchEvents(models.Model):
    EVENT_TYPES = (
        ('GOAL', 'Goal'),
        ('YELLOW_CARD', 'Yellow Card'),
        ('RED_CARD', 'Red Card'),
        ('FOUL', 'Foul'),
        ('AUTOGOAL', 'Autogoal'),
        ('PENALTY', 'Penalty'),
        ('OUT_OF_MATCH', 'Out of the match'),
    )
    type = models.CharField(max_length=1, choices=EVENT_TYPES)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return self.match.id














