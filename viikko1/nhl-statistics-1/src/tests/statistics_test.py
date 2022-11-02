import unittest
from statistics import Statistics
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

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_haku_palauttaa_pelaajan(self):
        self.assertEqual(self.statistics.search("Semenko").name,
        self.statistics._players[0].name)

    def test_haku_ei_palauta_mitaan(self):
        self.assertEqual(self.statistics.search("Antonio"), None)

    def test_tiimit_palauttaa_oikean_maaran_pelaajia(self):
        tiimi = self.statistics.team("EDM")
        self.assertEqual(len(tiimi), 3)

    def test_top_1_palauttaa_yhden(self):
        top = self.statistics.top(1)
        self.assertEqual(len(top), 1)

    def test_top_1_points_palauttaa_oikean(self):
        top = self.statistics.top(1, 1)
        self.assertEqual(top[0], self.statistics._players[4])

    def test_top_1_goals_palauttaa_oikean(self):
        top = self.statistics.top(1, 2)
        self.assertEqual(top[0], self.statistics._players[1])

    def test_top_1_assists_palauttaa_oikean(self):
        top = self.statistics.top(1, 3)
        self.assertEqual(top[0], self.statistics._players[4])