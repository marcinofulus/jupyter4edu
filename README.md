## Jupyter4edu Erasmus+ project,

This repository contains teaching materials used during Erasmus+ project: Jupyter@edu.

## Content

You can find here a collection of noetbooks which have beed used in teaching at European University Cyprus,  University of Augsburg and University of Silesia. They contain  different  approaches to the way of using `Jupyter` notebook and `nbgrader` software. 

Most of notebooks contain tests and are compatible with `nbgrader` software. It means that it is easy to produce student version (without solution) and check automatically corectness of the solution.

### Excercises in scientific programming

[Excercises in scientific programming](https://github.com/marcinofulus/jupyter4edu/tree/master/augsburg/exercises) contain 8 selected  problems in scientific programming. In this approach is has been used in a small class, and the main notebook was given to students. Supplementary notebooks explaining in details some technical aspects are provided to each topic. In this way the materials was  accessible for students with little programming skills. More advanced students can proceed directly to the main problem.


 - [BirthdayProblem.ipynb](https://github.com/marcinofulus/jupyter4edu/tree/master/augsburg/exercises/BirthdayProblem) solves a classical problem of finding two persons have their birthday on the same day of the year  by means of a simulation. It condrawing birthdays at random. The supplemental material contain brief explanation of lists and sets in `Python`: [~ListsAndSets.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/BirthdayProblem/~ListsAndSets.ipynb).
 
 - [GameOfLife.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/GameOfLife/GameOfLife.ipynb) 
The game of life simulates the dynamics of some living species according to a few simple rules devised by the British mathematician J. H. Conway. The excercise contain its implementation using `numpy` and `scipy` library.  It introduces user to the practical application of discrete [convolution operator](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/GameOfLife/~Convolution.ipynb). An important and attractive element is also visualisation of time evolution of the system using `ipywidgets` interface to `matplotlib` library.

 -  [JuliaSet.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/JuliaSet/JuliaSet.ipynb) Julia sets offer a possibility to generate beautiful images. The supplementary notebooks contain in depth explanation of:
     
     - [RGB and HSV color models](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/JuliaSet/~ColorIntro.ipynb),
     - [Color Representation](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/JuliaSet/~ColorRepresentation.ipynb).
     - [Grid data structure](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/JuliaSet/~Grid.ipynb)
     - [Iteration prescription for Julia set](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/JuliaSet/~JuliaIteration.ipynb)
 
 - [Parrondo Paradox])(https://github.com/marcinofulus/jupyter4edu/tree/master/augsburg/exercises/ParrondoParadox)
We will define two games for which the probability to loose exceeds the probability to win. Surprisingly, by choosing an appropriate alternating sequence of the two loosing games, one finds that one wins in the long run. This situation is known as Parrondo's paradox. The notebooks provice guided implementation of simulation algorithm of this phenomena. Supplementary materials explains some aspects of [random number generation](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/ParrondoParadox/~RandomNumbers.ipynb) and provide instructions for implementing all parts of the algorithm [GameA.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/ParrondoParadox/~GameA.ipynb),[GameB.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/ParrondoParadox/~GameB.ipynb), [AlternatingAB.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/ParrondoParadox/~AlternatingAB.ipynb)

- Calculation of [Pi](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Pi/Pi.ipynb) by means of the arithmetic-geometric mean. This problem is supplemented by [IntegerAsString.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Pi/~IntegerAsString.ipynb).

 - [Symbolic computation Polynomials](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Polynomials/Polynomials.ipynb). This excercise contains supplementary explanations of Python sets:[Sets.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Polynomials/~Sets.ipynb),[Setdefault.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Polynomials/~Setdefault.ipynb)
 
 
 - Determine the number of primes which can be interpreted as time [Prime Time](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/PrimeTime/Primetime.ipynb). This exercise contain practice of important aspects of Python programming: [list comprehension](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/PrimeTime/~ListComprehensions.ipynb) and demonstrates an angorithm known as [Sieve of Eratosthenes](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/PrimeTime/~SieveOfEratosthenes.ipynb)
 
 - [Diagonal sum in a spiral](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Spiral/Spiral.ipynb) is an interesting reason to gain some algorithmic practice in [functions](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Spiral/~IntroFunctions.ipynb) and [lists](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Spiral/~IntroLists.ipynb).
 
### General relativity using symbolic computer algebra

This collection of notebooks illustrates the application of symbolic computer algebra in Python to problems of general relativity. It is based on SymPy and GraviPy. It uses interactive  3d visualisation using [K3d-jupyter](https://github.com/K3D-tools/K3D-jupyter).

[Introduction to GraviPy](https://render.githubusercontent.com/view/IntroductionGravipy.ipynb)
[Geodesics and Christoffel symbols](https://render.githubusercontent.com/view/Geodesics.ipynb)
[Schwarzschild solution](https://render.githubusercontent.com/view/SchwarzschildMetric.ipynb)
[Embedding of the Schwarzschild solution](https://render.githubusercontent.com/view/EmbeddingSchwarzschild.ipynb)
[Eddington-Finkelstein coordinates](https://render.githubusercontent.com/view/EddingtonFinkelstein.ipynb)
[Tolman-Oppenheimer-Volkoff equation](https://render.githubusercontent.com/view/TOVEquation.ipynb)

Jupyter notebooks which have been used in 


[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/marcinofulus/jupyter4edu/master)

Mybinder with Jupyterlab: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/marcinofulus/jupyter4edu/master?urlpath=lab)





## Acknowledgments

<table class="none">
<tr>
<td>
  <img src="https://eacea.ec.europa.eu/sites/eacea-site/files/logosbeneficaireserasmusleft_en.jpg" width="260">
</td>
<td>
  This repository was created as part of the Erasmus+  project
  <a href="https://jupyter4edu.smcebi.edu.pl/">Jupyter@edu</a>

</td>
</tr>
</table>
