import json
import os
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch


fake_pyboy = types.ModuleType("pyboy")
fake_pyboy.PyBoy = object
fake_pyboy.logger = types.SimpleNamespace(log_level=lambda _level: None)
sys.modules.setdefault("pyboy", fake_pyboy)

from Control.coins import coinsPriceMet, getCoins, updateCoins
from Games.dfm import game_logic
from Games.highlow import evaluateBet


class DisplayStub:
    def __init__(self):
        self.config_calls = []

    def config(self, **kwargs):
        self.config_calls.append(kwargs)


class CoinStoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.old_cwd = os.getcwd()
        self.addCleanup(os.chdir, self.old_cwd)
        os.chdir(self.tmp.name)

        database = Path("Database")
        database.mkdir()
        (database / "users.json").write_text(
            json.dumps(
                {
                    "users": [
                        {"username": "rehan", "password": "secret", "coins": 9000},
                        {"username": "guest", "password": "guest", "coins": 500},
                    ]
                }
            ),
            encoding="utf-8",
        )

    def test_get_coins_returns_current_user_balance(self):
        self.assertEqual(getCoins("rehan"), 9000)
        self.assertEqual(getCoins("guest"), 500)

    def test_update_coins_persists_balance_and_updates_display(self):
        display = DisplayStub()

        updateCoins("rehan", 1200, display)

        self.assertEqual(getCoins("rehan"), 1200)
        self.assertEqual(display.config_calls[-1], {"text": "1,200"})
        self.assertTrue(Path("Database/rpg_rehan.txt").exists())

    def test_coins_price_met_spends_or_rejects_paid_games(self):
        display = DisplayStub()

        self.assertIsNone(coinsPriceMet("rehan", display))
        self.assertEqual(getCoins("rehan"), 1000)

        self.assertFalse(coinsPriceMet("guest", display))
        self.assertEqual(getCoins("guest"), 500)


class MiniGameLogicTests(unittest.TestCase):
    def test_duck_fish_mosquito_handles_exit_and_invalid_input(self):
        self.assertEqual(game_logic("exit"), "exit")
        self.assertEqual(game_logic("not-a-number"), "not_num")

        with patch("Games.dfm.random.randint", return_value=2):
            self.assertEqual(game_logic("4"), "out_of_range")

    def test_duck_fish_mosquito_outcomes_are_deterministic_when_random_is_patched(self):
        with patch("Games.dfm.random.randint", return_value=1):
            self.assertEqual(game_logic("1"), ("draw", 0, 0))

        with patch("Games.dfm.random.randint", return_value=2):
            self.assertEqual(game_logic("1"), ("usr_win", 1, 0))

        with patch("Games.dfm.random.randint", return_value=3):
            self.assertEqual(game_logic("1"), ("comp_win", 2, 0))

    def test_highlow_outcomes_are_deterministic_when_random_is_patched(self):
        output = StringIO()

        with redirect_stdout(output), patch("Games.highlow.random.randint", return_value=9):
            self.assertEqual(evaluateBet("h"), "usr_win")

        with redirect_stdout(output), patch("Games.highlow.random.randint", return_value=4):
            self.assertEqual(evaluateBet("h"), "usr_loss")

        with redirect_stdout(output), patch("Games.highlow.random.randint", return_value=7):
            self.assertEqual(evaluateBet("l"), "usr_loss")


if __name__ == "__main__":
    unittest.main()
