import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_finds_player(self):
        player = self.stats.search("Semenko")
        self.assertEqual(str(player), "Semenko EDM 4 + 12 = 16")
    
    def test_search_player_not_found_is_none(self):
        player = self.stats.search("None")
        self.assertAlmostEqual(player, None)
    
    def test_team_returns_correct_number_of_players(self):
        team = self.stats.team("EDM")
        self.assertAlmostEqual(len(team), 3)
    
    def test_empty_team_is_zero(self):
        team = self.stats.team("None")
        self.assertAlmostEqual(len(team), 0)
    
    def test_top_by_points(self):
        top = self.stats.top(1)
        self.assertEqual(str(top[0]), "Gretzky EDM 35 + 89 = 124")
    
    def test_top_by_goals(self):
        top = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(str(top[0]), "Lemieux PIT 45 + 54 = 99")
    
    def test_top_by_assists(self):
        top = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(str(top[0]), "Gretzky EDM 35 + 89 = 124")