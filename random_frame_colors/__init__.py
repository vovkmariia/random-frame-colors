# python 3.14
#
# random_frame_colors
#
# Offers an alternative to a built-in "Add frame" functionality in Substance Designer. When used,
# newly created frames are automatically assigned a random, visually distinct color instead of the default blue.
#
# Created by Mariia Vovk - https://github.com/vovkmariia - February 2026


# importing the required dependencies for Substance Designer Python API
import os
import sd
import re
import weakref

from functools import partial
from collections import OrderedDict

from sd.tools import io
from sd.tools import graphlayout
from sd.api import sdmodule, SDHistoryUtils
from sd.api import sdproperty
from sd.api import sdtypeenum

from sd.ui.graphgrid import *
from sd.api.sbs.sdsbscompgraph import *
from sd.api.sdgraphobjectpin import *
from sd.api.sdgraphobjectframe import *
from sd.api.sdgraphobjectcomment import *
from sd.api.sdproperty import SDPropertyCategory
from sd.api.sdvalueserializer import SDValueSerializer
from sd.api.sdapplication import SDApplicationPath

from PySide6 import QtCore, QtGui, QtWidgets, QtSvg

# importing libraries required by the custom function of the plugin
import random
from .colors import *


#------function for loading UI icons from SVG files (from factory plugin 'node_align_tools')--------------------------

def loadSvgIcon(iconName, size):
    currentDir = os.path.dirname(__file__)
    iconFile = os.path.abspath(os.path.join(currentDir, iconName + '.svg'))

    svgRenderer = QtSvg.QSvgRenderer(iconFile)
    if svgRenderer.isValid():
        pixmap = QtGui.QPixmap(QtCore.QSize(size, size))

        if not pixmap.isNull():
            pixmap.fill(QtCore.Qt.transparent)
            painter = QtGui.QPainter(pixmap)
            svgRenderer.render(painter)
            painter.end()

        return QtGui.QIcon(pixmap)

    return None


#------------ START MAIN CUSTOM FUNCTIONS ---------------------------------------------------------------------------

class randomColorFrameToolbar(QtWidgets.QToolBar):
    __toolbarList = {}

    def create_random_color_frame(self):
        with SDHistoryUtils.UndoGroup("Random Frame Colors"):

            # getting the application and UI manager object
            ctx = sd.getContext()
            app = ctx.getSDApplication()
            uiMgr = app.getQtForPythonUIMgr()

            # getting the current graph
            sdGraph = uiMgr.getCurrentGraph()

            # getting selected nodes (as SDSBSCompNode objects)
            selected_nodes = uiMgr.getCurrentGraphSelectedNodes()  # returns selected nodes in an SDArray
            if not selected_nodes:
                print("No nodes selected.")
                return

            # calculating a bounding box for the frame
            min_x = min(node.getPosition()[0] for node in selected_nodes)
            # .getPosition() returns an instance of a
            # float2 class. by accessing attributes
            # with [0] and [1] we get a float for performing
            # calculations
            min_y = min(node.getPosition()[1] for node in selected_nodes)
            max_x = max(node.getPosition()[0] for node in selected_nodes)
            max_y = max(node.getPosition()[1] for node in selected_nodes)

            padding = 80

            # preparing the floats
            x_pos = (min_x - padding)
            y_pos = (min_y - padding)
            x_size = (max_x - min_x) + padding * 2
            y_size = (max_y - min_y) + padding * 2

            # creating a frame
            frame = SDGraphObjectFrame.sNew(sdGraph)

            # assigning our floats to float2 x and y attributes
            frame_pos = frame.getPosition()
            frame_pos.x = x_pos
            frame_pos.y = y_pos
            frame_size = frame.getSize()
            frame_size.x = x_size
            frame_size.y = y_size

            print(f"Number of available unique colors: {len(self.temp_color_options)}")

            if len(self.temp_color_options) == 0:
                self.temp_color_options = color_options.copy()
                print("All colors are used. Resetting the dictionary.")

            # getting a random color from a dictionary
            random_key = random.choice(list(self.temp_color_options.keys()))
            frame_colors = self.temp_color_options[random_key]
            R = frame_colors[0]
            G = frame_colors[1]
            B = frame_colors[2]
            A = frame_colors[3]
            value = self.temp_color_options.pop(random_key)
            print(f"Color generated: {random_key}")

            # applying the layout of the frame
            frame.setPosition(frame_pos)
            frame.setSize(frame_size)
            frame.setTitle("Frame")
            frame.setColor(ColorRGBA(R, G, B, A))

    def __init__(self, graphViewID, uiMgr):
        super(randomColorFrameToolbar, self).__init__(parent=uiMgr.getMainWindow())
        # creating a dictionary of available colors
        self.temp_color_options = color_options.copy()

        self.setObjectName("vovkmariia.random_frame_colors_toolbar")

        self.__graphViewID = graphViewID
        self.__uiMgr = uiMgr

        act = self.addAction(loadSvgIcon("color_frame", 24), "Color_Frame")
        act.setToolTip(self.tr("Create Frame with Random Color"))
        act.triggered.connect(self.create_random_color_frame)


        self.__toolbarList[graphViewID] = weakref.ref(self)
        self.destroyed.connect(partial(randomColorFrameToolbar.__onToolbarDeleted, graphViewID=graphViewID))

    def tooltip(self):
        return self.tr("Create Frame with Random Color")


    # (from factory plugin 'node_align_tools')
    @classmethod
    def __onToolbarDeleted(cls, graphViewID):
        del cls.__toolbarList[graphViewID]

    # (from factory plugin 'node_align_tools')
    @classmethod
    def removeAllToolbars(cls):
        for toolbar in cls.__toolbarList.values():
            if toolbar():
                toolbar().deleteLater()

#------------ END MAIN CUSTOM FUNCTIONS --------------------------------------------------------------------------

# (from factory plugin 'node_align_tools')
def onNewGraphViewCreated(graphViewID, uiMgr):
    # Ignore graph types not supported by the Python API.
    if not uiMgr.getCurrentGraph():
        return

    toolbar = randomColorFrameToolbar(graphViewID, uiMgr)
    uiMgr.addToolbarToGraphView(
        graphViewID,
        toolbar,
        icon = loadSvgIcon("color_frame", 24),
        tooltip = toolbar.tooltip())

graphViewCreatedCallbackID = 0

# (from factory plugin 'node_align_tools')
def initializeSDPlugin():

    # Get the application and UI manager object.
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()

    if uiMgr:
        global graphViewCreatedCallbackID
        graphViewCreatedCallbackID = uiMgr.registerGraphViewCreatedCallback(
            partial(onNewGraphViewCreated, uiMgr=uiMgr))


# (from factory plugin 'node_align_tools')
def uninitializeSDPlugin():
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()

    if uiMgr:
        global graphViewCreatedCallbackID
        uiMgr.unregisterCallback(graphViewCreatedCallbackID)
        randomColorFrameToolbar.removeAllToolbars()