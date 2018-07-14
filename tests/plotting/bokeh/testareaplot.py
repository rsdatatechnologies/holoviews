from holoviews.element import Area

from .testplot import TestBokehPlot, bokeh_renderer


class TestAreaPlot(TestBokehPlot):

    def test_area_padding_square(self):
        area = Area([(1, 1), (2, 2), (3, 3)]).options(padding=0.2)
        plot = bokeh_renderer.get_plot(area)
        x_range, y_range = plot.handles['x_range'], plot.handles['y_range']
        self.assertEqual(x_range.start, 0.8)
        self.assertEqual(x_range.end, 3.2)
        self.assertEqual(y_range.start, 0)
        self.assertEqual(y_range.end, 3.2999999999999998)

    def test_area_with_lower_vdim(self):
        area = Area([(1, 0.5, 1), (2, 1.5, 2), (3, 2.5, 3)], vdims=['y', 'y2']).options(padding=0.2)
        plot = bokeh_renderer.get_plot(area)
        x_range, y_range = plot.handles['x_range'], plot.handles['y_range']
        self.assertEqual(x_range.start, 0.8)
        self.assertEqual(x_range.end, 3.2)
        self.assertEqual(y_range.start, 0.25)
        self.assertEqual(y_range.end, 3.25)

    def test_area_padding_square(self):
        area = Area([(1, 1, 0.5), (2, 2, 1.5), (3, 3, 2.5)]).options(padding=0.2)
        plot = bokeh_renderer.get_plot(area)
        x_range, y_range = plot.handles['x_range'], plot.handles['y_range']
        self.assertEqual(x_range.start, 0.8)
        self.assertEqual(x_range.end, 3.2)
        self.assertEqual(y_range.start, 0)
        self.assertEqual(y_range.end, 3.2999999999999998)
        
    def test_area_padding_negative(self):
        area = Area([(1, -1), (2, -2), (3, -3)]).options(padding=0.2)
        plot = bokeh_renderer.get_plot(area)
        x_range, y_range = plot.handles['x_range'], plot.handles['y_range']
        self.assertEqual(x_range.start, 0.8)
        self.assertEqual(x_range.end, 3.2)
        self.assertEqual(y_range.start, -3.2)
        self.assertEqual(y_range.end, 0)

    def test_area_padding_mixed(self):
        area = Area([(1, 1), (2, -2), (3, 3)]).options(padding=0.2)
        plot = bokeh_renderer.get_plot(area)
        x_range, y_range = plot.handles['x_range'], plot.handles['y_range']
        self.assertEqual(x_range.start, 0.8)
        self.assertEqual(x_range.end, 3.2)
        self.assertEqual(y_range.start, -2.5)
        self.assertEqual(y_range.end, 3.5)
        
    def test_area_padding_hard_range(self):
        area = Area([(1, 1), (2, 2), (3, 3)]).redim.range(y=(0, 4)).options(padding=0.2)
        plot = bokeh_renderer.get_plot(area)
        x_range, y_range = plot.handles['x_range'], plot.handles['y_range']
        self.assertEqual(x_range.start, 0.8)
        self.assertEqual(x_range.end, 3.2)
        self.assertEqual(y_range.start, 0)
        self.assertEqual(y_range.end, 4)

    def test_area_padding_soft_range(self):
        area = Area([(1, 1), (2, 2), (3, 3)]).redim.soft_range(y=(0, 3.5)).options(padding=0.2)
        plot = bokeh_renderer.get_plot(area)
        x_range, y_range = plot.handles['x_range'], plot.handles['y_range']
        self.assertEqual(x_range.start, 0.8)
        self.assertEqual(x_range.end, 3.2)
        self.assertEqual(y_range.start, 0)
        self.assertEqual(y_range.end, 3.5)

    def test_area_padding_nonsquare(self):
        area = Area([(1, 1), (2, 2), (3, 3)]).options(padding=0.2, width=600)
        plot = bokeh_renderer.get_plot(area)
        x_range, y_range = plot.handles['x_range'], plot.handles['y_range']
        self.assertEqual(x_range.start, 0.9)
        self.assertEqual(x_range.end, 3.1)
        self.assertEqual(y_range.start, 0)
        self.assertEqual(y_range.end, 3.2999999999999998)

    def test_area_padding_logx(self):
        area = Area([(1, 1), (2, 2), (3,3)]).options(padding=0.2, logx=True)
        plot = bokeh_renderer.get_plot(area)
        x_range, y_range = plot.handles['x_range'], plot.handles['y_range']
        self.assertEqual(x_range.start, 0.89595845984076228)
        self.assertEqual(x_range.end, 3.3483695221017129)
        self.assertEqual(y_range.start, 0)
        self.assertEqual(y_range.end, 3.3)
    
    def test_area_padding_logy(self):
        area = Area([(1, 1), (2, 2), (3, 3)]).options(padding=0.2, logy=True)
        plot = bokeh_renderer.get_plot(area)
        x_range, y_range = plot.handles['x_range'], plot.handles['y_range']
        self.assertEqual(x_range.start, 0.8)
        self.assertEqual(x_range.end, 3.2)
        self.assertEqual(y_range.start, 0.033000000000000002)
        self.assertEqual(y_range.end, 3.2999999999999998)