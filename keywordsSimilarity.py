#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  keywordsSimilarity.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
#  

def CoefJaccard(set1, set2):
    set1 = set(set1.split())
    set2 = set(set2.split())
    return float(len(set1 & set2)) / len(set1 | set2)

artificialIntelligence = 'Genetic Algorithm	Neural Network	Machine Learning	Mobile Robot	Artificial Intelligent	Indexing Terms	Satisfiability	Fuzzy Set	Real Time	Knowledge Base	Evolutionary Algorithm	Multi Agent System	Decision Making	Problem Solving	Expert System	Logic Programs	Learning Algorithm	Reinforcement Learning	Genetics	Case Study	Fuzzy Logic	Knowledge Representation	Large Scale	Optimization Problem	Data Mining	Degree of Freedom	Genetic Program	Local Search	Decision Tree	Control System	Evolutionary Computing	particle swarm optimizer	Robot Manipulator	Search Space	Path Planning	Pattern Recognition	Fuzzy System	Simulated Annealing	Objective Function	Artificial Neural Network	bayesian network	Fuzzy Control	tabu search	Autonomous Agent	Three Dimensional	Rough Set	Motion Planning	Intelligent System	Fuzzy Model	Indexation	Rule Based	First Order	Knowledge Acquisition	Description Logic	Membership Function	Self Organization	Intelligent Agent	Natural Language	Feature Selection	Dynamic Environment	multiagent system	Computational Complexity	Optimal Solution	Support Vector Machine	Scheduling Problem	Case Base Reasoning	Knowledge Based System	Computer Vision	Semantic Web	Data Structure	Agent Based	Fuzzy Rules	Computer Simulation	Combinatorial Optimization	multiobjective optimization	State Space	Humanoid Robot	Nonlinear System	Autonomous Robot	Software Agent	Dynamic Program	Dynamic System	Point of View	Search Algorithm	Computer Model	Obstacle Avoidance	World Wide Web	Traveling Salesman Problem	Fuzzy Controller	Information Retrieval	Benchmark Problem	Constraint Satisfaction Problem	Particle Swarm	Supervised Learning	Global Optimization	Fuzzy Set Theory	Adaptive Control	Theorem Proving	Real World Application	Configuration Space'
machineLearning = 'Neural Network	Pattern Recognition	Indexing Terms	Support Vector Machine	Learning Algorithm	Machine Learning	Computer Vision	Face Recognition	Feature Extraction	Image Processing	High Dimensionality	Image Segmentation	Pattern Classification	Real Time	Feature Space	Decision Tree	Principal Component Analysis	Feature Selection	backpropagation	Edge Detection	Object Recognition	Maximum Likelihood	Statistical Learning Theory	Supervised Learning	Reinforcement Learning	Radial Basis Function	Support Vector	Em Algorithm	Self Organization	Image Analysis	Hidden Markov Model	Artificial Neural Network	Independent Component Analysis	Genetic Algorithm	Statistical Model	Three Dimensional	Dimensional Reduction	Indexation	Unsupervised Learning	Gradient Descent	Large Scale	Maximum Likelihood Estimate	Statistical Pattern Recognition	Cluster Algorithm	Markov Random Field	Error Rate	Optimization Problem	High Dimensional Data	Satisfiability	Mobile Robot	Nearest Neighbor	Image Sequence	Neural Net	Speech Recognition	Classification Accuracy	Digital Image Processing	Factor Analysis	Wavelet Transform	Local Minima	Probability Distribution	Radial Basis Function Network	Self Organized Map	Back Propagation	Parameter Estimation	Probabilistic Model	Feature Vector	Face Detection	Objective Function	Signal Processing	Degree of Freedom	Scene Analysis	Efficient Algorithm	Computer Simulation	Facial Expression	Learning Problems	Recurrent Neural Network	Machine Vision	Dynamic System	bayesian network	Mutual Information	Missing Values	Image Database	Character Recognition	Dynamic Program	Feedforward Neural Network	Finite Mixture Model	Linear Discriminate Analysis	Image Retrieval	Incomplete Data	Kernel Method	Image Representation	Computational Complexity	Texture Features	Learning Methods	Prior Knowledge	Expectation Maximization	Cost Function	Multi Layer Perceptron	iterative reweighted least squares	Data Mining'

print '-'*60
print 'Retorna o coeficiente de Jaccard, entre 0 e 1'
print '-'*60
print CoefJaccard(artificialIntelligence,machineLearning)
print '-'*60
print
print
print
