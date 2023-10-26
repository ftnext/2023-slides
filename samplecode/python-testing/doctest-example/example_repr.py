class Awesome:
    """
    >>> Awesome("PyCon APAC")
    Awesome('PyCon APAC')
    """

    def __init__(self, string: str) -> None:
        self.string = string

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.string!r})"


from dataclasses import dataclass


@dataclass
class Fabulous:
    """
    >>> Fabulous("PyCon APAC")
    Fabulous(string='PyCon APAC')
    """

    string: str
