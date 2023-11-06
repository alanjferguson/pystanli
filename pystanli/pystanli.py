from typing import Optional

from pylatex.base_classes import LatexObject
from pylatex.package import Package
from pylatex import NoEscape

import os


class StanliSty():
    """
    Singleton to track which stanli package we are using
    """

    _stanli_package = "stanli"

    @classmethod
    def get(self):
        return self._stanli_package

    @classmethod
    def update(self, sty_path:str):
        """
        Parameters
        ----------
        sty_path: str
            Path to updated stanli.sty
        """

        # Remove .sty extension from path
        root, ext = os.path.splitext(sty_path)

        self._stanli_package = NoEscape(root)


class _StanliObject(LatexObject):
    """Class for all stanli objects"""

    def __init__(self):
        self.packages = [Package(StanliSty.get())]
        super().__init__()

    def dumps(self):
        """Return representation"""
        return self.__repr__()


class Point(_StanliObject):
    """Stanli Point Class"""

    def __init__(self, name: str, x: float, y: float):
        """
        Constructs a stanli point object

        Parameters
        ----------
        name: str
            Point name
        x: float
            X coordinate
        y: float
            Y coordinate
        """
        self._name = name
        self._x = x
        self._y = y

        super().__init__()

    def __repr__(self):
        return r"\point{{{}}}{{{}}}{{{}}};".format(self._name, self._x, self._y)

    @property
    def name(self):
        return self._name


class Support(_StanliObject):
    """Stanli Support Class"""

    def __init__(self, type: str, point: str, rotation: Optional[float] = 0.0):
        """
        Constructs a stanli support object

        Parameters
        ----------
        type: str
            The type of support to draw.
        point: str
            Name of the stanli point to draw support at.
        rotation: Optional[float]
            Angle from x-axis to draw support at. Defaults to 0.0.
        """
        self._type = type
        self._point = point
        self._rotation = rotation

        super().__init__()

    def __repr__(self):
        return r"\support{{{}}}{{{}}}[{}];".format(
            self._type, self._point, self._rotation
        )


class Hinge(_StanliObject):
    """Stanli Hinge Class"""

    def __init__(self, type: str, point: str):
        """
        Constructs a stanli hinge object

        Parameters
        ----------
        type: str
            The type of hinge to draw.
        point: str
            Name of the stanli point to draw hinge at.
        """
        self._type = type
        self._point = point

        super().__init__()

    def __repr__(self):
        return r"\hinge{{{}}}{{{}}};".format(self._type, self._point)


class Beam(_StanliObject):
    """Stanli Beam Class"""

    def __init__(
        self,
        type: str,
        start_point: str,
        end_point: str,
        round_start_point: Optional[bool] = False,
        round_end_point: Optional[bool] = False,
    ):
        """
        Constructs a stanli beam object

        Parameters
        ----------
        type: str
            The type of beam to draw.
        start_point: str
            Name of the stanli point for start of beam.
        end_point: str
            Name of the stanli point for end of beam.
        round_start_point: Optional[bool]
            Draw rounded cap at start of beam if True. Defaults to False.
        round_end_point: Optional[bool]
            Draw rounded cap at end of beam if True. Defaults to False.
        """
        self._type = type
        self._start_point = start_point
        self._end_point = end_point
        self._round_start_point = round_start_point
        self._round_end_point = round_end_point

        super().__init__()

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

    def __init__(
        self,
        type: str,
        start_point: str,
        end_point: str,
        origin_dist: float,
        label: Optional[str] = None,
    ):
        """
        Constructs a stanli dimensioning object

        Parameters
        ----------
        type: str
            The type of dimension to draw.
        start_point: str
            Name of the stanli point for start of dimension.
        end_point: str
            Name of the stanli point for end of dimension.
        origin_dist: float
            Offset from origin for dimension annotation.
        label: Optional[str]
            Label to annotate dimension. Defaults to ''.
        """
        self._type = type
        self._start_point = start_point
        self._end_point = end_point
        self._origin_dist = origin_dist
        self._label = label

        super().__init__()

    def __repr__(self):
        ret_str = r"\dimensioning{{{}}}{{{}}}{{{}}}{{{}}}".format(
            self._type, self._start_point, self._end_point, self._origin_dist
        )
        if self._label is not None:
            ret_str += "[{}]".format(self._label)
        return ret_str + ";"


class InfluenceLine(_StanliObject):
    """Stanli Influence Line Class"""

    def __init__(
        self,
        start_point: str,
        end_point: str,
        vert_dist: float,
        arrow_pos: Optional[float] = 0.5,
    ):
        """
        Constructs stanli influence line object

        Parameters
        ----------
        start_point: str
            Name of the stanli point for start of influence line.
        end_point: str
            Name of the stanli point for end of influence line.
        vert_dist:
            Offset at which to draw influence line.
        arrow_pos: Optional[float]
            Relative position along length of influence line to place arrow. Defaults to 0.5.
        """
        self._start_point = start_point
        self._end_point = end_point
        self._vert_dist = vert_dist
        self._arrow_pos = arrow_pos

        super().__init__()

    def __repr__(self):
        ret_str = r"\influenceline{{{}}}{{{}}}{{{}}}".format(
            self._start_point, self._end_point, self._vert_dist
        )
        if self._arrow_pos is not None:
            ret_str += "[{}]".format(self._arrow_pos)
        return ret_str + ";"


class Scaling(_StanliObject):
    """Stanli Scaling Class"""

    def __init__(self, scale_factor: float):
        """
        Constructs a stanli scaling object

        Parameters
        ----------
        scale_factor: float
            Amount to scale lengths of the system by.
        """
        self._scale_factor = scale_factor

        super().__init__()

    def __repr__(self):
        return r"\scaling{{{}}};".format(self._scale_factor)


class Notation(_StanliObject):
    """Stanli Notation Class"""

    def __init__(
        self,
        type: str,
        point: str,
        label: str,
        end_point: Optional[str] = None,
        position: Optional[float] = None,
        orientation: Optional[str] = None,
        text_orientation: Optional[str] = None,
    ):
        """
        Constructs a stanli notation object

        Parameters
        ----------
        type: str
            The type of annotation to draw.
        point: str
            Name of the stanli point to draw annotation at.
        label: str
            Text to include in annotation.
        end_point: Optional[str]
            Name of the stanli point for end of line annotation.
        position: Optional[float]
            Relative position along line annotation to place mark/label.
        orientation: Optional[str]
            Orientation of label relative to point.
        text_orientation: Optional[str]
            Text alignment orientation.
        """
        self._type = type
        self._point = point
        self._label = label
        self._end_point = end_point if end_point is not None else ""
        self._position = position if position is not None else ""
        self._orientation = orientation if orientation is not None else ""
        self._text_orientation = (
            text_orientation if text_orientation is not None else ""
        )

        super().__init__()

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
