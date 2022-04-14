# These are some homework exercises to practice working 
#  with pandas and psychopy.

## Exercise A
# 1. Load pandas and psychopy
import pandas as pd
from psychopy import sound, core, visual
import numpy as np


# 2. Load the picture verification simuli file
#    (look up the .read_csv method of pandas)
stimuli = pd.read_csv('picture_verification_stimuli.csv')


# 3. Loop over the item names, and print them on the screen
#    (you can loop over a single column just like a list!)
for word in stimuli['item']:
    print(word)

# 4. Now, change your code to show a text stimulus with each item name,
#     with a 1 second pause in between, instead of using print().
window = visual.Window()
message = visual.TextStim(window)

for word in stimuli['item']:
    message.text = word
    message.draw()
    window.flip()
    core.wait(1)


# 5. Loop over the item paths, and use them to create image stimuli;
#     display each image for 1 second.
window = visual.Window()
images = []
for item_path in stimuli['image_file']:
    image_stim = visual.ImageStim(window, image=item_path)
    images.append(image_stim)

images = np.random.permutation(images)

for image in images:
    image.draw()
    window.flip()
    core.wait(1)


## Exercise B
# 1. Load the lexical decision stimuli file 
lexical_decision_stimuli = pd.read_csv('lexical_decision_stimuli.csv')


# 2. Select all the high frequency words (HF)
#    (you can do this using masks, just like how we selected a single row)
hf_words = lexical_decision_stimuli[lexical_decision_stimuli['freq_category'] == 'HF']


# 3. Loop over the words, and create a sound stimulus for each
#    (you can specify the relative path as f'sounds/HF/{sound_name}.wav')
# 4. Play the sounds one-by-one, making sure there is some time between them

for word in hf_words['word']:
    sound_stim = sound.Sound(f'sounds/HF/{word}.wav')
    sound_stim.play()
    core.wait(2)



