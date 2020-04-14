/******************* 
 * Simpleidea Test *
 *******************/

import { PsychoJS } from 'https://pavlovia.org/lib/core.js';
import * as core from 'https://pavlovia.org/lib/core.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data.js';
import { Scheduler } from 'https://pavlovia.org/lib/util.js';
import * as util from 'https://pavlovia.org/lib/util.js';
import * as visual from 'https://pavlovia.org/lib/visual.js';
import { Sound } from 'https://pavlovia.org/lib/sound.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0, 0, 0]),
  units: 'pix'
});

// store info about the experiment session:
let expName = 'simpleIdea';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(routine_1_InitExperimentRoutineBegin);
flowScheduler.add(routine_1_InitExperimentRoutineEachFrame);
flowScheduler.add(routine_1_InitExperimentRoutineEnd);
flowScheduler.add(routine_2_WelcomeScreenRoutineBegin);
flowScheduler.add(routine_2_WelcomeScreenRoutineEachFrame);
flowScheduler.add(routine_2_WelcomeScreenRoutineEnd);
const BlockLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(BlockLoopLoopBegin, BlockLoopLoopScheduler);
flowScheduler.add(BlockLoopLoopScheduler);
flowScheduler.add(BlockLoopLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.1.2';

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var routine_1_InitExperimentClock;
var routine_2_WelcomeScreenClock;
var WelcomeText;
var routine_3_DemonstrationClock;
var DemoText;
var routine_4_Trial_InstructionsClock;
var TrialInst;
var routine_5a_PlaceAvatarInitClock;
var routine_5b_PlacingAvatarClock;
var PlacementArea;
var AvatarMouse;
var leftTarget;
var rightTarget;
var AvatarPlace;
var routine_5c_DrivingAvatarClock;
var DrivingMouse;
var DrivingBoundary;
var AvatarPlaced;
var LeftBuild;
var RightBuild;
var AvatarDrive;
var upClick;
var downClick;
var leftClick;
var rightClick;
var upShape;
var downShape;
var rightShape;
var leftShape;
var routine_5d_TrialFeedbackClock;
var DrivingBoundaryFeedback;
var AvatarPlacedFeedback;
var LeftFeedback;
var RightFeedback;
var AvatarFeedback;
var text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "routine_1_InitExperiment"
  routine_1_InitExperimentClock = new util.Clock();
  // Initialize components for Routine "routine_2_WelcomeScreen"
  routine_2_WelcomeScreenClock = new util.Clock();
  WelcomeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'WelcomeText',
    text: 'Welcome to the experiment\n\nPress Space to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 25,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "routine_3_Demonstration"
  routine_3_DemonstrationClock = new util.Clock();
  DemoText = new visual.TextStim({
    win: psychoJS.window,
    name: 'DemoText',
    text: 'Temp text\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 20,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "routine_4_Trial_Instructions"
  routine_4_Trial_InstructionsClock = new util.Clock();
  TrialInst = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialInst',
    text: "You will place the 'truck' by clicing between the two lines on screen.\nOnce you are happy with the placement, press the spacebar to begin the trial.\nAfter a short amount of time, one of the two buidlings will catch fire,\nat which point you are to drive the truck towards this buidling.\n\nPress the spacebar to continue",
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 20,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "routine_5a_PlaceAvatarInit"
  routine_5a_PlaceAvatarInitClock = new util.Clock();
  // Initialize components for Routine "routine_5b_PlacingAvatar"
  routine_5b_PlacingAvatarClock = new util.Clock();
  PlacementArea = new visual.Rect ({
    win: psychoJS.window, name: 'PlacementArea',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 100],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([0, 0, 0]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  AvatarMouse = new core.Mouse({
    win: psychoJS.window,
  });
  AvatarMouse.mouseClock = new util.Clock();
  leftTarget = new visual.Rect ({
    win: psychoJS.window, name: 'leftTarget',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  rightTarget = new visual.Rect ({
    win: psychoJS.window, name: 'rightTarget',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  AvatarPlace = new visual.Rect ({
    win: psychoJS.window, name: 'AvatarPlace',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "routine_5c_DrivingAvatar"
  routine_5c_DrivingAvatarClock = new util.Clock();
  DrivingMouse = new core.Mouse({
    win: psychoJS.window,
  });
  DrivingMouse.mouseClock = new util.Clock();
  DrivingBoundary = new visual.Rect ({
    win: psychoJS.window, name: 'DrivingBoundary',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 100],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([0, 0, 0]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  AvatarPlaced = new visual.Rect ({
    win: psychoJS.window, name: 'AvatarPlaced',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  LeftBuild = new visual.Rect ({
    win: psychoJS.window, name: 'LeftBuild',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  RightBuild = new visual.Rect ({
    win: psychoJS.window, name: 'RightBuild',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  AvatarDrive = new visual.Rect ({
    win: psychoJS.window, name: 'AvatarDrive',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  upClick = new visual.Rect ({
    win: psychoJS.window, name: 'upClick',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  downClick = new visual.Rect ({
    win: psychoJS.window, name: 'downClick',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  leftClick = new visual.Rect ({
    win: psychoJS.window, name: 'leftClick',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -10, interpolate: true,
  });
  
  rightClick = new visual.Rect ({
    win: psychoJS.window, name: 'rightClick',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -11, interpolate: true,
  });
  
  upShape = new visual.ShapeStim ({
    win: psychoJS.window, name: 'upShape',
    units: 'height',
    vertices: [[-[1.0, 1.0][0]/2.0, -[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0, -[1.0, 1.0][1]/2.0], [0, [1.0, 1.0][1]/2.0]],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -12, interpolate: true,
  });
  
  downShape = new visual.ShapeStim ({
    win: psychoJS.window, name: 'downShape',
    units: 'height',
    vertices: [[-[1.0, 1.0][0]/2.0, -[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0, -[1.0, 1.0][1]/2.0], [0, [1.0, 1.0][1]/2.0]],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -13, interpolate: true,
  });
  
  rightShape = new visual.ShapeStim ({
    win: psychoJS.window, name: 'rightShape',
    units: 'height',
    vertices: [[-[1.0, 1.0][0]/2.0, -[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0, -[1.0, 1.0][1]/2.0], [0, [1.0, 1.0][1]/2.0]],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -14, interpolate: true,
  });
  
  leftShape = new visual.ShapeStim ({
    win: psychoJS.window, name: 'leftShape',
    units: 'height',
    vertices: [[-[1.0, 1.0][0]/2.0, -[1.0, 1.0][1]/2.0], [+[1.0, 1.0][0]/2.0, -[1.0, 1.0][1]/2.0], [0, [1.0, 1.0][1]/2.0]],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -15, interpolate: true,
  });
  
  // Initialize components for Routine "routine_5d_TrialFeedback"
  routine_5d_TrialFeedbackClock = new util.Clock();
  DrivingBoundaryFeedback = new visual.Rect ({
    win: psychoJS.window, name: 'DrivingBoundaryFeedback',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([0, 0, 0]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  AvatarPlacedFeedback = new visual.Rect ({
    win: psychoJS.window, name: 'AvatarPlacedFeedback',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  LeftFeedback = new visual.Rect ({
    win: psychoJS.window, name: 'LeftFeedback',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  RightFeedback = new visual.Rect ({
    win: psychoJS.window, name: 'RightFeedback',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  AvatarFeedback = new visual.Rect ({
    win: psychoJS.window, name: 'AvatarFeedback',
    units: 'height',
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(1.0),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 150], height: 20,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var routine_1_InitExperimentComponents;
function routine_1_InitExperimentRoutineBegin() {
  //------Prepare to start Routine 'routine_1_InitExperiment'-------
  t = 0;
  routine_1_InitExperimentClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  routine_1_InitExperimentComponents = [];
  
  for (const thisComponent of routine_1_InitExperimentComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function routine_1_InitExperimentRoutineEachFrame() {
  //------Loop for each frame of Routine 'routine_1_InitExperiment'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = routine_1_InitExperimentClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of routine_1_InitExperimentComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function routine_1_InitExperimentRoutineEnd() {
  //------Ending Routine 'routine_1_InitExperiment'-------
  for (const thisComponent of routine_1_InitExperimentComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "routine_1_InitExperiment" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var WelcomeEscape;
var routine_2_WelcomeScreenComponents;
function routine_2_WelcomeScreenRoutineBegin() {
  //------Prepare to start Routine 'routine_2_WelcomeScreen'-------
  t = 0;
  routine_2_WelcomeScreenClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  WelcomeEscape = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  routine_2_WelcomeScreenComponents = [];
  routine_2_WelcomeScreenComponents.push(WelcomeText);
  routine_2_WelcomeScreenComponents.push(WelcomeEscape);
  
  for (const thisComponent of routine_2_WelcomeScreenComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function routine_2_WelcomeScreenRoutineEachFrame() {
  //------Loop for each frame of Routine 'routine_2_WelcomeScreen'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = routine_2_WelcomeScreenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *WelcomeText* updates
  if (frameN >= 0.0 && WelcomeText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    WelcomeText.tStart = t;  // (not accounting for frame time here)
    WelcomeText.frameNStart = frameN;  // exact frame index
    WelcomeText.setAutoDraw(true);
  }

  
  // *WelcomeEscape* updates
  if (t >= 0.0 && WelcomeEscape.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    WelcomeEscape.tStart = t;  // (not accounting for frame time here)
    WelcomeEscape.frameNStart = frameN;  // exact frame index
    WelcomeEscape.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { WelcomeEscape.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (WelcomeEscape.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      WelcomeEscape.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      WelcomeEscape.rt = WelcomeEscape.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of routine_2_WelcomeScreenComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function routine_2_WelcomeScreenRoutineEnd() {
  //------Ending Routine 'routine_2_WelcomeScreen'-------
  for (const thisComponent of routine_2_WelcomeScreenComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (WelcomeEscape.keys === undefined || WelcomeEscape.keys.length === 0) {    // No response was made
      WelcomeEscape.keys = undefined;
  }
  
  psychoJS.experiment.addData('WelcomeEscape.keys', WelcomeEscape.keys);
  if (typeof WelcomeEscape.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('WelcomeEscape.rt', WelcomeEscape.rt);
      routineTimer.reset();
      }
  
  // the Routine "routine_2_WelcomeScreen" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var BlockLoop;
var currentLoop;
function BlockLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  BlockLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'BlockLoop'});
  psychoJS.experiment.addLoop(BlockLoop); // add the loop to the experiment
  currentLoop = BlockLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBlockLoop of BlockLoop) {
    thisScheduler.add(importConditions(BlockLoop));
    const DemoLoopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(DemoLoopLoopBegin, DemoLoopLoopScheduler);
    thisScheduler.add(DemoLoopLoopScheduler);
    thisScheduler.add(DemoLoopLoopEnd);
    thisScheduler.add(routine_4_Trial_InstructionsRoutineBegin);
    thisScheduler.add(routine_4_Trial_InstructionsRoutineEachFrame);
    thisScheduler.add(routine_4_Trial_InstructionsRoutineEnd);
    const DecisionTrialLoopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(DecisionTrialLoopLoopBegin, DecisionTrialLoopLoopScheduler);
    thisScheduler.add(DecisionTrialLoopLoopScheduler);
    thisScheduler.add(DecisionTrialLoopLoopEnd);
  }

  return Scheduler.Event.NEXT;
}

var DemoLoop;
function DemoLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  DemoLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'DemoLoop'});
  psychoJS.experiment.addLoop(DemoLoop); // add the loop to the experiment
  currentLoop = DemoLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisDemoLoop of DemoLoop) {
    thisScheduler.add(importConditions(DemoLoop));
    thisScheduler.add(routine_3_DemonstrationRoutineBegin);
    thisScheduler.add(routine_3_DemonstrationRoutineEachFrame);
    thisScheduler.add(routine_3_DemonstrationRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisDemoLoop));
  }

  return Scheduler.Event.NEXT;
}


function DemoLoopLoopEnd() {
  psychoJS.experiment.removeLoop(DemoLoop);

  return Scheduler.Event.NEXT;
}

var DecisionTrialLoop;
function DecisionTrialLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  DecisionTrialLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: num_trials, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'DecisionTrialLoop'});
  psychoJS.experiment.addLoop(DecisionTrialLoop); // add the loop to the experiment
  currentLoop = DecisionTrialLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisDecisionTrialLoop of DecisionTrialLoop) {
    thisScheduler.add(importConditions(DecisionTrialLoop));
    thisScheduler.add(routine_5a_PlaceAvatarInitRoutineBegin);
    thisScheduler.add(routine_5a_PlaceAvatarInitRoutineEachFrame);
    thisScheduler.add(routine_5a_PlaceAvatarInitRoutineEnd);
    thisScheduler.add(routine_5b_PlacingAvatarRoutineBegin);
    thisScheduler.add(routine_5b_PlacingAvatarRoutineEachFrame);
    thisScheduler.add(routine_5b_PlacingAvatarRoutineEnd);
    thisScheduler.add(routine_5c_DrivingAvatarRoutineBegin);
    thisScheduler.add(routine_5c_DrivingAvatarRoutineEachFrame);
    thisScheduler.add(routine_5c_DrivingAvatarRoutineEnd);
    thisScheduler.add(routine_5d_TrialFeedbackRoutineBegin);
    thisScheduler.add(routine_5d_TrialFeedbackRoutineEachFrame);
    thisScheduler.add(routine_5d_TrialFeedbackRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisDecisionTrialLoop));
  }

  return Scheduler.Event.NEXT;
}


function DecisionTrialLoopLoopEnd() {
  psychoJS.experiment.removeLoop(DecisionTrialLoop);

  return Scheduler.Event.NEXT;
}


function BlockLoopLoopEnd() {
  psychoJS.experiment.removeLoop(BlockLoop);

  return Scheduler.Event.NEXT;
}

var routine_3_DemonstrationComponents;
function routine_3_DemonstrationRoutineBegin() {
  //------Prepare to start Routine 'routine_3_Demonstration'-------
  t = 0;
  routine_3_DemonstrationClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  routine_3_DemonstrationComponents = [];
  routine_3_DemonstrationComponents.push(DemoText);
  
  for (const thisComponent of routine_3_DemonstrationComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function routine_3_DemonstrationRoutineEachFrame() {
  //------Loop for each frame of Routine 'routine_3_Demonstration'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = routine_3_DemonstrationClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *DemoText* updates
  if (t >= 0.0 && DemoText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    DemoText.tStart = t;  // (not accounting for frame time here)
    DemoText.frameNStart = frameN;  // exact frame index
    DemoText.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (DemoText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    DemoText.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of routine_3_DemonstrationComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function routine_3_DemonstrationRoutineEnd() {
  //------Ending Routine 'routine_3_Demonstration'-------
  for (const thisComponent of routine_3_DemonstrationComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var InstSkip;
var routine_4_Trial_InstructionsComponents;
function routine_4_Trial_InstructionsRoutineBegin() {
  //------Prepare to start Routine 'routine_4_Trial_Instructions'-------
  t = 0;
  routine_4_Trial_InstructionsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  InstSkip = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  routine_4_Trial_InstructionsComponents = [];
  routine_4_Trial_InstructionsComponents.push(TrialInst);
  routine_4_Trial_InstructionsComponents.push(InstSkip);
  
  for (const thisComponent of routine_4_Trial_InstructionsComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function routine_4_Trial_InstructionsRoutineEachFrame() {
  //------Loop for each frame of Routine 'routine_4_Trial_Instructions'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = routine_4_Trial_InstructionsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *TrialInst* updates
  if (t >= 0.0 && TrialInst.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    TrialInst.tStart = t;  // (not accounting for frame time here)
    TrialInst.frameNStart = frameN;  // exact frame index
    TrialInst.setAutoDraw(true);
  }

  
  // *InstSkip* updates
  if (t >= 1 && InstSkip.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    InstSkip.tStart = t;  // (not accounting for frame time here)
    InstSkip.frameNStart = frameN;  // exact frame index
    InstSkip.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { InstSkip.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (InstSkip.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      InstSkip.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      InstSkip.rt = InstSkip.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of routine_4_Trial_InstructionsComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function routine_4_Trial_InstructionsRoutineEnd() {
  //------Ending Routine 'routine_4_Trial_Instructions'-------
  for (const thisComponent of routine_4_Trial_InstructionsComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (InstSkip.keys === undefined || InstSkip.keys.length === 0) {    // No response was made
      InstSkip.keys = undefined;
  }
  
  psychoJS.experiment.addData('InstSkip.keys', InstSkip.keys);
  if (typeof InstSkip.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('InstSkip.rt', InstSkip.rt);
      routineTimer.reset();
      }
  
  // the Routine "routine_4_Trial_Instructions" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var routine_5a_PlaceAvatarInitComponents;
function routine_5a_PlaceAvatarInitRoutineBegin() {
  //------Prepare to start Routine 'routine_5a_PlaceAvatarInit'-------
  t = 0;
  routine_5a_PlaceAvatarInitClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  routine_5a_PlaceAvatarInitComponents = [];
  
  for (const thisComponent of routine_5a_PlaceAvatarInitComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function routine_5a_PlaceAvatarInitRoutineEachFrame() {
  //------Loop for each frame of Routine 'routine_5a_PlaceAvatarInit'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = routine_5a_PlaceAvatarInitClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of routine_5a_PlaceAvatarInitComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function routine_5a_PlaceAvatarInitRoutineEnd() {
  //------Ending Routine 'routine_5a_PlaceAvatarInit'-------
  for (const thisComponent of routine_5a_PlaceAvatarInitComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "routine_5a_PlaceAvatarInit" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var gotValidClick;
var PlacingKeyboard;
var routine_5b_PlacingAvatarComponents;
function routine_5b_PlacingAvatarRoutineBegin() {
  //------Prepare to start Routine 'routine_5b_PlacingAvatar'-------
  t = 0;
  routine_5b_PlacingAvatarClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the AvatarMouse
  // current position of the mouse:
  AvatarMouse.x = [];
  AvatarMouse.y = [];
  AvatarMouse.leftButton = [];
  AvatarMouse.midButton = [];
  AvatarMouse.rightButton = [];
  AvatarMouse.time = [];
  gotValidClick = false; // until a click is received
  AvatarMouse.mouseClock.reset();
  PlacingKeyboard = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  routine_5b_PlacingAvatarComponents = [];
  routine_5b_PlacingAvatarComponents.push(PlacementArea);
  routine_5b_PlacingAvatarComponents.push(AvatarMouse);
  routine_5b_PlacingAvatarComponents.push(leftTarget);
  routine_5b_PlacingAvatarComponents.push(rightTarget);
  routine_5b_PlacingAvatarComponents.push(PlacingKeyboard);
  routine_5b_PlacingAvatarComponents.push(AvatarPlace);
  
  for (const thisComponent of routine_5b_PlacingAvatarComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var prevButtonState;
function routine_5b_PlacingAvatarRoutineEachFrame() {
  //------Loop for each frame of Routine 'routine_5b_PlacingAvatar'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = routine_5b_PlacingAvatarClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *PlacementArea* updates
  if (t >= 0.0 && PlacementArea.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    PlacementArea.tStart = t;  // (not accounting for frame time here)
    PlacementArea.frameNStart = frameN;  // exact frame index
    PlacementArea.setAutoDraw(true);
  }

  
  if (PlacementArea.status === PsychoJS.Status.STARTED){ // only update if being drawn
    PlacementArea.setSize([Screen_width, (box_size + 10)]);
  }
  // *AvatarMouse* updates
  if (frameN >= 0.0 && AvatarMouse.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AvatarMouse.tStart = t;  // (not accounting for frame time here)
    AvatarMouse.frameNStart = frameN;  // exact frame index
    AvatarMouse.status = PsychoJS.Status.STARTED;
    prevButtonState = AvatarMouse.getPressed();  // if button is down already this ISN'T a new click
    }
  if (AvatarMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = AvatarMouse.getPressed();
    const xys = AvatarMouse.getPos();
    AvatarMouse.x.push(xys[0]);
    AvatarMouse.y.push(xys[1]);
    AvatarMouse.leftButton.push(buttons[0]);
    AvatarMouse.midButton.push(buttons[1]);
    AvatarMouse.rightButton.push(buttons[2]);
    AvatarMouse.time.push(AvatarMouse.mouseClock.getTime());
  }
  
  // *leftTarget* updates
  if (t >= 0.0 && leftTarget.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    leftTarget.tStart = t;  // (not accounting for frame time here)
    leftTarget.frameNStart = frameN;  // exact frame index
    leftTarget.setAutoDraw(true);
  }

  
  if (leftTarget.status === PsychoJS.Status.STARTED){ // only update if being drawn
    leftTarget.setPos([left_target, 0]);
    leftTarget.setSize([box_size, box_size]);
    leftTarget.setFillColor(new util.Color(box_build));
    leftTarget.setLineColor(box_build);
  }
  
  // *rightTarget* updates
  if (t >= 0.0 && rightTarget.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    rightTarget.tStart = t;  // (not accounting for frame time here)
    rightTarget.frameNStart = frameN;  // exact frame index
    rightTarget.setAutoDraw(true);
  }

  
  if (rightTarget.status === PsychoJS.Status.STARTED){ // only update if being drawn
    rightTarget.setPos([right_target, 0]);
    rightTarget.setSize([box_size, box_size]);
    rightTarget.setFillColor(new util.Color(box_build));
    rightTarget.setLineColor(box_build);
  }
  
  // *PlacingKeyboard* updates
  if (t >= 0.0 && PlacingKeyboard.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    PlacingKeyboard.tStart = t;  // (not accounting for frame time here)
    PlacingKeyboard.frameNStart = frameN;  // exact frame index
    PlacingKeyboard.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { PlacingKeyboard.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (PlacingKeyboard.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      PlacingKeyboard.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      PlacingKeyboard.rt = PlacingKeyboard.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *AvatarPlace* updates
  if (t >= 0.0 && AvatarPlace.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AvatarPlace.tStart = t;  // (not accounting for frame time here)
    AvatarPlace.frameNStart = frameN;  // exact frame index
    AvatarPlace.setAutoDraw(true);
  }

  
  if (AvatarPlace.status === PsychoJS.Status.STARTED){ // only update if being drawn
    AvatarPlace.setPos([Avatar_x, Avatar_y]);
    AvatarPlace.setSize([box_size, box_size]);
    AvatarPlace.setFillColor(new util.Color(box_truck));
    AvatarPlace.setLineColor(box_truck);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of routine_5b_PlacingAvatarComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function routine_5b_PlacingAvatarRoutineEnd() {
  //------Ending Routine 'routine_5b_PlacingAvatar'-------
  for (const thisComponent of routine_5b_PlacingAvatarComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('AvatarMouse.x', AvatarMouse.x);
  psychoJS.experiment.addData('AvatarMouse.y', AvatarMouse.y);
  psychoJS.experiment.addData('AvatarMouse.leftButton', AvatarMouse.leftButton);
  psychoJS.experiment.addData('AvatarMouse.midButton', AvatarMouse.midButton);
  psychoJS.experiment.addData('AvatarMouse.rightButton', AvatarMouse.rightButton);
  psychoJS.experiment.addData('AvatarMouse.time', AvatarMouse.time);
  
  
  // check responses
  if (PlacingKeyboard.keys === undefined || PlacingKeyboard.keys.length === 0) {    // No response was made
      PlacingKeyboard.keys = undefined;
  }
  
  psychoJS.experiment.addData('PlacingKeyboard.keys', PlacingKeyboard.keys);
  if (typeof PlacingKeyboard.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('PlacingKeyboard.rt', PlacingKeyboard.rt);
      routineTimer.reset();
      }
  
  // the Routine "routine_5b_PlacingAvatar" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var DrivingKeys;
var routine_5c_DrivingAvatarComponents;
function routine_5c_DrivingAvatarRoutineBegin() {
  //------Prepare to start Routine 'routine_5c_DrivingAvatar'-------
  t = 0;
  routine_5c_DrivingAvatarClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the DrivingMouse
  // current position of the mouse:
  DrivingMouse.x = [];
  DrivingMouse.y = [];
  DrivingMouse.leftButton = [];
  DrivingMouse.midButton = [];
  DrivingMouse.rightButton = [];
  DrivingMouse.time = [];
  DrivingMouse.clicked_name = [];
  gotValidClick = false; // until a click is received
  DrivingKeys = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  routine_5c_DrivingAvatarComponents = [];
  routine_5c_DrivingAvatarComponents.push(DrivingMouse);
  routine_5c_DrivingAvatarComponents.push(DrivingKeys);
  routine_5c_DrivingAvatarComponents.push(DrivingBoundary);
  routine_5c_DrivingAvatarComponents.push(AvatarPlaced);
  routine_5c_DrivingAvatarComponents.push(LeftBuild);
  routine_5c_DrivingAvatarComponents.push(RightBuild);
  routine_5c_DrivingAvatarComponents.push(AvatarDrive);
  routine_5c_DrivingAvatarComponents.push(upClick);
  routine_5c_DrivingAvatarComponents.push(downClick);
  routine_5c_DrivingAvatarComponents.push(leftClick);
  routine_5c_DrivingAvatarComponents.push(rightClick);
  routine_5c_DrivingAvatarComponents.push(upShape);
  routine_5c_DrivingAvatarComponents.push(downShape);
  routine_5c_DrivingAvatarComponents.push(rightShape);
  routine_5c_DrivingAvatarComponents.push(leftShape);
  
  for (const thisComponent of routine_5c_DrivingAvatarComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function routine_5c_DrivingAvatarRoutineEachFrame() {
  //------Loop for each frame of Routine 'routine_5c_DrivingAvatar'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = routine_5c_DrivingAvatarClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // *DrivingMouse* updates
  if (frameN >= delay && DrivingMouse.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    DrivingMouse.tStart = t;  // (not accounting for frame time here)
    DrivingMouse.frameNStart = frameN;  // exact frame index
    DrivingMouse.status = PsychoJS.Status.STARTED;
    DrivingMouse.mouseClock.reset();
    prevButtonState = DrivingMouse.getPressed();  // if button is down already this ISN'T a new click
    }
  if (DrivingMouse.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    DrivingMouse.status = PsychoJS.Status.FINISHED;
  }
  if (DrivingMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = DrivingMouse.getPressed();
    const xys = DrivingMouse.getPos();
    DrivingMouse.x.push(xys[0]);
    DrivingMouse.y.push(xys[1]);
    DrivingMouse.leftButton.push(buttons[0]);
    DrivingMouse.midButton.push(buttons[1]);
    DrivingMouse.rightButton.push(buttons[2]);
    DrivingMouse.time.push(DrivingMouse.mouseClock.getTime());
    // check if the mouse was inside our 'clickable' objects
    gotValidClick = false;
    for (const obj of [upShape, downShape, rightShape, leftShape]) {
      if (obj.contains(DrivingMouse)) {
        gotValidClick = true;
        DrivingMouse.clicked_name.push(obj.name)
      }
    }
  }
  
  // *DrivingKeys* updates
  if (frameN >= delay && DrivingKeys.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    DrivingKeys.tStart = t;  // (not accounting for frame time here)
    DrivingKeys.frameNStart = frameN;  // exact frame index
    DrivingKeys.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { DrivingKeys.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (DrivingKeys.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    DrivingKeys.status = PsychoJS.Status.FINISHED;
  }

  if (DrivingKeys.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['up', 'down', 'right', 'left']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      DrivingKeys.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      DrivingKeys.rt = DrivingKeys.clock.getTime();
    }
  }
  
  
  // *DrivingBoundary* updates
  if (frameN >= 0.0 && DrivingBoundary.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    DrivingBoundary.tStart = t;  // (not accounting for frame time here)
    DrivingBoundary.frameNStart = frameN;  // exact frame index
    DrivingBoundary.setAutoDraw(true);
  }

  if (DrivingBoundary.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    DrivingBoundary.setAutoDraw(false);
  }
  
  if (DrivingBoundary.status === PsychoJS.Status.STARTED){ // only update if being drawn
    DrivingBoundary.setSize([Screen_width, (box_size + 10)]);
  }
  
  // *AvatarPlaced* updates
  if (frameN >= 0.0 && AvatarPlaced.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AvatarPlaced.tStart = t;  // (not accounting for frame time here)
    AvatarPlaced.frameNStart = frameN;  // exact frame index
    AvatarPlaced.setAutoDraw(true);
  }

  if (AvatarPlaced.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    AvatarPlaced.setAutoDraw(false);
  }
  
  if (AvatarPlaced.status === PsychoJS.Status.STARTED){ // only update if being drawn
    AvatarPlaced.setPos([Avatar_x, Avatar_y]);
    AvatarPlaced.setSize([box_size, box_size]);
    AvatarPlaced.setFillColor(new util.Color(box_placed));
    AvatarPlaced.setLineColor(box_placed);
  }
  
  // *LeftBuild* updates
  if (frameN >= 0.0 && LeftBuild.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    LeftBuild.tStart = t;  // (not accounting for frame time here)
    LeftBuild.frameNStart = frameN;  // exact frame index
    LeftBuild.setAutoDraw(true);
  }

  if (LeftBuild.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    LeftBuild.setAutoDraw(false);
  }
  
  if (LeftBuild.status === PsychoJS.Status.STARTED){ // only update if being drawn
    LeftBuild.setPos([left_target, 0]);
    LeftBuild.setSize([box_size, box_size]);
    LeftBuild.setFillColor(new util.Color(left_colour));
    LeftBuild.setLineColor(left_colour);
  }
  
  // *RightBuild* updates
  if (frameN >= 0.0 && RightBuild.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    RightBuild.tStart = t;  // (not accounting for frame time here)
    RightBuild.frameNStart = frameN;  // exact frame index
    RightBuild.setAutoDraw(true);
  }

  if (RightBuild.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    RightBuild.setAutoDraw(false);
  }
  
  if (RightBuild.status === PsychoJS.Status.STARTED){ // only update if being drawn
    RightBuild.setPos([right_target, 0]);
    RightBuild.setSize([box_size, box_size]);
    RightBuild.setFillColor(new util.Color(right_colour));
    RightBuild.setLineColor(right_colour);
  }
  
  // *AvatarDrive* updates
  if (t >= 0.0 && AvatarDrive.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AvatarDrive.tStart = t;  // (not accounting for frame time here)
    AvatarDrive.frameNStart = frameN;  // exact frame index
    AvatarDrive.setAutoDraw(true);
  }

  if (AvatarDrive.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    AvatarDrive.setAutoDraw(false);
  }
  
  if (AvatarDrive.status === PsychoJS.Status.STARTED){ // only update if being drawn
    AvatarDrive.setPos([AvatarDrive_x, AvatarDrive_y]);
    AvatarDrive.setSize([box_size, box_size]);
    AvatarDrive.setFillColor(new util.Color(box_truck));
    AvatarDrive.setLineColor(box_truck);
  }
  
  // *upClick* updates
  if (frameN >= 0 && upClick.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    upClick.tStart = t;  // (not accounting for frame time here)
    upClick.frameNStart = frameN;  // exact frame index
    upClick.setAutoDraw(true);
  }

  if (upClick.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    upClick.setAutoDraw(false);
  }
  
  if (upClick.status === PsychoJS.Status.STARTED){ // only update if being drawn
    upClick.setPos([Arrow_x[0], Arrow_y[0]]);
    upClick.setSize([Arrow_size, Arrow_size]);
    upClick.setOri(Arrow_orient[0]);
    upClick.setFillColor(new util.Color([1, 1, 1]));
    upClick.setLineColor([(- 1), (- 1), (- 1)]);
  }
  
  // *downClick* updates
  if (t >= 0.0 && downClick.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    downClick.tStart = t;  // (not accounting for frame time here)
    downClick.frameNStart = frameN;  // exact frame index
    downClick.setAutoDraw(true);
  }

  if (downClick.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    downClick.setAutoDraw(false);
  }
  
  if (downClick.status === PsychoJS.Status.STARTED){ // only update if being drawn
    downClick.setPos([Arrow_x[1], Arrow_y[1]]);
    downClick.setSize([Arrow_size, Arrow_size]);
    downClick.setOri(Arrow_orient[1]);
  }
  
  // *leftClick* updates
  if (t >= 0.0 && leftClick.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    leftClick.tStart = t;  // (not accounting for frame time here)
    leftClick.frameNStart = frameN;  // exact frame index
    leftClick.setAutoDraw(true);
  }

  if (leftClick.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    leftClick.setAutoDraw(false);
  }
  
  if (leftClick.status === PsychoJS.Status.STARTED){ // only update if being drawn
    leftClick.setPos([Arrow_x[2], Arrow_y[2]]);
    leftClick.setSize([Arrow_size, Arrow_size]);
    leftClick.setOri(Arrow_orient[2]);
  }
  
  // *rightClick* updates
  if (t >= 0.0 && rightClick.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    rightClick.tStart = t;  // (not accounting for frame time here)
    rightClick.frameNStart = frameN;  // exact frame index
    rightClick.setAutoDraw(true);
  }

  if (rightClick.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    rightClick.setAutoDraw(false);
  }
  
  if (rightClick.status === PsychoJS.Status.STARTED){ // only update if being drawn
    rightClick.setPos([Arrow_x[3], Arrow_y[3]]);
    rightClick.setSize([Arrow_size, Arrow_size]);
    rightClick.setOri(0);
  }
  
  // *upShape* updates
  if (t >= 0.0 && upShape.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    upShape.tStart = t;  // (not accounting for frame time here)
    upShape.frameNStart = frameN;  // exact frame index
    upShape.setAutoDraw(true);
  }

  if (upShape.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    upShape.setAutoDraw(false);
  }
  
  if (upShape.status === PsychoJS.Status.STARTED){ // only update if being drawn
    upShape.setPos([Arrow_x[0], Arrow_y[0]]);
    upShape.setSize([Arrow_size, Arrow_size]);
    upShape.setOri(Arrow_orient[0]);
    upShape.setFillColor(new util.Color(up_col));
    upShape.setLineColor([(- 1), (- 1), (- 1)]);
  }
  
  // *downShape* updates
  if (t >= 0.0 && downShape.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    downShape.tStart = t;  // (not accounting for frame time here)
    downShape.frameNStart = frameN;  // exact frame index
    downShape.setAutoDraw(true);
  }

  if (downShape.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    downShape.setAutoDraw(false);
  }
  
  if (downShape.status === PsychoJS.Status.STARTED){ // only update if being drawn
    downShape.setPos([Arrow_x[1], Arrow_y[1]]);
    downShape.setSize([Arrow_size, Arrow_size]);
    downShape.setOri(Arrow_orient[1]);
    downShape.setFillColor(new util.Color(down_col));
    downShape.setLineColor([(- 1), (- 1), (- 1)]);
  }
  
  // *rightShape* updates
  if (t >= 0.0 && rightShape.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    rightShape.tStart = t;  // (not accounting for frame time here)
    rightShape.frameNStart = frameN;  // exact frame index
    rightShape.setAutoDraw(true);
  }

  if (rightShape.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    rightShape.setAutoDraw(false);
  }
  
  if (rightShape.status === PsychoJS.Status.STARTED){ // only update if being drawn
    rightShape.setPos([Arrow_x[3], Arrow_y[3]]);
    rightShape.setSize([Arrow_size, Arrow_size]);
    rightShape.setOri(Arrow_orient[3]);
    rightShape.setFillColor(new util.Color(right_col));
    rightShape.setLineColor([(- 1), (- 1), (- 1)]);
  }
  
  // *leftShape* updates
  if (t >= 0.0 && leftShape.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    leftShape.tStart = t;  // (not accounting for frame time here)
    leftShape.frameNStart = frameN;  // exact frame index
    leftShape.setAutoDraw(true);
  }

  if (leftShape.status === PsychoJS.Status.STARTED && frameN >= (Trial_time + delay)) {
    leftShape.setAutoDraw(false);
  }
  
  if (leftShape.status === PsychoJS.Status.STARTED){ // only update if being drawn
    leftShape.setPos([Arrow_x[2], Arrow_y[2]]);
    leftShape.setSize([Arrow_size, Arrow_size]);
    leftShape.setOri(Arrow_orient[2]);
    leftShape.setFillColor(new util.Color(left_col));
    leftShape.setLineColor([(- 1), (- 1), (- 1)]);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of routine_5c_DrivingAvatarComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function routine_5c_DrivingAvatarRoutineEnd() {
  //------Ending Routine 'routine_5c_DrivingAvatar'-------
  for (const thisComponent of routine_5c_DrivingAvatarComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('DrivingMouse.x', DrivingMouse.x);
  psychoJS.experiment.addData('DrivingMouse.y', DrivingMouse.y);
  psychoJS.experiment.addData('DrivingMouse.leftButton', DrivingMouse.leftButton);
  psychoJS.experiment.addData('DrivingMouse.midButton', DrivingMouse.midButton);
  psychoJS.experiment.addData('DrivingMouse.rightButton', DrivingMouse.rightButton);
  psychoJS.experiment.addData('DrivingMouse.time', DrivingMouse.time);
  psychoJS.experiment.addData('DrivingMouse.clicked_name', DrivingMouse.clicked_name);
  
  
  // check responses
  if (DrivingKeys.keys === undefined || DrivingKeys.keys.length === 0) {    // No response was made
      DrivingKeys.keys = undefined;
  }
  
  psychoJS.experiment.addData('DrivingKeys.keys', DrivingKeys.keys);
  if (typeof DrivingKeys.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('DrivingKeys.rt', DrivingKeys.rt);
      }
  
  // the Routine "routine_5c_DrivingAvatar" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var routine_5d_TrialFeedbackComponents;
function routine_5d_TrialFeedbackRoutineBegin() {
  //------Prepare to start Routine 'routine_5d_TrialFeedback'-------
  t = 0;
  routine_5d_TrialFeedbackClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  routine_5d_TrialFeedbackComponents = [];
  routine_5d_TrialFeedbackComponents.push(DrivingBoundaryFeedback);
  routine_5d_TrialFeedbackComponents.push(AvatarPlacedFeedback);
  routine_5d_TrialFeedbackComponents.push(LeftFeedback);
  routine_5d_TrialFeedbackComponents.push(RightFeedback);
  routine_5d_TrialFeedbackComponents.push(AvatarFeedback);
  routine_5d_TrialFeedbackComponents.push(text);
  
  for (const thisComponent of routine_5d_TrialFeedbackComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function routine_5d_TrialFeedbackRoutineEachFrame() {
  //------Loop for each frame of Routine 'routine_5d_TrialFeedback'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = routine_5d_TrialFeedbackClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *DrivingBoundaryFeedback* updates
  if (t >= 0.0 && DrivingBoundaryFeedback.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    DrivingBoundaryFeedback.tStart = t;  // (not accounting for frame time here)
    DrivingBoundaryFeedback.frameNStart = frameN;  // exact frame index
    DrivingBoundaryFeedback.setAutoDraw(true);
  }

  if (DrivingBoundaryFeedback.status === PsychoJS.Status.STARTED && frameN >= 120) {
    DrivingBoundaryFeedback.setAutoDraw(false);
  }
  
  if (DrivingBoundaryFeedback.status === PsychoJS.Status.STARTED){ // only update if being drawn
    DrivingBoundaryFeedback.setPos([0, 100]);
    DrivingBoundaryFeedback.setSize([Screen_width, (box_size + 10)]);
  }
  
  // *AvatarPlacedFeedback* updates
  if (t >= 0 && AvatarPlacedFeedback.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AvatarPlacedFeedback.tStart = t;  // (not accounting for frame time here)
    AvatarPlacedFeedback.frameNStart = frameN;  // exact frame index
    AvatarPlacedFeedback.setAutoDraw(true);
  }

  if (AvatarPlacedFeedback.status === PsychoJS.Status.STARTED && frameN >= 120) {
    AvatarPlacedFeedback.setAutoDraw(false);
  }
  
  if (AvatarPlacedFeedback.status === PsychoJS.Status.STARTED){ // only update if being drawn
    AvatarPlacedFeedback.setPos([Avatar_x, Avatar_y]);
    AvatarPlacedFeedback.setSize([box_size, box_size]);
    AvatarPlacedFeedback.setFillColor(new util.Color(box_placed));
    AvatarPlacedFeedback.setLineColor(box_placed);
  }
  
  // *LeftFeedback* updates
  if (t >= 0.0 && LeftFeedback.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    LeftFeedback.tStart = t;  // (not accounting for frame time here)
    LeftFeedback.frameNStart = frameN;  // exact frame index
    LeftFeedback.setAutoDraw(true);
  }

  if (LeftFeedback.status === PsychoJS.Status.STARTED && frameN >= 120) {
    LeftFeedback.setAutoDraw(false);
  }
  
  if (LeftFeedback.status === PsychoJS.Status.STARTED){ // only update if being drawn
    LeftFeedback.setPos([left_target, 0]);
    LeftFeedback.setSize([box_size, box_size]);
    LeftFeedback.setFillColor(new util.Color(left_colour));
    LeftFeedback.setLineColor(left_colour);
  }
  
  // *RightFeedback* updates
  if (t >= 0.0 && RightFeedback.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    RightFeedback.tStart = t;  // (not accounting for frame time here)
    RightFeedback.frameNStart = frameN;  // exact frame index
    RightFeedback.setAutoDraw(true);
  }

  if (RightFeedback.status === PsychoJS.Status.STARTED && frameN >= 120) {
    RightFeedback.setAutoDraw(false);
  }
  
  if (RightFeedback.status === PsychoJS.Status.STARTED){ // only update if being drawn
    RightFeedback.setPos([right_target, 0]);
    RightFeedback.setSize([box_size, box_size]);
    RightFeedback.setFillColor(new util.Color(right_colour));
    RightFeedback.setLineColor(right_colour);
  }
  
  // *AvatarFeedback* updates
  if (t >= 0.0 && AvatarFeedback.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AvatarFeedback.tStart = t;  // (not accounting for frame time here)
    AvatarFeedback.frameNStart = frameN;  // exact frame index
    AvatarFeedback.setAutoDraw(true);
  }

  if (AvatarFeedback.status === PsychoJS.Status.STARTED && frameN >= 120) {
    AvatarFeedback.setAutoDraw(false);
  }
  
  if (AvatarFeedback.status === PsychoJS.Status.STARTED){ // only update if being drawn
    AvatarFeedback.setPos([AvatarDrive_x, AvatarDrive_y]);
    AvatarFeedback.setSize([box_size, box_size]);
    AvatarFeedback.setFillColor(new util.Color(box_truck));
    AvatarFeedback.setLineColor(box_truck);
  }
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  if (text.status === PsychoJS.Status.STARTED && frameN >= 120) {
    text.setAutoDraw(false);
  }
  
  if (text.status === PsychoJS.Status.STARTED){ // only update if being drawn
    text.setText(Feedback_text);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of routine_5d_TrialFeedbackComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function routine_5d_TrialFeedbackRoutineEnd() {
  //------Ending Routine 'routine_5d_TrialFeedback'-------
  for (const thisComponent of routine_5d_TrialFeedbackComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "routine_5d_TrialFeedback" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisScheduler, thisTrial) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      thisScheduler.stop();
    } else if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
