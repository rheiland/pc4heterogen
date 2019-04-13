# pc4heterogen

[![Build Status](https://travis-ci.com/rheiland/pc4heterogen.svg?branch=master)](https://travis-ci.com/rheiland/pc4heterogen)

A PhysiCell heterogeneous cancer tumor example using a Jupyter notebook GUI. This app can be run at https://nanohub.org/tools/pc4heterogen.

This model demonstrates competition in a tumor with heterogeneous growth characteristics. It is based on a published PhysiCell example in Ghaffarizadeh et al. (2018) [1]. In this model, cancer cells rapidly divide while consuming oxygen, which drives the emergence of hypoxic gradients. Greater availability of oxygen drives faster proliferation, while low oxygen can trigger necrotic death, creating a necrotic core (brown cells) in the center of the tumor. Each cell expresses a mutant "oncoprotein" *p*, which determines how well the cells can respond to oxygen availability to enter the cell cycle. Cells with greater *p* expression divide more rapidly. In the demonstration, cells are shaded from blue (lowest *p* and least proliferative) to yellow (greatest *p* and most proliferative).

Cells are initially distributed assigned a random *p* expression following a Gaussian distribution. Here are some emergent features to notice:

* Faster proliferating cells (yellow) expand clonally in small but growing patches.

* The overall color distribution starts very very heterogeneous (with a "salt and pepper" spatial distribution of *p*), but becomes more uniform over time as clones emerge and expand.

* The increasing uniformity of color shows that selection is choosing winners (yellower cells).

More details about the model can be found at https://nanohub.org/resources/pc4heterogen/about

[1] Ghaffarizadeh A, Heiland R, Friedman SH, Mumenthaler SM, Macklin P (2018) PhysiCell: An open source physics-based cell simulator for 3-D multicellular systems. PLoS Comput Biol 14(2): e1005991. https://doi.org/10.1371/journal.pcbi.1005991
