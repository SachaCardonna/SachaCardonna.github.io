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

<style>
  details.pub {
    position: relative;
    background-color: rgba(0, 0, 0, 0.03);
    border-radius: 6px;
    padding: 0.6em 0.8em 0.6em 3.1em;
    margin-bottom: 0.9em;
  }
  details.pub[open] { background-color: rgba(0, 0, 0, 0.05); }

.pub-badge {
  position: absolute;
  top: 0.65em;
  left: 0.6em;
  text-align: center;
  font-size: 0.8em;
  line-height: 1.1;
  opacity: 0.7;
}

.pub-badge .num { font-weight: 700; }
.pub-badge .year { font-size: 0.9em; }

/* Arrow */
.pub-badge .arrow {
  display: inline-block;
  margin-top: 0.15em;
  font-size: 0.9em;
  transition: transform 0.25s ease;
}

/* Rotate arrow when open */
details[open] .pub-badge .arrow {
  transform: rotate(90deg);
}

  summary.pub-summary {
    cursor: pointer;
    font-weight: normal;
    list-style: none;
  }
  summary.pub-summary::-webkit-details-marker { display: none; }

  .pub-line {
    display: flex;
    flex-direction: column;
    gap: 0.1em;
  }
  summary.pub-summary {
  padding: 0.6em 0.8em 0.6em 3.1em;
}

  .pub-authors {
  font-weight: 400;
  font-size: 0.9em;
  opacity: 0.9;
}
  .pub-title { font-weight: 700; }
  .pub-authors {
  font-weight: 400;
  font-size: 0.9em;
  opacity: 0.9;
}

  .pub-links {
    margin-top: 0.45em;
    display: flex;
    flex-wrap: wrap;
    gap: 0.5em 0.7em;
  }
  .pub-links a {
    text-decoration: none;
    border-bottom: 1px dotted rgba(0,0,0,0.35);
  }

  .pub-grid-2 {
    margin-top: 0.7em;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }
  .pub-grid-3 {
    margin-top: 0.7em;
    display: grid;
    grid-template-columns: 1fr 1.35fr 1fr;
    gap: 10px;
  }
  .pub-grid-2 img, .pub-grid-3 img {
    width: 100%;
    height: auto;
    border-radius: 6px;
    display: block;
  }

  .pub-abstract {
    margin-top: 0.55em;
    line-height: 1.35;
  }
</style>

<details class="pub">
  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">3</div>
    <div class="year">2026</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors">S. Cardonna, D. Lannes, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">Numerical resolution of 2D nonlinear shallow-water equations with a partly immersed surface obstacle</span>
      <span class="pub-tail"><i>In preparation</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
    Work in progress on a 2D wave–structure interaction model and its numerical resolution.
  </div>

  <div class="pub-links">
    <a href="#">PDF</a>
    <a href="#">HAL</a>
  </div>
</details>

<details class="pub">
  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">2</div>
    <div class="year">2025</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors">S. Cardonna, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">An high-order robust scheme for 2D nonlinear shallow water equations with topography and friction effects on unstructured grids</span>
      <span class="pub-tail"><i>Submitted</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
We introduce monolithic DG–FV subcell convex property preserving schemes for the 2D nonlinear shallow-water equations. The method is based on a high-order DG formulation interpreted as a FV-like scheme on a sub-partition with reconstructed interface fluxes. Blended fluxes are used at each time step and subcell interface to enforce key convex properties, including a discrete maximum principle and water-height positivity. The scheme is well-balanced at the subcell level for motionless steady states, provided suitable reconstructions of local mean values. Numerical experiments confirm the ability of the method to control nonphysical oscillations, preserve positive mean water height and satisfy cell and subcell entropy inequalities.
  </div>

  <div class="pub-links">
    <a href="#">PDF</a>
    <a href="#">HAL</a>
  </div>

  <div class="pub-grid-2">
    <img src="{{ site.baseurl }}/images/tsunami2d_2.png">
    <img src="{{ site.baseurl }}/images/tsunami2d_theta.png">
  </div>
</details>

<details class="pub">

  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">1</div>
    <div class="year">2025</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors">S. Cardonna, A. Haidar, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">Local subcell monolithic DG/FV methods for nonlinear shallow-water models with source terms</span>
      <span class="pub-tail"><i>Submitted</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
