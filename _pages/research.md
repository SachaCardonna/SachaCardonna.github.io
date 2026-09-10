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

<p class="publication-lead-note"><span class="publication-lead-mark" aria-hidden="true">*</span><span>An asterisk identifies the lead author, when applicable.</span></p>

<style>
  details.pub {
    position: relative;
    background: var(--content-soft);
    border: 1px solid var(--content-line);
    border-radius: 11px;
    padding: 0.8em 0.9em 0.8em 3.25em;
    margin-bottom: 0.9em;
  }
  details.pub[open] { border-color: rgba(127,127,127,.36); background: rgba(127,127,127,.08); }

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
details.pub[open] > summary .pub-badge .arrow {
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
    display: inline-flex;
    align-items: center;
    min-height: 38px;
    padding: .42rem .82rem;
    border: 1px solid var(--global-link-color);
    border-radius: 999px;
    color: var(--global-link-color);
    font-size: .72rem;
    font-weight: 600;
    text-decoration: none;
    transition: transform .18s ease, background .18s ease;
  }
  .pub-links a:hover { transform: translateY(-1px); background: var(--content-soft); }

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
  grid-template-rows: 200px;  /* ← AJOUT : hauteur fixe pour la ligne */
  gap: 10px;
}

.pub-grid-2 img, .pub-grid-3 img {
  width: 100%;
  height: 100%;           /* ← CHANGÉ : de 'auto' à '100%' */
  object-fit: cover;      /* ← AJOUT : crop sans déformation */
  object-position: center;/* ← AJOUT : centre le crop */
  border-radius: 6px;
  display: block;
}


  .pub-abstract {
    width: 100%;
    max-width: none;
    box-sizing: border-box;
    margin-top: 0.85rem;
    padding-top: 0.8rem;
    border-top: 1px solid var(--content-line);
    color: var(--global-text-color-light);
    font-size: 0.72rem;
    line-height: 1.68;
    text-wrap: pretty;
    hyphens: auto;
  }
  .pub-abstract::before {
    content: "Abstract";
    display: block;
    margin-bottom: 0.42rem;
    color: var(--global-link-color);
    font-size: 0.61rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }
  .pub-abstract br {
    display: block;
    content: "";
    margin-top: 0.72rem;
  }
  @media (max-width: 600px) {
    .pub-abstract { font-size: 0.74rem; line-height: 1.62; }
  }

  /* Editorial publication cards */
  details.pub {
    padding: 0;
    margin-bottom: .5rem;
    overflow: hidden;
    border: 1px solid var(--content-line);
    border-radius: 12px;
    background: var(--global-bg-color);
    box-shadow: none;
    transition: border-color .18s ease, box-shadow .18s ease, transform .18s ease;
  }
  details.pub:hover {
    border-color: rgba(127,127,127,.4);
    box-shadow: 0 7px 20px rgba(0,0,0,.055);
    transform: translateY(-1px);
  }
  details.pub[open] {
    border-color: var(--content-line);
    border-left: 3px solid var(--global-link-color);
    background: var(--global-bg-color);
    box-shadow: 0 8px 24px rgba(0,0,0,.055);
    transform: none;
  }
  summary.pub-summary {
    display: grid;
    grid-template-columns: 2.5rem minmax(0,1fr);
    gap: .55rem;
    align-items: start;
    padding: .52rem .9rem;
  }
  details.pub[open] summary.pub-summary {
    border-bottom: 1px solid var(--content-line);
  }
  .pub-badge {
    position: static;
    padding-top: .05rem;
    color: var(--content-muted);
    font-size: .65rem;
    opacity: 1;
  }
  .pub-badge .num {
    color: var(--global-link-color);
    font-size: .76rem;
    font-weight: 800;
  }
  .pub-badge .year {
    margin-top: .12rem;
    font-size: .6rem;
  }
  .pub-badge .arrow {
    margin-top: .3rem;
    color: var(--global-link-color);
    font-size: .82rem;
  }
  .pub-line { gap: .18rem; }
  .pub-authors {
    color: var(--content-muted);
    font-size: .67rem;
    opacity: 1;
  }
  .pub-title {
    color: var(--global-text-color);
    font-size: .8rem;
    font-weight: 750;
    line-height: 1.42;
  }
  .pub-tail {
    margin-top: .08rem;
    color: var(--global-link-color);
    font-size: .63rem;
    font-weight: 650;
  }
  .pub-abstract {
    width: auto;
    margin: .72rem 1rem 0;
    padding: 0;
    border: 0;
    color: var(--global-text-color);
    font-size: .72rem;
    line-height: 1.68;
  }
  .pub-abstract::before {
    content: "Abstract";
    margin-bottom: .35rem;
    font-size: .6rem;
  }
  .pub-grid-2,
  .pub-grid-3 {
    margin: .7rem 1rem 0;
    gap: .55rem;
  }
  .pub-grid-2 img,
  .pub-grid-3 img {
    border: 1px solid var(--content-line);
    border-radius: 9px;
  }
  details.pub > .pub-grid-2:last-child,
  details.pub > .pub-grid-3:last-child { margin-bottom: .75rem; }
  .pub-links {
    margin: .65rem 1rem .75rem;
  }
  .pub-links a {
    min-height: 34px;
    padding: .34rem .75rem;
    font-size: .68rem;
  }
  @media (max-width: 600px) {
    summary.pub-summary {
      grid-template-columns: 2rem minmax(0,1fr);
      gap: .55rem;
      padding: .5rem .72rem;
    }
    .pub-abstract { margin-right: .8rem; margin-left: .8rem; }
    .pub-grid-2,
    .pub-grid-3 {
      grid-template-columns: 1fr;
      grid-template-rows: none;
      margin-right: .8rem;
      margin-left: .8rem;
    }
    .pub-grid-2 img,
    .pub-grid-3 img { height: auto; }
    .pub-links { margin-right: .8rem; margin-left: .8rem; }
  }
  .publication-archive {
    margin: 1rem 0 2rem;
  }
  .publication-lead-note {
    display: flex;
    align-items: center;
    gap: .42rem;
    margin: 0 0 .65rem;
    color: var(--content-muted);
    font-size: .68rem;
    line-height: 1.4;
  }
  .publication-lead-mark {
    display: inline-block;
    flex: 0 0 auto;
    color: var(--global-link-color);
    font-size: .58rem;
    line-height: 1;
  }
  .lead-author::after {
    content: "*";
    display: inline-block;
    position: relative;
    top: -.36em;
    margin-left: -.01rem;
    color: var(--global-link-color);
    font-size: .54rem;
    line-height: 1;
  }
  .publication-year__items {
    padding: .2rem 0 .45rem;
  }
  .publication-year__items > details.pub:last-child {
    margin-bottom: 0;
  }
  .pub-figure-strip {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: .65rem;
    margin: .7rem 1rem 0;
  }
  .pub-figure-strip img {
    width: auto;
    max-width: 100%;
    object-fit: contain;
    border: 1px solid var(--content-line);
    border-radius: 9px;
    background: #fff;
  }
  .pub-figure-strip--surf img { height: 12rem; }
  .pub-figure-strip--ale img { height: 10.5rem; }
  .pub-figure-strip--si img { height: 8rem; }
  .pub-figure-strip--pinn img { height: 10rem; }
  details.pub > .pub-figure-strip:last-child {
    margin-bottom: .75rem;
  }
  @media (max-width: 600px) {
    .pub-figure-strip {
      margin-right: .8rem;
      margin-left: .8rem;
    }
    .pub-figure-strip--surf img { height: 9rem; }
    .pub-figure-strip--ale img { height: 8rem; }
    .pub-figure-strip--si img { height: 6.5rem; }
    .pub-figure-strip--pinn img { height: 8rem; }
  }
