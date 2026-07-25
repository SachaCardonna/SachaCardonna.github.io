---
layout: archive
title: "Recherche"
author_profile: true
permalink: /fr/recherche/
lang: fr
translation_url: /research/
---



{% include base_path %}

Découvrez mes publications, les conférences et conférences auxquelles j'ai participé et mes intérêts de recherche.

## Publications
<hr style="margin-top: -0.1em; margin-bottom: 1em;">

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

  /* Cartes éditoriales des publications */
  details.pub {
    padding: 0;
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
    gap: .8rem;
    align-items: start;
    padding: .9rem 1rem;
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
    font-size: .84rem;
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
    margin: 1rem 1rem 0;
    padding: 0;
    border: 0;
    color: var(--global-text-color);
    font-size: .72rem;
    line-height: 1.68;
  }
  .pub-abstract::before {
    content: "Résumé";
    margin-bottom: .5rem;
    font-size: .6rem;
  }
  .pub-grid-2,
  .pub-grid-3 {
    margin: .9rem 1rem 0;
    gap: .55rem;
  }
  .pub-grid-2 img,
  .pub-grid-3 img {
    border: 1px solid var(--content-line);
    border-radius: 9px;
  }
  details.pub > .pub-grid-2:last-child,
  details.pub > .pub-grid-3:last-child { margin-bottom: 1rem; }
  .pub-links {
    margin: .85rem 1rem 1rem;
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
      padding: .8rem;
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
</style>

<details class="pub">
  <summary class="pub-summary">
    <div class="pub-badge">
    <div class="num">4</div>
    <div class="year">2026</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors">S. Cardonna, D. Lannes, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">Numerical resolution of 2D nonlinear shallow-water equations with a partly immersed surface obstacle (Part II)</span>
      <span class="pub-tail"><i>En préparation</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
    Travail en cours consacré à la modélisation bidimensionnelle des interactions entre vagues et structures, ainsi qu’à la conception et à l’analyse des méthodes numériques associées.
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
      <span class="pub-authors">S. Cardonna, D. Lannes, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">Numerical resolution of 2D nonlinear shallow-water equations with a partly immersed surface obstacle (Part I)</span>
      <span class="pub-tail"><i>En préparation</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
    Travail en cours consacré à la modélisation bidimensionnelle des interactions entre vagues et structures, ainsi qu’à la conception et à l’analyse des méthodes numériques associées.
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
    <div class="num">2</div>
    <div class="year">2025</div>
      <div class="arrow">›</div>
  </div>
    <div class="pub-line">
      <span class="pub-authors">S. Cardonna, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">A high-order robust subcell monolithic DG/FV formulation for nonlinear shallow-water equations on unstructured grids</span>
      <span class="pub-tail"><i>Soumis</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
Nous proposons une nouvelle méthode numérique d’ordre élevé pour les équations bidimensionnelles non linéaires de Saint-Venant sur maillages non structurés. Elle repose sur l’approche monolithique subcell DG/FV récemment introduite dans [Vilar:2025] : une discrétisation Discontinuous Galerkin (DG) d’ordre élevé est réécrite sous une forme de type Finite Volume (FV) sur une sous-grille, au moyen de flux reconstruits, puis combinée à l’échelle des sous-cellules avec une méthode FV robuste de premier ordre.<br><br>
Les flux numériques sont obtenus comme des combinaisons convexes des flux DG reconstruits et des flux FV. Les coefficients de mélange sont calculés localement à chaque interface de sous-cellule afin d’imposer les propriétés de stabilité non linéaire requises. Le schéma reste ainsi robuste en présence de forts gradients, de chocs et de fronts sec-mouillé, tout en conservant une précision d’ordre élevé dans les zones régulières.<br><br>
Une attention particulière est portée à la discrétisation du terme source bathymétrique. Le schéma est exactement équilibré (<i>well-balanced</i>) pour les états stationnaires au repos grâce à des reconstructions hydrostatiques soigneusement définies à deux niveaux : entre les éléments, sur les traces polynomiales d’ordre élevé, puis entre les sous-cellules, sur les valeurs constantes par morceaux. Cette construction préserve les équilibres au repos sur des maillages entièrement non structurés, jusque dans chaque sous-cellule.<br><br>
La méthode est entièrement <i>a priori</i> : elle ne nécessite ni détection <i>a posteriori</i>, ni recalcul, ni adaptation locale, et demeure conservative par construction. Les expériences numériques montrent qu’elle capture précisément les interfaces sec-mouillé multidimensionnelles, contrôle les oscillations parasites au voisinage des discontinuités et résout des structures d’écoulement localisées à l’intérieur d’éléments de maillage relativement grands.
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
      <span class="pub-authors">S. Cardonna, A. Haidar, F. Marche &amp; F. Vilar</span>
      <span class="pub-title">Local subcell monolithic DG/FV methods for nonlinear shallow-water models with source terms</span>
      <span class="pub-tail"><i>Soumis</i></span>
    </div>
  </summary>

  <div class="pub-abstract">
Cet article apporte plusieurs contributions à l’approximation numérique des modèles d’écoulement en eau peu profonde. Nous introduisons une méthode monolithique locale subcell DG/FV d’ordre élevé pour des équations non linéaires à surface libre comportant des termes sources. Le cadre couvre à la fois les équations hyperboliques de Saint-Venant et les équations de Green–Naghdi, faiblement dispersives et pleinement non linéaires, qui constituent deux approximations asymptotiques des équations générales des vagues en régime d’eau peu profonde.<br><br>
La méthode part d’une formulation classique Discontinuous Galerkin (DG), réécrite comme une discrétisation particulière de type Finite Volume (FV) sur une sous-partition grâce à des flux d’interface reconstruits d’ordre élevé. Nous étudions en particulier la discrétisation des termes sources bathymétriques et des termes différentiels d’ordre supérieur issus des corrections dispersives. Des flux mélangés <i>a priori</i>, définis comme des combinaisons convexes des flux reconstruits d’ordre élevé et de flux FV robustes de premier ordre, sont introduits à chaque interface de sous-cellule. Leurs coefficients sont calculés de manière adaptative afin de garantir au niveau discret des propriétés de convexité essentielles, notamment la positivité de la hauteur d’eau.<br><br>
Le terme source bathymétrique est lui aussi discrétisé à l’échelle des sous-cellules à partir de l’approximation polynomiale DG. Nous montrons qu’un choix précis de reconstructions hydrostatiques, combinant plusieurs niveaux de précision aux échelles locale et globale, permet d’obtenir une propriété <i>well-balanced</i> jusque dans les sous-cellules et de préserver exactement les états stationnaires au repos.<br><br>
Nous couplons enfin cette stratégie locale subcell DG/FV, robuste et <i>well-balanced</i>, à une méthode Discontinuous Galerkin d’ordre élevé avec pénalisation intérieure afin d’approximer de manière cohérente et précise les contributions dispersives des équations de Green–Naghdi. Les expériences numériques mettent en évidence la convergence et la robustesse de l’approche, sa capacité à préserver les états stationnaires, à éviter les oscillations non physiques près des discontinuités et à maintenir la positivité de la hauteur d’eau.
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


<!-- ________________________________ -->

## Conférences et affiches
<hr style="margin-top: -0.1em; margin-bottom: 1em;">

<div class="talk-archive">
<details class="talk-year" open>
  <summary><span class="talk-year__label">2026</span><span class="talk-year__count">4 conférences</span><span class="talk-year__arrow" aria-hidden="true">›</span></summary>
  <div class="talk-timeline dot-timeline">
  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">4 mai 2026</span><span>Minho, Portugal</span></div>
      <h3><a href="https://shark-fv.eu/home-shark/">SHARK-FV26</a> <span class="talk-card__event-note">— Sharing Higher order Advanced Research Known-how on Finite Volume</span></h3>
      <p class="talk-card__title">Subcell monolithic DG/FV–HHO–SSP-RK scheme for a new wave-structure interaction model</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/SHARK_FV26.pdf">Diapositives</a></div>
    </div>
  </article>

  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">19 mars 2026</span><span>University of Waterloo · Waterloo, Canada</span></div>
      <h3><a href="https://uwaterloo.ca/applied-mathematics/events/applied-math-colloquium">Applied Maths Colloquium</a> <span class="talk-card__event-note">— Seminar of the Applied Mathematics group at UW</span></h3>
      <p class="talk-card__title">A high-order DG/FV convex property preserving scheme for hyperbolic systems with applications to shallow water flows and fluid-structure interaction</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/uw_colloquium.pdf">Diapositives</a></div>
    </div>
  </article>

  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">2 mars 2026</span><span>ENPC · Champs-sur-Marne, France</span></div>
      <h3><a href="https://cjcma2026.sciencesconf.org">CJC-MA</a> <span class="talk-card__event-note">— Congrès des Jeunes Chercheur.e.s en Mathématiques Appliquées</span></h3>
      <p class="talk-card__title">Modeling and numerical simulation of floating structures in shallow-water flows</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/CJCMA.pdf">Diapositives</a></div>
    </div>
  </article>

  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">19 février 2026</span><span>Montpellier, France</span></div>
      <h3>Métiers des mathématiques <span class="talk-card__event-note">— Conférence destinée aux étudiants de licence et de master</span></h3>
      <p class="talk-card__title">Modèles et méthodes numériques pour les interactions entre vagues et structures flottantes</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/metier_des_maths.pdf">Diapositives</a></div>
    </div>
  </article>

  </div>
</details>

<details class="talk-year" open>
  <summary><span class="talk-year__label">2025</span><span class="talk-year__count">3 conférences</span><span class="talk-year__arrow" aria-hidden="true">›</span></summary>
  <div class="talk-timeline dot-timeline">
  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">14 juillet 2025</span><span>McGill University · Montréal, Canada</span></div>
      <h3><a href="https://icosahom2025.org/index.html">ICOSAHOM</a> <span class="talk-card__event-note">— International Congress on Spectral and High Order Methods</span></h3>
      <p class="talk-card__title">Local subcell monolithic DG/FV scheme for NSW equations with source terms on unstructured grids</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/ICOSAHOM.pdf">Diapositives</a></div>
    </div>
  </article>

  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">2 juin 2025</span><span>Montpellier, France</span></div>
      <h3><a href="https://www.umontpellier.fr/agenda/semaine-du-pole-mips">MIPS Colloquia</a> <span class="talk-card__event-note">— Semaine du pôle Mathématiques, Informatique, Physique, Systèmes</span></h3>
      <p class="talk-card__title">Designing numerical methods for free-surface flows towards reliable wave-structure interactions</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/MIPS.pdf">Diapositives</a></div>
    </div>
  </article>

  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">13 mai 2025</span><span>Aussois, France</span></div>
      <h3><a href="https://cimav2025.sciencesconf.org">CIMAV</a> <span class="talk-card__event-note">— Congrès Interdisciplinaire sur les Modèles Avancés de Vagues</span></h3>
      <p class="talk-card__title">A high-order robust DG/FV scheme for nonlinear shallow water equations with source terms on unstructured grids</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/CIMAV.pdf">Diapositives</a></div>
    </div>
  </article>

  </div>
</details>

<details class="talk-year">
  <summary><span class="talk-year__label">2024</span><span class="talk-year__count">1 affiche</span><span class="talk-year__arrow" aria-hidden="true">›</span></summary>
  <div class="talk-timeline dot-timeline">
  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">15 mars 2024</span><span>Montpellier, France</span></div>
      <h3>Ph.D. Day <span class="talk-card__event-note">— Séminaire des Doctorants</span></h3>
      <p class="talk-card__title">Monolithic DG/FV schemes on 1D nonlinear shallow water equations</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/poster_phd_day24.pdf">Affiche</a></div>
    </div>
  </article>

  </div>
</details>

<details class="talk-year">
  <summary><span class="talk-year__label">2023</span><span class="talk-year__count">1 conférence</span><span class="talk-year__arrow" aria-hidden="true">›</span></summary>
  <div class="talk-timeline dot-timeline">
  <article>
    <span class="timeline-dot" aria-hidden="true"></span>
    <div class="talk-card">
      <div class="talk-card__meta"><span class="talk-card__date">25 octobre 2023</span><span>Montpellier, France</span></div>
      <h3>Introduction to newcomers <span class="talk-card__event-note">— Séminaire des Doctorants</span></h3>
      <p class="talk-card__title">Modeling, solving &amp; implementing PDEs from waves-structure interactions</p>
      <div class="talk-card__actions"><a class="resource-button" href="{{ site.url }}/files/talks/SEMDOC.pdf">Diapositives</a></div>
    </div>
  </article>
  </div>
</details>
</div>


## Déclaration de recherche
<hr style="margin-top: -0.1em; margin-bottom: 1em;">
 Mes recherches se situent à l'intersection de la modélisation mathématique, de l'analyse numérique et de l'étude des équations aux dérivées partielles (EDP) décrivant les écoulements de fluides. En particulier, au cours de ma thèse, je me suis concentré sur les systèmes non linéaires de lois d'équilibre hyperbolique, qui servent à modéliser l'évolution des quantités transportées et conservées dans le temps. Ces systèmes prennent la forme générale
<div style="text-align: center;">
$$
\partial_t \mathbf{U}(\mathbf{x},t) + \nabla_{\!\mathbf{x}} \cdot \mathbb{F}(\mathbf{U}) = \mathbf{S}(\mathbf{U}, \mathbf{x},t),
$$
</div>
où $\mathbf{U}$ représente le vecteur des variables conservées (nos inconnues), $\mathbb{F}$ la fonction de flux qui peut être non linéaire, et $\mathbf{S}$ termes sources possibles résultant de la géométrie, de forces externes ou d’effets de couplage. Le défi mathématique est que même des données initiales fluides peuvent générer des discontinuités en un temps fini, ce qui rend l’étude analytique de tels systèmes extrêmement délicate. En raison du manque de régularité des solutions faibles, seuls des résultats théoriques partiels sont disponibles, et l'approximation numérique de ces phénomènes doit souvent combiner précision d'ordre élevé avec stabilité et robustesse.

Parmi les nombreux exemples de tels systèmes, les équations non linéaires en eau peu profonde (NSW) jouent un rôle central dans la communauté des vagues ; ils fournissent un modèle asymptotique dérivé des équations d'Euler incompressibles sous l'hypothèse d'un petit rapport d'aspect (la profondeur du fluide est beaucoup plus petite que l'échelle horizontale). Malgré leur nature asymptotique, les équations en eaux peu profondes restent extrêmement utiles en pratique. Ils fournissent une description précise des principaux mécanismes physiques régissant les écoulements à surface libre, tout en évitant le coût de calcul prohibitif associé à la résolution des équations d'Euler ou de Navier-Stokes entièrement tridimensionnelles. Ils offrent ainsi un compromis efficace entre réalisme physique et efficacité numérique. Même s'ils ne tiennent pas compte des effets dispersifs (captés dans des modèles plus raffinés comme le Boussinesq ou Green–Naghdi systèmes), ils restent l’une des approximations les plus largement utilisées et les plus robustes pour les simulations pratiques d’écoulement.
Étant donné un paramétrage fluide $b$ de la variation bathymétrique, les équations NSW se lisent comme
<div style="text-align: center;">
$$
\begin{cases}
      \partial_t\:\!\eta + \nabla_{\!\mathbf{x}} \cdot \mathbf{q} = \mathbf{S}_1[b](\mathbf{v}), \\
      \partial_t \:\!\mathbf{q} + \nabla_{\!\mathbf{x}} \cdot \left( \mathbf{u} \otimes \mathbf{q} + \frac{g\eta}{2}(\eta - 2b)\mathbb{I}_2  \right) = \mathbf{S}_2[b](\mathbf{v}),
\end{cases} \nonumber
$$
</div>
avec $\mathbf{v} = (\eta,\mathbf{q})^t$, où $\eta$ est l'élévation totale de l'eau, $\mathbf{q}$ est le débit horizontal, et $\mathbf{S}\[b\](\mathbf{v})$ est un terme source générique pouvant contenir des effets de topographie, de frottement et/ou de Coriolis.

D’un point de vue numérique cependant, leur discrétisation pose plusieurs défis. Capturer à la fois les solutions lisses et les discontinuités nécessite des schémas stables en présence de chocs, préservant la positivité de la hauteur d'eau ($i.e.$ assurer au niveau discret que $H\geq0$), et maintenir des états stationnaires tels que l’équilibre dit « du lac au repos ». De plus, dans de nombreuses configurations réalistes, l’écoulement interagit avec des géométries complexes, des obstacles ou des frontières mobiles, ce qui nécessite des cadres numériques robustes et flexibles.

### Nouveaux cadres numériques d'ordre élevé pour l'asymptotique des eaux peu profondes
Dans l’analyse numérique des modèles non linéaires en eaux peu profondes, deux grandes familles de méthodes coexistent. D’une part, les systèmes classiques de volumes finis (FV) sont extrêmement robustes : ils sont capables de gérer les chocs naturels, les zones sèches et les variations brusques de topographie sans s’effondrer. Cependant, ils fournissent généralement une précision initialement faible et ont tendance à être trop diffusifs. En revanche, les méthodes par éléments finis, notamment discontinuous Galerkin (DG), peuvent atteindre des ordres de précision arbitrairement élevés et sont bien adaptées aux géométries complexes, mais elles sont beaucoup plus sensibles aux instabilités numériques et nécessitent des mécanismes de stabilisation supplémentaires pour garantir la robustesse.

La stratégie numérique que j'ai développée vise à combiner le meilleur des deux mondes dans un cadre unique et cohérent. En nous appuyant sur une méthode initialement introduite par mon directeur de thèse François Vilar, nous avons reformulé le domaine de calcul en subdivisant chaque élément du maillage en subcells et permettre aux représentations FV et DG de coexister localement, rendant possible la fusion de deux paradigmes normalement incompatibles au sein d'une structure unifiée. Grâce à un mélange convexe entre les contributions volumes finis (responsables de la robustesse) et celles DG d'ordre élevé (responsables de la précision), la méthode s'adapte dynamiquement à la régularité locale de la solution. Cela garantit que le schéma reste préservant la positivité, stable autour des états stables et précis dans les régions lisses.

Ce cadre a d'abord été développé et analysé dans un cadre unidimensionnel, dans un travail axé sur la construction de la méthode et sur la préservation de certaines propriétés théoriques clés. 
Dans ce premier article, nous avons également proposé une extension naturelle de l’approche du Green–Naghdi équations, qui forment une correction dispersive du système NSW.
En effet, dans ce contexte, les effets dispersifs sont reformulés comme un problème elliptique auxiliaire qui introduit un terme source supplémentaire dans les équations NSW. L’une des principales forces du cadre proposé réside précisément dans le traitement de ces termes sources : la méthode les traite de manière cohérente et unifiée, sans avoir recours à des artefacts numériques supplémentaires. La partie elliptique est résolue à l'aide d'un SWIP-DG (Pénalité intérieure pondérée symétrique Discontinuous Galerkin), garantissant stabilité et précision. Cette stratégie de couplage produit un modèle dispersif d'ordre élevé capable de capturer Green–Naghdi-type solutions avec une excellente précision et stabilité, tout en préservant la simplicité et la robustesse du solveur en eaux peu profondes.

Plus récemment, cette approche monolithique a été étendue aux maillages bidimensionnels non structurés. L'extension du cadre aux configurations bidimensionnelles représente une avancée majeure, tant techniquement que théoriquement. La formulation proposée résout avec succès ces difficultés et présente d'excellentes propriétés numériques : elle atteint une précision d'ordre élevé même sur des maillages grossiers et très irréguliers, tout en conservant sa robustesse en présence de bathymétries complexes, de fronts secs et de repères difficiles. Ces résultats confirment la polyvalence et l’efficacité de l’approche, ce qui en fait un outil prometteur pour les simulations réalistes à grande échelle des écoulements en eaux peu profondes.

### Structures flottantes dans des régimes d'eau peu profonde
La demande croissante d’énergie marine renouvelable a motivé l’étude de dispositifs flottants capables de convertir le mouvement des vagues en électricité. D'un point de vue mathématique, ces systèmes impliquent des interactions fluide-structure complexes, dans lesquelles la dynamique d'un corps flottant doit être couplée à l'écoulement à surface libre. En collaboration avec David Lannes, nous développons un cadre théorique et numérique unifié pour décrire de telles interactions dans un régime asymptotique en eaux peu profondes, dans le but à la fois de cohérence mathématique et d'efficacité de calcul.

Le modèle résultant combine trois composants complémentaires : un système hyperbolique régissant l'écoulement extérieur (les équations non linéaires des eaux peu profondes), un ensemble d'équations différentielles ordinaires et un problème elliptique décrivant la distribution de pression interne. Construire un solveur stable et précis pour ce système couplé nécessite de traiter ces composants au sein d’une formulation unique et cohérente qui préserve les principaux invariants physiques et mathématiques.

Pour y parvenir, nous nous appuyons sur DG/FV cadre introduit dans la section précédente pour la partie hyperbolique, et sur les discrétisations avancées pour la composante elliptique basées sur Hybrid High-Order (HHO), qui sont des schémas de type éléments finis combinant des inconnues de cellules et de faces pour atteindre une précision d'ordre élevé tout en conservant la conservation locale, l'efficacité de calcul et la flexibilité sur des maillages très généraux. Ce travail en cours constitue la troisième contribution principale de ma thèse. Il fournit un cadre mathématiquement bien posé et numériquement efficace pour la simulation des interactions vague-structure dans des régimes d'eau peu profonde, avec des applications potentielles à l'étude et à l'optimisation des convertisseurs d'énergie houlomotrice et d'autres systèmes flottants pertinents pour les technologies marines renouvelables.
