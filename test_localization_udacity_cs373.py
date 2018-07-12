from localization_udacity_cs373 import move, sense, localize


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
    left_top_p = [
        [1.0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    left_bottom_p = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1.0, 0, 0, 0, 0],
    ]
    right_top_p = [
        [0, 0, 0, 0, 1.0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    right_bottom_p = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1.0],
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
    move_left_by_1 = [0, -1]
    move_right_by_1 = [0, 1]
    move_up_by_1 = [-1, 0]
    move_down_by_1 = [1, 0]
    p_exact_move = 1.0
    p_inexact_move = 0.825
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

    def test_border_move(self):
        assert move(self.left_top_p, self.move_left_by_1, self.p_exact_move) == self.right_top_p
        assert move(self.left_top_p, self.move_up_by_1, self.p_exact_move) == self.left_bottom_p
        assert move(self.right_top_p, self.move_up_by_1, self.p_exact_move) == self.right_bottom_p
        assert move(self.right_top_p, self.move_right_by_1, self.p_exact_move) == self.left_top_p
        assert move(self.left_bottom_p, self.move_left_by_1, self.p_exact_move) == self.right_bottom_p
        assert move(self.left_bottom_p, self.move_down_by_1, self.p_exact_move) == self.left_top_p
        assert move(self.right_bottom_p, self.move_right_by_1, self.p_exact_move) == self.left_bottom_p
        assert move(self.right_bottom_p, self.move_down_by_1, self.p_exact_move) == self.right_top_p


class TestSense(object):
    colors = [['R', 'G', 'G', 'R', 'R'],
              ['R', 'R', 'G', 'R', 'R'],
              ['R', 'R', 'G', 'G', 'R'],
              ['R', 'R', 'R', 'R', 'R']]
    p_init = 1.0 / float(len(colors)) / float(len(colors[0]))
    uniform_p = [[p_init for _ in range(len(colors[0]))] for _ in range(len(colors))]
    exact_sense = 1.0
    inexact_sense = 0.8
    exact_sense_p = [
        [0, 0.2, 0.2, 0, 0],
        [0, 0, 0.2, 0, 0],
        [0, 0, 0.2, 0.2, 0],
        [0, 0, 0, 0, 0],
    ]

    def test_exact_sense(self):
        assert sense(self.uniform_p, 'G', self.colors, self.exact_sense) == self.exact_sense_p


class TestLocalize(object):
    colors1 = [['G', 'G', 'G'],
               ['G', 'R', 'G'],
               ['G', 'G', 'G']]
    p1 = [[0.0, 0.0, 0.0],
          [0.0, 1.0, 0.0],
          [0.0, 0.0, 0.0]]
    colors2 = [['G', 'G', 'G'],
               ['G', 'R', 'R'],
               ['G', 'G', 'G']]
    p2 = [[0.0, 0.0, 0.0],
          [0.0, 0.5, 0.5],
          [0.0, 0.0, 0.0]]
    p3 = [[0.06666666666666665, 0.06666666666666665, 0.06666666666666665],
          [0.06666666666666665, 0.2666666666666667, 0.2666666666666667],
          [0.06666666666666665, 0.06666666666666665, 0.06666666666666665]]
    p4 = [[0.03333333333333332, 0.03333333333333332, 0.03333333333333332],
          [0.1333333333333333, 0.1333333333333333, 0.5333333333333334],
          [0.03333333333333332, 0.03333333333333332, 0.03333333333333332]]
    p5 = [[0.0, 0.0, 0.0],
          [0.0, 0.0, 1.0],
          [0.0, 0.0, 0.0]]
    p6 = [[0.028985507246376798, 0.028985507246376798, 0.028985507246376798],
          [0.07246376811594203, 0.2898550724637682, 0.46376811594202905],
          [0.028985507246376798, 0.028985507246376798, 0.028985507246376798]]
    p7 = [[0.0, 0.0, 0.0],
          [0.0, 0.3333333333333333, 0.6666666666666666],
          [0.0, 0.0, 0.0]]
    measurements = ['R']
    measurements4 = ['R', 'R']
    motions = [[0, 0]]
    motions4 = [[0, 0], [0, 1]]
    sensor_right = 1.0
    sensor_right3 = 0.8
    p_move = 1.0
    p_move6 = 0.5

    def test1(self):
        assert localize(self.colors1, self.measurements, self.motions, self.sensor_right, self.p_move) == self.p1

    def test2(self):
        assert localize(self.colors2, self.measurements, self.motions, self.sensor_right, self.p_move) == self.p2

    def test3(self):
        assert localize(self.colors2, self.measurements, self.motions, self.sensor_right3, self.p_move) == self.p3

    def test4(self):
        assert localize(self.colors2, self.measurements4, self.motions4, self.sensor_right3, self.p_move) == self.p4

    def test5(self):
        assert localize(self.colors2, self.measurements4, self.motions4, self.sensor_right, self.p_move) == self.p5

    def test6(self):
        assert localize(self.colors2, self.measurements4, self.motions4, self.sensor_right3, self.p_move6) == self.p6

    def test7(self):
        assert localize(self.colors2, self.measurements4, self.motions4, self.sensor_right, self.p_move6) == self.p7