</style>


<div class="publication-archive">
<details class="talk-year publication-year" open>
  <summary><span class="talk-year__label">2026</span><span class="talk-year__count">7 publications</span><span class="talk-year__arrow" aria-hidden="true">›</span></summary>
  <div class="publication-year__items">
<details class="pub">
  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">9</div>
    <div class="year">2026</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors">S. Cardonna &amp; M.-L. Hanot</span>
      <span class="pub-title">An exterior-calculus framework for mapped-polynomial Discontinuous Galerkin discretizations of hyperbolic conservation laws on manifolds</span>
      <span class="pub-tail"><i>In preparation</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
We develop an arbitrary-order Discontinuous Galerkin framework for hyperbolic conservation laws on curved manifolds represented by compatible local parametrizations.
The construction combines an exterior-calculus formulation with complete polynomial spaces transported from flat reference domains, retaining the local algebra of polynomial DG methods while accounting consistently for curved volume measures, covariant derivatives and interface traces.
Tangent-vector states are approximated in local frames, so that tangency is built into the discrete space, while scalar conservation follows from the cancellation of a common oriented numerical flux across cell interfaces.<br><br>
For unlimited linear transport, we establish a semi-discrete energy identity and an a priori bound expressed through the volume and trace defects of the physical $L^2$ projection, from which an $O(h^{k+1/2})$ estimate follows under uniform mapped-approximation assumptions and bounded oscillation of the reference velocity.<br><br>
For the shallow-water equations, positive cubature with prescribed interface nodes and cell-mean-preserving scaling are combined with third-order strong-stability-preserving Runge--Kutta integration.
For positive initial heights, an explicit CFL condition guarantees positivity of the updated cell means and control-point values, while the scheme preserves exact tangency and discrete water mass on closed meshes.<br><br>
Numerical experiments on the sphere assess accuracy and discontinuity transport for scalar advection, whereas wet- and dry-bed computations with a separate ambient-component prototype illustrate nonlinear shallow-water dynamics in the mapped spaces.
  </div>

  <div class="pub-figure-strip pub-figure-strip--surf">
    <img src="{{ site.baseurl }}/images/figs_articles/surf1.png" alt="Surface DG numerical result 1">
    <img src="{{ site.baseurl }}/images/figs_articles/surf2.png" alt="Surface DG numerical result 2">
    <img src="{{ site.baseurl }}/images/figs_articles/surf3.png" alt="Surface DG numerical result 3">
    <img src="{{ site.baseurl }}/images/figs_articles/surf4.png" alt="Surface DG numerical result 4">
  </div>

  <!-- <div class="pub-links">
    <a href="#">PDF</a>
    <a href="#">HAL</a>
  </div> -->
