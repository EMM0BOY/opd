import unittest
from flask import Flask
from flask_testing import TestCase
from flask1 import app
class QuadraticEquationSolverTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    def test_solve_quadratic_equation_two_real_roots(self):
        response = self.client.post('/solve', data=dict(a='1', b='0', c='-4'))
        self.assert200(response)
        self.assertIn('Корни уравнения: x1 = 2.0, x2 = -2.0', response.data.decode('utf-8'))
    def test_solve_quadratic_equation_one_real_root(self):
        response = self.client.post('/solve', data=dict(a='3', b='6', c='3'))
        self.assert200(response)
        self.assertIn('Уравнение имеет один корень: x = -1.0', response.data.decode('utf-8'))
    def test_solve_quadratic_equation_complex_roots(self):
        response = self.client.post('/solve', data=dict(a='1', b='1', c='1'))
        self.assert200(response)
        self.assertIn('Корни уравнения: x1 = -0.5 + 0.8660254037844386i, x2 = -0.5 - 0.8660254037844386i', response.data.decode('utf-8'))
if __name__ == '__main__':
    unittest.main()
