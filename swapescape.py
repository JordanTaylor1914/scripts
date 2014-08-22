##!/usr/bin/env python
from gi.repository import Gio
XKB_GSETTINGS_SCHEMA = "org.gnome.desktop.input-sources"
XKB_GSETTINGS_NAME = "xkb-options"


def toggle_swapescape():
    swapescape = 'caps:swapescape'
    setting = Gio.Settings(XKB_GSETTINGS_SCHEMA)
    opts = setting[XKB_GSETTINGS_NAME]
    if swapescape in opts:
        opts.remove(swapescape)
    else:
        opts.append(swapescape)
    setting[XKB_GSETTINGS_NAME] = opts


if __name__ == '__main__':
    toggle_swapescape()