</details>

<details class="pub">
  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">8</div>
    <div class="year">2026</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors">E. Bernardelli, W. Boscheri &amp; <span class="lead-author">S. Cardonna</span></span>
      <span class="pub-title">Involution-Preserving schemes through constrained mesh motion: a novel Arbitrary-Lagrangian-Eulerian framework</span>
      <span class="pub-tail"><i>In preparation</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
   In this work we present an involution-preserving Arbitrary Lagrangian-Eulerian (ALE) finite volume method for first-order hyperbolic systems on moving structured meshes. The proposed approach exploits the freedom in the choice of the ALE mesh velocity to construct a constrained mesh motion that is compatible with the differential structure of the governing equations. The method is formulated in a cell-centered framework on quadrilateral meshes, where discrete divergence and curl operators are defined through corner-based geometrical quantities and their associated closure identities. Particular attention is devoted to the consistent treatment of the evolving geometry and to the satisfaction of the Geometric Conservation Law.<br><br>
The framework is applied to two representative hyperbolic systems characterized by different involutions: the ideal magnetohydrodynamics equations, subject to the divergence-free constraint on the magnetic field, and the hyperbolic Euler-Heat equations, characterized by a curl-free thermal impulse. A second-order Runge-Kutta discretization is employed in time, with the mesh constraints consistently enforced throughout the stages. Numerical experiments on classical benchmark problems assess the accuracy and robustness of the proposed approach and demonstrate the preservation of the corresponding differential involutions on moving meshes.
  </div>

  <div class="pub-figure-strip pub-figure-strip--ale">
    <img src="{{ site.baseurl }}/images/figs_articles/ale1.png" alt="ALE numerical result 1">
    <img src="{{ site.baseurl }}/images/figs_articles/ale2.png" alt="ALE numerical result 2">
    <img src="{{ site.baseurl }}/images/figs_articles/ale3.png" alt="ALE numerical result 3">
    <img src="{{ site.baseurl }}/images/figs_articles/ale4.png" alt="ALE numerical result 3">
  </div>

  <!-- <div class="pub-links">
    <a href="#">PDF</a>
    <a href="#">HAL</a>
  </div> -->
