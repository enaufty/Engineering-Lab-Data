# E1: EXPERIMENTAL DESIGN FOR REGULATION OF FLUID FLOW THROUGH TUBING SYSTEMS

This repository contains a Python-based engineering tool to generate the **Moody Diagram** and calculate the **Darcy friction factor ($f$)** for fluid flow in pipes. It is designed to automate laboratory data analysis, replacing manual chart reading with precise computational methods.

## Overview

The **Moody Diagram** is a cornerstone of fluid mechanics, relating the **Reynolds number ($Re$)**, **relative roughness ($\epsilon/D$)**, and the **Darcy friction factor ($f$)**. This tool is particularly useful for Bioengineering applications, such as designing bioreactor piping or analyzing fluid transport in medical devices.



### Technical Background

The script models fluid behavior across three distinct regimes:

1. **Laminar Flow ($Re < 2300$):** Friction is calculated using the linear relationship: 
   $$f = \frac{64}{Re}$$
2. **Transitional Zone ($2300 < Re < 4000$):** A shaded gray region in the plot representing the unstable transition between flow types.
3. **Turbulent Flow ($Re > 4000$):** The script utilizes the **Haaland Equation**, an explicit and highly accurate approximation of the Colebrook-White equation:
   $$\frac{1}{\sqrt{f}} \approx -1.8 \log_{10} \left[ \left( \frac{\epsilon/D}{3.7} \right)^{1.11} + \frac{6.9}{Re} \right]$$
