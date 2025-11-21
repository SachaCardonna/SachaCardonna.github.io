---
permalink: /
title: "Hello there! <span style=\"font-family: monospace; font-weight: 600;\">☺</span>"
excerpt: "Hello there! <span style=\"font-family: monospace; font-weight: 600;\">☺</span>"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I'm a Ph.D. student in Mathematics, under the supervision of [François Vilar](https://vilar.perso.math.cnrs.fr) & [Fabien Marche](https://imag.umontpellier.fr/~marche/) at [Institut Montpelliérain Alexander Grothendieck](https://imag.umontpellier.fr) (IMAG - UMR 5149).

I'm also a teaching assistant for the Department of Mathematics at [Montpellier Faculty of Sciences](https://sciences.edu.umontpellier.fr) & [Polytech Montpellier Engineering School](https://www.polytech.umontpellier.fr).

## Research interests

During my thesis, I design and implement arbitrary-order finite elements methods for partial differential equations arising in the modeling of water waves and wave–structure interactions. For instance, one of the systems I have studied extensively is the nonlinear shallow water equations (NSW), which represent a nonlinear hyperbolic system with source term: 
<div style="text-align: center;">
$$
\begin{cases}
      \partial_t\:\!\eta + \nabla_{\!\mathbf{x}} \cdot \mathbf{q} = \mathbf{S}_1[b](\mathbf{v}), \\
      \partial_t \:\!\mathbf{q} + \nabla_{\!\mathbf{x}} \cdot \left( \mathbf{u} \otimes \mathbf{q} + \frac{g\eta}{2}(\eta - 2b)\mathbb{I}_2  \right) = \mathbf{S}_2[b](\mathbf{v}),
\end{cases} \nonumber
$$
</div>
with $\mathbf{v} = (\eta,\mathbf{q})^t$, where $\eta$ is water total elevation, $\mathbf{q}$ is the horizontal discharge, $b$ a smooth parametrization of topography and $\mathbf{S}\[b\](\mathbf{v})$ is a generic source term that may contains topography, friction and/or Coriolis effects.
Visitors can find some numerical results and simulation in [Softwares](https://sachacardonna.github.io/codes).

More generally, I am interested in modeling and numerical analysis of partial differential equations (PDEs), and their applications to physics problems, mainly fluid mechanics.

- <b>Modeling</b>. Conservation laws, non-linear hyperbolic systems, dispersive equations, elliptic equations, models coupling...
- <b>Numerical analysis</b>. Finite elements & discontinuous Galerkin methods, finite volume schemes, monolithic DG-FV subcells & hybrid high-order methods, well-balancing, entropy-preserving schemes, ALE approaches...
- <b>Scientific computing</b>. Object oriented and generic programming, parallel computing...
- <b>Applications</b>. Fluid mechanics, nonlinear shallow water equations, Green-Naghdi equations, wave-structure interactions...

## News & highlights

- I have been invited to give a talk at [CJC-MA26](https://cjcma2026.sciencesconf.org) during the special session "Ocean", funded by the [RTTE](https://rtte.math.cnrs.fr/).
- I will be visiting the [RAPSODI](https://www.inria.fr/fr/rapsodi) team in Lille in December, kindly invited by my friend [Marien Hanot](https://marienhanot.fr).
- I talked about high-order monolithic methods at [ICOSAHOM 2025](https://icosahom2025.org) in Montréal, see the [slides]({{ site.url }}/files/talks/ICOSAHOM.pdf).
- During [MIPS Week](https://www.umontpellier.fr/agenda/semaine-du-pole-mips), I talked about some aspects of modeling and scientific computing to non-experts scientists, see the [presentation]({{ site.url }}/files/talks/MIPS.pdf). 
- Made a presentation at the [CIMAV 2025](https://cimav2025.sciencesconf.org) conference in May, held in Aussois, see the [beamer]({{ site.url }}/files/talks/CIMAV.pdf). 