</details>

<details class="pub">
  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">7</div>
    <div class="year">2026</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors">W. Boscheri, <span class="lead-author">S. Cardonna</span>, L. Gude Vila &amp; M. Lupi</span>
      <span class="pub-title">A locally and globally divergence-free semi-implicit FV/DG scheme for magnetohydrodynamics at all Mach and Alfvén numbers</span>
      <span class="pub-tail"><i>In preparation</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
    We present a semi-implicit finite volume/discontinuous Galerkin method for planar ideal magnetohydrodynamics on Cartesian meshes, with particular emphasis on the local and global preservation of the magnetic divergence constraint. The magnetic field is represented by five divergence-free vector basis functions, ensuring local solenoidality by construction. Global compatibility is obtained through a mass-orthogonal projection enforcing two normal-trace moments on each interior face. These constraints yield a globally divergence-free field when satisfied exactly, while numerical interface compatibility is controlled by the projection tolerance. <br><br>
    The governing equations are split into an explicit material transport subsystem and implicit magnetic and acoustic subsystems, resulting in two sequential linear solves. Within the magnetic update, subcell balances of the magnetic stress supply the force at the DG quadrature nodes without introducing additional magnetic unknowns. Second-order finite volume reconstruction is combined with nonlinear stabilization within the locally solenoidal space. For smooth solutions, second-order temporal accuracy is obtained by Richardson extrapolation of the complete semi-implicit update, including the normal-trace projection and its accompanying energy correction. <br><br>
    The numerical assessment considers smooth vortices, planar Riemann problems, blast waves, the rotor, the Orszag–Tang vortex and low-Mach magnetic-loop advection, with emphasis on cell-average accuracy, shock resolution and preservation of the magnetic constraint across different Mach and Alfvén regimes.
  </div>

  <div class="pub-figure-strip pub-figure-strip--si">
    <img src="{{ site.baseurl }}/images/figs_articles/si1.png" alt="Semi-implicit MHD numerical result 1">
    <img src="{{ site.baseurl }}/images/figs_articles/si2.png" alt="Semi-implicit MHD numerical result 2">
    <img src="{{ site.baseurl }}/images/figs_articles/si3.png" alt="Semi-implicit MHD numerical result 3">
  </div>

  <!-- <div class="pub-links">
    <a href="#">PDF</a>
    <a href="#">HAL</a>
  </div> -->
</details>

<details class="pub">
  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">6</div>
    <div class="year">2026</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors">S. Cardonna &amp; A. Haidar</span>
      <span class="pub-title">A unified well-balanced, positivity-preserving and shock-capturing variational physics-informed neural method for shallow-water flows</span>
      <span class="pub-tail"><i>In preparation</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
    We introduce a variational physics-informed neural discretization for the
nonlinear shallow-water system with bathymetry. One global neural network
defines a nonlinear space--time trial manifold, whereas local affine or
bilinear test functions measure the balance law through cellwise spatial
moments at sampled times. The method is built in the free-surface variables
$(\eta,\mathbf q)$: the canonical output map enforces $H=\eta-b\geq0$ and
$\mathbf q=H\mathbf u$, the initial state and lakes at rest are inherited by the trial
manifold, and shock-forming calculations add a positive mechanical-energy
defect and a differentiable localized viscosity. These mechanisms are part of
one discrete least-squares problem rather than independent post-processing
steps.<br><br>
We give two results specific to this construction. First, an exact identity
expresses the well-balanced residual generated by an arbitrary scalar
positivity map. It proves distributional preservation of wet--dry lakes for
the positive-part map, quantifies the loss floor created by a numerical film
or a softplus regularization, and implies that no smooth strictly positive
scalar map can preserve every wet--dry lake at rest. Second, the implemented
viscosity is proved to be $O(h^2)$ in smooth regions, to reach the $O(h)$
shock-capturing scale in $O(h)$ layers, and to vanish distributionally along
uniformly BV-bounded refined sequences. These statements separate exact
properties of the trial manifold from quadrature and optimization defects;
they do not turn finitely many VPINN moments into a general convergence
theorem. Wet- and dry-bed dam breaks, fully wet and partially dry equilibria,
and one- and two-dimensional moving-shoreline Thacker solutions assess the
different structural mechanisms.
  </div>

  <div class="pub-figure-strip pub-figure-strip--pinn">
    <img src="{{ site.baseurl }}/images/figs_articles/pinn1.png" alt="Variational PINN numerical result 1">
    <img src="{{ site.baseurl }}/images/figs_articles/pinn2.png" alt="Variational PINN numerical result 2">
    <img src="{{ site.baseurl }}/images/figs_articles/pinn3.png" alt="Variational PINN numerical result 3">
    <img src="{{ site.baseurl }}/images/figs_articles/pinn4.png" alt="Variational PINN numerical result 4">
  </div>

  <!-- <div class="pub-links">
    <a href="#">PDF</a>
    <a href="#">HAL</a>
  </div> -->
