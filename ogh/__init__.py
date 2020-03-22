import os
# import wx
# import wx.aui
import pcbnew
import hermite
import layout


# Register OGH plugin
ogh_plugin = hermite.OGH_Plugin()
ogh_plugin.defaults()
ogh_plugin.register()
