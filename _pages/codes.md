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
<i> Language. </i> C++, Python (visualization).<br>
<i> Developers. </i> Fabien Marche (main), Sacha Cardonna, Arnaud Duran, Matthieu Rigal...

WaveBox is a multi-models numerical platform initiated by Fabien Marche, dedicated to the approximations of the solutions of several shallow water asymptotics in the surface dimension d = 2 with efficient combined Hybridized Discontinuous Galerkin (HDG), Hybrid High Order (HHO), Monolithic DG/FV subcells and DG methods on general unstructured meshes (for Saint-Venant, Boussinesq and Green-Naghdi equations). 

Main features are: 
- Sub-models CPU-GPU co-processing;
- Arbitrary order of accuracy (h and p-adaptivity);
- Robust treatment of the run-up and flooding processes (strict maximum-principle enforcement);
- Well-balancing for motionless steady states;
- Unstructured meshes & mesh subdivision;
- Wave breaking treatment with dynamic switching strategy.

<section class="wavebox-gallery" aria-labelledby="wavebox-gallery-title">
  <div class="wavebox-gallery__header">
    <div>
      <p class="wavebox-gallery__eyebrow">Numerical simulations</p>
      <h3 id="wavebox-gallery-title">Explore WaveBox in motion</h3>
    </div>
    <span class="wavebox-gallery__count"><strong id="wavebox-current">01</strong> / <span id="wavebox-total">24</span></span>
  </div>

  <label class="wavebox-gallery__label" for="wavebox-select">Choose a simulation</label>
  <div class="wavebox-gallery__select-wrap">
    <select id="wavebox-select" class="wavebox-gallery__select">
      <option value="{{ site.baseurl }}/images/GN_dispersive.gif" data-type="image" data-degree="P³ · 1D">Green–Naghdi dam-break with dispersive shock</option>
      <option value="{{ site.baseurl }}/images/1d_boat.gif" data-type="image" data-degree="P³ · 1D">Wave generator</option>
      <option value="{{ site.baseurl }}/images/fixed_obj_topo.gif" data-type="image" data-degree="P⁶ · 1D">Wave interacting with a fixed object and topography</option>
      <option value="{{ site.baseurl }}/images/rock_wave_P6.mp4" data-type="video" data-degree="P⁶ · 2D">Collapsing wave interacting with a rock</option>
      <option value="{{ site.baseurl }}/images/tidal_P2.avi" data-type="video" data-degree="P² · 2D · View 1">Tidal wave interacting with a rock</option>
      <option value="{{ site.baseurl }}/images/tidal_P2_2.avi" data-type="video" data-degree="P² · 2D · View 2">Tidal wave interacting with a rock</option>
      <option value="{{ site.baseurl }}/images/wet_dam_break_P4.avi" data-type="video" data-degree="P⁴ · 2D">Dam-break on a wet bed</option>
      <option value="{{ site.baseurl }}/images/circ_dam_P3.avi" data-type="video" data-degree="P³ · 2D">Circular dam-break on a wet bed</option>
      <option value="{{ site.baseurl }}/images/cg_periodic_P2.mp4" data-type="video" data-degree="P² · 2D">Carrier–Greenspan periodic solution</option>
      <option value="{{ site.baseurl }}/images/tsunami_P2.mp4" data-type="video" data-degree="P² · 2D">Tsunami on three conical islands</option>
      <option value="{{ site.baseurl }}/images/single_wave_stationnary.mp4" data-type="video" data-degree="P² · 2D">Single wave on a partly immersed stationary pontoon</option>
      <option value="{{ site.baseurl }}/images/prescribed_motion_object.avi" data-type="video" data-degree="P² · 2D">Wave generator</option>
      <option value="{{ site.baseurl }}/images/pontoon_equilibrium_up.avi" data-type="video" data-degree="P² · 2D · Upward motion">Pontoon returning to equilibrium</option>
      <option value="{{ site.baseurl }}/images/pontoon_equilibrium_down.avi" data-type="video" data-degree="P² · 2D · Downward motion">Pontoon returning to equilibrium</option>
      <option value="{{ site.baseurl }}/images/single_wave_newton.avi" data-type="video" data-degree="P⁵ · 2D">Single wave on a freely moving pontoon</option>
      <option value="{{ site.baseurl }}/images/shock_wave_newton.avi" data-type="video" data-degree="P² · 2D">Shock-wave on a freely moving pontoon</option>
      <option value="{{ site.baseurl }}/images/single_wave_stationnary_cylinder.avi" data-type="video" data-degree="P² · 2D">Single wave on a partly immersed stationary cylinder</option>
      <option value="{{ site.baseurl }}/images/single_wave_cylinder_beach.avi" data-type="video" data-degree="P¹ · 2D">Single wave on a stationary cylinder and a beach</option>
      <option value="{{ site.baseurl }}/images/mesh_ale_evolution_laplacian.gif" data-type="image" data-degree="P² · ALE · Laplacian smoothing">Mesh motion around an oscillating cylinder</option>
      <option value="{{ site.baseurl }}/images/mesh_ale_evolution_elasticity.gif" data-type="image" data-degree="P² · ALE · Pseudo-elasticity">Mesh motion around an oscillating cylinder</option>
      <option value="{{ site.baseurl }}/images/spring_beach.avi" data-type="video" data-degree="P¹ · ALE · 2D">Wave run-up generated by an impulsively stopped piston</option>
      <option value="{{ site.baseurl }}/images/spring_ale.mp4" data-type="video" data-degree="P² · ALE · 2D">Periodic wave generation by an oscillating piston</option>
      <option value="{{ site.baseurl }}/images/ale_dual.avi" data-type="video" data-degree="P¹ · ALE · View 1">Translating and oscillating cylinder in shallow-water flow</option>
      <option value="{{ site.baseurl }}/images/oscillating_cylinder.avi" data-type="video" data-degree="P¹ · ALE · View 2">Translating and oscillating cylinder in shallow-water flow</option>
    </select>
  </div>

  <div class="wavebox-gallery__stage" id="wavebox-stage" aria-live="polite">
    <img src="{{ site.baseurl }}/images/GN_dispersive.gif" alt="Green–Naghdi dam-break with dispersive shock simulation">
  </div>

  <div class="wavebox-gallery__footer">
    <div class="wavebox-gallery__caption">
      <span id="wavebox-meta">P³ · 1D</span>
      <strong id="wavebox-caption">Green–Naghdi dam-break with dispersive shock</strong>
    </div>
    <div class="wavebox-gallery__nav" aria-label="Simulation navigation">
      <button type="button" id="wavebox-prev" aria-label="Previous simulation">←</button>
      <button type="button" id="wavebox-next" aria-label="Next simulation">→</button>
    </div>
  </div>