</details>

<details class="pub">
  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">5</div>
    <div class="year">2026</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors"><span class="lead-author">S. Cardonna</span>, D. Lannes, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">Combined local subcell monolithic DG/FV-ALE-HHO scheme for wave-structure interactions in shallow-water flows (Part II)</span>
      <span class="pub-tail"><i>In preparation</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
    Work in progress on a 2DH wave–structure interaction model and its high-order numerical resolution.
  </div>

  <div class="pub-grid-2">
    <img src="{{ site.baseurl }}/images/wave_inter_1.png">
    <img src="{{ site.baseurl }}/images/wave_inter_2.png">
  </div>

  <!-- <div class="pub-links">
    <a href="#">PDF</a>
    <a href="#">HAL</a>
  </div> -->
</details>

<details class="pub">
  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">4</div>
    <div class="year">2026</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors"><span class="lead-author">S. Cardonna</span>, D. Lannes, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">Combined local subcell monolithic DG/FV-ALE-HHO scheme for wave-structure interactions in shallow-water flows (Part I)</span>
      <span class="pub-tail"><i>In preparation</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
    Work in progress on a 2DH wave–structure interaction model and its high-order numerical resolution.
  </div>

  <div class="pub-grid-2">
    <img src="{{ site.baseurl }}/images/wave_inter_1.png">
    <img src="{{ site.baseurl }}/images/wave_inter_2.png">
  </div>

  <!-- <div class="pub-links">
    <a href="#">PDF</a>
    <a href="#">HAL</a>
  </div> -->
</details>


<details class="pub">
  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">3</div>
    <div class="year">2026</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors"><span class="lead-author">S. Cardonna</span>, D. Lannes, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">Dirichlet-to-Neumann operators for shallow-water wave-structure interactions: modeling and DG-HHO approximation</span>
      <span class="pub-tail"><i>In preparation</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
    Work in progress on a 2DH wave–structure interaction model and its high-order numerical resolution.
  </div>

  <div class="pub-grid-2">
    <img src="{{ site.baseurl }}/images/wave_inter_1.png">
    <img src="{{ site.baseurl }}/images/wave_inter_2.png">
  </div>

  <!-- <div class="pub-links">
    <a href="#">PDF</a>
    <a href="#">HAL</a>
  </div> -->
</details>

  </div>
</details>

<details class="talk-year publication-year" open>
  <summary><span class="talk-year__label">2025</span><span class="talk-year__count">2 publications</span><span class="talk-year__arrow" aria-hidden="true">›</span></summary>
  <div class="publication-year__items">

<details class="pub">
  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">2</div>
    <div class="year">2025</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors"><span class="lead-author">S. Cardonna</span>, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">A high-order robust subcell monolithic DG/FV formulation for nonlinear shallow-water equations on unstructured grids</span>
      <span class="pub-tail"><i>Submitted to Journal of Computational Physics</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
