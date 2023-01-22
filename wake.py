#!/usr/bin/env python3
from pathlib import Path
from util import write_effect

effect = [
    {
        'rgb_array': '#fff #0d0d0d #0d0d0d #0d0d0d',
        'sleep': 100
    },
    {
        'rgb_array': '#0d0d0d #fff #0d0d0d #0d0d0d',
        'sleep': 100
    },
    {
        'rgb_array': '#0d0d0d #0d0d0d #fff #0d0d0d',
        'sleep': 100
    },
    {
        'rgb_array': '#0d0d0d #0d0d0d #0d0d0d #fff',
        'sleep': 120
    },
    {
        'rgb_array': '#0d0d0d #0d0d0d #0d0d0d #0d0d0d',
        'sleep': 400
    },
    {
        'rgb_array': '#0d0d0d #0d0d0d #0d0d0d #fff',
        'sleep': 120
    },
    {
        'rgb_array': '#0d0d0d #0d0d0d #fff #0d0d0d',
        'sleep': 100
    },
    {
        'rgb_array': '#0d0d0d #fff #0d0d0d #0d0d0d',
        'sleep': 100
    },
    {
        'rgb_array': '#fff #0d0d0d #0d0d0d #0d0d0d',
        'sleep': 100
    }
]

if __name__ == '__main__':
    write_effect(Path(__file__).with_suffix('.json'), effect)
