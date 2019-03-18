import unittest
import Tic_Tac_Toe_Controller

class TestTicTacToe(unittest.TestCase):
    def test_Tic_Tac_Toe_Controller(self):
        self.gameController = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller()
        player1 = "Player Name 1"
        player2 = "Computer"
        self.gameController.init_players_data(player1)
        gamePlayer1 = self.gameController.getPlayer1()
        gamePlayer2 = self.gameController.getPlayer2()
        self.assertEqual(gamePlayer1, player1)
        self.assertEqual(gamePlayer2, player2)

    def test_newMove(self):
        self.gameController = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller()
        player1 = "Player Name 1"
        player2 = "Computer"
        cell_size = 160
        x = 150
        y = 150
        move = self.gameController.newMove(x, y, cell_size)
        self.assertEqual(move.movePlace["x"], 0)
        self.assertEqual(move.movePlace["y"], 0)

    def test_newMoveVsComputer(self):
        self.gameController = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller()
        player1 = "Player Name 1"
        player2 = "Computer"
        cell_size = 160
        move = self.gameController.newMoveVsComputer(cell_size)

        self.assertNotEqual(move["x"], -1)
        self.assertNotEqual(move["y"], -1)

    def test_get_player_start(self):
        self.gameController = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller()
        turn = self.gameController.gameData.get_player_start()
        self.assertGreaterEqual(turn, 0)
        self.assertLessEqual(turn, 1)

    def test_check_game_over_X(self):
        self.gameController = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller()
        squares = [[1, 1, 1],
                   [2, 0, 0],
                   [0, 2, 0]]
        self.gameController.gameData.board.squares = squares
        game_over = self.gameController.gameData.check_game_over()
        self.assertEqual(game_over, 1)

    def test_check_game_over_Y(self):
        self.gameController = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller()
        squares = [[1, 2, 1],
                   [2, 2, 1],
                   [1, 2, 0]]
        self.gameController.gameData.board.squares = squares
        game_over = self.gameController.gameData.check_game_over()
        self.assertEqual(game_over, 2)

    def test_check_game_over_D1(self):
        self.gameController = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller()
        squares = [[1, 2, 0],
                   [2, 1, 1],
                   [0, 2, 1]]
        self.gameController.gameData.board.squares = squares
        game_over = self.gameController.gameData.check_game_over()
        self.assertEqual(game_over, 1)

    def test_check_game_over_D2(self):
        self.gameController = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller()
        squares = [[1, 2, 2],
                   [1, 2, 1],
                   [2, 1, 1]]
        self.gameController.gameData.board.squares = squares
        game_over = self.gameController.gameData.check_game_over()
        self.assertEqual(game_over, 2)

    def test_check_game_over_Draw(self):
        self.gameController = Tic_Tac_Toe_Controller.Tic_Tac_Toe_Controller()
        squares = [[1, 2, 2],
                   [2, 1, 1],
                   [1, 1, 2]]
        self.gameController.gameData.board.squares = squares
        game_over = self.gameController.gameData.check_game_over()
        self.assertEqual(game_over, 0)

if __name__ == '__main__':
    unittest.main()