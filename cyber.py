#!/usr/bin/env python3
from pathlib import Path
from util import write_effect

effect = [
    {
        "rgb_array": '#000 #000 #000 #000',
        "sleep": 0
    },
    {
        "rgb_array": '#000 #200 #200 #000',
        "step_type": "Transition",
        "brightness": 1,
        "delay_between_steps": 30,
        "sleep": 0
    },
    {
        "rgb_array": '#0ff #200 #200 #200',
        "sleep": 20
    },
    {
        "rgb_array": '#000 #0ff #200 #200',
        "sleep": 20
    },
    {
        "rgb_array": '#000 #110 #0ff #200',
        "sleep": 50
    },
    {
        "rgb_array": '#000 #110 #220 #0ff',
        "sleep": 50
    },
    {
        "rgb_array": '#000 #110 #220 #000',
        "sleep": 0
    },
    {
        "rgb_array": '#220 #220 #220 #220',
        "step_type": "Transition",
        "delay_between_steps": 150,
        "sleep": 0
        # "sleep": 10000
    },
    {
        "rgb_array": '#110 #ff0 #ff0 #110',
        "step_type": "Transition",
        "delay_between_steps": 2,
        "sleep": 50
        # "sleep": 10000
    },
    {
        "rgb_array": '#00f #ff0 #ff0 #90f',
        "brightness": 2,
        "sleep": 100
    },
    {
        "rgb_array": '#000 #000 #000 #000',
        "sleep": 500
    },
    {
        "rgb_array": '#000 #ff0 #ff0 #000',
        "sleep": 1000
    },
    {
        "rgb_array": '#000 #0ff #ff0 #000',
        "sleep": 150
    },
    {
        "rgb_array": '#000 #ff0 #ff0 #000',
        "sleep": 300
    },
    {
        "rgb_array": '#ff0 #0ff #ff0 #000',
        "sleep": 800
    },
    {
        "rgb_array": '#0ff #0ff #0ff #0ff',
        "sleep": 100
    },
    {
        "rgb_array": '#ff0 #ff0 #ff0 #ff0',
        "sleep": 300
    },
]

for idx, sleep in enumerate(
    (
        100,
        200,

        50,
        400,

        100,
        200,
        50,
        100,
        50,
        100,
        100,
        800,
    ) * 4
):
    effect += [
        {
            "rgb_array": '#0ff #ff0 #ff0 #0ff' if idx % 2 == 0 else '#ff0 #ff0 #ff0 #ff0',
            "sleep": sleep
        }
    ]

if __name__ == '__main__':
    write_effect(Path(__file__).with_suffix('.json'), effect, loop=True)
