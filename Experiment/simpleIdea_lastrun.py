#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on April 15, 2020, at 16:33
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'simpleIdea'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\Github\\Online_Avatar\\Experiment\\simpleIdea_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1200, 600], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "routine_1_InitExperiment"
routine_1_InitExperimentClock = core.Clock()
# get packages we might need 
# import random

# Experiment running conditions
deltas = [200, 300, 400, 500, 600]
num_reps = 1
num_repsEsts = 1
num_blocks = 2

#delta_order = []
#for d in deltas:
#    for rep in range(0,num_reps):
#        delta_order.append(d)

#demo_delta = []
#for b in range(0,num_blocks):
#    for d in deltas:
#        for rep in range(0, num_repsEsts):
#            demo_delta.append(d)
 
# delta_order = shuffle(numpy.repeat(deltas, num_reps))
# shuffle(delta_order)

# get number of repetitions for trials and demo
demo_trials = num_repsEsts * len(deltas)
num_trials = num_reps * len(deltas)
num_conf_trials = 2 * len(deltas)



# Screen settings 
Screen_height = 600
Screen_width = 1200

# Trial conditions 
Trial_time = 120 # this is specified in frames for now

# avatar setup 
avatar_speed = 4
avatar_y_offset = 100
avatar_reach = 30
box_size = 50
box_truck   = [1,-1,-1]
box_placed  = [.5,-.5,-.5]
box_build   = [.09, -.45,-.85]
box_burning = [.64, -.17, -.76]
box_burnt   = [-.9, -.9, -.9]

# Control Arrows
Arrow_init_colour = [1,1,1]
Arrow_clik_colour = [0,0,1]
Arrow_size = 40
Arrow_orient = [0,180,270,90]

# this needs to be set by size of the object
init_posx = -150
init_posy = 0
padding = 5
Arrow_y = [init_posx,init_posx-(2*Arrow_size)-(2*padding),init_posx-Arrow_size - padding, init_posx-Arrow_size - padding]
Arrow_x = [init_posy, init_posy, -Arrow_size-padding, Arrow_size+padding]






# Initialize components for Routine "routine_2_WelcomeScreen"
routine_2_WelcomeScreenClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Welcome to the experiment\n\nPress Space to continue',
    font='Arial',
    pos=(0, 0), height=25, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_2a_DemoExplanation"
routine_2a_DemoExplanationClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='In this part, you will gain some practice moving the avatar towards a single target. \nAfter pressing the spacebar to start the trial, a shord period of time will pass, after which the target will turn orange.\nYour task is to drive the avatar towards this target within the time limit. To do this, you will click the arrow boxes at the bottom of the screen.\n\nPress the spacebar to continue',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_3a_PracticeInit"
routine_3a_PracticeInitClock = core.Clock()
# init trial counter
trial_num_demo = 0 


