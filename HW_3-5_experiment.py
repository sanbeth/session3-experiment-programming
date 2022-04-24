import pandas as pd
from psychopy import core, sound, visual, event
import numpy as np

# 1. Load the lexical decision stimuli file 
stimuli = pd.read_csv('lexical_decision_stimuli.csv')

# 2. Present an auditory stimulus
for word in stimuli['word']:
    sound_stim = sound.Sound(f'sounds/all/{word}.wav')
    sound_stim.play()
    core.wait(2)

# 3. Fixation cross-screen 
# 4. Decision screen
# 5. Clock
# 6. Keys to press
# 7. Record the response & timing 
window = visual.Window()
message = visual.TextStim(window)
fixation = visual.TextStim(window, text='+')
clock = core.Clock()

results = []

for word in stimuli['word']:
    sound_stim = sound.Sound(f'sounds/all/{word}.wav')
    sound_stim.play()
    fixation.draw()
    window.flip()
    message.text = word
    message.draw()
    window.flip()
    start_time = clock.getTime()
    keys = event.waitKeys(maxWait=5, keyList=['x', 'm'], timeStamped=clock, clearEvents=True)
    if keys is not None:
        key, end_time = keys[0]
    else:
        key = None
        end_time = clock.getTime()
    
    results.append({
        'start_time': start_time,
        'end_time': end_time,
        'key': key
    })
    
results = pd.DataFrame(results)
results['reaction_time'] = results['end_time'] - results['start_time']
results.to_csv('output.csv')


