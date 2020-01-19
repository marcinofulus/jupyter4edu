[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/marcinofulus/jupyter4edu/master)

# Jupyter4edu Erasmus+ project,

This repository contains materials produced and used in teaching during Erasmus+ project: Jupyter@edu.


## How to use?

In order to run notebooks, one can clone this repository and setup Python environment based on  included  `environment.yml` file.  

The other possibility is to launch binder container which starts temporary [Jupyter Notebook](http://mybinder.org/v2/gh/marcinofulus/jupyter4edu/master) or [Jupyter lab](http://mybinder.org/v2/gh/marcinofulus/jupyter4edu/master?urlpath=lab) interface



## Content

You can find here a collection of notebooks which have beed used in teaching at European University Cyprus,  University of Augsburg and University of Silesia. They contain  different  approaches to the way of using `Jupyter` notebook and `nbgrader` software. 

Most of notebooks contain tests and are compatible with `nbgrader` software. It means that it is easy to produce student version (without solution) and check automatically corectness of the solution.

### Exercises in scientific programming

[Exercises in scientific programming](https://github.com/marcinofulus/jupyter4edu/tree/master/augsburg/exercises) contain 8 selected problems in scientific programming. Is has been used in a small class. The main notebook containing the probem description and tests was distributed among students. Supplementary notebooks explaining in details some technical aspects were available  for each topic. In this way the materials was accessible for students with little programming skills. More advanced students can proceed directly to the main problem.

 - [BirthdayProblem.ipynb](https://github.com/marcinofulus/jupyter4edu/tree/master/augsburg/exercises/BirthdayProblem) solves a classical problem of finding two persons have their birthday on the same day of the year by means of a simulation. It contains drawing birthdays at random. The supplemental material explains in brief lists and sets in Python: [~ListsAndSets.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/BirthdayProblem/~ListsAndSets.ipynb).
 
 - [GameOfLife.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/GameOfLife/GameOfLife.ipynb) 
The game of life simulates the dynamics of some living species according to a few simple rules devised by the British mathematician J. H. Conway. The exercise contain its implementation using `numpy` and `scipy` library.  It introduces user to the practical application of discrete [convolution operator](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/GameOfLife/~Convolution.ipynb). An important and attractive element is also visualisation of time evolution of the system using `ipywidgets` interface to `matplotlib` library.

 -  [JuliaSet.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/JuliaSet/JuliaSet.ipynb) Julia sets offer a possibility to generate beautiful images. The supplementary notebooks contain in depth explanation of:
     
     - [RGB and HSV color models](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/JuliaSet/~ColorIntro.ipynb),
     - [Color Representation](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/JuliaSet/~ColorRepresentation.ipynb).
     - [Grid data structure](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/JuliaSet/~Grid.ipynb)
     - [Iteration prescription for Julia set](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/JuliaSet/~JuliaIteration.ipynb)
 
 - [Parrondo Paradox](https://github.com/marcinofulus/jupyter4edu/tree/master/augsburg/exercises/ParrondoParadox)
We will define two games for which the probability to loose exceeds the probability to win. Surprisingly, by choosing an appropriate alternating sequence of the two loosing games, one finds that one wins in the long run. This situation is known as Parrondo's paradox. The notebooks provide guided implementation of simulation algorithm of this phenomena. Supplementary materials explains some aspects of [random number generation](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/ParrondoParadox/~RandomNumbers.ipynb) and provide instructions for implementing all parts of the algorithm [GameA.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/ParrondoParadox/~GameA.ipynb), [GameB.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/ParrondoParadox/~GameB.ipynb), [AlternatingAB.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/ParrondoParadox/~AlternatingAB.ipynb)

- Calculation of [Pi](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Pi/Pi.ipynb) by means of the arithmetic-geometric mean. This problem is supplemented by [IntegerAsString.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Pi/~IntegerAsString.ipynb).

- [Symbolic computation Polynomials](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Polynomials/Polynomials.ipynb). This exercise contains supplementary explanations of Python sets:[Sets.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Polynomials/~Sets.ipynb),[Setdefault.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Polynomials/~Setdefault.ipynb)
 
 
 - Determine the number of primes which can be interpreted as time [Prime Time.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/PrimeTime/Primetime.ipynb). This exercise contain practice of important aspects of Python programming: [list comprehension](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/PrimeTime/~ListComprehensions.ipynb) and demonstrates an angorithm known as [Sieve of Eratosthenes](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/PrimeTime/~SieveOfEratosthenes.ipynb)
 
 - [Diagonal sum in a spiral](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Spiral/Spiral.ipynb) is an interesting inspiration to gain some algorithmic practice in using  Python [functions](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Spiral/~IntroFunctions.ipynb) and [lists](https://github.com/marcinofulus/jupyter4edu/blob/master/augsburg/exercises/Spiral/~IntroLists.ipynb).
 
### General relativity using symbolic computer algebra

This collection of notebooks illustrates the application of symbolic computer algebra in Python to problems of general relativity. It is based on SymPy and GraviPy. It uses interactive  3d visualisation using [K3D-jupyter](https://github.com/K3D-tools/K3D-jupyter).

 - [Introduction to GraviPy](https://render.githubusercontent.com/view/IntroductionGravipy.ipynb)
 - [Geodesics and Christoffel symbols](https://render.githubusercontent.com/view/Geodesics.ipynb)
 - [Schwarzschild solution](https://render.githubusercontent.com/view/SchwarzschildMetric.ipynb)
 - [Embedding of the Schwarzschild solution](https://render.githubusercontent.com/view/EmbeddingSchwarzschild.ipynb)
 - [Eddington-Finkelstein coordinates](https://render.githubusercontent.com/view/EddingtonFinkelstein.ipynb)
 - [Tolman-Oppenheimer-Volkoff equation](https://render.githubusercontent.com/view/TOVEquation.ipynb)

### Introduction to artificial intelligence in Python

This set of exercises contain  problem sets for tutorials and supplementary materials lectures.
All exercices are compatible with `nbgrader` and it has been used in a classroom. 

#### Tutorial problems
 
 - Introduction of [numpy](https://github.com/marcinofulus/jupyter4edu/tree/master/katowice/introAI/Numpy)	
 - Step by step implementation of [naive Bayes classifier](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/Bayes/Naive_Bayes_5steps.ipynb)
 - Classical approach to [MNIST dataset](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/MNIST/MNIST_sklearn_knn_SVM.ipynb). There are two versions of this material, the second one uses smaller [NIST8x8 dataset](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/MNIST/NIST8x8_sklearn_knn_SVM_linear.ipynb).
 - [Logistic regression](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/Logistic_regression/Logistic_regression.ipynb) with the steepest descent method. This approach uses `numpy` vector notation: dot products and broadcasting rules.
 - [Principal Componen Analysis](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/PCA/PCA.ipynb) - implementation with  `numpy.linalg` module. 
 - Step by stem implementation of	[kNN algorithm](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/kNN/kNN.ipynb) and [minimum distance classifier](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/kNN/min_distance.ipynb)
 - [Classification Trees](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/Trees/Classification_trees.ipynb), [random forest](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/Trees/RandomForest.ipynb) and [boosting](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/Trees/XGBoost.ipynb) with XGboost library.
 - Neural networkss
   - Minimalizasion algorithms in machine learning [minimum](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/minimum/01_minimum.ipynb)	
   -	Implementation of a single [neuron]()https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/neuron/01_neuron.ipynb in object oriented fashion. It is used for [logistic regression](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/neuron/02_regresja_logistyczna.ipynb), [AND gate](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/neuron/03_bramka_AND.ipynb) and [OR gate](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/neuron/04_bramka_XOR.ipynb)
   - Implementation of a neural network from scratch: 
    - [single layer](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/network/01_layer.ipynb)
    - [network of layers](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/network/02_network.ipynb)
    - the implementation is tested on [XOR gate](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/network/03_bramka_XOR.ipynb), [function fitting](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/network/04_fitowanie_funkcji.ipynb) and [MNIST](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/network/05_MNIST.ipynb) dataset.   
 - [Cross validation](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI/cross_validation/CV.ipynb) in machine learning.	

#### Lecture Materials

This collection contains notebooks which were distributed during lectures. They contain worked example of current topic with a simple task which has to be completed in several minutes. The answers were collected during the same lecture using nbgrader software.   

- [Types of a norm of a vector](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz1/Quiz_norm.ipynb)
- Plotting [Gaussian distribution](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz2/Quiz_Gauss.ipynb) approximating  arbitrarily distrubuted data.
- [Linear regression](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz3/Quiz_reglin.ipynb) - implementation of linear regression and "gradient checking".
- Stochastic gradient descent algorithm: implementation in the case of linear regression in [one variable](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz4/Quiz_reglin-sgd.ipynb) and [many variables](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz4/Quiz_reglin-sgd_multi.ipynb).
- [Confusion matrix](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz5/Quiz_confusion_matrix.ipynb) and Receiver operating characteristic
- [Perceptron](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz6/Quiz_Perceptron.ipynb) implementation of an algorythm, dual form and kernel trick.
- Properties of [SVM](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz7/Quiz_SVM_example_numerical_sklearn.ipynb) method based on experiments of its implementation in sklearn.
- [Minimal distance classifier](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz8/Quiz_minimum_distance_as_linear.ipynb) as a linear classifier. Exact computation of decision areas.
- [Gini index](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz9/Quiz_Gini.ipynb) - implementation and properties.
- Fisher's Linear Discriminant Analysis  [LDA](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz10/Quiz_LDA.ipynb) - implementation and its comparison to `sklearn` 
- Clustering using [k-means](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz11/Quiz_k-means.ipynb)
- Implementation of a [forward pass](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz13/Quiz_nn_forward_pass.ipynb) in fully connected neural network using numpy vectorized operations.
- Implementation of a [backward pass](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/introAI_Quizzes/Quiz12/Quiz_backpropagation.ipynb) in fully connected neural network using numpy vectorized operations..





### Python in introductory mathematics course


- [01-Intro_Tutorial_Students.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/01_Intro_Tutorial_Students.ipynb)
- [02_Sets_1.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/02_Sets_1.ipynb)
- [03_Sets_2.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/03_Sets_2.ipynb)
- [04_Functions_1.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/04_Functions_1.ipynb)
- [05_Functions_2.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/05_Functions_2.ipynb)
- [06_Relations_1.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/06_Relations_1.ipynb)
- [07_Relations_2.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/07_Relations_2.ipynb)

### Python in introductory physics course

- [08_Gravity_Kepler's_Laws.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/08_Gravity_Kepler's_Laws.ipynb)
- [09_Electromagnetic_fields.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/09_Electromagnetic_fields.ipynb)
- [10_Newton's Law of Gravity.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/10_Newton's%20Law%20of%20Gravity.ipynb)
- [11_Planets_Dancing.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/11_Planets_Dancing.ipynb)
- [12_Projectile Motion.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/12_Projectile%20Motion.ipynb)
- [13_Toy Model of the Solar System.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/13_Toy%20Model%20of%20the%20Solar%20System.ipynb)
- [14_Work_&_Energy.ipynb](https://github.com/marcinofulus/jupyter4edu/blob/master/cyprus/14_Work_%26_Energy.ipynb)


### Java course

Java kernel (IJava), makes possible to use Jupyter notebook for java programming. There are materials of 13 [notebooks](https://github.com/marcinofulus/jupyter4edu/tree/master/katowice/java). 

- [Built-in data types](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/01%2BBuilt-in%2Bdata%2Btypes.ipynb)
- [Operators and instructions](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/02%2BOperators%2Band%2Binstructions.ipynb)
- [Object data types](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/03%2BObject%2Bdata%2Btypes.ipynb)
- [Fields methods and constructors](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/04%2BFields%252C%2Bmethods%2Band%2Bconstructors.ipynb)
- [Basic Java API](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/05%2BBasic%2BJava%2BAPI.ipynb)
- [Inheritance and polymorphism](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/06%2BInheritance%2Band%2Bpolymorphism.ipynb)
- [Abstract classes and interfaces](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/07%2BAbstract%2Bclasses%2Band%2Binterfaces.ipynb)
- [Handling exceptions](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/08%2BHandling%2Bexceptions.ipynb)
- [Multithreading](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/09%2BMultithreading.ipynb)
- [Generic data types](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/10%2BGeneric%2Bdata%2Btypes.ipynb)
- [Sets, lists, queues- maps](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/11%2BSets%252C%2Blists%252C%2Bqueues%252C%2Bmaps.ipynb)
- [Case study I - Arkanoid](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/12%2BCase%2Bstudy%2BI.ipynb)
- [Case study II - http server](https://github.com/marcinofulus/jupyter4edu/blob/master/katowice/java/13%2BCase%2Bstudy%2BII.ipynb)







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