# Initialize components for Routine "routine_3b_PresentSetup"
routine_3b_PresentSetupClock = core.Clock()
Avatar_x_demo = 0
Avatar_y_demo = 100
borderlinesDemo = visual.Rect(
    win=win, name='borderlinesDemo',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
AvatarDemo = visual.Rect(
    win=win, name='AvatarDemo',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
DemoTarget = visual.Rect(
    win=win, name='DemoTarget',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
StartDemoTrial = visual.TextStim(win=win, name='StartDemoTrial',
    text='Press the spacebar to start the trial',
    font='Arial',
    pos=[0,0], height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "routine_3c_driving"
routine_3c_drivingClock = core.Clock()
DemoMouse = event.Mouse(win=win)
x, y = [None, None]
DemoMouse.mouseClock = core.Clock()
boundaryDemo = visual.Rect(
    win=win, name='boundaryDemo',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
AvatarPlacedDemo = visual.Rect(
    win=win, name='AvatarPlacedDemo',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
DemoTargetDrive = visual.Rect(
    win=win, name='DemoTargetDrive',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
AvatarDriveDemo = visual.Rect(
    win=win, name='AvatarDriveDemo',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
UpClickDemo = visual.Rect(
    win=win, name='UpClickDemo',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
DownClickDemo = visual.Rect(
    win=win, name='DownClickDemo',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
LeftClickDemo = visual.Rect(
    win=win, name='LeftClickDemo',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
RightClickDemo = visual.Rect(
    win=win, name='RightClickDemo',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
UpArrow = visual.ShapeStim(
    win=win, name='UpArrow',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
DownArrow = visual.ShapeStim(
    win=win, name='DownArrow',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
LeftArrow = visual.ShapeStim(
    win=win, name='LeftArrow',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
RightArrow = visual.ShapeStim(
    win=win, name='RightArrow',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)

# Initialize components for Routine "routine_3d_feedback"
routine_3d_feedbackClock = core.Clock()
AvatarFeedbackDemo = visual.Rect(
    win=win, name='AvatarFeedbackDemo',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
BoundaryFeedBack = visual.Rect(
    win=win, name='BoundaryFeedBack',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
PlacedFeedback = visual.Rect(
    win=win, name='PlacedFeedback',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
AvatarDemoFeedback = visual.Rect(
    win=win, name='AvatarDemoFeedback',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
FeedbackText = visual.TextStim(win=win, name='FeedbackText',
    text='default text',
    font='Arial',
    pos=[0,0], height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
FeedbackText_2 = visual.TextStim(win=win, name='FeedbackText_2',
    text='Press the spacebar to continue',
    font='Arial',
    pos=[0,0], height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "routine_4_Trial_Instructions"
routine_4_Trial_InstructionsClock = core.Clock()
TrialInst = visual.TextStim(win=win, name='TrialInst',
    text="You will place the 'truck' by clicing between the two lines on screen.\nOnce you are happy with the placement, press the spacebar to begin the trial.\nAfter a short amount of time, one of the two buidlings will catch fire,\nat which point you are to drive the truck towards this buidling.\n\nPress the spacebar to continue",
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_5a_PlaceAvatarInit"
routine_5a_PlaceAvatarInitClock = core.Clock()
trial_num = 0

# Initialize components for Routine "routine_5b_PlacingAvatar"
routine_5b_PlacingAvatarClock = core.Clock()
PlacementArea = visual.Rect(
    win=win, name='PlacementArea',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
AvatarMouse = event.Mouse(win=win)
x, y = [None, None]
AvatarMouse.mouseClock = core.Clock()
leftTarget = visual.Rect(
    win=win, name='leftTarget',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
rightTarget = visual.Rect(
    win=win, name='rightTarget',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
AvatarPlace = visual.Rect(
    win=win, name='AvatarPlace',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
Avatar_x = 0
Avatar_y = 100

# Initialize components for Routine "routine_5c_DrivingAvatar"
routine_5c_DrivingAvatarClock = core.Clock()
DrivingMouse = event.Mouse(win=win)
x, y = [None, None]
DrivingMouse.mouseClock = core.Clock()
DrivingBoundary = visual.Rect(
    win=win, name='DrivingBoundary',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
AvatarPlaced = visual.Rect(
    win=win, name='AvatarPlaced',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
LeftBuild = visual.Rect(
    win=win, name='LeftBuild',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
RightBuild = visual.Rect(
    win=win, name='RightBuild',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
AvatarDrive = visual.Rect(
    win=win, name='AvatarDrive',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
upClick = visual.Rect(
    win=win, name='upClick',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
downClick = visual.Rect(
    win=win, name='downClick',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
leftClick = visual.Rect(
    win=win, name='leftClick',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
rightClick = visual.Rect(
    win=win, name='rightClick',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
upShape = visual.ShapeStim(
    win=win, name='upShape',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
downShape = visual.ShapeStim(
    win=win, name='downShape',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
rightShape = visual.ShapeStim(
    win=win, name='rightShape',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
leftShape = visual.ShapeStim(
    win=win, name='leftShape',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)

# Initialize components for Routine "routine_5d_TrialFeedback"
routine_5d_TrialFeedbackClock = core.Clock()
DrivingBoundaryFeedback = visual.Rect(
    win=win, name='DrivingBoundaryFeedback',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
AvatarPlacedFeedback = visual.Rect(
    win=win, name='AvatarPlacedFeedback',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
LeftFeedback = visual.Rect(
    win=win, name='LeftFeedback',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
RightFeedback = visual.Rect(
    win=win, name='RightFeedback',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
AvatarFeedback = visual.Rect(
    win=win, name='AvatarFeedback',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 150), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press the spacebar to continue',
    font='Arial',
    pos=[0,0], height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "routine_6_ConfidenceExplanation"
routine_6_ConfidenceExplanationClock = core.Clock()

# Initialize components for Routine "routine_6a_Confidence"
routine_6a_ConfidenceClock = core.Clock()
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1, low=0, high=1, precision=100, showValue=False, scale='Will the Avatar reach the targer? 0 = No, 1 = Yes', markerStart='4')
ConfBoundary = visual.Rect(
    win=win, name='ConfBoundary',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
ConfAvatar = visual.Rect(
    win=win, name='ConfAvatar',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
ConfTarget = visual.Rect(
    win=win, name='ConfTarget',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "routine_1_InitExperiment"-------
t = 0
routine_1_InitExperimentClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# get packages we might need 
# import random

# Experiment running conditions
#deltas = [200, 300, 400, 500, 600]
#num_trials = 5

# Screen settings 
#Screen_height = 600
#Screen_width = 1200

# Trial conditions 
#Trial_time = 120 # this is specified in frames for now

# avatar setup 
#avatar_speed = 3
#avatar_y_offset = 100
#avatar_reach = 55
#box_size = 50
#box_truck   = [1,-1,-1]
#box_placed  = [.5,-.5,-.5]
#box_build   = [.09, -.45,-.85]
#box_burning = [.64, -.17, -.76]
#box_burnt   = [-.9, -.9, -.9]

# Control Arrows
#Arrow_init_colour = [1,1,1]
#Arrow_clik_colour = [0,0,1]
#Arrow_size = 30
#Arrow_orient = [0,180,270,90]
#Arrow_y = [-150,-220,-185,-185]
#Arrow_x = [0, 0, -35, 35]





# keep track of which components have finished
routine_1_InitExperimentComponents = []
for thisComponent in routine_1_InitExperimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "routine_1_InitExperiment"-------
while continueRoutine:
    # get current time
    t = routine_1_InitExperimentClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_1_InitExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_1_InitExperiment"-------
for thisComponent in routine_1_InitExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "routine_1_InitExperiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "routine_2_WelcomeScreen"-------
t = 0
routine_2_WelcomeScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
WelcomeEscape = keyboard.Keyboard()
# keep track of which components have finished
routine_2_WelcomeScreenComponents = [WelcomeText, WelcomeEscape]
for thisComponent in routine_2_WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "routine_2_WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = routine_2_WelcomeScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeText* updates
    if frameN >= 0.0 and WelcomeText.status == NOT_STARTED:
        # keep track of start time/frame for later
        WelcomeText.tStart = t  # not accounting for scr refresh
        WelcomeText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(WelcomeText, 'tStartRefresh')  # time at next scr refresh
        WelcomeText.setAutoDraw(True)
    
    # *WelcomeEscape* updates
    if t >= 0.0 and WelcomeEscape.status == NOT_STARTED:
        # keep track of start time/frame for later
        WelcomeEscape.tStart = t  # not accounting for scr refresh
        WelcomeEscape.frameNStart = frameN  # exact frame index
        win.timeOnFlip(WelcomeEscape, 'tStartRefresh')  # time at next scr refresh
        WelcomeEscape.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(WelcomeEscape.clock.reset)  # t=0 on next screen flip
        WelcomeEscape.clearEvents(eventType='keyboard')
    if WelcomeEscape.status == STARTED:
        theseKeys = WelcomeEscape.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            WelcomeEscape.keys = theseKeys.name  # just the last key pressed
            WelcomeEscape.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_2_WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_2_WelcomeScreen"-------
for thisComponent in routine_2_WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelcomeText.started', WelcomeText.tStartRefresh)
thisExp.addData('WelcomeText.stopped', WelcomeText.tStopRefresh)
# check responses
if WelcomeEscape.keys in ['', [], None]:  # No response was made
    WelcomeEscape.keys = None
thisExp.addData('WelcomeEscape.keys',WelcomeEscape.keys)
if WelcomeEscape.keys != None:  # we had a response
    thisExp.addData('WelcomeEscape.rt', WelcomeEscape.rt)
thisExp.addData('WelcomeEscape.started', WelcomeEscape.tStartRefresh)
thisExp.addData('WelcomeEscape.stopped', WelcomeEscape.tStopRefresh)
thisExp.nextEntry()
# the Routine "routine_2_WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
BlockLoop = data.TrialHandler(nReps=num_blocks, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='BlockLoop')
thisExp.addLoop(BlockLoop)  # add the loop to the experiment
thisBlockLoop = BlockLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
if thisBlockLoop != None:
    for paramName in thisBlockLoop:
        exec('{} = thisBlockLoop[paramName]'.format(paramName))

for thisBlockLoop in BlockLoop:
    currentLoop = BlockLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
    if thisBlockLoop != None:
        for paramName in thisBlockLoop:
            exec('{} = thisBlockLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "routine_2a_DemoExplanation"-------
    t = 0
    routine_2a_DemoExplanationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    EndDemoExplantion = keyboard.Keyboard()
    # init trial counter
    trial_num_demo = 0 
    
    demo_delta = []
    
    for d in deltas:
        for rep in range(0, num_repsEsts):
            demo_delta.append(d)
    
    # keep track of which components have finished
    routine_2a_DemoExplanationComponents = [text_3, EndDemoExplantion]
    for thisComponent in routine_2a_DemoExplanationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine_2a_DemoExplanation"-------
    while continueRoutine:
        # get current time
        t = routine_2a_DemoExplanationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # not accounting for scr refresh
            text_3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *EndDemoExplantion* updates
        if t >= 2 and EndDemoExplantion.status == NOT_STARTED:
            # keep track of start time/frame for later
            EndDemoExplantion.tStart = t  # not accounting for scr refresh
            EndDemoExplantion.frameNStart = frameN  # exact frame index
            win.timeOnFlip(EndDemoExplantion, 'tStartRefresh')  # time at next scr refresh
            EndDemoExplantion.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(EndDemoExplantion.clock.reset)  # t=0 on next screen flip
            EndDemoExplantion.clearEvents(eventType='keyboard')
        if EndDemoExplantion.status == STARTED:
            theseKeys = EndDemoExplantion.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                EndDemoExplantion.keys = theseKeys.name  # just the last key pressed
                EndDemoExplantion.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_2a_DemoExplanationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_2a_DemoExplanation"-------
    for thisComponent in routine_2a_DemoExplanationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BlockLoop.addData('text_3.started', text_3.tStartRefresh)
    BlockLoop.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if EndDemoExplantion.keys in ['', [], None]:  # No response was made
        EndDemoExplantion.keys = None
    BlockLoop.addData('EndDemoExplantion.keys',EndDemoExplantion.keys)
    if EndDemoExplantion.keys != None:  # we had a response
        BlockLoop.addData('EndDemoExplantion.rt', EndDemoExplantion.rt)
    BlockLoop.addData('EndDemoExplantion.started', EndDemoExplantion.tStartRefresh)
    BlockLoop.addData('EndDemoExplantion.stopped', EndDemoExplantion.tStopRefresh)
    # the Routine "routine_2a_DemoExplanation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    DemoLoop = data.TrialHandler(nReps=demo_trials, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='DemoLoop')
    thisExp.addLoop(DemoLoop)  # add the loop to the experiment
    thisDemoLoop = DemoLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDemoLoop.rgb)
    if thisDemoLoop != None:
        for paramName in thisDemoLoop:
            exec('{} = thisDemoLoop[paramName]'.format(paramName))
    
    for thisDemoLoop in DemoLoop:
        currentLoop = DemoLoop
        # abbreviate parameter names if possible (e.g. rgb = thisDemoLoop.rgb)
        if thisDemoLoop != None:
            for paramName in thisDemoLoop:
                exec('{} = thisDemoLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "routine_3a_PracticeInit"-------
        t = 0
        routine_3a_PracticeInitClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # get delta for this trial
        delta_thisD = demo_delta[trial_num_demo] - avatar_y_offset
        
        # choose presentation side 
        choice = random()
        if choice <.5:
            delta_thisD = -delta_thisD
        
        # set the delay on each trial so pariticpants can't predict 
        # when to respond
        delay = round((random() * 90)) + 60
        
        # keep track of which components have finished
        routine_3a_PracticeInitComponents = []
        for thisComponent in routine_3a_PracticeInitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_3a_PracticeInit"-------
        while continueRoutine:
            # get current time
            t = routine_3a_PracticeInitClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_3a_PracticeInitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_3a_PracticeInit"-------
        for thisComponent in routine_3a_PracticeInitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial_num_demo += 1
        # the Routine "routine_3a_PracticeInit" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "routine_3b_PresentSetup"-------
        t = 0
        routine_3b_PresentSetupClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        DemoKeyboard = keyboard.Keyboard()
        # keep track of which components have finished
        routine_3b_PresentSetupComponents = [borderlinesDemo, DemoKeyboard, AvatarDemo, DemoTarget, StartDemoTrial]
        for thisComponent in routine_3b_PresentSetupComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_3b_PresentSetup"-------
        while continueRoutine:
            # get current time
            t = routine_3b_PresentSetupClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *borderlinesDemo* updates
            if t >= 0.0 and borderlinesDemo.status == NOT_STARTED:
                # keep track of start time/frame for later
                borderlinesDemo.tStart = t  # not accounting for scr refresh
                borderlinesDemo.frameNStart = frameN  # exact frame index
                win.timeOnFlip(borderlinesDemo, 'tStartRefresh')  # time at next scr refresh
                borderlinesDemo.setAutoDraw(True)
            if borderlinesDemo.status == STARTED:  # only update if drawing
                borderlinesDemo.setPos((0, avatar_y_offset), log=False)
                borderlinesDemo.setSize((Screen_width + 10, box_size + 10), log=False)
            
            # *DemoKeyboard* updates
            if t >= 0.0 and DemoKeyboard.status == NOT_STARTED:
                # keep track of start time/frame for later
                DemoKeyboard.tStart = t  # not accounting for scr refresh
                DemoKeyboard.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DemoKeyboard, 'tStartRefresh')  # time at next scr refresh
                DemoKeyboard.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(DemoKeyboard.clock.reset)  # t=0 on next screen flip
                DemoKeyboard.clearEvents(eventType='keyboard')
            if DemoKeyboard.status == STARTED:
                theseKeys = DemoKeyboard.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    DemoKeyboard.keys = theseKeys.name  # just the last key pressed
                    DemoKeyboard.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *AvatarDemo* updates
            if t >= 0.0 and AvatarDemo.status == NOT_STARTED:
                # keep track of start time/frame for later
                AvatarDemo.tStart = t  # not accounting for scr refresh
                AvatarDemo.frameNStart = frameN  # exact frame index
                win.timeOnFlip(AvatarDemo, 'tStartRefresh')  # time at next scr refresh
                AvatarDemo.setAutoDraw(True)
            if AvatarDemo.status == STARTED:  # only update if drawing
                AvatarDemo.setPos((Avatar_x_demo, Avatar_y_demo), log=False)
                AvatarDemo.setSize((box_size, box_size), log=False)
                AvatarDemo.setFillColor(box_truck, log=False)
                AvatarDemo.setLineColor(box_truck, log=False)
            
            # *DemoTarget* updates
            if t >= 0.0 and DemoTarget.status == NOT_STARTED:
                # keep track of start time/frame for later
                DemoTarget.tStart = t  # not accounting for scr refresh
                DemoTarget.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DemoTarget, 'tStartRefresh')  # time at next scr refresh
                DemoTarget.setAutoDraw(True)
            if DemoTarget.status == STARTED:  # only update if drawing
                DemoTarget.setPos((delta_thisD, 0), log=False)
                DemoTarget.setSize((box_size, box_size), log=False)
                DemoTarget.setFillColor(box_build, log=False)
                DemoTarget.setLineColor(box_build, log=False)
            
            # *StartDemoTrial* updates
            if t >= 0.0 and StartDemoTrial.status == NOT_STARTED:
                # keep track of start time/frame for later
                StartDemoTrial.tStart = t  # not accounting for scr refresh
                StartDemoTrial.frameNStart = frameN  # exact frame index
                win.timeOnFlip(StartDemoTrial, 'tStartRefresh')  # time at next scr refresh
                StartDemoTrial.setAutoDraw(True)
            if StartDemoTrial.status == STARTED:  # only update if drawing
                StartDemoTrial.setPos((0, avatar_y_offset + box_size + 10), log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_3b_PresentSetupComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_3b_PresentSetup"-------
        for thisComponent in routine_3b_PresentSetupComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        DemoLoop.addData('borderlinesDemo.started', borderlinesDemo.tStartRefresh)
        DemoLoop.addData('borderlinesDemo.stopped', borderlinesDemo.tStopRefresh)
        # check responses
        if DemoKeyboard.keys in ['', [], None]:  # No response was made
            DemoKeyboard.keys = None
        DemoLoop.addData('DemoKeyboard.keys',DemoKeyboard.keys)
        if DemoKeyboard.keys != None:  # we had a response
            DemoLoop.addData('DemoKeyboard.rt', DemoKeyboard.rt)
        DemoLoop.addData('DemoKeyboard.started', DemoKeyboard.tStartRefresh)
        DemoLoop.addData('DemoKeyboard.stopped', DemoKeyboard.tStopRefresh)
        DemoLoop.addData('AvatarDemo.started', AvatarDemo.tStartRefresh)
        DemoLoop.addData('AvatarDemo.stopped', AvatarDemo.tStopRefresh)
        DemoLoop.addData('DemoTarget.started', DemoTarget.tStartRefresh)
        DemoLoop.addData('DemoTarget.stopped', DemoTarget.tStopRefresh)
        DemoLoop.addData('StartDemoTrial.started', StartDemoTrial.tStartRefresh)
        DemoLoop.addData('StartDemoTrial.stopped', StartDemoTrial.tStopRefresh)
        # the Routine "routine_3b_PresentSetup" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "routine_3c_driving"-------
        t = 0
        routine_3c_drivingClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        frameDemo = 0
        target_colour = box_build
        
        Avatar_x_Demo = 0 
        Avatar_y_Demo = avatar_y_offset
        
        # set colours for arrows 
        up_col    = Arrow_init_colour
        down_col  = Arrow_init_colour
        left_col  = Arrow_init_colour
        right_col = Arrow_init_colour
        # setup some python lists for storing info about the DemoMouse
        DemoMouse.x = []
        DemoMouse.y = []
        DemoMouse.leftButton = []
        DemoMouse.midButton = []
        DemoMouse.rightButton = []
        DemoMouse.time = []
        DemoMouse.clicked_name = []
        gotValidClick = False  # until a click is received
        boundaryDemo.setSize((Screen_width + 10, box_size + 10))
        # keep track of which components have finished
        routine_3c_drivingComponents = [DemoMouse, boundaryDemo, AvatarPlacedDemo, DemoTargetDrive, AvatarDriveDemo, UpClickDemo, DownClickDemo, LeftClickDemo, RightClickDemo, UpArrow, DownArrow, LeftArrow, RightArrow]
        for thisComponent in routine_3c_drivingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_3c_driving"-------
        while continueRoutine:
            # get current time
            t = routine_3c_drivingClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            frameDemo += 1
            
            # stop mouse moving if it's too early
            if frameDemo <= delay:
                DrivingMouse.setPos(newPos =(0, Arrow_y[2]))
            
            # change colour after delay
            if frameDemo >= delay:
                target_colour = box_burning
                
            # update position 
            if DemoMouse.isPressedIn(UpClickDemo):
                Avatar_y_Demo += avatar_speed
                up_col = Arrow_clik_colour
            elif DemoMouse.isPressedIn(DownClickDemo):
                Avatar_y_Demo -= avatar_speed
                down_col = Arrow_clik_colour
            elif DemoMouse.isPressedIn(RightClickDemo):
                Avatar_x_Demo += avatar_speed
                right_col = Arrow_clik_colour
            elif DemoMouse.isPressedIn(LeftClickDemo):
                Avatar_x_Demo -= avatar_speed
                left_col = Arrow_clik_colour
            else:
                # reset the colours if nothing is clicked
                up_col    = Arrow_init_colour
                down_col  = Arrow_init_colour
                left_col  = Arrow_init_colour
                right_col = Arrow_init_colour
            
            
            # check for success or failure
            # Was the target reached?
            x_dist = Avatar_x_Demo - delta_thisD
            y_dist = Avatar_y_Demo - 0
            dist = (x_dist)**2 + (y_dist)**2
            
            
            if dist <= avatar_reach**2:
                success = 1
                continueRoutine = False
                target_colour = box_build
            
            # has time run out?
            if frameDemo >= Trial_time + delay:
                success = 0
                target_colour = box_burnt
            # *DemoMouse* updates
            if frameN >= delay and DemoMouse.status == NOT_STARTED:
                # keep track of start time/frame for later
                DemoMouse.tStart = t  # not accounting for scr refresh
                DemoMouse.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DemoMouse, 'tStartRefresh')  # time at next scr refresh
                DemoMouse.status = STARTED
                DemoMouse.mouseClock.reset()
                prevButtonState = DemoMouse.getPressed()  # if button is down already this ISN'T a new click
            if DemoMouse.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                DemoMouse.tStop = t  # not accounting for scr refresh
                DemoMouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DemoMouse, 'tStopRefresh')  # time at next scr refresh
                DemoMouse.status = FINISHED
            if DemoMouse.status == STARTED:  # only update if started and not finished!
                x, y = DemoMouse.getPos()
                DemoMouse.x.append(x)
                DemoMouse.y.append(y)
                buttons = DemoMouse.getPressed()
                DemoMouse.leftButton.append(buttons[0])
                DemoMouse.midButton.append(buttons[1])
                DemoMouse.rightButton.append(buttons[2])
                DemoMouse.time.append(DemoMouse.mouseClock.getTime())
            
            # *boundaryDemo* updates
            if t >= 0.0 and boundaryDemo.status == NOT_STARTED:
                # keep track of start time/frame for later
                boundaryDemo.tStart = t  # not accounting for scr refresh
                boundaryDemo.frameNStart = frameN  # exact frame index
                win.timeOnFlip(boundaryDemo, 'tStartRefresh')  # time at next scr refresh
                boundaryDemo.setAutoDraw(True)
            if boundaryDemo.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                boundaryDemo.tStop = t  # not accounting for scr refresh
                boundaryDemo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(boundaryDemo, 'tStopRefresh')  # time at next scr refresh
                boundaryDemo.setAutoDraw(False)
            if boundaryDemo.status == STARTED:  # only update if drawing
                boundaryDemo.setPos((0, avatar_y_offset), log=False)
            
            # *AvatarPlacedDemo* updates
            if t >= 0.0 and AvatarPlacedDemo.status == NOT_STARTED:
                # keep track of start time/frame for later
                AvatarPlacedDemo.tStart = t  # not accounting for scr refresh
                AvatarPlacedDemo.frameNStart = frameN  # exact frame index
                win.timeOnFlip(AvatarPlacedDemo, 'tStartRefresh')  # time at next scr refresh
                AvatarPlacedDemo.setAutoDraw(True)
            if AvatarPlacedDemo.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                AvatarPlacedDemo.tStop = t  # not accounting for scr refresh
                AvatarPlacedDemo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AvatarPlacedDemo, 'tStopRefresh')  # time at next scr refresh
                AvatarPlacedDemo.setAutoDraw(False)
            if AvatarPlacedDemo.status == STARTED:  # only update if drawing
                AvatarPlacedDemo.setPos((0, avatar_y_offset), log=False)
                AvatarPlacedDemo.setSize((box_size, box_size), log=False)
                AvatarPlacedDemo.setFillColor(box_placed, log=False)
                AvatarPlacedDemo.setLineColor(box_placed, log=False)
            
            # *DemoTargetDrive* updates
            if t >= 0.0 and DemoTargetDrive.status == NOT_STARTED:
                # keep track of start time/frame for later
                DemoTargetDrive.tStart = t  # not accounting for scr refresh
                DemoTargetDrive.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DemoTargetDrive, 'tStartRefresh')  # time at next scr refresh
                DemoTargetDrive.setAutoDraw(True)
            if DemoTargetDrive.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                DemoTargetDrive.tStop = t  # not accounting for scr refresh
                DemoTargetDrive.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DemoTargetDrive, 'tStopRefresh')  # time at next scr refresh
                DemoTargetDrive.setAutoDraw(False)
            if DemoTargetDrive.status == STARTED:  # only update if drawing
                DemoTargetDrive.setPos((delta_thisD, 0), log=False)
                DemoTargetDrive.setSize((box_size, box_size), log=False)
                DemoTargetDrive.setFillColor(target_colour, log=False)
                DemoTargetDrive.setLineColor(target_colour, log=False)
            
            # *AvatarDriveDemo* updates
            if t >= 0.0 and AvatarDriveDemo.status == NOT_STARTED:
                # keep track of start time/frame for later
                AvatarDriveDemo.tStart = t  # not accounting for scr refresh
                AvatarDriveDemo.frameNStart = frameN  # exact frame index
                win.timeOnFlip(AvatarDriveDemo, 'tStartRefresh')  # time at next scr refresh
                AvatarDriveDemo.setAutoDraw(True)
            if AvatarDriveDemo.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                AvatarDriveDemo.tStop = t  # not accounting for scr refresh
                AvatarDriveDemo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AvatarDriveDemo, 'tStopRefresh')  # time at next scr refresh
                AvatarDriveDemo.setAutoDraw(False)
            if AvatarDriveDemo.status == STARTED:  # only update if drawing
                AvatarDriveDemo.setPos((Avatar_x_Demo, Avatar_y_Demo), log=False)
                AvatarDriveDemo.setSize((box_size, box_size), log=False)
                AvatarDriveDemo.setFillColor(box_truck, log=False)
                AvatarDriveDemo.setLineColor(box_truck, log=False)
            
            # *UpClickDemo* updates
            if t >= 0.0 and UpClickDemo.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpClickDemo.tStart = t  # not accounting for scr refresh
                UpClickDemo.frameNStart = frameN  # exact frame index
                win.timeOnFlip(UpClickDemo, 'tStartRefresh')  # time at next scr refresh
                UpClickDemo.setAutoDraw(True)
            if UpClickDemo.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                UpClickDemo.tStop = t  # not accounting for scr refresh
                UpClickDemo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(UpClickDemo, 'tStopRefresh')  # time at next scr refresh
                UpClickDemo.setAutoDraw(False)
            if UpClickDemo.status == STARTED:  # only update if drawing
                UpClickDemo.setPos((Arrow_x[0], Arrow_y[0]), log=False)
                UpClickDemo.setSize((Arrow_size, Arrow_size), log=False)
                UpClickDemo.setFillColor([1,1,1], log=False)
                UpClickDemo.setLineColor([-1,-1,-1], log=False)
            
            # *DownClickDemo* updates
            if t >= 0.0 and DownClickDemo.status == NOT_STARTED:
                # keep track of start time/frame for later
                DownClickDemo.tStart = t  # not accounting for scr refresh
                DownClickDemo.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DownClickDemo, 'tStartRefresh')  # time at next scr refresh
                DownClickDemo.setAutoDraw(True)
            if DownClickDemo.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                DownClickDemo.tStop = t  # not accounting for scr refresh
                DownClickDemo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DownClickDemo, 'tStopRefresh')  # time at next scr refresh
                DownClickDemo.setAutoDraw(False)
            if DownClickDemo.status == STARTED:  # only update if drawing
                DownClickDemo.setPos((Arrow_x[1], Arrow_y[1]), log=False)
                DownClickDemo.setSize((Arrow_size, Arrow_size), log=False)
            
            # *LeftClickDemo* updates
            if t >= 0.0 and LeftClickDemo.status == NOT_STARTED:
                # keep track of start time/frame for later
                LeftClickDemo.tStart = t  # not accounting for scr refresh
                LeftClickDemo.frameNStart = frameN  # exact frame index
                win.timeOnFlip(LeftClickDemo, 'tStartRefresh')  # time at next scr refresh
                LeftClickDemo.setAutoDraw(True)
            if LeftClickDemo.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                LeftClickDemo.tStop = t  # not accounting for scr refresh
                LeftClickDemo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(LeftClickDemo, 'tStopRefresh')  # time at next scr refresh
                LeftClickDemo.setAutoDraw(False)
            if LeftClickDemo.status == STARTED:  # only update if drawing
                LeftClickDemo.setPos((Arrow_x[2], Arrow_y[2]), log=False)
                LeftClickDemo.setSize((Arrow_size, Arrow_size), log=False)
            
            # *RightClickDemo* updates
            if t >= 0.0 and RightClickDemo.status == NOT_STARTED:
                # keep track of start time/frame for later
                RightClickDemo.tStart = t  # not accounting for scr refresh
                RightClickDemo.frameNStart = frameN  # exact frame index
                win.timeOnFlip(RightClickDemo, 'tStartRefresh')  # time at next scr refresh
                RightClickDemo.setAutoDraw(True)
            if RightClickDemo.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                RightClickDemo.tStop = t  # not accounting for scr refresh
                RightClickDemo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RightClickDemo, 'tStopRefresh')  # time at next scr refresh
                RightClickDemo.setAutoDraw(False)
            if RightClickDemo.status == STARTED:  # only update if drawing
                RightClickDemo.setPos((Arrow_x[3], Arrow_y[3]), log=False)
                RightClickDemo.setSize((Arrow_size, Arrow_size), log=False)
            
            # *UpArrow* updates
            if t >= 0.0 and UpArrow.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpArrow.tStart = t  # not accounting for scr refresh
                UpArrow.frameNStart = frameN  # exact frame index
                win.timeOnFlip(UpArrow, 'tStartRefresh')  # time at next scr refresh
                UpArrow.setAutoDraw(True)
            if UpArrow.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                UpArrow.tStop = t  # not accounting for scr refresh
                UpArrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(UpArrow, 'tStopRefresh')  # time at next scr refresh
                UpArrow.setAutoDraw(False)
            if UpArrow.status == STARTED:  # only update if drawing
                UpArrow.setPos((Arrow_x[0], Arrow_y[0]), log=False)
                UpArrow.setSize((Arrow_size, Arrow_size), log=False)
                UpArrow.setOri((Arrow_orient[0]), log=False)
                UpArrow.setFillColor(up_col, log=False)
                UpArrow.setLineColor([-1,-1,-1], log=False)
            
            # *DownArrow* updates
            if t >= 0.0 and DownArrow.status == NOT_STARTED:
                # keep track of start time/frame for later
                DownArrow.tStart = t  # not accounting for scr refresh
                DownArrow.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DownArrow, 'tStartRefresh')  # time at next scr refresh
                DownArrow.setAutoDraw(True)
            if DownArrow.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                DownArrow.tStop = t  # not accounting for scr refresh
                DownArrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DownArrow, 'tStopRefresh')  # time at next scr refresh
                DownArrow.setAutoDraw(False)
            if DownArrow.status == STARTED:  # only update if drawing
                DownArrow.setPos((Arrow_x[1], Arrow_y[1]), log=False)
                DownArrow.setSize((Arrow_size, Arrow_size), log=False)
                DownArrow.setOri(Arrow_orient[1], log=False)
                DownArrow.setFillColor(down_col, log=False)
            
            # *LeftArrow* updates
            if t >= 0.0 and LeftArrow.status == NOT_STARTED:
                # keep track of start time/frame for later
                LeftArrow.tStart = t  # not accounting for scr refresh
                LeftArrow.frameNStart = frameN  # exact frame index
                win.timeOnFlip(LeftArrow, 'tStartRefresh')  # time at next scr refresh
                LeftArrow.setAutoDraw(True)
            if LeftArrow.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                LeftArrow.tStop = t  # not accounting for scr refresh
                LeftArrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(LeftArrow, 'tStopRefresh')  # time at next scr refresh
                LeftArrow.setAutoDraw(False)
            if LeftArrow.status == STARTED:  # only update if drawing
                LeftArrow.setPos((Arrow_x[2], Arrow_y[2]), log=False)
                LeftArrow.setSize((Arrow_size, Arrow_size), log=False)
                LeftArrow.setOri(Arrow_orient[2], log=False)
                LeftArrow.setFillColor(left_col, log=False)
            
            # *RightArrow* updates
            if t >= 0.0 and RightArrow.status == NOT_STARTED:
                # keep track of start time/frame for later
                RightArrow.tStart = t  # not accounting for scr refresh
                RightArrow.frameNStart = frameN  # exact frame index
                win.timeOnFlip(RightArrow, 'tStartRefresh')  # time at next scr refresh
                RightArrow.setAutoDraw(True)
            if RightArrow.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                RightArrow.tStop = t  # not accounting for scr refresh
                RightArrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RightArrow, 'tStopRefresh')  # time at next scr refresh
                RightArrow.setAutoDraw(False)
            if RightArrow.status == STARTED:  # only update if drawing
                RightArrow.setPos((Arrow_x[3], Arrow_y[3]), log=False)
                RightArrow.setSize((Arrow_size, Arrow_size), log=False)
                RightArrow.setOri(Arrow_orient[3], log=False)
                RightArrow.setFillColor(right_col, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_3c_drivingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_3c_driving"-------
        for thisComponent in routine_3c_drivingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for DemoLoop (TrialHandler)
        DemoLoop.addData('DemoMouse.x', DemoMouse.x)
        DemoLoop.addData('DemoMouse.y', DemoMouse.y)
        DemoLoop.addData('DemoMouse.leftButton', DemoMouse.leftButton)
        DemoLoop.addData('DemoMouse.midButton', DemoMouse.midButton)
        DemoLoop.addData('DemoMouse.rightButton', DemoMouse.rightButton)
        DemoLoop.addData('DemoMouse.time', DemoMouse.time)
        DemoLoop.addData('DemoMouse.clicked_name', DemoMouse.clicked_name)
        DemoLoop.addData('DemoMouse.started', DemoMouse.tStart)
        DemoLoop.addData('DemoMouse.stopped', DemoMouse.tStop)
        DemoLoop.addData('boundaryDemo.started', boundaryDemo.tStartRefresh)
        DemoLoop.addData('boundaryDemo.stopped', boundaryDemo.tStopRefresh)
        DemoLoop.addData('AvatarPlacedDemo.started', AvatarPlacedDemo.tStartRefresh)
        DemoLoop.addData('AvatarPlacedDemo.stopped', AvatarPlacedDemo.tStopRefresh)
        DemoLoop.addData('DemoTargetDrive.started', DemoTargetDrive.tStartRefresh)
        DemoLoop.addData('DemoTargetDrive.stopped', DemoTargetDrive.tStopRefresh)
        DemoLoop.addData('AvatarDriveDemo.started', AvatarDriveDemo.tStartRefresh)
        DemoLoop.addData('AvatarDriveDemo.stopped', AvatarDriveDemo.tStopRefresh)
        DemoLoop.addData('UpClickDemo.started', UpClickDemo.tStartRefresh)
        DemoLoop.addData('UpClickDemo.stopped', UpClickDemo.tStopRefresh)
        DemoLoop.addData('DownClickDemo.started', DownClickDemo.tStartRefresh)
        DemoLoop.addData('DownClickDemo.stopped', DownClickDemo.tStopRefresh)
        DemoLoop.addData('LeftClickDemo.started', LeftClickDemo.tStartRefresh)
        DemoLoop.addData('LeftClickDemo.stopped', LeftClickDemo.tStopRefresh)
        DemoLoop.addData('RightClickDemo.started', RightClickDemo.tStartRefresh)
        DemoLoop.addData('RightClickDemo.stopped', RightClickDemo.tStopRefresh)
        DemoLoop.addData('UpArrow.started', UpArrow.tStartRefresh)
        DemoLoop.addData('UpArrow.stopped', UpArrow.tStopRefresh)
        DemoLoop.addData('DownArrow.started', DownArrow.tStartRefresh)
        DemoLoop.addData('DownArrow.stopped', DownArrow.tStopRefresh)
        DemoLoop.addData('LeftArrow.started', LeftArrow.tStartRefresh)
        DemoLoop.addData('LeftArrow.stopped', LeftArrow.tStopRefresh)
        DemoLoop.addData('RightArrow.started', RightArrow.tStartRefresh)
        DemoLoop.addData('RightArrow.stopped', RightArrow.tStopRefresh)
        # the Routine "routine_3c_driving" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "routine_3d_feedback"-------
        t = 0
        routine_3d_feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if success == 1:
            Feedback_Text = "You made it! :)"
        elif success == 0: 
            Feedback_Text = "The house burnt down :/"
        DemoFeedBackMoveOn = keyboard.Keyboard()
        # keep track of which components have finished
        routine_3d_feedbackComponents = [AvatarFeedbackDemo, BoundaryFeedBack, PlacedFeedback, AvatarDemoFeedback, FeedbackText, DemoFeedBackMoveOn, FeedbackText_2]
        for thisComponent in routine_3d_feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_3d_feedback"-------
        while continueRoutine:
            # get current time
            t = routine_3d_feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AvatarFeedbackDemo* updates
            if t >= 0.0 and AvatarFeedbackDemo.status == NOT_STARTED:
                # keep track of start time/frame for later
                AvatarFeedbackDemo.tStart = t  # not accounting for scr refresh
                AvatarFeedbackDemo.frameNStart = frameN  # exact frame index
                win.timeOnFlip(AvatarFeedbackDemo, 'tStartRefresh')  # time at next scr refresh
                AvatarFeedbackDemo.setAutoDraw(True)
            if AvatarFeedbackDemo.status == STARTED:  # only update if drawing
                AvatarFeedbackDemo.setPos((delta_thisD, 0), log=False)
                AvatarFeedbackDemo.setSize((box_size, box_size), log=False)
                AvatarFeedbackDemo.setFillColor(target_colour, log=False)
                AvatarFeedbackDemo.setLineColor(target_colour, log=False)
            
            # *BoundaryFeedBack* updates
            if t >= 0.0 and BoundaryFeedBack.status == NOT_STARTED:
                # keep track of start time/frame for later
                BoundaryFeedBack.tStart = t  # not accounting for scr refresh
                BoundaryFeedBack.frameNStart = frameN  # exact frame index
                win.timeOnFlip(BoundaryFeedBack, 'tStartRefresh')  # time at next scr refresh
                BoundaryFeedBack.setAutoDraw(True)
            if BoundaryFeedBack.status == STARTED:  # only update if drawing
                BoundaryFeedBack.setPos((0, avatar_y_offset), log=False)
                BoundaryFeedBack.setSize((Screen_width + 10, box_size + 10), log=False)
            
            # *PlacedFeedback* updates
            if t >= 0.0 and PlacedFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                PlacedFeedback.tStart = t  # not accounting for scr refresh
                PlacedFeedback.frameNStart = frameN  # exact frame index
                win.timeOnFlip(PlacedFeedback, 'tStartRefresh')  # time at next scr refresh
                PlacedFeedback.setAutoDraw(True)
            if PlacedFeedback.status == STARTED:  # only update if drawing
                PlacedFeedback.setPos((0, avatar_y_offset), log=False)
                PlacedFeedback.setSize((box_size, box_size), log=False)
                PlacedFeedback.setFillColor(box_placed, log=False)
                PlacedFeedback.setLineColor(box_placed, log=False)
            
            # *AvatarDemoFeedback* updates
            if t >= 0.0 and AvatarDemoFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                AvatarDemoFeedback.tStart = t  # not accounting for scr refresh
                AvatarDemoFeedback.frameNStart = frameN  # exact frame index
                win.timeOnFlip(AvatarDemoFeedback, 'tStartRefresh')  # time at next scr refresh
                AvatarDemoFeedback.setAutoDraw(True)
            if AvatarDemoFeedback.status == STARTED:  # only update if drawing
                AvatarDemoFeedback.setPos((Avatar_x_Demo, Avatar_y_Demo), log=False)
                AvatarDemoFeedback.setSize((box_size, box_size), log=False)
                AvatarDemoFeedback.setFillColor(box_truck, log=False)
                AvatarDemoFeedback.setLineColor(box_truck, log=False)
            
            # *FeedbackText* updates
            if t >= 0.0 and FeedbackText.status == NOT_STARTED:
                # keep track of start time/frame for later
                FeedbackText.tStart = t  # not accounting for scr refresh
                FeedbackText.frameNStart = frameN  # exact frame index
                win.timeOnFlip(FeedbackText, 'tStartRefresh')  # time at next scr refresh
                FeedbackText.setAutoDraw(True)
            if FeedbackText.status == STARTED:  # only update if drawing
                FeedbackText.setPos((0, avatar_y_offset + box_size + 10), log=False)
                FeedbackText.setText(Feedback_Text, log=False)
            
            # *DemoFeedBackMoveOn* updates
            if frameN >= 60 and DemoFeedBackMoveOn.status == NOT_STARTED:
                # keep track of start time/frame for later
                DemoFeedBackMoveOn.tStart = t  # not accounting for scr refresh
                DemoFeedBackMoveOn.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DemoFeedBackMoveOn, 'tStartRefresh')  # time at next scr refresh
                DemoFeedBackMoveOn.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(DemoFeedBackMoveOn.clock.reset)  # t=0 on next screen flip
                DemoFeedBackMoveOn.clearEvents(eventType='keyboard')
            if DemoFeedBackMoveOn.status == STARTED:
                theseKeys = DemoFeedBackMoveOn.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    DemoFeedBackMoveOn.keys = theseKeys.name  # just the last key pressed
                    DemoFeedBackMoveOn.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *FeedbackText_2* updates
            if t >= 0.0 and FeedbackText_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                FeedbackText_2.tStart = t  # not accounting for scr refresh
                FeedbackText_2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(FeedbackText_2, 'tStartRefresh')  # time at next scr refresh
                FeedbackText_2.setAutoDraw(True)
            if FeedbackText_2.status == STARTED:  # only update if drawing
                FeedbackText_2.setPos((0, -avatar_y_offset), log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_3d_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_3d_feedback"-------
        for thisComponent in routine_3d_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        DemoLoop.addData('AvatarFeedbackDemo.started', AvatarFeedbackDemo.tStartRefresh)
        DemoLoop.addData('AvatarFeedbackDemo.stopped', AvatarFeedbackDemo.tStopRefresh)
        DemoLoop.addData('BoundaryFeedBack.started', BoundaryFeedBack.tStartRefresh)
        DemoLoop.addData('BoundaryFeedBack.stopped', BoundaryFeedBack.tStopRefresh)
        DemoLoop.addData('PlacedFeedback.started', PlacedFeedback.tStartRefresh)
        DemoLoop.addData('PlacedFeedback.stopped', PlacedFeedback.tStopRefresh)
        DemoLoop.addData('AvatarDemoFeedback.started', AvatarDemoFeedback.tStartRefresh)
        DemoLoop.addData('AvatarDemoFeedback.stopped', AvatarDemoFeedback.tStopRefresh)
        DemoLoop.addData('FeedbackText.started', FeedbackText.tStartRefresh)
        DemoLoop.addData('FeedbackText.stopped', FeedbackText.tStopRefresh)
        # check responses
        if DemoFeedBackMoveOn.keys in ['', [], None]:  # No response was made
            DemoFeedBackMoveOn.keys = None
        DemoLoop.addData('DemoFeedBackMoveOn.keys',DemoFeedBackMoveOn.keys)
        if DemoFeedBackMoveOn.keys != None:  # we had a response
            DemoLoop.addData('DemoFeedBackMoveOn.rt', DemoFeedBackMoveOn.rt)
        DemoLoop.addData('DemoFeedBackMoveOn.started', DemoFeedBackMoveOn.tStartRefresh)
        DemoLoop.addData('DemoFeedBackMoveOn.stopped', DemoFeedBackMoveOn.tStopRefresh)
        DemoLoop.addData('FeedbackText_2.started', FeedbackText_2.tStartRefresh)
        DemoLoop.addData('FeedbackText_2.stopped', FeedbackText_2.tStopRefresh)
        # the Routine "routine_3d_feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed demo_trials repeats of 'DemoLoop'
    
    
    # ------Prepare to start Routine "routine_4_Trial_Instructions"-------
    t = 0
    routine_4_Trial_InstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    InstSkip = keyboard.Keyboard()
    trial_num = 0
    
    delta_order = []
    for d in deltas:
        for rep in range(0,num_reps):
            delta_order.append(d)
     
    # delta_order = shuffle(numpy.repeat(deltas, num_reps))
    shuffle(delta_order)
    # keep track of which components have finished
    routine_4_Trial_InstructionsComponents = [TrialInst, InstSkip]
    for thisComponent in routine_4_Trial_InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine_4_Trial_Instructions"-------
    while continueRoutine:
        # get current time
        t = routine_4_Trial_InstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TrialInst* updates
        if t >= 0.0 and TrialInst.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialInst.tStart = t  # not accounting for scr refresh
            TrialInst.frameNStart = frameN  # exact frame index
            win.timeOnFlip(TrialInst, 'tStartRefresh')  # time at next scr refresh
            TrialInst.setAutoDraw(True)
        
        # *InstSkip* updates
        if t >= 1 and InstSkip.status == NOT_STARTED:
            # keep track of start time/frame for later
            InstSkip.tStart = t  # not accounting for scr refresh
            InstSkip.frameNStart = frameN  # exact frame index
            win.timeOnFlip(InstSkip, 'tStartRefresh')  # time at next scr refresh
            InstSkip.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(InstSkip.clock.reset)  # t=0 on next screen flip
            InstSkip.clearEvents(eventType='keyboard')
        if InstSkip.status == STARTED:
            theseKeys = InstSkip.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                InstSkip.keys = theseKeys.name  # just the last key pressed
                InstSkip.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_4_Trial_InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_4_Trial_Instructions"-------
    for thisComponent in routine_4_Trial_InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BlockLoop.addData('TrialInst.started', TrialInst.tStartRefresh)
    BlockLoop.addData('TrialInst.stopped', TrialInst.tStopRefresh)
    # check responses
    if InstSkip.keys in ['', [], None]:  # No response was made
        InstSkip.keys = None
    BlockLoop.addData('InstSkip.keys',InstSkip.keys)
    if InstSkip.keys != None:  # we had a response
        BlockLoop.addData('InstSkip.rt', InstSkip.rt)
    BlockLoop.addData('InstSkip.started', InstSkip.tStartRefresh)
    BlockLoop.addData('InstSkip.stopped', InstSkip.tStopRefresh)
    # the Routine "routine_4_Trial_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    DecisionTrialLoop = data.TrialHandler(nReps=num_trials, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='DecisionTrialLoop')
    thisExp.addLoop(DecisionTrialLoop)  # add the loop to the experiment
    thisDecisionTrialLoop = DecisionTrialLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDecisionTrialLoop.rgb)
    if thisDecisionTrialLoop != None:
        for paramName in thisDecisionTrialLoop:
            exec('{} = thisDecisionTrialLoop[paramName]'.format(paramName))
    
    for thisDecisionTrialLoop in DecisionTrialLoop:
        currentLoop = DecisionTrialLoop
        # abbreviate parameter names if possible (e.g. rgb = thisDecisionTrialLoop.rgb)
        if thisDecisionTrialLoop != None:
            for paramName in thisDecisionTrialLoop:
                exec('{} = thisDecisionTrialLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "routine_5a_PlaceAvatarInit"-------
        t = 0
        routine_5a_PlaceAvatarInitClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # get delta for this trial
        delta_thisT = delta_order[trial_num] - avatar_y_offset
        
        # set target position
        left_target = -delta_thisT
        right_target = delta_thisT
        
        # set the delay on each trial so pariticpants can't predict 
        # when to respond
        delay = round((random() * 90)) + 60
        
        # Tried to append another trial given some condition
        # Might not be able to do that too easily... 
        #if delta_thisT == 200:
        #    deltas.append(200)
        #    num_trials += 1
        
        
        # setting colours
        left_colour = box_build
        right_colour = box_build
        
        # choose target
        choice = random()
        if choice <.5:
            target = "left"
        else: 
            target = "right"
            
        # Isn't quite working... but it's not the most important step just now
        # choice = random.choice([0,1])
        # print(choice)
        #if choice == 1:
        #    left_colour = box_burning
        #    right_colour = box_build
        #else :
        #    left_colour = box_burning
        #    right_colour = box_build
        # keep track of which components have finished
        routine_5a_PlaceAvatarInitComponents = []
        for thisComponent in routine_5a_PlaceAvatarInitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_5a_PlaceAvatarInit"-------
        while continueRoutine:
            # get current time
            t = routine_5a_PlaceAvatarInitClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_5a_PlaceAvatarInitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_5a_PlaceAvatarInit"-------
        for thisComponent in routine_5a_PlaceAvatarInitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial_num += 1
        # the Routine "routine_5a_PlaceAvatarInit" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "routine_5b_PlacingAvatar"-------
        t = 0
        routine_5b_PlacingAvatarClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the AvatarMouse
        AvatarMouse.x = []
        AvatarMouse.y = []
        AvatarMouse.leftButton = []
        AvatarMouse.midButton = []
        AvatarMouse.rightButton = []
        AvatarMouse.time = []
        gotValidClick = False  # until a click is received
        AvatarMouse.mouseClock.reset()
        PlacingKeyboard = keyboard.Keyboard()
        frame = 0
        Avatar_x = 0
        # keep track of which components have finished
        routine_5b_PlacingAvatarComponents = [PlacementArea, AvatarMouse, leftTarget, rightTarget, PlacingKeyboard, AvatarPlace]
        for thisComponent in routine_5b_PlacingAvatarComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_5b_PlacingAvatar"-------
        while continueRoutine:
            # get current time
            t = routine_5b_PlacingAvatarClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PlacementArea* updates
            if t >= 0.0 and PlacementArea.status == NOT_STARTED:
                # keep track of start time/frame for later
                PlacementArea.tStart = t  # not accounting for scr refresh
                PlacementArea.frameNStart = frameN  # exact frame index
                win.timeOnFlip(PlacementArea, 'tStartRefresh')  # time at next scr refresh
                PlacementArea.setAutoDraw(True)
            if PlacementArea.status == STARTED:  # only update if drawing
                PlacementArea.setPos((0, avatar_y_offset), log=False)
                PlacementArea.setSize((Screen_width, box_size + 10), log=False)
            # *AvatarMouse* updates
            if frameN >= 0.0 and AvatarMouse.status == NOT_STARTED:
                # keep track of start time/frame for later
                AvatarMouse.tStart = t  # not accounting for scr refresh
                AvatarMouse.frameNStart = frameN  # exact frame index
                win.timeOnFlip(AvatarMouse, 'tStartRefresh')  # time at next scr refresh
                AvatarMouse.status = STARTED
                prevButtonState = AvatarMouse.getPressed()  # if button is down already this ISN'T a new click
            if AvatarMouse.status == STARTED:  # only update if started and not finished!
                x, y = AvatarMouse.getPos()
                AvatarMouse.x.append(x)
                AvatarMouse.y.append(y)
                buttons = AvatarMouse.getPressed()
                AvatarMouse.leftButton.append(buttons[0])
                AvatarMouse.midButton.append(buttons[1])
                AvatarMouse.rightButton.append(buttons[2])
                AvatarMouse.time.append(AvatarMouse.mouseClock.getTime())
            
            # *leftTarget* updates
            if t >= 0.0 and leftTarget.status == NOT_STARTED:
                # keep track of start time/frame for later
                leftTarget.tStart = t  # not accounting for scr refresh
                leftTarget.frameNStart = frameN  # exact frame index
                win.timeOnFlip(leftTarget, 'tStartRefresh')  # time at next scr refresh
                leftTarget.setAutoDraw(True)
            if leftTarget.status == STARTED:  # only update if drawing
                leftTarget.setPos((left_target, 0), log=False)
                leftTarget.setSize((box_size, box_size), log=False)
                leftTarget.setFillColor(box_build, log=False)
                leftTarget.setLineColor(box_build, log=False)
            
            # *rightTarget* updates
            if t >= 0.0 and rightTarget.status == NOT_STARTED:
                # keep track of start time/frame for later
                rightTarget.tStart = t  # not accounting for scr refresh
                rightTarget.frameNStart = frameN  # exact frame index
                win.timeOnFlip(rightTarget, 'tStartRefresh')  # time at next scr refresh
                rightTarget.setAutoDraw(True)
            if rightTarget.status == STARTED:  # only update if drawing
                rightTarget.setPos((right_target, 0), log=False)
                rightTarget.setSize((box_size, box_size), log=False)
                rightTarget.setFillColor(box_build, log=False)
                rightTarget.setLineColor(box_build, log=False)
            
            # *PlacingKeyboard* updates
            if t >= 0.0 and PlacingKeyboard.status == NOT_STARTED:
                # keep track of start time/frame for later
                PlacingKeyboard.tStart = t  # not accounting for scr refresh
                PlacingKeyboard.frameNStart = frameN  # exact frame index
                win.timeOnFlip(PlacingKeyboard, 'tStartRefresh')  # time at next scr refresh
                PlacingKeyboard.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(PlacingKeyboard.clock.reset)  # t=0 on next screen flip
                PlacingKeyboard.clearEvents(eventType='keyboard')
            if PlacingKeyboard.status == STARTED:
                theseKeys = PlacingKeyboard.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    PlacingKeyboard.keys = theseKeys.name  # just the last key pressed
                    PlacingKeyboard.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *AvatarPlace* updates
            if t >= 0.0 and AvatarPlace.status == NOT_STARTED:
                # keep track of start time/frame for later
                AvatarPlace.tStart = t  # not accounting for scr refresh
                AvatarPlace.frameNStart = frameN  # exact frame index
                win.timeOnFlip(AvatarPlace, 'tStartRefresh')  # time at next scr refresh
                AvatarPlace.setAutoDraw(True)
            if AvatarPlace.status == STARTED:  # only update if drawing
                AvatarPlace.setPos((Avatar_x, Avatar_y), log=False)
                AvatarPlace.setSize((box_size, box_size), log=False)
                AvatarPlace.setFillColor(box_truck, log=False)
                AvatarPlace.setLineColor(box_truck, log=False)
            # check for mouse click
            if AvatarMouse.getPos()[1] > 100 - (box_size/2) and AvatarMouse.getPos()[1] < 100 + (box_size/2):
                if AvatarMouse.getPressed()[0]:
                    Avatar_x = AvatarMouse.getPos()[0]
                    Avatar_y = 100
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_5b_PlacingAvatarComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_5b_PlacingAvatar"-------
        for thisComponent in routine_5b_PlacingAvatarComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        DecisionTrialLoop.addData('PlacementArea.started', PlacementArea.tStartRefresh)
        DecisionTrialLoop.addData('PlacementArea.stopped', PlacementArea.tStopRefresh)
        # store data for DecisionTrialLoop (TrialHandler)
        DecisionTrialLoop.addData('AvatarMouse.x', AvatarMouse.x)
        DecisionTrialLoop.addData('AvatarMouse.y', AvatarMouse.y)
        DecisionTrialLoop.addData('AvatarMouse.leftButton', AvatarMouse.leftButton)
        DecisionTrialLoop.addData('AvatarMouse.midButton', AvatarMouse.midButton)
        DecisionTrialLoop.addData('AvatarMouse.rightButton', AvatarMouse.rightButton)
        DecisionTrialLoop.addData('AvatarMouse.time', AvatarMouse.time)
        DecisionTrialLoop.addData('AvatarMouse.started', AvatarMouse.tStart)
        DecisionTrialLoop.addData('AvatarMouse.stopped', AvatarMouse.tStop)
        DecisionTrialLoop.addData('leftTarget.started', leftTarget.tStartRefresh)
        DecisionTrialLoop.addData('leftTarget.stopped', leftTarget.tStopRefresh)
        DecisionTrialLoop.addData('rightTarget.started', rightTarget.tStartRefresh)
        DecisionTrialLoop.addData('rightTarget.stopped', rightTarget.tStopRefresh)
        # check responses
        if PlacingKeyboard.keys in ['', [], None]:  # No response was made
            PlacingKeyboard.keys = None
        DecisionTrialLoop.addData('PlacingKeyboard.keys',PlacingKeyboard.keys)
        if PlacingKeyboard.keys != None:  # we had a response
            DecisionTrialLoop.addData('PlacingKeyboard.rt', PlacingKeyboard.rt)
        DecisionTrialLoop.addData('PlacingKeyboard.started', PlacingKeyboard.tStartRefresh)
        DecisionTrialLoop.addData('PlacingKeyboard.stopped', PlacingKeyboard.tStopRefresh)
        DecisionTrialLoop.addData('AvatarPlace.started', AvatarPlace.tStartRefresh)
        DecisionTrialLoop.addData('AvatarPlace.stopped', AvatarPlace.tStopRefresh)
        # the Routine "routine_5b_PlacingAvatar" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "routine_5c_DrivingAvatar"-------
        t = 0
        routine_5c_DrivingAvatarClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the DrivingMouse
        DrivingMouse.x = []
        DrivingMouse.y = []
        DrivingMouse.leftButton = []
        DrivingMouse.midButton = []
        DrivingMouse.rightButton = []
        DrivingMouse.time = []
        DrivingMouse.clicked_name = []
        gotValidClick = False  # until a click is received
        DrivingKeys = keyboard.Keyboard()
        AvatarDrive_x = Avatar_x
        AvatarDrive_y = Avatar_y
        
        # get target location 
        if target == "left":
            target_x = left_target
        elif target == "right":
            target_x = right_target
        target_y = 0
        
        # centre mouse by controls
        DrivingMouse.setPos(newPos =(0, Arrow_y[2]))
        
        # frame counter 
        frame = 0
        
        state = "null"
        
        # set colours for arrows 
        up_col    = Arrow_init_colour
        down_col  = Arrow_init_colour
        left_col  = Arrow_init_colour
        right_col = Arrow_init_colour
        
        # keep track of which components have finished
        routine_5c_DrivingAvatarComponents = [DrivingMouse, DrivingKeys, DrivingBoundary, AvatarPlaced, LeftBuild, RightBuild, AvatarDrive, upClick, downClick, leftClick, rightClick, upShape, downShape, rightShape, leftShape]
        for thisComponent in routine_5c_DrivingAvatarComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_5c_DrivingAvatar"-------
        while continueRoutine:
            # get current time
            t = routine_5c_DrivingAvatarClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *DrivingMouse* updates
            if frameN >= delay and DrivingMouse.status == NOT_STARTED:
                # keep track of start time/frame for later
                DrivingMouse.tStart = t  # not accounting for scr refresh
                DrivingMouse.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DrivingMouse, 'tStartRefresh')  # time at next scr refresh
                DrivingMouse.status = STARTED
                DrivingMouse.mouseClock.reset()
                prevButtonState = DrivingMouse.getPressed()  # if button is down already this ISN'T a new click
            if DrivingMouse.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                DrivingMouse.tStop = t  # not accounting for scr refresh
                DrivingMouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DrivingMouse, 'tStopRefresh')  # time at next scr refresh
                DrivingMouse.status = FINISHED
            if DrivingMouse.status == STARTED:  # only update if started and not finished!
                x, y = DrivingMouse.getPos()
                DrivingMouse.x.append(x)
                DrivingMouse.y.append(y)
                buttons = DrivingMouse.getPressed()
                DrivingMouse.leftButton.append(buttons[0])
                DrivingMouse.midButton.append(buttons[1])
                DrivingMouse.rightButton.append(buttons[2])
                DrivingMouse.time.append(DrivingMouse.mouseClock.getTime())
            
            # *DrivingKeys* updates
            if frameN >= delay and DrivingKeys.status == NOT_STARTED:
                # keep track of start time/frame for later
                DrivingKeys.tStart = t  # not accounting for scr refresh
                DrivingKeys.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DrivingKeys, 'tStartRefresh')  # time at next scr refresh
                DrivingKeys.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(DrivingKeys.clock.reset)  # t=0 on next screen flip
                DrivingKeys.clearEvents(eventType='keyboard')
            if DrivingKeys.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                DrivingKeys.tStop = t  # not accounting for scr refresh
                DrivingKeys.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DrivingKeys, 'tStopRefresh')  # time at next scr refresh
                DrivingKeys.status = FINISHED
            if DrivingKeys.status == STARTED:
                theseKeys = DrivingKeys.getKeys(keyList=['up', 'down', 'right', 'left'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    DrivingKeys.keys = theseKeys.name  # just the last key pressed
                    DrivingKeys.rt = theseKeys.rt
            
            # *DrivingBoundary* updates
            if frameN >= 0.0 and DrivingBoundary.status == NOT_STARTED:
                # keep track of start time/frame for later
                DrivingBoundary.tStart = t  # not accounting for scr refresh
                DrivingBoundary.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DrivingBoundary, 'tStartRefresh')  # time at next scr refresh
                DrivingBoundary.setAutoDraw(True)
            if DrivingBoundary.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                DrivingBoundary.tStop = t  # not accounting for scr refresh
                DrivingBoundary.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DrivingBoundary, 'tStopRefresh')  # time at next scr refresh
                DrivingBoundary.setAutoDraw(False)
            if DrivingBoundary.status == STARTED:  # only update if drawing
                DrivingBoundary.setPos((0, avatar_y_offset), log=False)
                DrivingBoundary.setSize((Screen_width, box_size + 10), log=False)
            # add to frame count and check whether to change colour
            frame += 1
            
            # keep mouse in place until trial starts
            if frame < delay:
                DrivingMouse.setPos(newPos =(0, Arrow_y[2]))
                
            # Don't draw the target early
            if frame >= delay:
                if target == "left":
                    left_colour = box_burning
                elif target == "right":
                    right_colour = box_burning
            
            # Probably don't need this now since keys aren't great
            key_pressed = DrivingKeys.keys
            
            # use the mouse to drive the avatar
            if DrivingMouse.isPressedIn(upClick):
                AvatarDrive_y += avatar_speed
                up_col = Arrow_clik_colour
            elif DrivingMouse.isPressedIn(downClick):
                AvatarDrive_y -= avatar_speed
                down_col = Arrow_clik_colour
            elif DrivingMouse.isPressedIn(rightClick):
                AvatarDrive_x += avatar_speed
                right_col = Arrow_clik_colour
            elif DrivingMouse.isPressedIn(leftClick):
                AvatarDrive_x -= avatar_speed
                left_col = Arrow_clik_colour
            else:
                # reset the colours if nothing is clicked
                up_col    = Arrow_init_colour
                down_col  = Arrow_init_colour
                left_col  = Arrow_init_colour
                right_col = Arrow_init_colour
            
            # Works by allowing people to set the direction of travel and the
            # avatar will drive in that direction until another key is pressed 
            # NB: needs to only store the last key press
            #if key_pressed == 'up': 
            #    AvatarDrive_y += avatar_speed
            #elif key_pressed == 'down':
            #    AvatarDrive_y -= avatar_speed
            #elif key_pressed == 'right':
            #    AvatarDrive_x += avatar_speed
            #elif key_pressed == 'left':
            #    AvatarDrive_x -= avatar_speed
            
            # check for success or failure
            # Was the target reached?
            x_dist = AvatarDrive_x - target_x
            y_dist = AvatarDrive_y - target_y
            dist = (x_dist)**2 + (y_dist)**2
            
            
            if dist <= avatar_reach**2:
                success = 1
                #routine_5c_DrivingAvatar.finished = True
                continueRoutine = False
            
            # has time run out?
            if frame >= Trial_time + delay:
                success = 0
                if target == "left":
                    left_colour = box_burnt
                elif target == "right":
                    right_colour = box_burnt
            
            # *AvatarPlaced* updates
            if frameN >= 0.0 and AvatarPlaced.status == NOT_STARTED:
                # keep track of start time/frame for later
                AvatarPlaced.tStart = t  # not accounting for scr refresh
                AvatarPlaced.frameNStart = frameN  # exact frame index
                win.timeOnFlip(AvatarPlaced, 'tStartRefresh')  # time at next scr refresh
                AvatarPlaced.setAutoDraw(True)
            if AvatarPlaced.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                AvatarPlaced.tStop = t  # not accounting for scr refresh
                AvatarPlaced.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AvatarPlaced, 'tStopRefresh')  # time at next scr refresh
                AvatarPlaced.setAutoDraw(False)
            if AvatarPlaced.status == STARTED:  # only update if drawing
                AvatarPlaced.setPos((Avatar_x, Avatar_y), log=False)
                AvatarPlaced.setSize((box_size, box_size), log=False)
                AvatarPlaced.setFillColor(box_placed, log=False)
                AvatarPlaced.setLineColor(box_placed, log=False)
            
            # *LeftBuild* updates
            if frameN >= 0.0 and LeftBuild.status == NOT_STARTED:
                # keep track of start time/frame for later
                LeftBuild.tStart = t  # not accounting for scr refresh
                LeftBuild.frameNStart = frameN  # exact frame index
                win.timeOnFlip(LeftBuild, 'tStartRefresh')  # time at next scr refresh
                LeftBuild.setAutoDraw(True)
            if LeftBuild.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                LeftBuild.tStop = t  # not accounting for scr refresh
                LeftBuild.frameNStop = frameN  # exact frame index
                win.timeOnFlip(LeftBuild, 'tStopRefresh')  # time at next scr refresh
                LeftBuild.setAutoDraw(False)
            if LeftBuild.status == STARTED:  # only update if drawing
                LeftBuild.setPos((left_target, 0), log=False)
                LeftBuild.setSize((box_size, box_size), log=False)
                LeftBuild.setFillColor(left_colour, log=False)
                LeftBuild.setLineColor(left_colour, log=False)
            
            # *RightBuild* updates
            if frameN >= 0.0 and RightBuild.status == NOT_STARTED:
                # keep track of start time/frame for later
                RightBuild.tStart = t  # not accounting for scr refresh
                RightBuild.frameNStart = frameN  # exact frame index
                win.timeOnFlip(RightBuild, 'tStartRefresh')  # time at next scr refresh
                RightBuild.setAutoDraw(True)
            if RightBuild.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                RightBuild.tStop = t  # not accounting for scr refresh
                RightBuild.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RightBuild, 'tStopRefresh')  # time at next scr refresh
                RightBuild.setAutoDraw(False)
            if RightBuild.status == STARTED:  # only update if drawing
                RightBuild.setPos((right_target, 0), log=False)
                RightBuild.setSize((box_size, box_size), log=False)
                RightBuild.setFillColor(right_colour, log=False)
                RightBuild.setLineColor(right_colour, log=False)
            
            # *AvatarDrive* updates
            if t >= 0.0 and AvatarDrive.status == NOT_STARTED:
                # keep track of start time/frame for later
                AvatarDrive.tStart = t  # not accounting for scr refresh
                AvatarDrive.frameNStart = frameN  # exact frame index
                win.timeOnFlip(AvatarDrive, 'tStartRefresh')  # time at next scr refresh
                AvatarDrive.setAutoDraw(True)
            if AvatarDrive.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                AvatarDrive.tStop = t  # not accounting for scr refresh
                AvatarDrive.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AvatarDrive, 'tStopRefresh')  # time at next scr refresh
                AvatarDrive.setAutoDraw(False)
            if AvatarDrive.status == STARTED:  # only update if drawing
                AvatarDrive.setPos((AvatarDrive_x, AvatarDrive_y), log=False)
                AvatarDrive.setSize((box_size, box_size), log=False)
                AvatarDrive.setFillColor(box_truck, log=False)
                AvatarDrive.setLineColor(box_truck, log=False)
            
            # *upClick* updates
            if frameN >= 0 and upClick.status == NOT_STARTED:
                # keep track of start time/frame for later
                upClick.tStart = t  # not accounting for scr refresh
                upClick.frameNStart = frameN  # exact frame index
                win.timeOnFlip(upClick, 'tStartRefresh')  # time at next scr refresh
                upClick.setAutoDraw(True)
            if upClick.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                upClick.tStop = t  # not accounting for scr refresh
                upClick.frameNStop = frameN  # exact frame index
                win.timeOnFlip(upClick, 'tStopRefresh')  # time at next scr refresh
                upClick.setAutoDraw(False)
            if upClick.status == STARTED:  # only update if drawing
                upClick.setPos((Arrow_x[0], Arrow_y[0]), log=False)
                upClick.setSize((Arrow_size, Arrow_size), log=False)
                upClick.setOri(Arrow_orient[0], log=False)
                upClick.setFillColor([1,1,1], log=False)
                upClick.setLineColor([-1,-1,-1], log=False)
            
            # *downClick* updates
            if t >= 0.0 and downClick.status == NOT_STARTED:
                # keep track of start time/frame for later
                downClick.tStart = t  # not accounting for scr refresh
                downClick.frameNStart = frameN  # exact frame index
                win.timeOnFlip(downClick, 'tStartRefresh')  # time at next scr refresh
                downClick.setAutoDraw(True)
            if downClick.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                downClick.tStop = t  # not accounting for scr refresh
                downClick.frameNStop = frameN  # exact frame index
                win.timeOnFlip(downClick, 'tStopRefresh')  # time at next scr refresh
                downClick.setAutoDraw(False)
            if downClick.status == STARTED:  # only update if drawing
                downClick.setPos((Arrow_x[1], Arrow_y[1]), log=False)
                downClick.setSize((Arrow_size, Arrow_size), log=False)
                downClick.setOri(Arrow_orient[1], log=False)
            
            # *leftClick* updates
            if t >= 0.0 and leftClick.status == NOT_STARTED:
                # keep track of start time/frame for later
                leftClick.tStart = t  # not accounting for scr refresh
                leftClick.frameNStart = frameN  # exact frame index
                win.timeOnFlip(leftClick, 'tStartRefresh')  # time at next scr refresh
                leftClick.setAutoDraw(True)
            if leftClick.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                leftClick.tStop = t  # not accounting for scr refresh
                leftClick.frameNStop = frameN  # exact frame index
                win.timeOnFlip(leftClick, 'tStopRefresh')  # time at next scr refresh
                leftClick.setAutoDraw(False)
            if leftClick.status == STARTED:  # only update if drawing
                leftClick.setPos((Arrow_x[2], Arrow_y[2]), log=False)
                leftClick.setSize((Arrow_size, Arrow_size), log=False)
                leftClick.setOri(Arrow_orient[2], log=False)
            
            # *rightClick* updates
            if t >= 0.0 and rightClick.status == NOT_STARTED:
                # keep track of start time/frame for later
                rightClick.tStart = t  # not accounting for scr refresh
                rightClick.frameNStart = frameN  # exact frame index
                win.timeOnFlip(rightClick, 'tStartRefresh')  # time at next scr refresh
                rightClick.setAutoDraw(True)
            if rightClick.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                rightClick.tStop = t  # not accounting for scr refresh
                rightClick.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rightClick, 'tStopRefresh')  # time at next scr refresh
                rightClick.setAutoDraw(False)
            if rightClick.status == STARTED:  # only update if drawing
                rightClick.setPos((Arrow_x[3], Arrow_y[3]), log=False)
                rightClick.setSize((Arrow_size, Arrow_size), log=False)
                rightClick.setOri(0, log=False)
            
            # *upShape* updates
            if t >= 0.0 and upShape.status == NOT_STARTED:
                # keep track of start time/frame for later
                upShape.tStart = t  # not accounting for scr refresh
                upShape.frameNStart = frameN  # exact frame index
                win.timeOnFlip(upShape, 'tStartRefresh')  # time at next scr refresh
                upShape.setAutoDraw(True)
            if upShape.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                upShape.tStop = t  # not accounting for scr refresh
                upShape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(upShape, 'tStopRefresh')  # time at next scr refresh
                upShape.setAutoDraw(False)
            if upShape.status == STARTED:  # only update if drawing
                upShape.setPos((Arrow_x[0], Arrow_y[0]), log=False)
                upShape.setSize((Arrow_size, Arrow_size), log=False)
                upShape.setOri(Arrow_orient[0], log=False)
                upShape.setFillColor(up_col, log=False)
                upShape.setLineColor([-1,-1,-1], log=False)
            
            # *downShape* updates
            if t >= 0.0 and downShape.status == NOT_STARTED:
                # keep track of start time/frame for later
                downShape.tStart = t  # not accounting for scr refresh
                downShape.frameNStart = frameN  # exact frame index
                win.timeOnFlip(downShape, 'tStartRefresh')  # time at next scr refresh
                downShape.setAutoDraw(True)
            if downShape.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                downShape.tStop = t  # not accounting for scr refresh
                downShape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(downShape, 'tStopRefresh')  # time at next scr refresh
                downShape.setAutoDraw(False)
            if downShape.status == STARTED:  # only update if drawing
                downShape.setPos((Arrow_x[1], Arrow_y[1]), log=False)
                downShape.setSize((Arrow_size, Arrow_size), log=False)
                downShape.setOri(Arrow_orient[1], log=False)
                downShape.setFillColor(down_col, log=False)
                downShape.setLineColor([-1,-1,-1], log=False)
            
            # *rightShape* updates
            if t >= 0.0 and rightShape.status == NOT_STARTED:
                # keep track of start time/frame for later
                rightShape.tStart = t  # not accounting for scr refresh
                rightShape.frameNStart = frameN  # exact frame index
                win.timeOnFlip(rightShape, 'tStartRefresh')  # time at next scr refresh
                rightShape.setAutoDraw(True)
            if rightShape.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                rightShape.tStop = t  # not accounting for scr refresh
                rightShape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rightShape, 'tStopRefresh')  # time at next scr refresh
                rightShape.setAutoDraw(False)
            if rightShape.status == STARTED:  # only update if drawing
                rightShape.setPos((Arrow_x[3], Arrow_y[3]), log=False)
                rightShape.setSize((Arrow_size, Arrow_size), log=False)
                rightShape.setOri(Arrow_orient[3], log=False)
                rightShape.setFillColor(right_col, log=False)
                rightShape.setLineColor([-1,-1,-1], log=False)
            
            # *leftShape* updates
            if t >= 0.0 and leftShape.status == NOT_STARTED:
                # keep track of start time/frame for later
                leftShape.tStart = t  # not accounting for scr refresh
                leftShape.frameNStart = frameN  # exact frame index
                win.timeOnFlip(leftShape, 'tStartRefresh')  # time at next scr refresh
                leftShape.setAutoDraw(True)
            if leftShape.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                leftShape.tStop = t  # not accounting for scr refresh
                leftShape.frameNStop = frameN  # exact frame index
                win.timeOnFlip(leftShape, 'tStopRefresh')  # time at next scr refresh
                leftShape.setAutoDraw(False)
            if leftShape.status == STARTED:  # only update if drawing
                leftShape.setPos((Arrow_x[2], Arrow_y[2]), log=False)
                leftShape.setSize((Arrow_size, Arrow_size), log=False)
                leftShape.setOri(Arrow_orient[2], log=False)
                leftShape.setFillColor(left_col, log=False)
                leftShape.setLineColor([-1,-1,-1], log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_5c_DrivingAvatarComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_5c_DrivingAvatar"-------
        for thisComponent in routine_5c_DrivingAvatarComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for DecisionTrialLoop (TrialHandler)
        DecisionTrialLoop.addData('DrivingMouse.x', DrivingMouse.x)
        DecisionTrialLoop.addData('DrivingMouse.y', DrivingMouse.y)
        DecisionTrialLoop.addData('DrivingMouse.leftButton', DrivingMouse.leftButton)
        DecisionTrialLoop.addData('DrivingMouse.midButton', DrivingMouse.midButton)
        DecisionTrialLoop.addData('DrivingMouse.rightButton', DrivingMouse.rightButton)
        DecisionTrialLoop.addData('DrivingMouse.time', DrivingMouse.time)
        DecisionTrialLoop.addData('DrivingMouse.clicked_name', DrivingMouse.clicked_name)
        DecisionTrialLoop.addData('DrivingMouse.started', DrivingMouse.tStart)
        DecisionTrialLoop.addData('DrivingMouse.stopped', DrivingMouse.tStop)
        # check responses
        if DrivingKeys.keys in ['', [], None]:  # No response was made
            DrivingKeys.keys = None
        DecisionTrialLoop.addData('DrivingKeys.keys',DrivingKeys.keys)
        if DrivingKeys.keys != None:  # we had a response
            DecisionTrialLoop.addData('DrivingKeys.rt', DrivingKeys.rt)
        DecisionTrialLoop.addData('DrivingKeys.started', DrivingKeys.tStartRefresh)
        DecisionTrialLoop.addData('DrivingKeys.stopped', DrivingKeys.tStopRefresh)
        DecisionTrialLoop.addData('DrivingBoundary.started', DrivingBoundary.tStartRefresh)
        DecisionTrialLoop.addData('DrivingBoundary.stopped', DrivingBoundary.tStopRefresh)
        # Establish success or failure 
        
        # This was a dumb thought... ignore that 
        #if (AvatarDrive_y)**2 + (AvatarDrive_x)**2 == (avatar_reach)**2:
        #    success = 1
        #    if target == "left":
        #        left_colour = box_build
        #    elif target == "right":
        #        right_colour = box_build
        
        
        # check if time ran out
        if success == 0:
            if target == "left":
                left_colour = box_burnt
            elif target == "right":
                right_colour = box_burnt
        if success == 1:
            if target == "left":
                left_colour = box_build
            elif target == "right":
                right_colour = box_build
        
        DecisionTrialLoop.addData('AvatarPlaced.started', AvatarPlaced.tStartRefresh)
        DecisionTrialLoop.addData('AvatarPlaced.stopped', AvatarPlaced.tStopRefresh)
        DecisionTrialLoop.addData('LeftBuild.started', LeftBuild.tStartRefresh)
        DecisionTrialLoop.addData('LeftBuild.stopped', LeftBuild.tStopRefresh)
        DecisionTrialLoop.addData('RightBuild.started', RightBuild.tStartRefresh)
        DecisionTrialLoop.addData('RightBuild.stopped', RightBuild.tStopRefresh)
        DecisionTrialLoop.addData('AvatarDrive.started', AvatarDrive.tStartRefresh)
        DecisionTrialLoop.addData('AvatarDrive.stopped', AvatarDrive.tStopRefresh)
        DecisionTrialLoop.addData('upClick.started', upClick.tStartRefresh)
        DecisionTrialLoop.addData('upClick.stopped', upClick.tStopRefresh)
        DecisionTrialLoop.addData('downClick.started', downClick.tStartRefresh)
        DecisionTrialLoop.addData('downClick.stopped', downClick.tStopRefresh)
        DecisionTrialLoop.addData('leftClick.started', leftClick.tStartRefresh)
        DecisionTrialLoop.addData('leftClick.stopped', leftClick.tStopRefresh)
        DecisionTrialLoop.addData('rightClick.started', rightClick.tStartRefresh)
        DecisionTrialLoop.addData('rightClick.stopped', rightClick.tStopRefresh)
        DecisionTrialLoop.addData('upShape.started', upShape.tStartRefresh)
        DecisionTrialLoop.addData('upShape.stopped', upShape.tStopRefresh)
        DecisionTrialLoop.addData('downShape.started', downShape.tStartRefresh)
        DecisionTrialLoop.addData('downShape.stopped', downShape.tStopRefresh)
        DecisionTrialLoop.addData('rightShape.started', rightShape.tStartRefresh)
        DecisionTrialLoop.addData('rightShape.stopped', rightShape.tStopRefresh)
        DecisionTrialLoop.addData('leftShape.started', leftShape.tStartRefresh)
        DecisionTrialLoop.addData('leftShape.stopped', leftShape.tStopRefresh)
        # the Routine "routine_5c_DrivingAvatar" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "routine_5d_TrialFeedback"-------
        t = 0
        routine_5d_TrialFeedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if success == 1:
            Feedback_text = "You made it! :)"
        elif success == 0: 
            Feedback_text = "The house burnt down :/"
        TrialMoveOn = keyboard.Keyboard()
        # keep track of which components have finished
        routine_5d_TrialFeedbackComponents = [DrivingBoundaryFeedback, AvatarPlacedFeedback, LeftFeedback, RightFeedback, AvatarFeedback, text, TrialMoveOn, text_2]
        for thisComponent in routine_5d_TrialFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_5d_TrialFeedback"-------
        while continueRoutine:
            # get current time
            t = routine_5d_TrialFeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *DrivingBoundaryFeedback* updates
            if t >= 0 and DrivingBoundaryFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                DrivingBoundaryFeedback.tStart = t  # not accounting for scr refresh
                DrivingBoundaryFeedback.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DrivingBoundaryFeedback, 'tStartRefresh')  # time at next scr refresh
                DrivingBoundaryFeedback.setAutoDraw(True)
            if DrivingBoundaryFeedback.status == STARTED:  # only update if drawing
                DrivingBoundaryFeedback.setPos((0, avatar_y_offset), log=False)
                DrivingBoundaryFeedback.setSize((Screen_width, box_size + 10), log=False)
            
            # *AvatarPlacedFeedback* updates
            if t >= 0 and AvatarPlacedFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                AvatarPlacedFeedback.tStart = t  # not accounting for scr refresh
                AvatarPlacedFeedback.frameNStart = frameN  # exact frame index
                win.timeOnFlip(AvatarPlacedFeedback, 'tStartRefresh')  # time at next scr refresh
                AvatarPlacedFeedback.setAutoDraw(True)
            if AvatarPlacedFeedback.status == STARTED:  # only update if drawing
                AvatarPlacedFeedback.setPos((Avatar_x, Avatar_y), log=False)
                AvatarPlacedFeedback.setSize((box_size, box_size), log=False)
                AvatarPlacedFeedback.setFillColor(box_placed, log=False)
                AvatarPlacedFeedback.setLineColor(box_placed, log=False)
            
            # *LeftFeedback* updates
            if t >= 0.0 and LeftFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                LeftFeedback.tStart = t  # not accounting for scr refresh
                LeftFeedback.frameNStart = frameN  # exact frame index
                win.timeOnFlip(LeftFeedback, 'tStartRefresh')  # time at next scr refresh
                LeftFeedback.setAutoDraw(True)
            if LeftFeedback.status == STARTED:  # only update if drawing
                LeftFeedback.setPos((left_target, 0), log=False)
                LeftFeedback.setSize((box_size, box_size), log=False)
                LeftFeedback.setFillColor(left_colour, log=False)
                LeftFeedback.setLineColor(left_colour, log=False)
            
            # *RightFeedback* updates
            if t >= 0.0 and RightFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                RightFeedback.tStart = t  # not accounting for scr refresh
                RightFeedback.frameNStart = frameN  # exact frame index
                win.timeOnFlip(RightFeedback, 'tStartRefresh')  # time at next scr refresh
                RightFeedback.setAutoDraw(True)
            if RightFeedback.status == STARTED:  # only update if drawing
                RightFeedback.setPos((right_target, 0), log=False)
                RightFeedback.setSize((box_size, box_size), log=False)
                RightFeedback.setFillColor(right_colour, log=False)
                RightFeedback.setLineColor(right_colour, log=False)
            
            # *AvatarFeedback* updates
            if t >= 0.0 and AvatarFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                AvatarFeedback.tStart = t  # not accounting for scr refresh
                AvatarFeedback.frameNStart = frameN  # exact frame index
                win.timeOnFlip(AvatarFeedback, 'tStartRefresh')  # time at next scr refresh
                AvatarFeedback.setAutoDraw(True)
            if AvatarFeedback.status == STARTED:  # only update if drawing
                AvatarFeedback.setPos((AvatarDrive_x, AvatarDrive_y), log=False)
                AvatarFeedback.setSize((box_size, box_size), log=False)
                AvatarFeedback.setFillColor(box_truck, log=False)
                AvatarFeedback.setLineColor(box_truck, log=False)
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t  # not accounting for scr refresh
                text.frameNStart = frameN  # exact frame index
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:  # only update if drawing
                text.setText(Feedback_text, log=False)
            
            # *TrialMoveOn* updates
            if t >= 0.0 and TrialMoveOn.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialMoveOn.tStart = t  # not accounting for scr refresh
                TrialMoveOn.frameNStart = frameN  # exact frame index
                win.timeOnFlip(TrialMoveOn, 'tStartRefresh')  # time at next scr refresh
                TrialMoveOn.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(TrialMoveOn.clock.reset)  # t=0 on next screen flip
                TrialMoveOn.clearEvents(eventType='keyboard')
            if TrialMoveOn.status == STARTED:
                theseKeys = TrialMoveOn.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    TrialMoveOn.keys = theseKeys.name  # just the last key pressed
                    TrialMoveOn.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_2* updates
            if t >= 0.0 and text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_2.tStart = t  # not accounting for scr refresh
                text_2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:  # only update if drawing
                text_2.setPos((0, -avatar_y_offset), log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_5d_TrialFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_5d_TrialFeedback"-------
        for thisComponent in routine_5d_TrialFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        DecisionTrialLoop.addData('DrivingBoundaryFeedback.started', DrivingBoundaryFeedback.tStartRefresh)
        DecisionTrialLoop.addData('DrivingBoundaryFeedback.stopped', DrivingBoundaryFeedback.tStopRefresh)
        DecisionTrialLoop.addData('AvatarPlacedFeedback.started', AvatarPlacedFeedback.tStartRefresh)
        DecisionTrialLoop.addData('AvatarPlacedFeedback.stopped', AvatarPlacedFeedback.tStopRefresh)
        DecisionTrialLoop.addData('LeftFeedback.started', LeftFeedback.tStartRefresh)
        DecisionTrialLoop.addData('LeftFeedback.stopped', LeftFeedback.tStopRefresh)
        DecisionTrialLoop.addData('RightFeedback.started', RightFeedback.tStartRefresh)
        DecisionTrialLoop.addData('RightFeedback.stopped', RightFeedback.tStopRefresh)
        DecisionTrialLoop.addData('AvatarFeedback.started', AvatarFeedback.tStartRefresh)
        DecisionTrialLoop.addData('AvatarFeedback.stopped', AvatarFeedback.tStopRefresh)
        DecisionTrialLoop.addData('text.started', text.tStartRefresh)
        DecisionTrialLoop.addData('text.stopped', text.tStopRefresh)
        # check responses
        if TrialMoveOn.keys in ['', [], None]:  # No response was made
            TrialMoveOn.keys = None
        DecisionTrialLoop.addData('TrialMoveOn.keys',TrialMoveOn.keys)
        if TrialMoveOn.keys != None:  # we had a response
            DecisionTrialLoop.addData('TrialMoveOn.rt', TrialMoveOn.rt)
        DecisionTrialLoop.addData('TrialMoveOn.started', TrialMoveOn.tStartRefresh)
        DecisionTrialLoop.addData('TrialMoveOn.stopped', TrialMoveOn.tStopRefresh)
        DecisionTrialLoop.addData('text_2.started', text_2.tStartRefresh)
        DecisionTrialLoop.addData('text_2.stopped', text_2.tStopRefresh)
        # the Routine "routine_5d_TrialFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed num_trials repeats of 'DecisionTrialLoop'
    
    
    # ------Prepare to start Routine "routine_6_ConfidenceExplanation"-------
    t = 0
    routine_6_ConfidenceExplanationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    trial_num_conf = 0
    
    conf_reps = 2
    conf_delta = []
    for d in deltas:
        for reps in range(0, conf_reps):
            conf_delta.append(d)
    shuffle(conf_delta)
    # keep track of which components have finished
    routine_6_ConfidenceExplanationComponents = []
    for thisComponent in routine_6_ConfidenceExplanationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine_6_ConfidenceExplanation"-------
    while continueRoutine:
        # get current time
        t = routine_6_ConfidenceExplanationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_6_ConfidenceExplanationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_6_ConfidenceExplanation"-------
    for thisComponent in routine_6_ConfidenceExplanationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "routine_6_ConfidenceExplanation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ConfidenceLoop = data.TrialHandler(nReps=num_conf_trials, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ConfidenceLoop')
    thisExp.addLoop(ConfidenceLoop)  # add the loop to the experiment
    thisConfidenceLoop = ConfidenceLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisConfidenceLoop.rgb)
    if thisConfidenceLoop != None:
        for paramName in thisConfidenceLoop:
            exec('{} = thisConfidenceLoop[paramName]'.format(paramName))
    
    for thisConfidenceLoop in ConfidenceLoop:
        currentLoop = ConfidenceLoop
        # abbreviate parameter names if possible (e.g. rgb = thisConfidenceLoop.rgb)
        if thisConfidenceLoop != None:
            for paramName in thisConfidenceLoop:
                exec('{} = thisConfidenceLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "routine_6a_Confidence"-------
        t = 0
        routine_6a_ConfidenceClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        rating.reset()
        d = conf_delta[trial_num_conf] - avatar_y_offset
        if random() < .5:
            d = d * -1
        
        # keep track of which components have finished
        routine_6a_ConfidenceComponents = [rating, ConfBoundary, ConfAvatar, ConfTarget]
        for thisComponent in routine_6a_ConfidenceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_6a_Confidence"-------
        while continueRoutine:
            # get current time
            t = routine_6a_ConfidenceClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *rating* updates
            if t >= 0.0 and rating.status == NOT_STARTED:
                # keep track of start time/frame for later
                rating.tStart = t  # not accounting for scr refresh
                rating.frameNStart = frameN  # exact frame index
                win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
                rating.setAutoDraw(True)
            continueRoutine &= rating.noResponse  # a response ends the trial
            
            # *ConfBoundary* updates
            if t >= 0.0 and ConfBoundary.status == NOT_STARTED:
                # keep track of start time/frame for later
                ConfBoundary.tStart = t  # not accounting for scr refresh
                ConfBoundary.frameNStart = frameN  # exact frame index
                win.timeOnFlip(ConfBoundary, 'tStartRefresh')  # time at next scr refresh
                ConfBoundary.setAutoDraw(True)
            if ConfBoundary.status == STARTED:  # only update if drawing
                ConfBoundary.setPos((0, avatar_y_offset), log=False)
                ConfBoundary.setSize((Screen_width + 10, box_size + 10), log=False)
            
            # *ConfAvatar* updates
            if t >= 0.0 and ConfAvatar.status == NOT_STARTED:
                # keep track of start time/frame for later
                ConfAvatar.tStart = t  # not accounting for scr refresh
                ConfAvatar.frameNStart = frameN  # exact frame index
                win.timeOnFlip(ConfAvatar, 'tStartRefresh')  # time at next scr refresh
                ConfAvatar.setAutoDraw(True)
            if ConfAvatar.status == STARTED:  # only update if drawing
                ConfAvatar.setPos((0, avatar_y_offset), log=False)
                ConfAvatar.setSize((box_size, box_size), log=False)
                ConfAvatar.setFillColor(box_truck, log=False)
                ConfAvatar.setLineColor(box_truck, log=False)
            
            # *ConfTarget* updates
            if t >= 0.0 and ConfTarget.status == NOT_STARTED:
                # keep track of start time/frame for later
                ConfTarget.tStart = t  # not accounting for scr refresh
                ConfTarget.frameNStart = frameN  # exact frame index
                win.timeOnFlip(ConfTarget, 'tStartRefresh')  # time at next scr refresh
                ConfTarget.setAutoDraw(True)
            if ConfTarget.status == STARTED:  # only update if drawing
                ConfTarget.setPos((d, 0), log=False)
                ConfTarget.setSize((box_size, box_size), log=False)
                ConfTarget.setFillColor(box_build, log=False)
                ConfTarget.setLineColor(box_build, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_6a_ConfidenceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_6a_Confidence"-------
        for thisComponent in routine_6a_ConfidenceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for ConfidenceLoop (TrialHandler)
        ConfidenceLoop.addData('rating.response', rating.getRating())
        ConfidenceLoop.addData('rating.rt', rating.getRT())
        ConfidenceLoop.addData('rating.started', rating.tStart)
        ConfidenceLoop.addData('rating.stopped', rating.tStop)
        trial_num_conf += 1
        ConfidenceLoop.addData('ConfBoundary.started', ConfBoundary.tStartRefresh)
        ConfidenceLoop.addData('ConfBoundary.stopped', ConfBoundary.tStopRefresh)
        ConfidenceLoop.addData('ConfAvatar.started', ConfAvatar.tStartRefresh)
        ConfidenceLoop.addData('ConfAvatar.stopped', ConfAvatar.tStopRefresh)
        ConfidenceLoop.addData('ConfTarget.started', ConfTarget.tStartRefresh)
        ConfidenceLoop.addData('ConfTarget.stopped', ConfTarget.tStopRefresh)
        # the Routine "routine_6a_Confidence" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed num_conf_trials repeats of 'ConfidenceLoop'
    
# completed num_blocks repeats of 'BlockLoop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
