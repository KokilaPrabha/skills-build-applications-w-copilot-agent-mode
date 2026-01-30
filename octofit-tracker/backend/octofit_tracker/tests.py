from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel")
        self.user = User.objects.create(name="Iron Man", email="ironman@marvel.com", team=self.team)
        self.activity = Activity.objects.create(user=self.user, activity="Suit Training", duration=45)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)
        self.workout = Workout.objects.create(name="Agility Drills", suggested_for="Marvel")

    def test_user_creation(self):
        self.assertEqual(self.user.email, "ironman@marvel.com")

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Marvel")

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity, "Suit Training")

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 100)

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Agility Drills")
