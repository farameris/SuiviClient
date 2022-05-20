import sys

from PyQt5 import QtCore

from analytisstools.gui.main import MyApp
from analytisstools.utils.io import readJS
from suiviclient.data import _MAINJSON
from suiviclient.gui.mainwindow import MyMainWindow

orgname = readJS(_MAINJSON, "orgname")
orgdomain = readJS(_MAINJSON, "orgdomain")
appname = readJS(_MAINJSON, "appname")
date = readJS(_MAINJSON, "date")
appversion = readJS(_MAINJSON, "appversion")

myapp = MyApp(sys.argv)
QtCore.QCoreApplication.setOrganizationName(orgname)
QtCore.QCoreApplication.setOrganizationDomain(orgdomain)
QtCore.QCoreApplication.setApplicationName(appname)
QtCore.QCoreApplication.setApplicationVersion(appversion)

mymain = MyMainWindow(
    titre="{} (version {} - {})".format(appname, appversion, date))
mymain.show()
mymain.statusBar().showMessage("Ready")

myapp.launchQApp()
