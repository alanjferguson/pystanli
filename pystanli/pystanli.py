from pylatex.base_classes import LatexObject
from pylatex.package import Package

_stanli_package = "stanli"


def update_stanli_sty(sty_path):
    """
    Args
    ----
    sty_path: str
        Path to updated stanli.sty
    """
    _stanli_package = sty_path


class _StanliObject(LatexObject):
    """Class for all stanli objects"""

    packages = [Package(_stanli_package)]

    def dumps(self):
        """Return representation"""
        return self.__repr__()


class Point(_StanliObject):
    """Stanli Point Class"""

    def __init__(self, name, x, y):
        """
        Args
        ----
        name: string
            Point name
        x: float or int
            X coordinate
        y: float or int
            Y coordinate
        """
        self._name = name
        self._x = x
        self._y = y

    def __repr__(self):
        return r"\point{{{}}}{{{}}}{{{}}};".format(self._name, self._x, self._y)

    @property
    def name(self):
        return self._name


class Support(_StanliObject):
    """Stanli Support Class"""

    def __init__(self, type, point, rotation=None):
        self._type = type
        self._point = point
        self._rotation = rotation

    def __repr__(self):
        ret_str = r"\support{{{}}}{{{}}}".format(self._type, self._point)
        if self._rotation is not None:
            ret_str += "[{}]".format(self._rotation)
        return ret_str + ";"


class Hinge(_StanliObject):
    """Stanli Hinge Class"""

    def __init__(self, type, point):
        self._type = 1
        self._point = point

    def __repr__(self):
        return r"\hinge{{{}}}{{{}}};".format(self._type, self._point)


class Beam(_StanliObject):
    """Stanli Beam Class"""

    def __init__(
        self,
        type,
        start_point,
        end_point,
        round_start_point=False,
        round_end_point=False,
    ):
        self._type = type
        self._start_point = start_point
        self._end_point = end_point
        self._round_start_point = round_start_point
        self._round_end_point = round_end_point

    def __repr__(self):
        if self._type in [1, 2, 4]:
            ret_str = r"\beam{{{}}}{{{}}}{{{}}}[{:d}][{:d}];".format(
                self._type,
                self._start_point,
                self._end_point,
                self._round_start_point,
                self._round_end_point,
            )
        elif self._type == 3:
            ret_str = r"\beam{{{}}}{{{}}}{{{}}};".format(
                self._type, self._start_point, self._end_point
            )
        return ret_str


class Dimensioning(_StanliObject):
    """Stanli Dimensioning Class"""

    def __init__(self, type, start_point, end_point, origin_dist, label=None):
        self._type = type
        self._start_point = start_point
        self._end_point = end_point
        self._origin_dist = origin_dist
        self._label = label

    def __repr__(self):
        ret_str = r"\dimensioning{{{}}}{{{}}}{{{}}}{{{}}}".format(
            self._type, self._start_point, self._end_point, self._origin_dist
        )
        if self._label is not None:
            ret_str += "[{}]".format(self._label)
        return ret_str + ";"


class InfluenceLine(_StanliObject):
    """Stanli Influence Line Class"""

    def __init__(self, start_point, end_point, vert_dist, arrow_pos=None):
        self._start_point = start_point
        self._end_point = end_point
        self._vert_dist = vert_dist
        self._arrow_pos = arrow_pos

    def __repr__(self):
        ret_str = r"\influenceline{{{}}}{{{}}}{{{}}}".format(
            self._start_point, self._end_point, self._vert_dist
        )
        if self._arrow_pos is not None:
            ret_str += "[{}]".format(self._arrow_pos)
        return ret_str + ";"


class Scaling(_StanliObject):
    """Stanli Scaling Class"""

    def __init__(self, scale_factor):
        self._scale_factor = scale_factor

    def __repr__(self):
        return r"\scaling{{{}}};".format(self._scale_factor)


class Notation(_StanliObject):
    """Stanli Notation Class"""

    def __init__(
        self,
        type,
        point,
        label,
        end_point=None,
        position=None,
        orientation=None,
        text_orientation=None,
    ):
        self._type = str(type)
        self._point = point
        self._label = label
        self._end_point = end_point if end_point is not None else ""
        self._position = position if position is not None else ""
        self._orientation = orientation if orientation is not None else ""
        self._text_orientation = (
            text_orientation if text_orientation is not None else ""
        )

    def __repr__(self):
        ret_str = r"\notation{{{}}}{{{}}}".format(self._type, self._point)
        if self._type in ["1", "2", "6"]:
            ret_str += r"{{{}}}".format(self._label)
            if self._orientation and self._type != "6":
                ret_str += r"[{}]".format(self._orientation)
        else:
            ret_str += r"{{{}}}[{}][{}][{}]".format(
                self._end_point, self._label, self._position, self._orientation
            )
            if self._type in ["4", "5"]:
                ret_str += r"[{}]".format(self._text_orientation)

        return ret_str + ";"
