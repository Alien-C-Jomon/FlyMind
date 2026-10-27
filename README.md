# 🧬 FlyMind: From Connectome to Behavior in a 3D Virtual World

## 📖 Introduction & Overview

**FlyMind** is an advanced, integrated neuro-computational project that bridges real-world connectomics data from the *Drosophila melanogaster* (fruit fly) brain with spiking neural network simulation and an interactive 3D virtual environment. Created as a passionate independent hobby project by **Alien C Jomon**, a 10th-grade student and developer, FlyMind answers a fundamental question in neuroscience: *How does a static wiring diagram of physical brain cells generate dynamic, real-world behaviors like seeking food or fleeing from toxins?*

Instead of treating brain data as a passive spreadsheet, FlyMind brings a fly's decision-making brain to life in real-time, translating neural computations directly into physical actions within a custom 3D simulation sandbox.

---

## ⚙️ How FlyMind Works: The Architecture Pipeline

FlyMind operates through a seamless 4-stage pipeline that connects biological data directly to synthetic behavior:

1. **Connectome Data Ingestion**: The project utilizes public synaptic connectivity matrices and cell-type annotations from FlyWire and Shiu et al. (2023). Specifically, it targets the **Subesophageal Zone (SEZ)**—the primary gustatory and taste-processing center of the insect brain.
2. **Spiking Neural Network Modeling**: Using Python’s `Brian2` library, FlyMind simulates leaky integrate-and-fire (LIF) neurons. It models how sensory receptor activation propagates through local neural circuits when stimulated.
3. **Quantitative Neural Analysis**: By running differential sensory simulations, FlyMind uncovers striking circuit asymmetry:
* **Sugar Stimulation**: Triggers a robust, widespread activation cascade across **255 downstream neurons**, representing a strong positive feeding and approach drive.
* **Control / Water Stimulation**: Recruits a sparse, restricted pathway of only **19 neurons**.


4. **3D Behavioral Mapping (Ursina Engine)**: The quantitative neural firing data drives a custom 3D virtual environment built with the `Ursina Engine`. An interactive yellow fly agent perceives its virtual environment:
* When **Sugar** is present, the neural output drives an approach vector toward the reward.
* When **Bitter** punishments are introduced, the sensory circuit triggers an immediate avoidance vector, causing the fly to frantically scurry away.
* Stimuli feature realistic **10-second decay timers**, mimicking transient chemical cues in nature.



---

## 🛠️ Key Technical Stack

* **Language**: Python 3.14
* **Neural Simulation**: Brian2 (Spiking Neural Network Engine)
* **3D Virtual Environment**: Ursina Engine (Game & Physics Framework)
* **Data & Analytics**: Pandas, NumPy, SciPy, PyArrow
* **Workflow Automation**: Custom batch scripting (`run_game.bat`) for instant one-click execution.

---

## 🔮 Future Vision & Horizons

While FlyMind currently models a localized gustatory sensory sub-circuit in an insect brain, the broader implications of this computational pipeline open up extraordinary possibilities for the future:

1. **Scaling to Mammals and Humans**: As connectomics mapping scales up—moving from insect brains to recent mouse brain and human cortical tissue connectome maps—the exact same computational frameworks can be adapted to analyze mammalian and human neural pathways.
2. **Whole-Brain Emulation & Digital Consciousness**: By faithfully modeling synaptic weights, ion channels, and spiking dynamics in silicon, science inches closer to whole-brain emulation.
3. **Living Inside a Computer**: In the long-term future, advanced connectome-based simulations could allow virtual agents—or eventually emulated biological minds—to perceive, learn, and "live" entirely within synthetic computational substrates. This paves the way for breakthroughs in neuromorphic AI, brain-computer interfaces, and a deeper understanding of the nature of consciousness itself.

---

## 📄 Research Hub & Resources

* Explore the tracked research workspace and documentation in the 🧬 [FlyMind](https://gemini.google.com/notebook/a840f232-de8d-459e-9bd9-ac1aaaae23e1) notebook workspace.
