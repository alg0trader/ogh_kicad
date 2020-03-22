import os
import pcbnew
import inspect


def get_path():
    # Get the script directory in order to locate icons.
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    return os.path.dirname(os.path.abspath(filename))


class OGH_Plugin(pcbnew.ActionPlugin):
    """
    Pcbnew OGH plugin.
    """
    def defaults(self):
        self.name = "OGH"
        self.category = "curved layout tool"
        self.description = "Generate optimized geometric hermite (OGH) curves in KiCad Pcbbnew"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.sep, get_path(), 'icons', 'hermite.png')

    def Run(self):
        pass


class OGH:
    """
    Generate Optimized Geometric Hermite (OGH)
    """
    pass