In this work, we propose a new high-order numerical method for the two-dimensional nonlinear shallow-water (NSW) equations on unstructured meshes. The approach is based on the subcell monolithic DG/FV method, recently introduced in [Vilar:2025], in which higher-order Discontinuous Galerkin (DG) schemes are blended, at the subcell scale, with lowest-order robust Finite Volume (FV) methods. This is made possible through the reformulation of high-order DG schemes as a FV-like schemes defined on a subgrid, through the introduction of some particular fluxes referred to as reconstructed fluxes.<br><br>
The strategy then relies on the introduction of blended numerical fluxes, defined as convex combinations of reconstructed high-order DG fluxes and robust first-order FV ones. The blending coefficients are locally computed at each subcell interface in order to enforce unavoidable nonlinear stability properties. This allows the scheme to remain stable in the presence of strong gradients, shocks, and wet-dry fronts, while still keeping high-order accuracy in smooth regions.
<br><br>
A particular attention is paid to the discrete formulation associated with the bathymetry source term. The scheme is designed to be well-balanced for motionless steady-states, thanks to some fine tuning of local hydrostatic-like reconstructions, respectively applied at two different scales and on two different kinds of approximations: i) at the level of DG fluxes between elements, focusing on suitable reconstructions of high-order polynomial traces, ii) at the level of FV fluxes between subcells, focusing on the reconstruction of subcell piecewise-constant values. This innovative two-levels reconstruction ensures that motionless steady states are not only exactly preserved on fully unstructured meshes, but also down to the subcell scale. <br><br>
This new numerical method relies on a fully a priori treatment, and does not require any a posteriori re-computing and adapting steps, while remaining conservative by construction. Several numerical experiments illustrate its ability to accurately capture multidimensional wet-dry interfaces, to control spurious oscillations near classical discontinuities, and accurately resolve localized flow-features inside relatively large mesh elements.
  </div>

  <div class="pub-grid-2">
    <img src="{{ site.baseurl }}/images/tsunami2d_2.png">
    <img src="{{ site.baseurl }}/images/tsunami2d_theta.png">
  </div>

  <div class="pub-links">
    <a href="{{ site.url }}/files/publications/monolithic_DGFV_subcell_NSW_2d.pdf">PDF</a>
    <a href="https://hal.science/hal-05630914">HAL</a>
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
      <span class="pub-authors"><span class="lead-author">S. Cardonna</span>, A. Haidar, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">Local subcell monolithic DG/FV methods for nonlinear shallow-water models with source terms</span>
      <span class="pub-tail"><i>Submitted to International Journal for Numerical Methods in Fluids</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
This paper contains several new contributions to the numerical approximation of shallow-water equations. 
We introduce a high-order local subcell monolithic DG/FV discretization method for the approximation of nonlinear free-surface shallow-water equations with source terms. 
This encompasses both nonlinear hyperbolic shallow-water equations (also known as Saint-Venant equations) and weakly-dispersive fully-nonlinear equations (known as Green-Naghdi equations), approximating 
the general free-surface water-wave equations in the shallow-water flow regime. <br><br>
The method is grounded on a classical Discontinuous Galerkin (DG) formulation, written as a particular Finite Volume (FV) discretization on a sub-partition, involving reconstructed high-order interface numerical fluxes. In the present work, we investigate the important issue of source terms discretization in the framework of such local subcell monolithic DG/FV strategies, 
focusing on the bathymetry source terms, and also higher-order differential source terms coming from dispersive corrections for higher-order asymptotic models. 
The originality of the method is the introduction of a priori blended fluxes, which are convex combinations of the so-called high-order reconstructed fluxes and low-order FV fluxes. 
The blending coefficients are adaptively computed for each subcell interface to enforce relevant convex properties at the discrete level, including water-height positivity. 
Starting from the DG piecewise polynomial approximation, the bathymetry source term is also discretized at the subcell level,
and we prove that a suitable well-balanced property, ensuring the preservation of motionless steady-states, can be achieved at the subcell-scale relying on some finely tuned combinations of various hydrostatic-like reconstructed states at lower/higher accuracy levels, simultaneously occurring at local and global scales. <br><br>
We also introduce an original and efficient combination of this new well-balanced local subcell monolithic DG/FV with a high-order Internal Penalty discontinuous-Galerkin method, in order to 
approximate the higher-order contributions appearing in the Green-Naghdi equations in a consistent and accurate way. 
We then conduct extensive evaluations of the resulting numerical methods, providing insights about the observed numerical convergence and the overall robustness, including the ability to preserve steady-states, to prevent nonphysical oscillations near discontinuities and to ensure the positivity of the water-height at the discrete level.
  </div>

  <div class="pub-grid-3">
    <img src="{{ site.baseurl }}/images/1d_2.png">
    <img src="{{ site.baseurl }}/images/dispersive.png">
    <img src="{{ site.baseurl }}/images/1d_3.png">
  </div>


  <div class="pub-links">
    <a href="{{ site.url }}/files/publications/monolithic_DGFV_subcell_NSW_GN.pdf">PDF</a>
    <a href="https://hal.science/hal-05434014">HAL</a>
  </div>

