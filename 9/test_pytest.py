
import pytest
from unittest.mock import MagicMock, patch

from circle import Circle
import math

class TestCircle:
    def setup(self):
        self.circle = Circle(2)
        
    def test_diameter(self):
       assert self.circle.diameter == 4

    def test_area(self):
       assert self.circle.area == 4 * math.pi

    def test_no_radius(self):
       del self.circle.radius
       with pytest.raises(AttributeError):
            self.circle.diameter
            
    # parametrize - реализация паттерна тестирования data provider
    @pytest.mark.parametrize('radius, result', [(2, 4), (3, 6), (10, 20)], ids=['r=2', 'r=3', 'r=10'])
    def test_diameter_parametrized(self, radius, result):
        circle = Circle(radius)
        assert circle.diameter == result
        
    # можно подменять объекты на моки - своеобразыне заглушки
    # моки очень полезны если есть какие-либо нестабильные зависимости, например сеть
    @patch('circle.Circle.area', property(MagicMock(return_value=1)))
    def test_diameter_mocked(self):
        circle = Circle(10)
        assert circle.area == 1
        
    # monkeypatch - фикстура - заранее подготовленное состояние окружения тестирования, 
    # требуемое для гарантии повторяемости процесса
    def test_diameter_monkypatched(self, monkeypatch):
        @property
        def mockreturn(self):
            return 2
        
        monkeypatch.setattr(Circle, 'area', mockreturn)
        circle = Circle(10)
        assert circle.area == 2  
