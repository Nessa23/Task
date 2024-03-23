import unittest

class TestGetScore(unittest.TestCase):
    def setUp(self):
        self.game_stamps = generate_game()

    def test_get_score_beginning(self):
        home_score, away_score = get_score(self.game_stamps, 0)
        self.assertEqual(home_score, 0)
        self.assertEqual(away_score, 0)

    def test_get_score_middle(self):
        offset = self.game_stamps[len(self.game_stamps) // 2]["offset"]
        home_score, away_score = get_score(self.game_stamps, offset)
        expected_home_score = self.game_stamps[len(self.game_stamps) // 2]["score"]["home"]
        expected_away_score = self.game_stamps[len(self.game_stamps) // 2]["score"]["away"]
        self.assertEqual(home_score, expected_home_score)
        self.assertEqual(away_score, expected_away_score)

    def test_get_score_end(self):
        offset = self.game_stamps[-1]["offset"]
        home_score, away_score = get_score(self.game_stamps, offset)
        expected_home_score = self.game_stamps[-1]["score"]["home"]
        expected_away_score = self.game_stamps[-1]["score"]["away"]
        self.assertEqual(home_score, expected_home_score)
        self.assertEqual(away_score, expected_away_score)

    def test_get_score_random(self):
        offset = random.randint(0, self.game_stamps[-1]["offset"])
        home_score, away_score = get_score(self.game_stamps, offset)
        index = next(i for i, stamp in enumerate(self.game_stamps) if stamp["offset"] > offset) - 1
        expected_home_score = self.game_stamps[index]["score"]["home"]
        expected_away_score = self.game_stamps[index]["score"]["away"]
        self.assertEqual(home_score, expected_home_score)
        self.assertEqual(away_score, expected_away_score)

if __name__ == "__main__":
    unittest.main()
