# Self_Organization
The molecular mechanisms of self-organization that orchestrate embryonic cells to create astonishing patterns have been among major questions of developmental biology. It is recently shown that embryonic stem cells (ESCs), when cultured in particular micropatterns, can self-organize and mimic early steps of pre-implantation embryogenesis. A systems-biology model to address this observation from a dynamical systems perspective is essential. Here, we propose a multicellular mathematical model for pattern formation during in vitro gastrulation of human ESCs. This model enhances the basic principles of Waddington epigenetic landscape with cell-cell communication, in order to enable pattern and tissue formation. We have used a minimal number of parameters in this model to prevent overfitting and show a very simple mechanism is sufficient to address different experimental observations such as the formation of three germ layers and trophectoderm, responses to altered culture conditions and micropattern diameters, and unexpected spotted forms of the germ layers under certain conditions. Moreover, we have tested different boundary conditions as well as various shapes, observed that the pattern is initiated from the boundary and gradually spread towards the center. This model provides a basis for in-silico modeling of self-organization.

For reading the full paper, you can follow this [link](https://www.biorxiv.org/content/early/2018/01/01/241604)

This code base provides all the necessary pieces to reproduce the main results of Self-organization paper. If you have any questions, please email [fooladi.hosein@gmail.com](fooladi.hosein@gmail.com)

# PREREQUISITES

* Python 
    + [Python (3.6)](https://www.python.org/downloads/)
    + [Numpy](http://www.numpy.org/)(>=1.13.1)
    + [Scipy](https://www.scipy.org/)(>=1.0.0)
    + [Matplotlib](https://matplotlib.org/)(>=2.0.0)
    + [Seaborn](https://seaborn.pydata.org/)(>=0.8.0)
    + [SALib](http://salib.github.io/SALib/)
* Morpheus
    + [Morpheus](https://imc.zih.tu-dresden.de/wiki/morpheus/doku.php) (Morpheus 2.0 RC2 aka version 1.9.3).Morpheus is user-friendly software designed for simulating and studying multicellular systems
    
# Simulation
All the simulation on one cell and studying dynamical system equations have been done in python. You can refer to 'BMP_Noggin' Notebook and run the experiment for different sets of parameters and reproduce figure 3 of the paper. 
 
 All the simulations in the multicellular system have been done with Morpheus. Morpheus is user-friendly software designed for simulating and studying multicellular systems [Starruß et al. 2014](https://academic.oup.com/bioinformatics/article/30/9/1331/234757). For running Morpheus simulation XML file is required. you can find XML files for reproducing results of the paper in Models_Morpheus folder.
    
    
## Citing this work
To cite this work, please use the following BibTeX entry:

```
@article{fooladi2019enhanced,
  title={Enhanced Waddington landscape model with cell--cell communication can explain molecular mechanisms of self-organization},
  author={Fooladi, Hosein and Moradi, Parsa and Sharifi-Zarchi, Ali and Hosein Khalaj, Babak},
  journal={Bioinformatics},
  volume={35},
  number={20},
  pages={4081--4088},
  year={2019},
  publisher={Oxford University Press}
}
```
