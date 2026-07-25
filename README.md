# Parametric Spirograph & Geometric Art Generator

A high-performance Python graphic rendering engine that implements parametric hypotrochoid algorithms to draw multi-layered, interactive wireframe art.

![Project Preview](your_screenshot_or_gif_url_here.png)

## 🚀 Key Engineering Highlights
* **Framerate Optimization**: Leverages screen buffering mechanisms (`turtle.tracer`) to decouple raw trigonometric math loops from visual rendering, ensuring consistent hardware execution.
* **Algorithmic Color Management**: Employs cyclic array indexing via modulo operations (`%`) to step through dynamic hex-code gradients smoothly across rendering sweeps.
* **Geometric Interlacing**: Uses micro-rotations (10-degree phase shifts) between main iteration loops to prevent shape overlap and generate structural wireframe density.

## 🧮 Mathematical Model
The drawing paths are computed iteratively using custom step angles fed directly into parametric mathematical vector equations:
* **X-Axis Mapping**: `x = (R - r) * cos(θ) + d * cos((R - r)/r * θ)`
* **Y-Axis Mapping**: `y = (R - r) * sin(θ) - d * sin((R - r)/r * θ)`

## 💻 Tech Stack & Dependencies
* **Core Runtime**: Python 3.x
* **Graphics Framework**: Standard Turtle Engine
* **Computation Engine**: Native Math Module (Trigonometric functions)

## 🔧 Installation & Execution
1. Clone the repository down to your local developer workspace:
   ```bash
   git clone https://github.com
   ```
2. Navigate directly into the project folder path:
   ```bash
   cd python-spirograph
   ```
3. Execute the graphic drawing script:
   ```bash
   python spirograph.py
   ```

## 🗺️ Engineering Roadmap
- [ ] Implement an interactive CLI allowing custom user entries for variables `R`, `r`, and `d`.
- [ ] Integrate a file-writer to automatically export completed canvas views into compressed `.png` image formats.
- [ ] Add random generation logic to generate unexpected geometric shapes dynamically.
-
