#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on April 14, 2020, at 10:39
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
deltas = [200, 300, 400, 500]
num_trials = 4

# Screen settings 
Screen_height = 600
Screen_width = 1200

# Trial conditions 
Trial_time = 120 # this is specified in frames for now

# avatar setup 
avatar_speed = 3
avatar_y_offset = 100
box_size = 50
box_truck   = [1,-1,-1]
box_placed  = [.5,-.5,-.5]
box_build   = [.09, -.45,-.85]
box_burning = [.64, -.17, -.76]
box_burnt   = [-.9, -.9, -.9]

# Control Arrows
Arrow_init_colour = [1,1,1]
Arrow_clik_colour = [0,0,1]
Arrow_size = 30
Arrow_orient = [0,180,270,90]
Arrow_y = [-150,-220,-185,-185]
Arrow_x = [0, 0, -35, 35]






# Initialize components for Routine "routine_2_WelcomeScreen"
routine_2_WelcomeScreenClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Welcome to the experiment\n\nPress Space to continue',
    font='Arial',
    pos=(0, 0), height=25, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_3_Demonstration"
routine_3_DemonstrationClock = core.Clock()
DemoText = visual.TextStim(win=win, name='DemoText',
    text='Temp text\n',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
    ori=0, pos=(0, 100),
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
text = visual.TextStim(win=win, name='text',
    text='Ready?',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Drive!',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
DrivingBoundary = visual.Rect(
    win=win, name='DrivingBoundary',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 100),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
AvatarPlaced = visual.Rect(
    win=win, name='AvatarPlaced',
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
LeftBuild = visual.Rect(
    win=win, name='LeftBuild',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
RightBuild = visual.Rect(
    win=win, name='RightBuild',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
TestCheck = visual.TextStim(win=win, name='TestCheck',
    text='default text',
    font='Arial',
    pos=(0, -50), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
upClick = visual.Rect(
    win=win, name='upClick',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
downClick = visual.Rect(
    win=win, name='downClick',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
leftClick = visual.Rect(
    win=win, name='leftClick',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
rightClick = visual.Rect(
    win=win, name='rightClick',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
upShape = visual.ShapeStim(
    win=win, name='upShape',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
downShape = visual.ShapeStim(
    win=win, name='downShape',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
rightShape = visual.ShapeStim(
    win=win, name='rightShape',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
leftShape = visual.ShapeStim(
    win=win, name='leftShape',
    vertices=[[-[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0,-[1.0, 1.0][1]/2.0], [0,[1.0, 1.0][1]/2.0]],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-18.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "routine_1_InitExperiment"-------
t = 0
routine_1_InitExperimentClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
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
BlockLoop = data.TrialHandler(nReps=1, method='random', 
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
    
    # set up handler to look after randomisation of conditions etc
    DemoLoop = data.TrialHandler(nReps=1, method='random', 
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
        
        # ------Prepare to start Routine "routine_3_Demonstration"-------
        t = 0
        routine_3_DemonstrationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        routine_3_DemonstrationComponents = [DemoText]
        for thisComponent in routine_3_DemonstrationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "routine_3_Demonstration"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = routine_3_DemonstrationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *DemoText* updates
            if t >= 0.0 and DemoText.status == NOT_STARTED:
                # keep track of start time/frame for later
                DemoText.tStart = t  # not accounting for scr refresh
                DemoText.frameNStart = frameN  # exact frame index
                win.timeOnFlip(DemoText, 'tStartRefresh')  # time at next scr refresh
                DemoText.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if DemoText.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                DemoText.tStop = t  # not accounting for scr refresh
                DemoText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DemoText, 'tStopRefresh')  # time at next scr refresh
                DemoText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in routine_3_DemonstrationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "routine_3_Demonstration"-------
        for thisComponent in routine_3_DemonstrationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        DemoLoop.addData('DemoText.started', DemoText.tStartRefresh)
        DemoLoop.addData('DemoText.stopped', DemoText.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'DemoLoop'
    
    
    # ------Prepare to start Routine "routine_4_Trial_Instructions"-------
    t = 0
    routine_4_Trial_InstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    InstSkip = keyboard.Keyboard()
    trial_num = 0
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
    DecisionTrialLoop = data.TrialHandler(nReps=num_trials, method='random', 
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
        delta_thisT = deltas[trial_num] - avatar_y_offset
        
        # set target position
        left_target = -delta_thisT
        right_target = delta_thisT
        
        # set the delay on each trial so pariticpants can't predict 
        # when to respond
        delay = round((random() * 100)) + 20
        
        # Tried to append another trial given some condition
        # Might not be able to do that too easily... 
        if delta_thisT == 200:
            deltas.append(200)
            num_trials += 1
        
        
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
        
        # put mouse to arrow part 
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
        routine_5c_DrivingAvatarComponents = [DrivingMouse, DrivingKeys, text, text_2, DrivingBoundary, AvatarPlaced, AvatarDrive, LeftBuild, RightBuild, TestCheck, upClick, downClick, leftClick, rightClick, upShape, downShape, rightShape, leftShape]
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
            
            # *text* updates
            if frameN >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t  # not accounting for scr refresh
                text.frameNStart = frameN  # exact frame index
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED and frameN >= delay:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
            
            # *text_2* updates
            if frameN >= delay and text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_2.tStart = t  # not accounting for scr refresh
                text_2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            if text_2.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
            
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
            # status just checks if we're listening to the keyboard
            state = 1
            
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
            
            # This works if we want to make participants tap their keyboard
            # NB: must be paired with storing all keys
            #if len(key_pressed) > 0:
            #    if key_pressed[-1] == 'up': 
            #        AvatarDrive_y += avatar_speed
            #        key_pressed.pop()
            #    elif key_pressed[-1] == 'down':
            #        AvatarDrive_y -= avatar_speed
            #        DrivingKeys.keys.pop()
            #    elif key_pressed[-1] == 'right':
            #        AvatarDrive_x += avatar_speed
            #        DrivingKeys.keys.pop()
            #    elif key_pressed[-1] == 'left':
            #        AvatarDrive_x -= avatar_speed
            #        DrivingKeys.keys.pop()
            
            
            
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
            
            # *TestCheck* updates
            if frameN >= 0.0 and TestCheck.status == NOT_STARTED:
                # keep track of start time/frame for later
                TestCheck.tStart = t  # not accounting for scr refresh
                TestCheck.frameNStart = frameN  # exact frame index
                win.timeOnFlip(TestCheck, 'tStartRefresh')  # time at next scr refresh
                TestCheck.setAutoDraw(True)
            if TestCheck.status == STARTED and frameN >= Trial_time + delay:
                # keep track of stop time/frame for later
                TestCheck.tStop = t  # not accounting for scr refresh
                TestCheck.frameNStop = frameN  # exact frame index
                win.timeOnFlip(TestCheck, 'tStopRefresh')  # time at next scr refresh
                TestCheck.setAutoDraw(False)
            if TestCheck.status == STARTED:  # only update if drawing
                TestCheck.setText(state
, log=False)
            
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
        DecisionTrialLoop.addData('text.started', text.tStartRefresh)
        DecisionTrialLoop.addData('text.stopped', text.tStopRefresh)
        DecisionTrialLoop.addData('text_2.started', text_2.tStartRefresh)
        DecisionTrialLoop.addData('text_2.stopped', text_2.tStopRefresh)
        DecisionTrialLoop.addData('DrivingBoundary.started', DrivingBoundary.tStartRefresh)
        DecisionTrialLoop.addData('DrivingBoundary.stopped', DrivingBoundary.tStopRefresh)
        d = dir(DrivingKeys)
        
        #print(d)
        #print(DrivingKeys.stop)
        
        #for i in d:
        #    print(i + " " + d[i])
        
        #print(DrivingKeys['status'])
        DecisionTrialLoop.addData('AvatarPlaced.started', AvatarPlaced.tStartRefresh)
        DecisionTrialLoop.addData('AvatarPlaced.stopped', AvatarPlaced.tStopRefresh)
        DecisionTrialLoop.addData('AvatarDrive.started', AvatarDrive.tStartRefresh)
        DecisionTrialLoop.addData('AvatarDrive.stopped', AvatarDrive.tStopRefresh)
        DecisionTrialLoop.addData('LeftBuild.started', LeftBuild.tStartRefresh)
        DecisionTrialLoop.addData('LeftBuild.stopped', LeftBuild.tStopRefresh)
        DecisionTrialLoop.addData('RightBuild.started', RightBuild.tStartRefresh)
        DecisionTrialLoop.addData('RightBuild.stopped', RightBuild.tStopRefresh)
        DecisionTrialLoop.addData('TestCheck.started', TestCheck.tStartRefresh)
        DecisionTrialLoop.addData('TestCheck.stopped', TestCheck.tStopRefresh)
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
        thisExp.nextEntry()
        
    # completed num_trials repeats of 'DecisionTrialLoop'
    
# completed 1 repeats of 'BlockLoop'


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
