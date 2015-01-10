## Overview
This repo contains various things that were used to help in the design and building of an analog active 3-way 12dB/octave crossover (woofer, midrange, tweeter) with delays. In my project I configure the circuits to crossover at 125Hz and 2.7KHz. The crossover can be adapted to any audio frequencies by changing the capacitor and resistor values.


Some things you'll find in the repo:
* python utilities for help in selecting optimal capacitor and resistor values for a Sallen-Key topology active filter. To crossover at different frequencies, different combinations of resistors and capactitors may be used. Lower value resistors will reduce the Johnson Noise introduced into the signal by the resistors. Lower valued capacitors are likely to be cheaper. Finding a good combination of values that produce the desired crossover frequencies is a non-trivial exercise.
* DipTrace schematic files and PCB layouts
* PCB gerbers (both for the crossover circuit PCB and a corresponding dual-rail power supply)
* Pictures of the results
* LTSpice files for parts of the crossover design
* Bill Of Materials containing DigiKey part numbers that I used in this DIY project

## Background
The design is based off a design contained in <a href="http://www.amazon.com/Design-Active-Crossovers-Douglas-Self/dp/0240817389/ref=sr_1_3?ie=UTF8&qid=1420854829&sr=8-3&keywords=douglas+self">Douglas Self's excellent book "The Design of Active Crossovers"</a>.

The crossover can use either the solid NE5532 opamps or 10x more expensive, and more modern, LM4562 opamps (or a combination of both). I chose to use the LM4562's for the input stage and NE5532's for the filter and delay stages.
 
## Isaac's DIY Project

The nearly final product of this DIY product consists of these two working crossover/delay boards and their power supply:

![](./photos/crossover_boards.jpg)

Now I just need to put these in an enclosure of some kind (and add those two missing fuses you may have noticed in the picture). After doing this I'll measure the frequency response and noise floor more carefully.

