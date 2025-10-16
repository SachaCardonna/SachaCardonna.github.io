---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Explore my publications, the talks and conferences I participated in and my research interests.

## Publications
<hr style="margin-top: -0.1em; margin-bottom: 1em;">
<ol reversed>
  <li>
    S. Cardonna, F. Marche & F. Vilar - <b>Local monolithic DG-FV subcell correction for 2D NSW on unstructured grids</b>, <i>in preparation</i>.
    <div style="display: flex; justify-content: space-between; gap: 10px;">
      <img src="{{ site.baseurl }}/images/tsunami2d_2.png" alt="WaveBox Image 1" style="width: 48%; height: auto;">
      <img src="{{ site.baseurl }}/images/tsunami2d_theta.png" alt="WaveBox Image 3" style="width: 48%; height: auto;">
    </div>
  </li>
  <li>
    S. Cardonna, A. Haidar, F. Marche & F. Vilar - <b>Monolithic DG-FV subcell schemes for nonlinear hyperbolic system with source terms. Applications to shallow water asymptotics</b>, <i>in preparation</i>.
    <div style="display: flex; justify-content: space-between; gap: 10px;">
      <img src="{{ site.baseurl }}/images/1d_1.png" alt="WaveBox Image 1" style="width: 23%; height: auto;">
      <img src="{{ site.baseurl }}/images/1d_2.png" alt="WaveBox Image 2" style="width: 23%; height: auto;">
      <img src="{{ site.baseurl }}/images/1d_3.png" alt="WaveBox Image 3" style="width: 23%; height: auto;">
      <img src="{{ site.baseurl }}/images/1d_4.png" alt="WaveBox Image 4" style="width: 23%; height: auto;">
    </div>
  </li>
</ol>

## Talks & posters
<hr style="margin-top: -0.1em; margin-bottom: 1em;">
<b>ICOSAHOM - International Congress on Spectral and High Order Method</b> <br>
<i>Title</i>. Local subcell monolithic DG/FV scheme for NSW equations with source terms on unstructured grids. <br>
<i>Location</i>. Montréal, Canada. <br>
<i>Date</i>. 14/07/25.<br> 
[[Slides]({{ site.url }}/files/talks/ICOSAHOM.pdf)]

<b>MIPS Colloquia - Semaine du pôle Mathématiques, Informatique, Physique, Systèmes</b> <br>
<i>Title</i>. Designing numerical methods for free-surface flows towards reliable wave-structure interactions. <br>
<i>Location</i>. Montpellier, France. <br>
<i>Date</i>. 02/06/25.<br> 
[[Slides]({{ site.url }}/files/talks/MIPS.pdf)]

<b>CIMAV - Congrès Interdisciplinaire sur les Modèles Avancés de Vagues</b><br>
<i>Title</i>. An high-order robust DG/FV scheme for nonlinear shallow water equations with source terms on unstructured grids. <br>
<i>Location</i>. Aussois, France. <br>
<i>Date</i>. 13/05/25.<br> 
[[Slides]({{ site.url }}/files/talks/CIMAV.pdf)]

<b>Ph.D. Day - Séminaire des Doctorants</b> <br>
<i>Title</i>. Monolithic DG/FV schemes on 1D Nonlinear Shallow-Water <br>
<i>Location</i>. Montpellier, France. <br>
<i>Date</i>. 15/03/24.<br>
[[Poster]({{ site.url }}/files/talks/poster_phd_day24.pdf)]

<b>Introduction to newcomers - Séminaire des Doctorants</b> <br>
<i>Title</i>. Modeling, solving & implementing PDEs from waves-structure interactions. <br>
<i>Location</i>. Montpellier, France. <br>
<i>Date</i>. 25/10/23.<br>
[[Slides]({{ site.url }}/files/talks/SEMDOC.pdf)]


## Research statement
<hr style="margin-top: -0.1em; margin-bottom: 1em;">
 My research lies at the intersection of mathematical modeling, numerical analysis, and the study of partial differential equations (PDEs) describing fluid flows. In particular, during my PhD, I focused on nonlinear systems of hyperbolic balance laws, which are used to model the evolution of quantities that are transported and conserved in time. These systems take the general form
