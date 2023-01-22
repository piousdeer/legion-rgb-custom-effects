import json

ENDING = '#0d0d0d #0d0d0d #0d0d0d #0d0d0d'

def process_effect_step(step):
    step = {
        'step_type': 'Set',
        'speed': 1,
        'brightness': 1,
        'steps': 100,
        'delay_between_steps': 100,
        'sleep': 1000
    } | step

    rgb_array = []
    for color in step['rgb_array'].replace('#', '').split():
        if len(color) == 3:
            rgb_array += [int(x, 16)*17 for x in color]
        elif len(color) == 6:
            rgb_array += [int(x, 16)
                          for x in (color[:2], color[2:4], color[4:])]
    step['rgb_array'] = rgb_array

    return step


def write_effect(path, steps, loop=False):
    if not loop:
        steps.append({
            'rgb_array': ENDING,
            'sleep': 0
        })
    full_effect = {
        'effect_steps': [process_effect_step(step) for step in steps],
        'should_loop': loop
    }
    with path.open('w') as file:
        json.dump(full_effect, file)