</details>

  </div>
</details>
</div>

<!-- ________________________________ -->

## Talks & posters
<hr style="margin-top: -0.1em; margin-bottom: 1em;">

<div class="talk-archive">
<details class="talk-year" open>
  <summary><span class="talk-year__label">2026</span><span class="talk-year__count">4 talks</span><span class="talk-year__arrow" aria-hidden="true">›</span></summary>
  <div class="talk-timeline dot-timeline">
  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">4 May 2026</span><span>Minho, Portugal</span></div>
      <h3><a href="https://shark-fv.eu/home-shark/">SHARK-FV26</a> <span class="talk-card__event-note">— Sharing Higher order Advanced Research Known-how on Finite Volume</span></h3>
      <p class="talk-card__title">Subcell monolithic DG/FV–HHO–SSP-RK scheme for a new wave-structure interaction model</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/SHARK_FV26.pdf">Slides</a></div>
    </div>
  </article>

  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">19 March 2026</span><span>University of Waterloo · Waterloo, Canada</span></div>
      <h3><a href="https://uwaterloo.ca/applied-mathematics/events/applied-math-colloquium">Applied Maths Colloquium</a> <span class="talk-card__event-note">— Seminar of the Applied Mathematics group at UW</span></h3>
      <p class="talk-card__title">A high-order DG/FV convex property preserving scheme for hyperbolic systems with applications to shallow water flows and fluid-structure interaction</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/uw_colloquium.pdf">Slides</a></div>
    </div>
  </article>

  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">2 March 2026</span><span>ENPC · Champs-sur-Marne, France</span></div>
      <h3><a href="https://cjcma2026.sciencesconf.org">CJC-MA</a> <span class="talk-card__event-note">— Congrès des Jeunes Chercheur.e.s en Mathématiques Appliquées</span></h3>
      <p class="talk-card__title">Modeling and numerical simulation of floating structures in shallow-water flows</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/CJCMA.pdf">Slides</a></div>
    </div>
  </article>

  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">19 February 2026</span><span>Montpellier, France</span></div>
      <h3>Métiers des mathématiques <span class="talk-card__event-note">— Conference for bachelor’s and master’s students</span></h3>
      <p class="talk-card__title">Modèles et méthodes numériques pour les interactions entre vagues et structures flottantes</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/metier_des_maths.pdf">Slides</a></div>
    </div>
  </article>

  </div>
</details>

<details class="talk-year" open>
  <summary><span class="talk-year__label">2025</span><span class="talk-year__count">3 talks</span><span class="talk-year__arrow" aria-hidden="true">›</span></summary>
  <div class="talk-timeline dot-timeline">
  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">14 July 2025</span><span>McGill University · Montréal, Canada</span></div>
      <h3><a href="https://icosahom2025.org/index.html">ICOSAHOM</a> <span class="talk-card__event-note">— International Congress on Spectral and High Order Methods</span></h3>
      <p class="talk-card__title">Local subcell monolithic DG/FV scheme for NSW equations with source terms on unstructured grids</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/ICOSAHOM.pdf">Slides</a></div>
    </div>
  </article>

  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">2 June 2025</span><span>Montpellier, France</span></div>
      <h3><a href="https://www.umontpellier.fr/agenda/semaine-du-pole-mips">MIPS Colloquia</a> <span class="talk-card__event-note">— Semaine du pôle Mathématiques, Informatique, Physique, Systèmes</span></h3>
      <p class="talk-card__title">Designing numerical methods for free-surface flows towards reliable wave-structure interactions</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/MIPS.pdf">Slides</a></div>
    </div>
  </article>

  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">13 May 2025</span><span>Aussois, France</span></div>
      <h3><a href="https://cimav2025.sciencesconf.org">CIMAV</a> <span class="talk-card__event-note">— Congrès Interdisciplinaire sur les Modèles Avancés de Vagues</span></h3>
      <p class="talk-card__title">A high-order robust DG/FV scheme for nonlinear shallow water equations with source terms on unstructured grids</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/CIMAV.pdf">Slides</a></div>
    </div>
  </article>

  </div>
