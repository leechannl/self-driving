from localization_udacity_cs373 import move


class TestMove(object):
    colors = [['R', 'G', 'G', 'R', 'R'],
              ['R', 'R', 'G', 'R', 'R'],
              ['R', 'R', 'G', 'G', 'R'],
              ['R', 'R', 'R', 'R', 'R']]
    p_init = 1.0 / float(len(colors)) / float(len(colors[0]))
    uniform_p = [[p_init for _ in range(len(colors[0]))] for _ in range(len(colors))]
    nonuniform_p = [
        [1.0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    nonuniform_p_after_move_right_by_1 = [
        [0, 1.0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    nonuniform_p_after_move_down_by_1 = [
        [0, 0, 0, 0, 0],
        [1.0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    move_right_by_1 = [0, 1]
    move_down_by_1 = [1, 0]
    p_exact_move = 1.0
    p_inexact_move = 0.8
    p_after_inexact_move_down_by_1 = [
        [1 - p_inexact_move, p_inexact_move, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    def test_uniform(self):
        assert move(self.uniform_p, self.move_right_by_1, self.p_exact_move) == self.uniform_p

    def test_nonuniform_move_right_by_1(self):
        assert move(self.nonuniform_p, self.move_right_by_1,
                    self.p_exact_move) == self.nonuniform_p_after_move_right_by_1

    def test_nonuniform_move_down_by_1(self):
        assert move(self.nonuniform_p, self.move_down_by_1, self.p_exact_move) == self.nonuniform_p_after_move_down_by_1

    def test_inexact_move(self):
        assert move(self.nonuniform_p, self.move_right_by_1,
                    self.p_inexact_move) == self.p_after_inexact_move_down_by_1
