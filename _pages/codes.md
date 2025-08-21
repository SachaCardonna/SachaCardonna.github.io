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

<b> WaveBox - Multi-models C++ numerical platform for water-waves equations </b>  <br>
<i> Keywords. </i> DG, HDG, Saint-Venant, Boussinesq, Green-Naghdi, Finite-Volume subcells methods. <br>
<i> Language. </i> C++, Python (visualization).

WaveBox is a multi-models numerical platform created by Fabien Marche, dedicated to the approximations of the solutions of several shallow water asymptotics in the surface dimension d = 2 with efficient combined Hybridized Discontinuous Galerkin (HDG), Hybrid High Order (HHO), Monolithic DG-FV subcells and DG methods on general unstructured meshes (for Saint-Venant, Boussinesq and Green-Naghdi equations). Main features are: 
- Sub-models CPU-GPU co-processing;
- Arbitrary order of accuracy (h and p-adaptivity);
- Robust treatment of the run-up and flooding processes (strict maximum-principle enforcement);
- Well-balancing for motionless steady states;
- Unstructured meshes & mesh subdivision;
- Wave breaking treatment with dynamic switching strategy.

During my Ph.D., I developped a whole new section dedicated to high-order monolithic DG-FV schemes, with grid subdivisions and a priori stabilization methods, in 1D & 2D. I also developped several vizualization tools on Python. One of the main goals of our future work is to implement monolithic schemes on NSW coupled with a floating object.

Some numerical simulations: 
- $\mathbb{P}^6$ interaction between a collapsing wave and a rock ([MP4]({{ site.baseurl }}/images/rock_wave_P6.mp4))
- $\mathbb{P}^2$ interaction between a tidal wave and a rock ([AVI]({{ site.baseurl }}/images/tidal_P2.avi))
- $\mathbb{P}^4$ dam-break on a wet bed ([AVI]({{ site.baseurl }}/images/wet_dam_break_P4.avi))
<!-- - $\mathbb{P}^2$ Carrier-Greenspan periodic solution ([AVI]({{ site.baseurl }}/images/cg_periodic_P2.avi)) -->
- $\mathbb{P}^2$ tsunami on three conical islands ([MP4]({{ site.baseurl }}/images/tsunami_P2.mp4))
- $\mathbb{P}^3$ Green-Naghdi 1D dam-break with dispersive shock ([GIF]({{ site.baseurl }}/images/GN_dispersive.gif))
- $\mathbb{P}^3$ motion-prescribed floating object interactions ([GIF]({{ site.baseurl }}/images/1d_boat.gif))

<div style="display: flex; justify-content: space-between; gap: 7px;">
      <img src="{{ site.baseurl }}/images/1d_boat.gif" alt="WaveBox Image 2" style="width: 23%; height: auto;">
      <img src="{{ site.baseurl }}/images/tidal_P2.gif" alt="WaveBox Image 1" style="width: 48%; height: auto;">
      <img src="{{ site.baseurl }}/images/GN_dispersive.gif" alt="WaveBox Image 3" style="width: 23%; height: auto;">
</div>

***

<b> DG4SCL - Compact and student friendly code for DG methods on 1D SCL </b>  <br>
<i> Keywords. </i> Discontinuous Galerkin, Scalar Conservation Laws. <br>
<i> Language. </i> C++. 

During the early stages of my internship with F. Vilar and F. Marche, I embarked on the development of a compact C++ code focused on addressing Discontinuous Galerkin (DG) schemes for 1D conservation laws. 
This code is a work in progress, far from being complete or flawless. Its creation was driven by my commitment to simplicity and understandability. I strived to ensure that the code's structure and implementation were as straightforward as possible, enabling users to grasp the underlying concepts with ease.
By expanding its functionality and making it more comprehensive, I aim to create a valuable resource for students seeking a simplified example of DG schemes. This endeavor stems from my own experiences as a student, where access to such a resource would have greatly facilitated my understanding and learning process.

Contact me to get the source.

![DG4SCL Simulation]({{ site.baseurl }}/images/dg_lcs.png)
