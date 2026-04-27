<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a 4-bit down counter.

The counter starts at 15 (1111) after reset.
On every rising edge of the clock:
If ena = 1 and ui_in[0] = 1, the counter decrements by 1.
If ui_in[0] = 0, the counter holds its value.
When the counter reaches 0, it wraps back to 15.
The output is available on uo_out[3:0].

## How to test

Go to the test folder:

cd test

Run simulation:

make
Expected result:
Counter counts: 15 → 14 → ... → 0 → 15
Stops when ui_in[0] = 0

View waveform:

gtkwave tb.vcd
## External hardware

no external hardware used in your project (e.g. PMOD, LED display, etc), if any
