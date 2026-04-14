# E3: MEASURING VISCOSITY USING CAPILLARY AND ROTATIONAL VISCOMETERS

This project is a comprehensive computational analysis of fluid rheology, focusing on how concentration, temperature, and shear rate influence the flow behavior of different substances (Oil and Ketchup). It automates the data processing of laboratory measurements into precise analytical graphs.

## Project Scope: Clinical & Industrial Rheology

Understanding the viscosity profile of a fluid is critical in both bioengineering (e.g., blood flow, nutrient emulsions) and food engineering. This suite of scripts analyzes two distinct types of fluids:
1. **Newtonian Fluids (Oil):** Constant viscosity regardless of shear rate.
2. **Non-Newtonian Fluids (Ketchup):** Viscosity changes under stress (Pseudoplastic/Shear-thinning behavior).

### Key Analytical Components

#### 1. Concentration-Viscosity Relationship (`conc_vis_graph.py`)
Analyzes how the concentration of a solution affects its internal friction across different measurement speeds (RPM). This is vital for determining the optimal consistency of liquid supplements or chemical reagents.

#### 2. Thermal Sensitivity: Arrhenius Analysis (`temp_vis_graph.py`)
Models the relationship between temperature and viscosity using the **Arrhenius-type relationship**. By plotting $ln(\mu)$ vs $1/T$, the script helps in calculating the **Activation Energy** required for the fluid to flow.

#### 3. Shear Stress & Flow Behavior (`sample1_ketchup.py`, `sample1_oil.py`, etc.)
These scripts calculate and plot the **Shear Stress vs. Shear Rate (RPS)** profiles. 
* **Ketchup Analysis:** Demonstrates non-linear behavior, typical of complex biological fluids.
* **Oil Analysis:** Demonstrates linear Newtonian behavior, used as a control reference.