</section>

<style>
.wavebox-gallery { margin: 2rem 0 2.5rem; border: 1px solid rgba(127,127,127,.22); border-radius: 16px; overflow: hidden; background: rgba(127,127,127,.045); box-shadow: 0 14px 38px rgba(0,0,0,.07); }
.wavebox-gallery__header, .wavebox-gallery__footer { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 1.15rem 1.35rem; }
.wavebox-gallery__header h3 { margin: .05rem 0 0; font-size: 1.1rem; }
.wavebox-gallery__eyebrow, .wavebox-gallery__label { margin: 0; color: #65717d; font-size: .68rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
.wavebox-gallery__count { color: #78838e; font-size: .72rem; font-variant-numeric: tabular-nums; white-space: nowrap; }
.wavebox-gallery__count strong { color: inherit; font-size: .95rem; }
.wavebox-gallery__label { display: block; padding: .15rem 1.35rem .45rem; }
.wavebox-gallery__select-wrap { position: relative; margin: 0 1.35rem 1rem; }
.wavebox-gallery__select-wrap::after { content: "⌄"; position: absolute; top: 50%; right: 1rem; transform: translateY(-56%); pointer-events: none; font-size: 1.1rem; }
.wavebox-gallery__select { width: 100%; min-height: 46px; padding: .65rem 2.7rem .65rem .85rem; border: 1px solid rgba(127,127,127,.32); border-radius: 9px; background: var(--global-bg-color, #fff); color: inherit; font: inherit; font-size: .84rem; appearance: none; cursor: pointer; }
.wavebox-gallery__select:focus-visible, .wavebox-gallery__nav button:focus-visible { outline: 3px solid rgba(82,146,204,.35); outline-offset: 2px; }
.wavebox-gallery__stage { display: grid; place-items: center; min-height: 300px; aspect-ratio: 16 / 9; background: #071019; overflow: hidden; }
.wavebox-gallery__stage img, .wavebox-gallery__stage video { display: block; width: 100%; height: 100%; max-height: 580px; object-fit: contain; margin: 0; }
.wavebox-gallery__caption { display: grid; gap: .2rem; min-width: 0; }
.wavebox-gallery__caption span { color: #65717d; font-size: .68rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
.wavebox-gallery__caption strong { font-size: .83rem; line-height: 1.35; }
.wavebox-gallery__nav { display: flex; gap: .45rem; flex: 0 0 auto; }
.wavebox-gallery__nav button { width: 38px; height: 38px; border: 1px solid rgba(127,127,127,.3); border-radius: 50%; background: transparent; color: inherit; font-size: 1rem; cursor: pointer; transition: transform .18s ease, background .18s ease; }
.wavebox-gallery__nav button:hover { transform: translateY(-1px); background: rgba(127,127,127,.1); }
@media (max-width: 600px) { .wavebox-gallery__header, .wavebox-gallery__footer { padding: 1rem; } .wavebox-gallery__label { padding-left: 1rem; } .wavebox-gallery__select-wrap { margin: 0 1rem 1rem; } .wavebox-gallery__stage { min-height: 210px; } }
@media (prefers-reduced-motion: reduce) { .wavebox-gallery__nav button { transition: none; } }
</style>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var select = document.getElementById('wavebox-select');
  if (!select) return;
  var stage = document.getElementById('wavebox-stage');
  var caption = document.getElementById('wavebox-caption');
  var meta = document.getElementById('wavebox-meta');
  var current = document.getElementById('wavebox-current');
  document.getElementById('wavebox-total').textContent = select.options.length;

  function showSimulation(index) {
    select.selectedIndex = (index + select.options.length) % select.options.length;
    var option = select.options[select.selectedIndex];
    var media;
    stage.replaceChildren();
    if (option.dataset.type === 'video') {
      media = document.createElement('video');
      media.controls = true;
      media.preload = 'metadata';
      media.playsInline = true;
    } else {
      media = document.createElement('img');
    }
    media.src = option.value;
    media.setAttribute('aria-label', option.text + ' simulation');
    if (media.tagName === 'IMG') media.alt = option.text + ' simulation';
    stage.appendChild(media);
    caption.textContent = option.text;
    meta.textContent = option.dataset.degree;
    current.textContent = String(select.selectedIndex + 1).padStart(2, '0');
  }

  select.addEventListener('change', function () { showSimulation(select.selectedIndex); });
  document.getElementById('wavebox-prev').addEventListener('click', function () { showSimulation(select.selectedIndex - 1); });
  document.getElementById('wavebox-next').addEventListener('click', function () { showSimulation(select.selectedIndex + 1); });
});
</script>

***

<b> Bfree — Structure-preserving finite-volume solver for ideal magnetohydrodynamics </b> <br>
<i> Keywords. </i> Magnetohydrodynamics, Divergence-free schemes, Finite Volumes, Semi-implicit methods, ALE mesh motion. <br>
<i> Language. </i> Fortran, Python (visualization). <br>
<i> Developers. </i> Walter Boscheri (main), Mattia Lupi, Elena Bernardelli, Lidia Gude Vila & Sacha Cardonna.

Bfree is a research-oriented numerical platform for the simulation of two-dimensional ideal magnetohydrodynamics and Euler–Heat flows. Its main purpose is to design structure-preserving finite-volume methods that maintain fundamental differential constraints at the discrete level: the divergence-free condition of the magnetic field for ideal MHD and the curl-free condition of the thermal impulse for the Euler–Heat model.

Main features are:
- Divergence-free discretizations for the magnetic field in ideal MHD;
- Curl-free discretizations for the thermal impulse in the Euler–Heat system;
- Explicit Arbitrary Lagrangian–Eulerian (ALE) finite-volume schemes on moving meshes;
- Semi-implicit finite-volume schemes for low Mach and low Alfvén number regimes;
- Structure-preserving evolution of the discrete differential constraints;
- First- and second-order accurate spatial discretizations;
- Conservative monitoring of mass and total energy.

<div style="display: flex; justify-content: space-between; gap: 7px;">
      <img src="{{ site.baseurl }}/images/bfree1.gif" alt="bfree Image 2" style="width: 21%; height: auto;">
      <img src="{{ site.baseurl }}/images/bfree2.gif" alt="bfree Image 1" style="width: 21%; height: auto;">
      <img src="{{ site.baseurl }}/images/bfree3.gif" alt="bfree Image 3" style="width: 21%; height: auto;">
      <img src="{{ site.baseurl }}/images/bfree4.gif" alt="bfree Image 4" style="width: 21%; height: auto;">
</div>

***

<b> ManicoreFV - Discontinuous Galerkin code for conservation laws on surfaces </b>  <br>
<i> Keywords. </i> Discontinuous Galerkin, Finite Volumes, Conservation Laws, Surface PDEs, Curved Meshes. <br>
<i> Language. </i> C++, Python (visualization). <br>
<i> Developers. </i> Marien Hanot & Sacha Cardonna.

ManicoreFV is a C++ plaform for the numerical approximation of conservation laws on curved surfaces using Discontinuous Galerkin and finite-volume methods. It is a fork of [Manicore](https://mlhanot.github.io/Manicore/), the code developed by Marien Hanot for the implementation of numerical schemes on manifolds with general Riemannian metrics.

Main features are:
- Geometry-aware formulations based on the local charts, parametrizations and Riemannian metrics provided by the Manicore framework;
- High-order Discontinuous Galerkin discretizations of scalar conservation laws on curved surfaces, from piecewise-constant to high-order polynomial approximations;
- Explicit Runge--Kutta time integration with CFL-based time-step selection;
- Bound-preserving limiting for discontinuous solutions while maintaining local cell averages and global mass conservation.

<div style="display: flex; justify-content: space-between; gap: 7px;">
      <img src="{{ site.baseurl }}/images/limDG.gif" alt="bfree Image 2" style="width: 48%; height: auto;">
      <img src="{{ site.baseurl }}/images/slice_limDG.gif" alt="bfree Image 1" style="width: 48%; height: auto;">
</div>

***

<b> ShoreVPINN - Variational physics-informed neural solver for shallow-water flows </b>  <br>
<i> Keywords. </i> Variational Physics-Informed Neural Networks, Saint-Venant equations, wet-dry interfaces, wave run-up, machine learning. <br>
<i> Language. </i> Python (PyTorch). <br>
<i> Developers. </i> Ali Haidar & Sacha Cardonna.

ShoreVPINN is a research-oriented Python code exploring Variational Physics-Informed Neural Networks (VPINNs) for the approximation of the one-dimensional nonlinear shallow-water, or Saint-Venant, equations. Instead of relying exclusively on pointwise evaluations of the governing equations, the physical residuals are integrated against local test functions over a spatial mesh. This weak formulation is particularly well suited to flows involving variable topography and moving wet-dry interfaces.

Main features are:
- Variational enforcement of the mass and momentum equations using local finite-element test functions;
- Exact preservation of the initial condition through a hard-constrained neural ansatz;
- Positivity-preserving treatment of the water depth;
- Robust formulation of the momentum flux near wet-dry interfaces;
- Non-uniform spatial meshes with optional local refinement in the run-up region;
- Gauss-Legendre quadrature and stochastic batching over time slices;
- Automatic execution on CPU, CUDA GPUs and Apple Silicon GPUs.

<div style="display: flex; justify-content: space-between; gap: 7px;">
      <img src="{{ site.baseurl }}/images/shorevpinn1.gif" alt="WaveBox Image 2" style="width: 48%; height: auto;">
      <img src="{{ site.baseurl }}/images/shorevpinn2.gif" alt="WaveBox Image 1" style="width: 48%; height: auto;">
</div>

***

<b> DG4SCL - Compact and student friendly code for DG methods on 1D SCL </b>  <br>
<i> Keywords. </i> Discontinuous Galerkin, Scalar Conservation Laws. <br>
<i> Language. </i> C++, Python (visualization).<br>
<i> Developers. </i> Sacha Cardonna.

During the early stages of my internship with F. Vilar and F. Marche, I embarked on the development of a compact C++ code focused on addressing Discontinuous Galerkin (DG) schemes for 1D conservation laws. 
This code is a work in progress, far from being complete or flawless. Its creation was driven by my commitment to simplicity and understandability. I strived to ensure that the code's structure and implementation were as straightforward as possible, enabling users to grasp the underlying concepts with ease.
By expanding its functionality and making it more comprehensive, I aim to create a valuable resource for students seeking a simplified example of DG schemes. This endeavor stems from my own experiences as a student, where access to such a resource would have greatly facilitated my understanding and learning process.

Contact me to get the source.

![DG4SCL Simulation]({{ site.baseurl }}/images/dg_lcs.png)
