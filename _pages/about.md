---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I'm a Ph.D. student in Mathematics, under the supervision of [François Vilar](https://vilar.perso.math.cnrs.fr) & [Fabien Marche](https://imag.umontpellier.fr/~marche/) at [Institut Montpelliérain Alexander Grothendieck](https://imag.umontpellier.fr) (IMAG - UMR 5149).

I'm also a teaching assistant for the Department of Mathematics at [Montpellier Faculty of Sciences](https://sciences.edu.umontpellier.fr) & [Polytech Montpellier Engineering School](https://www.polytech.umontpellier.fr).

Research interests
======

During my thesis, I design and implement arbitrary-order methods for partial differential equations arising in the modeling of water waves and wave–structure interactions. For instance, one of the systems I have studied extensively is the nonlinear shallow water equations (NSW), which represent a nonlinear hyperbolic system with source term: 
<div style="text-align: center;">
$$
\begin{cases}
      \partial_t \eta + \nabla_{\mathbf{x}} \cdot \mathbf{q} = 0, \\
      \partial_t \mathbf{q} + \nabla_{\mathbf{x}} \cdot \left( \mathbf{u} \otimes \mathbf{q} + \frac{g\eta}{2}(\eta - 2b)\mathbb{I}_2  \right) = -g\eta \nabla_{\mathbf{x}} b,
\end{cases} \nonumber
$$
</div>
where $\eta$ is water total elevation, $\mathbf{q}=(q_x,q_y)^T$ is the horizontal discharge, and $\mathbf{B} = (0, -g\eta \nabla_{\mathbf{x}} b)^T$ the topography source term. 
Visitors can find some numerical results and simulation in [Softwares](https://sachacardonna.github.io/codes).

More generally, I am interested in modeling and numerical analysis of partial differential equations (PDEs), and their applications to physics problems, mainly fluid mechanics.

- <b>Modeling</b>. Conservation laws, non-linear hyperbolic systems, dispersive equations, elliptic equations, models coupling...
- <b>Numerical analysis</b>. Finite elements & discontinuous Galerkin methods, finite volume schemes, monolithic DG-FV subcells & hybrid high-order methods, well-balancing, entropy-preserving schemes, ALE approaches...
- <b>Scientific computing</b>. Object oriented and generic programming, parallel computing...
- <b>Applications</b>. Fluid mechanics, nonlinear shallow water equations, Green-Naghdi equations, wave-structure interactions...

News
======
- I will present my work at [ICOSAHOM 2025](https://icosahom2025.org) in July, which will take place in Montréal, Canada.
- I made a presentation at the [CIMAV 2025](https://cimav2025.sciencesconf.org) conference in May, held in Aussois, see the [slides]({{ site.url }}/files/talks/CIMAV.pdf). 
- I started writing my first articles, in collaboration with A. Haidar and my thesis directors, see [Research](https://sachacardonna.github.io/research) for more details. 