We propose a high-order local subcell monolithic DG–FV method for nonlinear shallow-water equations with source terms, covering both Saint-Venant and Green–Naghdi models. The approach relies on a DG formulation interpreted as a FV scheme on a sub-partition with reconstructed high-order interface fluxes. Source terms, including bathymetry and dispersive corrections, are discretized at the subcell level using a priori blended fluxes that enforce convex properties such as water-height positivity. A well-balanced property preserving motionless steady states is proved at the subcell scale. The method is coupled with a high-order interior-penalty DG scheme for the dispersive terms and is validated through extensive numerical tests demonstrating convergence, robustness, positivity preservation and suppression of nonphysical oscillations.
  </div>

  <div class="pub-links">
    <a href="#">PDF</a>
    <a href="#">HAL</a>
  </div>

  <div class="pub-grid-3">
    <img src="{{ site.baseurl }}/images/1d_2.png">
    <img src="{{ site.baseurl }}/images/dispersive.png">
    <img src="{{ site.baseurl }}/images/1d_3.png">
  </div>
</details>


<!-- ________________________________ -->

## Talks & posters
<hr style="margin-top: -0.1em; margin-bottom: 1em;">
<b>[ICOSAHOM](https://icosahom2025.org/index.html) - International Congress on Spectral and High Order Method</b> <br>
<i>Title</i>. Local subcell monolithic DG/FV scheme for NSW equations with source terms on unstructured grids. <br>
<i>Location</i>. Montréal, Canada. <br>
<i>Date</i>. 14/07/25.<br> 
[[Slides]({{ site.url }}/files/talks/ICOSAHOM.pdf)]

<b>[MIPS Colloquia](https://www.umontpellier.fr/agenda/semaine-du-pole-mips) - Semaine du pôle Mathématiques, Informatique, Physique, Systèmes</b> <br>
<i>Title</i>. Designing numerical methods for free-surface flows towards reliable wave-structure interactions. <br>
<i>Location</i>. Montpellier, France. <br>
<i>Date</i>. 02/06/25.<br> 
[[Slides]({{ site.url }}/files/talks/MIPS.pdf)]

<b>[CIMAV](https://cimav2025.sciencesconf.org) - Congrès Interdisciplinaire sur les Modèles Avancés de Vagues</b><br>
<i>Title</i>. An high-order robust DG/FV scheme for nonlinear shallow water equations with source terms on unstructured grids. <br>
<i>Location</i>. Aussois, France. <br>
<i>Date</i>. 13/05/25.<br> 
[[Slides]({{ site.url }}/files/talks/CIMAV.pdf)]

<b>Ph.D. Day - Séminaire des Doctorants</b> <br>
<i>Title</i>. Monolithic DG/FV schemes on 1D nonlinear shallow water equations. <br>
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

Among the many examples of such systems, the nonlinear shallow-water equations (NSW) play a central role in the water wave community; they provide an asymptotic model derived from the incompressible Euler equations under the assumption of small aspect ratio (the depth of the fluid is much smaller than the horizontal scale). Despite their asymptotic nature, the shallow water equations remain extremely valuable in practice. They provide an accurate description of the main physical mechanisms governing free-surface flows, while avoiding the prohibitive computational cost associated with solving the fully three-dimensional Euler or Navier–Stokes equations. They thus offer an effective compromise between physical realism and numerical efficiency. Even though they do not account for dispersive effects (captured in more refined models such as the Boussinesq or Green–Naghdi systems), they remain one of the most widely used and robust approximations for practical flow simulations.
Given a smooth parameterization $b$ of the bathymetry variation, the NSW equations read as
<div style="text-align: center;">
$$
\begin{cases}
      \partial_t\:\!\eta + \nabla_{\!\mathbf{x}} \cdot \mathbf{q} = \mathbf{S}_1[b](\mathbf{v}), \\
      \partial_t \:\!\mathbf{q} + \nabla_{\!\mathbf{x}} \cdot \left( \mathbf{u} \otimes \mathbf{q} + \frac{g\eta}{2}(\eta - 2b)\mathbb{I}_2  \right) = \mathbf{S}_2[b](\mathbf{v}),
\end{cases} \nonumber
$$
</div>
with $\mathbf{v} = (\eta,\mathbf{q})^t$, where $\eta$ is water total elevation, $\mathbf{q}$ is the horizontal discharge, and $\mathbf{S}\[b\](\mathbf{v})$ is a generic source term that may contains topography, friction and/or Coriolis effects.

From a numerical viewpoint, however, their discretization poses several challenges. Capturing both smooth solutions and discontinuities requires schemes that are stable in the presence of shocks, preserve the positivity of the water height ($i.e.$ ensuring at the discrete level that $H\geq0$), and maintain steady states such as the so-called “lake-at-rest” equilibrium. Moreover, in many realistic configurations, the flow interacts with complex geometries, obstacles, or moving boundaries, which demands robust and flexible numerical frameworks.

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