<div style="text-align: center;">
$$
\partial_t \mathbf{U}(\mathbf{x},t) + \nabla_{\!\mathbf{x}} \cdot \mathbb{F}(\mathbf{U}) = \mathbf{S}(\mathbf{U}, \mathbf{x},t),
$$
</div>
where $\mathbf{U}$ represents the vector of conserved variables (our unknowns), $\mathbb{F}$ the flux function that can be nonlinear, and $\mathbf{S}$ possible source terms arising from geometry, external forces, or coupling effects. The mathematical challenge is that even smooth initial data can generate discontinuities in finite time, which makes the analytical study of such systems extremely delicate. Because of the lack of regularity of weak solutions, only partial theoretical results are available, and the numerical approximation of these phenomena must often combine high-order accuracy with stability and robustness.

Among the many examples of such systems, the nonlinear shallow-water equations (NSW) play a central role in the water wave community; they provide an asymptotic model derived from the incompressible Euler equations under the assumption of small aspect ratio (the depth of the fluid is much smaller than the horizontal scale). In two horizontal dimensions, given a smooth parameterization $b$ of the bathymetry variation, denoting the free surface elevation by $\eta$, the water discharge by $\mathbf{q} = (q_x,q_y)^\top$, $\mathbf{u} = (u_x,u_y)^\top$ as the depth-averaged water velocity, and $g$ as the gravitational constant, the 2D NSW equations can be written as follows 
<div style="text-align: center;">
$$
    \partial_t \mathbf{v} + \nabla_{\!\mathbf{x}}\cdot \mathbb{F}(\mathbf{v}, b) = \mathbf{S}[b](\mathbf{v}) \quad \Leftrightarrow \quad
	\begin{cases}
	\partial_t \eta + \nabla_{\!\mathbf{x}}\cdot \mathbf{q} = 0, \\ 
	\partial_t \mathbf{q} + \nabla_{\!\mathbf{x}}\cdot \left( \mathbf{u} \otimes \mathbf{q} +\frac{g\eta}{2}(\eta-2b) \mathbb{I}_2 \right) = -g\eta\nabla_{\!\mathbf{x}} b,
	\end{cases}
$$
</div>
supplemented with some initial-data $\mathbf{v}(\cdot,0):= \mathbf{v}^0$ and where:

- $\mathbb{R}^2\times\mathbb{R}_+ \ni (\mathbf{x},t) \mapsto \mathbf{v}(\mathbf{x},t):= (\eta, q_x,q_y)(\mathbf{x},t)\in \mathcal{H}_b^+$ gathers the chosen flow description variables, with $\mathcal{H}_b^+ =\left{(\eta,q_x,q_y)\in\mathbb{R}^3 \mid H:=\eta-b\geq0\right},$
ensuring the well-posedness of the model by restricting $\mathbf{v}$ to the admissible set $\mathcal{H}_b^+$ where the water height $H$ remains non-negative,
- $\mathcal{H}_b^+\times\mathbb{R} \ni (\mathbf{v}, b)\mapsto \mathbb{F} (\mathbf{v}, b):= \left( \mathbf{q} , \, \mathbf{u} \otimes \mathbf{q} +\frac{g\eta}{2}(\eta-2b) \mathbb{I}_2\right)^\top \in \mathcal{M}_{3\times 2}(\mathbb{R})$ is the (nonlinear) flux function,
- $\mathcal{H}_b^+\ni \mathbf{v} \mapsto \mathbf{S}[b](\mathbf{v}):= (0, -g\eta\partial_x b, -g\eta\partial_y b)^\top \in \mathbb{R}^3$ stands for the bathymetry source term.

Despite their asymptotic nature, the shallow water equations remain extremely valuable in practice. They provide an accurate description of the main physical mechanisms governing free-surface flows, while avoiding the prohibitive computational cost associated with solving the fully three-dimensional Euler or Navier–Stokes equations. They thus offer an effective compromise between physical realism and numerical efficiency. Even though they do not account for dispersive effects (captured in more refined models such as the Boussinesq or Green–Naghdi systems), they remain one of the most widely used and robust approximations for practical flow simulations. 