</details>

<details class="talk-year">
  <summary><span class="talk-year__label">2024</span><span class="talk-year__count">1 poster</span><span class="talk-year__arrow" aria-hidden="true">›</span></summary>
  <div class="talk-timeline dot-timeline">
  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">15 March 2024</span><span>Montpellier, France</span></div>
      <h3>Ph.D. Day <span class="talk-card__event-note">— Séminaire des Doctorants</span></h3>
      <p class="talk-card__title">Monolithic DG/FV schemes on 1D nonlinear shallow water equations</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/poster_phd_day24.pdf">Poster</a></div>
    </div>
  </article>

  </div>
</details>

<details class="talk-year">
  <summary><span class="talk-year__label">2023</span><span class="talk-year__count">1 talk</span><span class="talk-year__arrow" aria-hidden="true">›</span></summary>
  <div class="talk-timeline dot-timeline">
  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">25 October 2023</span><span>Montpellier, France</span></div>
      <h3>Introduction to newcomers <span class="talk-card__event-note">— Séminaire des Doctorants</span></h3>
      <p class="talk-card__title">Modeling, solving &amp; implementing PDEs from waves-structure interactions</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/SEMDOC.pdf">Slides</a></div>
    </div>
  </article>
  </div>
</details>
</div>


## Ph.D. research statement
<hr style="margin-top: -0.1em; margin-bottom: 1em;">
 My research lies at the intersection of mathematical modeling, numerical analysis, and the study of partial differential equations (PDEs) describing fluid flows. In particular, during my PhD, I focused on nonlinear systems of hyperbolic balance laws, which are used to model the evolution of quantities that are transported and conserved in time. These systems take the general form
<div style="text-align: center;">
$$
\partial_t \bm{u}(\bm{x},t) + \nabla_{\!\bm{x}} \cdot \mathbb{F}(\bm{u}) = \bm{S}(\bm{u}, \bm{x},t),
$$
</div>
where $\bm{u}$ represents the vector of conserved variables (our unknowns), $\mathbb{F}$ the flux function that can be nonlinear, and $\bm{S}$ possible source terms arising from geometry, external forces, or coupling effects. The mathematical challenge is that even smooth initial data can generate discontinuities in finite time, which makes the analytical study of such systems extremely delicate. Because of the lack of regularity of weak solutions, only partial theoretical results are available, and the numerical approximation of these phenomena must often combine high-order accuracy with stability and robustness.

Among the many examples of such systems, the nonlinear shallow-water equations (NSW) play a central role in the water wave community; they provide an asymptotic model derived from the incompressible Euler equations under the assumption of small aspect ratio (the depth of the fluid is much smaller than the horizontal scale). Despite their asymptotic nature, the shallow water equations remain extremely valuable in practice. They provide an accurate description of the main physical mechanisms governing free-surface flows, while avoiding the prohibitive computational cost associated with solving the fully three-dimensional Euler or Navier–Stokes equations. They thus offer an effective compromise between physical realism and numerical efficiency. Even though they do not account for dispersive effects (captured in more refined models such as the Boussinesq or Green–Naghdi systems), they remain one of the most widely used and robust approximations for practical flow simulations.
Given a smooth parameterization $b$ of the bathymetry variation, the NSW equations read as
<div style="text-align: center;">
$$
\begin{cases}
      \partial_t\:\!\eta + \nabla_{\!\bm{x}} \cdot \bm{q} = \bm{S}_1[b](\bm{v}), \\
      \partial_t \:\!\bm{q} + \nabla_{\!\bm{x}} \cdot \left( \bm{u} \otimes \bm{q} + \frac{g\eta}{2}(\eta - 2b)\mathbb{I}_2  \right) = \bm{S}_2[b](\bm{v}),
\end{cases} \nonumber
$$
</div>
with $\bm{v} = (\eta,\bm{q})^t$, where $\eta$ is water total elevation, $\bm{q}$ is the horizontal discharge, and $\bm{S}\[b\](\bm{v})$ is a generic source term that may contains topography, friction and/or Coriolis effects.

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
