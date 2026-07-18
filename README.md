# Resistor Color Code Reader

A desktop GUI application built with Python and Tkinter that reads and generates resistor color codes. Supports 4, 5, and 6 band resistors with full bidirectional conversion. Pick colors to get a resistance value, or type a resistance value to see the colors.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Option 1: Download the executable (Windows, no Python required)](#option-1-download-the-executable-windows-no-python-required)
  - [Option 2: Run from source (Python required)](#option-2-run-from-source-python-required)
- [How to Use](#how-to-use)
- [Error Popups](#error-popups)
- [How Resistor Color Codes Work](#how-resistor-color-codes-work)
- [Built With](#built-with)
- [License](#license)
- [Author](#author)

<!-- 
  DEMO GIF/VIDEO GOES HERE
  Example: ![Demo](demo.gif)
  or: [Watch the demo video](link-to-video)
-->

## Features

- **4, 5, and 6 band support** — switch between band counts and the resistor graphic dynamically updates to show the correct number of color bands.
- **Interactive band selection** — click any individual band to choose its color from a dropdown.
- **Customizable resistor body color** — change the body color of the resistor to whatever you like (besides band colors).
- **Reset function** — reset all bands back to the currently selected body color.
- **Live digit/multiplier/tolerance breakdown** — displays the decoded value of each individual band (1st digit, 2nd digit, 3rd digit, multiplier, tolerance) as you select colors.
- **Resistance value display** — automatically calculates and displays the total resistance once all bands are set.
- **Flexible value entry** — type a resistance value in multiple formats and the bands will update to match, including:
  - Standard notation: `4700`
  - Shorthand with unit: `4.7k`
  - Mid-value notation: `4k7`
  
  All of the above are parsed identically and produce the same result.
- **Smart rounding for entered values** — if you type a value with more significant digits than the selected band count can represent, the calculator rounds it to the nearest valid resistor value and updates the bands to match.
- **Accurate to industry standard** — unlike some other online resistor tools, this reader does not incorrectly force a leading black (0) band for small resistance values. Color band generation follows proper resistor color code standards.

## Installation

### Option 1: Download the executable (Windows, no Python required)

1. Go to the [Releases](../../releases) page of this repository.
2. Download the latest `.exe` file.
3. Run the executable — no installation or setup needed.

> **Note:** Since the executable isn't code-signed, Windows SmartScreen or your antivirus may flag it as unrecognized. Click **More info → Run anyway** if this happens.

### Option 2: Run from source (Python required)

**Requirements:**
- Python 3.12
- Tkinter (included with most standard Python installations)

**Steps:**

1. Clone the repository:
   ```bash
   git clone https://github.com/claytonyen/resistor-code-reader.git
   cd resistor-code-reader
   ```
2. Run the application:
   ```bash
   python resistor_reader_gui.py
   ```

## How to Use

1. Select the number of bands (4, 5, or 6) using the buttons at the top.
2. Click on any band of the resistor to open a dropdown and assign that band's color.
3. (Optional) Click **Change Body Color** to customize the resistor's body color.
4. Click **Reset** to reset all bands back to the current body color.
5. As you set band colors, the digit/multiplier/tolerance values update automatically, and the final resistance value is shown in the display at the bottom.
6. Alternatively, type a resistance value into the entry field (e.g. `4700`, `4.7k`, or `4k7`) and the bands will automatically update to match.

## Error Popups

- **"Please select a different color for the resistor body."** - your selected body color is the same as a band color so choose a different one
- **"Too Many Decimal Points!"** - inputted value like 0.3.4
- **"Too Many Multipliers!"** - inputted value like 3k3g3
- **"Range Error"** - inputted value is too large to be displayed, > 999e9 or < 0.1
- **"Range Error Try on 5 Band"** while in 4 band mode inputted value is > 99e9 but can be displayed in 5 band mode
- **"Range Error Try on 4 Band"** while in 5 band mode inputted value is < 1 but can be displayed in 4 band mode

## How Resistor Color Codes Work

Each color on a resistor corresponds to a digit from 0–9. The bands are read left to right, based on which side has bands closer together.

- **4 Band:** 1st digit, 2nd digit, multiplier, tolerance
- **5 Band:** 1st digit, 2nd digit, 3rd digit, multiplier, tolerance
- **6 Band:** 1st digit, 2nd digit, 3rd digit, multiplier, tolerance, temperature coefficient

The digit bands are combined to form a base number, and the multiplier band tells you what power of ten to multiply that base number by. For example, a 4 band resistor with yellow, violet, red, and gold bands reads as digits `4` (yellow) and `7` (violet), a multiplier of `x100` (red), giving `47 x 100 = 4,700 Ω (4.7 KΩ)`, with a tolerance of ±5% (gold). Tolerance and temperature coefficient bands don't affect the base resistance value. They only indicate how much the actual resistance may vary from the stated value, and how much it drifts with temperature, respectively.

## Built With

- Python
- Tkinter

## License

MIT

## Author

Clayton Yen
