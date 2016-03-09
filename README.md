# pyRF
## Calculation of radiative forcing from GHGs

*Currently limited to CO<sub>2</sub> and CH<sub>4</sub>*

Forcing calculations include uncertainty for use in Monte Carlo analysis. Most of the 
uncertainty information comes from the IPCC AR5 supporting material, with two exceptions:

1. A covariance matrix for the CO<sub>2</sub> impulse response function is from Olivie and Peters (2013)
2. I have represented climate-carbon feedback uncertainty in methane with a triangular distribution. 
The mode (1 Gt C per deg C), is from Collins et al (2013). Uncertainty is represented as a 
triangular distribution with +/- 100%. This is based on the footnote of AR5 Table 8.7 that 
the uncertainties cc-fb are comparable in magnitude to the size of the effect.

***
## Current status

The python code is set up as a script with functions for CO<sub>2</sub> and CH<sub>4</sub>. The following items are on the near term to-do list:
1. Add classes
2. Add uncertainty for fraction of CH4 decomposition to CO<sub>2</sub> (currently fixed at 51%)
3. Add uncertainty for CO<sub>2</sub> IRF in the CH4 function (CO<sub>2</sub> from CH<sub>4</sub> decomposition)
4. Convert to an installable library

***
## Function outputs

*CO2* and *CH4* are designed to return the RF with default parameters. Increasing the 
number of runs will trigger a Monte Carlo calculation. The functions can return:
1. *output*, which is a Pandas dataframe with the mean forcing in each year and +/- one
sigma.
2. *full_output*, which is a numpy array with annual forcing for each run


## References
Olivié, D. J. L., & Peters, G. P. (2013). 
Variation in emission metrics due to variation in CO<sub>2</sub> and temperature impulse response functions. 
Earth Syst. Dynam., 4(2), 267–286. http://doi.org/10.5194/esd-4-267-2013

Collins, W. J., Fry, M. M., Yu, H., Fuglestvedt, J. S., Shindell, D. T., & West, J. J. (2013). 
Global and regional temperature-change potentials for near-term climate forcers. 
Atmos. Chem. Phys., 13(5), 2471–2485. http://doi.org/10.5194/acp-13-2471-2013