From a numerical viewpoint, however, their discretization poses several challenges. Capturing both smooth solutions and discontinuities requires schemes that are stable in the presence of shocks, preserve the positivity of the water height ($i.e.$ ensuring at the discrete level that $H\geq0$, s.t. $\mathbf{v}\in\mathcal{H}_b^+$), and maintain steady states such as the so-called “lake-at-rest” equilibrium. Moreover, in many realistic configurations, the flow interacts with complex geometries, obstacles, or moving boundaries, which demands robust and flexible numerical frameworks.

### New high-order numerical frameworks for shallow water asymptotics
In the numerical analysis of nonlinear shallow water models, two main families of methods coexist. On one hand, classical finite volume (FV) schemes are extremely robust: they are able to handle naturally shocks, dry areas, and abrupt variations of topography without breaking down. However, they usually provide initially low-order accuracy and tend to be too diffusive. On the other hand, finite element methods, in particular discontinuous Galerkin (DG) formulations, can reach arbitrarily high orders of precision and are well-suited for complex geometries, but they are much more sensitive to numerical instabilities and require additional stabilization mechanisms to ensure robustness.

The numerical strategy I have developed aims at combining the best of both worlds within a single and consistent framework. Building on a method initially introduced by my advisor François Vilar, we reformulated the computational domain by subdividing each mesh element into subcells and allowing both FV and DG representations to coexist locally, making it possible to merge two normally incompatible paradigms within a unified structure. Through a convex blending between the finite volume contributions (responsible for robustness) and the high-order DG ones (responsible for accuracy), the method dynamically adapts to the local regularity of the solution. It ensures that the scheme remains positivity-preserving, stable around steady states, and accurate in smooth regions.

This framework was first developed and analyzed in the one-dimensional setting, in a work focusing on the construction of the method and on the preservation of some key theoretical properties. 
In this first article, we also proposed a natural extension of the approach to the Green–Naghdi equations, which form a dispersive correction to the NSW system.
Indeed, in that setting, the dispersive effects are reformulated as an auxiliary elliptic problem that introduces an additional source term in the NSW equations. One of the main strengths of the proposed framework lies precisely in the treatment of such source terms: the method handles them in a consistent and unified way, without the need for additional numerical artifacts. The elliptic part is solved using a SWIP-DG (Symmetric Weighted Interior Penalty Discontinuous Galerkin) method, ensuring stability and precision. This coupling strategy yields a high-order dispersive model capable of capturing Green–Naghdi-type solutions with excellent accuracy and stability, while preserving the simplicity and robustness of the shallow water solver.

More recently, this monolithic approach has been extended to two-dimensional unstructured meshes. The extension of the framework to two-dimensional configurations represents a major step forward, both technically and theoretically. The proposed formulation successfully addresses these difficulties and exhibits excellent numerical properties: it achieves high-order accuracy even on coarse and highly irregular meshes, while maintaining robustness in the presence of complex bathymetries, dry fronts and challenging benchmarks. These results confirm the versatility and efficiency of the approach, making it a promising tool for large-scale realistic simulations of shallow water flows.

### Floating structures in shallow water regimes
The increasing demand for renewable marine energy has motivated the study of floating devices capable of converting wave motion into electricity. From a mathematical viewpoint, these systems involve complex fluid–structure interactions, where the dynamics of a floating body must be coupled with the free-surface flow. In collaboration with David Lannes, we are developing a unified theoretical and numerical framework to describe such interactions within an asymptotic shallow-water regime, aiming for both mathematical consistency and computational efficiency.

The resulting model combines three complementary components: a hyperbolic system governing the exterior flow (the nonlinear shallow-water equations), a set of ordinary differential equations, and an elliptic problem describing the internal pressure distribution. Building a stable and accurate solver for this coupled system requires treating these components within a single, coherent formulation that preserves the main physical and mathematical invariants.

To achieve this, we rely on the DG/FV framework introduced in the previous section for the hyperbolic part, and on advanced discretizations for the elliptic component based on Hybrid High-Order (HHO) methods, which are finite-element-like schemes combining cell and face unknowns to achieve high-order accuracy while retaining local conservation, computational efficiency and flexibility on very general meshes. This ongoing work constitutes the third main contribution of my thesis. It provides a mathematically well-posed and numerically efficient framework for the simulation of wave–structure interactions in shallow-water regimes, with potential applications to the study and optimization of wave energy converters and other floating systems relevant to renewable marine technologies.