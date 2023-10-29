---
layout: archive
title: "Codes & Softwares"
permalink: /codes/
author_profile: true
redirect_from:
  - /codes
---

{% include base_path %}

Read more about the scientific computing codes I made or participated in. 

***

<b> WaveBox </b>  <br>
<i> Keywords. </i> DG, HDG, Saint-Venant, Boussinesq, Green-Naghdi, Finite-Volume subcells methods. <br>
<i> Language. </i> C++.

WaveBox is a multi-models numerical platform created by Fabien Marche, dedicated to the approximations of the solutions of several shallow water asymptotics in the surface dimension d = 2 with efficient combined Hybridized Discontinuous Galerkin (HDG) and DG methods on general unstructured meshes (Saint-Venant, Boussinesq and Green-Naghdi equations). Main features are: 
- Sub-models CPU-GPU co-processing;
- Arbitrary order of accuracy (h and p-adaptivity);
- Robust treatment of the run-up and flooding processes (strict maximum-principle enforcement);
- Well-balancing for motionless steady states;
- Unstructured meshes;
- Wave breaking treatment with dynamic switching strategy.

During Ali Haidar's Ph.D., he implemented in WaveBox François Vilar's a posteriori stabilization methods for 1D Saint-Venant equations coupled with a floating object. During my internship and Ph.D., I implemented the monolithic subcell DG/FV convex property preserving schemes for 1D Saint-Venant equations. One of the main goals of my future work is to implement them for the two-dimensional case with a floating object.

For more informations, contact [Fabien Marche](https://imag.umontpellier.fr/~marche/).

***

<b> EasyDG4SCL </b>  <br>
<i> Keywords. </i> Discontinuous Galerkin, Scalar Conservation Laws. <br>
<i> Language. </i> C++. 

During the early stages of my internship with F. Vilar and F. Marche, I embarked on the development of a small C++ code focused on addressing Discontinuous Galerkin (DG) schemes for 1D conservation laws. 
This code is a work in progress, far from being complete or flawless. Its creation was driven by my commitment to simplicity and understandability. I strived to ensure that the code's structure and implementation were as straightforward as possible, enabling users to grasp the underlying concepts with ease.
By expanding its functionality and making it more comprehensive, I aim to create a valuable resource for students seeking a simplified example of DG schemes. This endeavor stems from my own experiences as a student, where access to such a resource would have greatly facilitated my understanding and learning process.

Contact me to get the source.

