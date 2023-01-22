#!/usr/bin/env python3
from pathlib import Path
from util import write_effect

effect = [
    {
        'rgb_array': '#0ff #200 #200 #200',
        'sleep': 40
    },
    {
        'rgb_array': '#000 #0ff #200 #200',
        'sleep': 40
    },
    {
        'rgb_array': '#000 #110 #0ff #200',
        'sleep': 80
    },
    {
        'rgb_array': '#000 #110 #220 #0ff',
        'sleep': 90
    },
    {
        'rgb_array': '#000 #110 #220 #000',
        'sleep': 400
    },
    {
        'rgb_array': '#00f #ff0 #ff0 #90f',
        'brightness': 2,
        'sleep': 600
    },
    {
        'rgb_array': '#000 #000 #000 #000',
        'sleep': 500
    },
    {
        'rgb_array': '#000 #ff0 #ff0 #000',
        'sleep': 1000
    },
    {
        'rgb_array': '#000 #0ff #ff0 #000',
        'sleep': 150
    },
    {
        'rgb_array': '#000 #ff0 #ff0 #000',
        'sleep': 300
    },
    {
        'rgb_array': '#ff0 #0ff #ff0 #000',
        'sleep': 800
    },
    {
        'rgb_array': '#0ff #0ff #0ff #0ff',
        'sleep': 100
    },
    {
        'rgb_array': '#ff0 #ff0 #ff0 #ff0',
        'sleep': 150
    },
    {
        'rgb_array': '#0ff #ff0 #ff0 #0ff',
        'sleep': 1000
    },
    {
        'rgb_array': '#000 #000 #000 #000',
        'sleep': 1000
    },
]

if __name__ == '__main__':
    write_effect(Path(__file__).with_suffix('.json'), effect)
