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

During my thesis, I work on Shallow-Water equations, which represent a nonlinear hyperbolic system with source term: 
<div style="text-align: center;">
$$
\partial_t\textbf{V}+\nabla \cdot \textbf{F}=\textbf{B} \Leftrightarrow \begin{cases}
      \partial_t \eta + \partial_x q_x + \partial_y q_y = 0, \\
      \partial_t \mathbf{q} + \nabla \cdot \left[ \mathbf{u} \otimes \mathbf{q} + \frac{1}{2}g\eta(\eta - 2b)\mathbf{I}_2  \right] = -g\eta \nabla b,
    \end{cases} \nonumber
$$
</div>
with $\textbf{V}=(\eta,q_x,q_y)^T$, where $\eta$ is water total elevation, $\textbf{q}=(q_x,q_y)^T$ is the horizontal discharge, $\textbf{B}$ the topography source term, and $\textbf{F}$ being the nonlinear flux function.

More generally, I am interested in theoretical and numerical analysis of partial differential equations (PDEs), and their applications to physics problems, mainly fluid mechanics.

- <b>Models</b>. Conservation laws, non-linear hyperbolic systems of PDEs, models coupling.
- <b>Numerics</b>. Discontinuous Galerkin & Finite-Volume schemes, well-balanced schemes, ALE approaches.
- <b>Applications</b>. Fluid mechanics, nonlinear Shallow-Water equations, dispersive PDEs.
- <b>Scientific computing</b>. Object oriented and generic programming, parallel computing.

Highlights
======
- I presented my work on Monolithic DG/FV schemes for 1D Nonlinear Shallow-Water in a poster session during IMAG Ph.D. Day the 20/03, see [Posters](https://sachacardonna.github.io/talks).
- I introduced applied mathematics to high-schoolers during MathC2+ program, see [Teaching](https://sachacardonna.github.io/teaching) for more details.
