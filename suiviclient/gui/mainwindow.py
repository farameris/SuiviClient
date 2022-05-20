import os
import re
import shutil
import subprocess
import sys
from copy import copy
from functools import partial
from time import time

from PyQt5 import QtCore, QtGui, QtWidgets, uic

from analytisstools.gui.popMessage import OkMessage, YNMessage, getSaisie, selectFile, selectRep
from analytisstools.images import _ICO_APYCHROM
from analytisstools.utils.io import getFullJS, set_ini

from suiviclient.data import _MAINGUI


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, titre="apybase", icone=_ICO_APYCHROM, parent=None):
        super(MyMainWindow, self).__init__(parent)
        uic.loadUi(_MAINGUI, self)
        self.setWindowTitle(titre)
        self.setWindowIcon(QtGui.QIcon(icone))

        # Check de la présence de la BDD
        if not os.path.exists(sqlite_db.database):
            self.actionChangeBDDPath(True)

        self.settings = QtCore.QSettings()
