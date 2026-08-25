<div align="center">

```text
      ┌──┐     ┌──┐                    tanish_doorsala :: v2026.1
      │░░│     │░░│                    ─────────────────────────
      │░░│     │░░│   HSA gripper       domain:  mechatronics
      └──┘     └──┘   (auxetic)          stack:   ROS 2 · C++ · Python
         ╲     ╱                         school:  UT Austin · Mech-E
          ╲   ╱
           ╲ ╱  ← wrist / J4
            │
           ╱ ╲
          ╱   ╲  ← J3 · servo
         ╱     ╲
        │       │
       ╱         ╲  ← J2
      ╱           ╲
     │      ●      │  ← J1 · NEMA-17
    ┌┴─────────────┴┐
    │ ▓▓▓ BASE ▓▓▓  │
    └───────────────┘
         ═══════
    // sketch → CAD → firmware → it moves
```

[![Portfolio](https://img.shields.io/badge/portfolio-tanish--doorsala.github.io-0d1117?style=for-the-badge&logo=googlechrome&logoColor=58a6ff)](https://tanish-doorsala.github.io)
[![LinkedIn](https://img.shields.io/badge/linkedin-veera--tanish--doorsala-0d1117?style=for-the-badge&logo=linkedin&logoColor=58a6ff)](https://www.linkedin.com/in/veera-tanish-doorsala/)
[![Email](https://img.shields.io/badge/email-veeratanish.doorsala@utexas.edu-0d1117?style=for-the-badge&logo=gmail&logoColor=58a6ff)](mailto:veeratanish.doorsala@utexas.edu)

</div>

```text
  CONTROL_LOOP :: MECH + EMBEDDED + VISION
  ==========================================
  closed-loop feedback ------------------------------------+
                                                            |
  +--------+   +--------+   +--------+   +--------+   +--------+
  |  CAD   |---|  FAB   |---|  MCU   |---| ROS 2  |---| VISION |
  |SolidWks|   |print/cut|  |ESP32/CAN|  |nodes/IK|   |CV/LiDAR|
  +--------+   +--------+   +---+----+   +--------+   +---+----+
                                  |                        |
                                  +------------+-----------+
                                               |
                                          +----------+
                                          | ACTUATOR |
                                          |HSA/steppr|
                                          +----------+
```

<p align="center">
  <img src="https://raw.githubusercontent.com/tanish-doorsala/tanish-doorsala/master/assets/control-loop.svg" alt="Mechatronics control loop schematic" width="720">
</p>

---

### `> cat about.txt`

```python
class Engineer:
    """Veera Tanish Doorsala — robotics from CAD to closed-loop control."""

    name       = "Veera Tanish Doorsala"
    school     = "UT Austin · Cockrell School of Engineering"
    degree     = "B.S. Mechanical Engineering"
    focus      = ["soft robotics", "embedded control", "computer vision", "real-time systems"]

    def __init__(self):
        self.motivation = (
            "Sketch something, wire it up, watch it move on its own — "
            "no manual input, just a system doing exactly what you designed."
        )

    def currently_running(self) -> list[str]:
        return [
            "MERGe Lab      → HSA grippers, PID, OptiTrack  [Prof. Lillian Chin]",
            "Longhorn Baja  → ESP32 + LoRa telemetry pipeline",
            "UT Austin EcoCAR → LiDAR point cloud perception",
            "DUM-E          → 4-axis ROS 2 arm · MoveIt · IK from scratch",
        ]
```

---

### `> ls ~/lab/`

| path | module | status |
| :--- | :--- | :---: |
| `merge_lab/hsa_gripper/` | SolidWorks · Grasshopper · PID · Arduino–ROS 2 · OptiTrack (~1% validation) | `ACTIVE` |
| `merge_lab/concentric_push_pull/` | Soft robotics controls · concentric tube platform | `ACTIVE` |
| `nrg_lab/closed_loop_extrusion/` | OpenCV · ROS 2 · CAN · ±0.2 mm extrusion accuracy | `SHIPPED` |
| `personal/DUM-E/` | 4-axis arm · NEMA-17 · MoveIt · 3 failed prints before base worked | `BUILD` |
| `ecocar/lidar_stack/` | Point clouds · PCL · Unreal + Simulink co-sim | `ACTIVE` |
| `baja/lora_telemetry/` | ESP32 · RFM95W · 915 MHz · live dashboard | `ACTIVE` |

<details>
<summary><code>> ls ~/archive/</code> · older builds</summary>

| path | stack |
| :--- | :--- |
| `makeathon/classroom_assist/` | ESP32 SAP · breadboard · web UI |
| `utsa/laser_spectroscopy/` | chemical propulsion research · Dr. Pineda |
| `personal/GripTide/` | surf grip pad CAD + Java sizing app |
| `personal/CalcApp/` | Gemini API · webcam OCR · real-time math solver |
| `ut_austin/f1_car/` | SolidWorks · laser-cut chassis · top obstacle course |

</details>

---

### `> git log --oneline --repos`

| repo | stack | link |
| :--- | :--- | :--- |
| `DUM-E` | ROS 2 · MoveIt · 4-axis arm | [github.com/tanish-doorsala/DUM-E](https://github.com/tanish-doorsala/DUM-E) |
| `concentric-tube-robot` | Python · soft robotics | [github.com/tanish-doorsala/concentric-tube-robot](https://github.com/tanish-doorsala/concentric-tube-robot) |
| `Motor-Commander` | C++ · stepper PWM control | [github.com/tanish-doorsala/Motor-Commander](https://github.com/tanish-doorsala/Motor-Commander) |
| `Unreal-Simulink` | MATLAB · Unreal Engine co-simulation | [github.com/tanish-doorsala/Unreal-Simulink-Co-simulation](https://github.com/tanish-doorsala/Unreal-Simulink-Co-simulation) |

---

### `> cat stack.toml`

```toml
[programming]
languages = ["Python", "C++", "Java"]
frameworks = ["ROS 2", "MoveIt", "OpenCV"]

[hardware]
mcu       = ["Arduino", "ESP32", "Raspberry Pi"]
buses     = ["CAN", "SPI", "I2C"]
fab       = ["SolidWorks", "Grasshopper/Rhino", "3D printing", "laser cutting"]

[systems]
perception = ["LiDAR", "Point Cloud Library", "Computer Vision"]
validation = ["OptiTrack / Motive", "MATLAB/Simulink", "Unreal Engine"]
control    = ["PID", "closed-loop extrusion", "inverse kinematics"]
```

---

### `> telemetry --private`

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=tanish-doorsala&show_icons=true&theme=dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=79c0ff&text_color=c9d1d9&include_all_commits=true&count_private=true" alt="stats" height="150">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=tanish-doorsala&layout=compact&theme=dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9&langs_count=8" alt="langs" height="150">
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=tanish-doorsala&theme=dark&hide_border=true&background=0d1117&ring=58a6ff&fire=79c0ff&currStreakLabel=58a6ff&sideLabels=c9d1d9&dates=484f58" alt="streak">
</p>

---

<div align="center">

```text
// open to internships · research · robotics · mechatronics · autonomous systems
// portfolio → https://tanish-doorsala.github.io
```

```diff
+ status: accepting connections
+ reply_to: veeratanish.doorsala@utexas.edu
```

</div>
