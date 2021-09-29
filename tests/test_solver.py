from unittest import TestCase

import pytest

from solver import add, square_equation_solver



def test_add():
    res = add(1, 2)
    assert res == 3

@pytest.mark.parametrize("args, expected_result", [
    ((1,2), 3),
    ((2,3), 5)
])
def test_add2(args, expected_result):
    res = add(*args)
    assert res == expected_result

class TestAddCase(TestCase):
    def test_ok(self):
        res = add(1, 2)
        self.assertEqual(res, 3)


class TestSquareEquationSolverUnitTests(TestCase):
    def test_checks_types(self):
        pass

    def test_raises_type_error(self):
        # try:
        #     square_equation_solver("", 1, 1.5)
        # except TypeError as e:
        #     print("Ok, errors", e)
        # else:
        #     self.fail("Did not raise")

        with self.assertRaises(TypeError):
            square_equation_solver("", 1, 1.5)

    def test_result_is_tuple(self):
        res = square_equation_solver(0, 0, 0)
        self.assertIsInstance(res, tuple)

    def test_no_results(self):
        res = square_equation_solver(0, 0, 1)
        self.assertEqual(res, (None, None))

    def test_solver_ok(self):
        res = square_equation_solver(1, -3, -4)
        self.assertEqual(res, (4, -1))


class TestSquareEquationSolver:
    def test_raises_type_error(self):
        with pytest.raises(TypeError) as exc_info:
            square_equation_solver("", 1, 1.5)
        print(exc_info)

    def test_result_is_tuple(self):
        res = square_equation_solver(0, 0, 0)
        assert isinstance(res, tuple)

    @pytest.mark.parametrize("args, expected_result", [
        ((1, -3, -4), (4, -1)),
        ((0, 0, 1), (None, None))
    ])
    def test_solves_ok(self, args, expected_result):
        res = square_equation_solver(*args)
        assert res == expected_result

    @pytest.mark.parametrize("args, expected_result", [
        pytest.param(
            (1, -3, -4), (4, -1),
            id="general"
        ),
        pytest.param(
            (0, 0, 1), (None, None),
            id="no results"
        ),
    ])
    def test_solves_ok2(self, args, expected_result):
        res = square_equation_solver(*args)
        assert res == expected_result