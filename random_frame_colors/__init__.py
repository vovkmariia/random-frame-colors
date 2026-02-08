# python 3.14
#
# random_frame_colors
#
# Offers an alternative to a built-in "Add frame" functionality in Substance Designer. When used,
# newly created frames are automatically assigned a random color, instead of the default blue.
#
# Created by Mariia Vovk - https://github.com/vovkmariia - February 2026


# importing the required dependencies for Substance Designer Python API
import os
import sd
import re
import weakref

from functools import partial
from collections import OrderedDict

import random
import colors

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


# getting the application and UI manager object
ctx = sd.getContext()
app = ctx.getSDApplication()
uiMgr = app.getQtForPythonUIMgr()

# getting the current graph.
sdGraph = uiMgr.getCurrentGraph()


#------------ START MAIN CUSTOM FUNCTIONS ---------------------------------------------------------------------------

with SDHistoryUtils.UndoGroup("Random Frame Colors"):

    # getting selected nodes (as SDSBSCompNode objects)
    selected_nodes = uiMgr.getCurrentGraphSelectedNodes() # returns selected nodes in an SDArray


    # calculating a bounding box for the frame
    min_x = min(node.getPosition()[0] for node in selected_nodes) # .getPosition() returns an instance of a
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

    # getting a random color from a dictionary
    frame_colors = random.choice(list(colors.color_options.values()))
    R = frame_colors[0]
    G = frame_colors[1]
    B = frame_colors[2]
    A = frame_colors[3]

    # applying the layout of the frame
    frame.setPosition(frame_pos)
    frame.setSize(frame_size)
    frame.setTitle("Frame")
    frame.setColor(ColorRGBA(R, G, B, A))

    sdGraph.setSelectedGraphObjects([frame])

#------------ END MAIN CUSTOM FUNCTIONS --------------------------------------------------------------------------

