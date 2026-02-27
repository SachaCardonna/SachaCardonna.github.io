---
permalink: /
title: "Hello there! <span style=\"font-family: monospace; font-weight: 600;\">☺</span>"
excerpt: "Hello there! <span style=\"font-family: monospace; font-weight: 600;\">☺</span>"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I'm a Ph.D. student in Mathematics, under the supervision of [François Vilar](https://vilar.perso.math.cnrs.fr) & [Fabien Marche](https://imag.umontpellier.fr/~Marche/) at [Institut Montpelliérain Alexander Grothendieck](https://imag.umontpellier.fr) (IMAG - UMR 5149).

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

<style>
details { margin-bottom: 0.3em; }
summary {
  padding-left: 2em;
  text-indent: -2em;
  list-style: none;  
  cursor: pointer;
  font-weight: 500;
}
details[open] summary { list-style-image: none; }
</style>

## News & highlights
<div class="news">
  <div class="table-responsive news-scroll">
    <table class="table table-sm table-borderless">
              <tr>
        <td scope="row">Jun 2026</td>
        <td style="width:85%">
          I will participate at the
          <a href="https://elenagaburro.it/sunhype2026.html" rel="external nofollow noopener" target="_blank">SUNHYPE 2026</a>
          in the city of Chania, in Greece.
        </td>
      </tr>
          <tr>
        <td scope="row">May 2026</td>
        <td style="width:85%">
          I will attend and present at
          <a href="https://shark-fv.eu/home-shark/" rel="external nofollow noopener" target="_blank">SHARK-FV26</a> near Porto, Portugal.
        </td>
      </tr>
            <tr>
        <td scope="row">Mar 2026</td>
        <td style="width:85%">
          I am invited by
          <a href="https://uwaterloo.ca/scholar/ddelreyf" rel="external nofollow noopener" target="_blank">David Del Rey Fernández</a>  
          to present at the
          <a href="https://uwaterloo.ca/applied-mathematics/events/applied-math-colloquium" rel="external nofollow noopener" target="_blank">Applied Maths Colloquium</a>
          at
          <a href="https://uwaterloo.ca" rel="external nofollow noopener" target="_blank">University of Waterloo</a>, Canada.
        </td>
      </tr>
      <tr>
        <td scope="row">Mar 2026</td>
        <td style="width:85%">
          I have been invited to give a talk at
          <a href="https://cjcma2026.sciencesconf.org" rel="external nofollow noopener" target="_blank">CJC-MA26</a>
          during the special session "Ocean", funded by the
          <a href="https://rtte.math.cnrs.fr/" rel="external nofollow noopener" target="_blank">RTTE</a>.
        </td>
      </tr>
            <tr>
        <td scope="row">Feb 2026</td>
        <td style="width:85%">
I gave a talk to undergraduate and master’s students about what it’s like to pursue a Ph.D. in mathematics, as part of a special conference on careers in mathematics.
        </td>
      </tr>
      <tr>
        <td scope="row">Dec 2025</td>
        <td style="width:85%">
          I visited the
          <a href="https://www.inria.fr/fr/rapsodi" rel="external nofollow noopener" target="_blank">RAPSODI</a>
          team in Lille, kindly invited by my friend
          <a href="https://marienhanot.fr" rel="external nofollow noopener" target="_blank">Marien Hanot</a>.
        </td>
      </tr>
      <tr>
        <td scope="row">Jul 2025</td>
        <td style="width:85%">
          I talked about high-order monolithic methods at
          <a href="https://icosahom2025.org" rel="external nofollow noopener" target="_blank">ICOSAHOM 2025</a>
          in Montréal, see the
          <a href="{{ site.url }}/files/talks/ICOSAHOM.pdf">slides</a>.
        </td>
      </tr>
      <tr>
        <td scope="row">Jun 2025</td>
        <td style="width:85%">
          During
          <a href="https://www.umontpellier.fr/agenda/semaine-du-pole-mips" rel="external nofollow noopener" target="_blank">MIPS Week</a>,
          I talked about some aspects of modeling and scientific computing to non-experts scientists, see the
          <a href="{{ site.url }}/files/talks/MIPS.pdf">presentation</a>.
        </td>
      </tr>
      <tr>
        <td scope="row">May 2025</td>
        <td style="width:85%">
          Made a presentation at the
          <a href="https://cimav2025.sciencesconf.org" rel="external nofollow noopener" target="_blank">CIMAV 2025</a>
          conference held in Aussois, see the
          <a href="{{ site.url }}/files/talks/CIMAV.pdf">beamer</a>.
        </td>
      </tr>
            <tr>
        <td scope="row">Jan 2025</td>
        <td style="width:85%">
         I attended the <a href="http://smai.emath.fr/spip.php?article932" rel="external nofollow noopener" target="_blank">CEA-SMAI/GAMNI25</a> at Institut Henri Poincaré, Paris.
        </td>
      </tr>
    </table>
  </div>
</div>

<style>
.news-scroll {
  max-height: 60vw;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
.news-scroll table {
  border: none;
  border-collapse: collapse;
}
.news-scroll td {
  border: none;
  padding: 8px 0;
  border-bottom: none !important;
}
.news td[scope="row"] {
  white-space: nowrap;
  padding-right: 1.2rem;
}
</style>
