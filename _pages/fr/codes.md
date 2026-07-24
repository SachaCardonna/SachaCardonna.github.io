---
layout: archive
title: "Logiciels"
author_profile: true
permalink: /fr/logiciels/
lang: fr
translation_url: /codes/
---



{% include base_path %}

Découvrez les codes de calcul scientifique que j’ai développés ou auxquels j’ai contribué.

<section class="software-card">
<h2 class="software-entry__title">WaveBox — Plateforme numérique C++ multi-modèle pour les équations de vagues</h2>
<dl class="software-facts">
  <div><dt>Mots-clés</dt><dd>DG · HDG · Saint-Venant · Boussinesq · Green-Naghdi · FV subcells</dd></div>
  <div><dt>Stack</dt><dd>C++ · Python</dd></div>
  <div><dt>Équipe</dt><dd>Fabien Marche <span class="software-role">lead</span> · Sacha Cardonna · Arnaud Duran · Matthieu Rigal ··· </dd></div>
</dl>

<p>WaveBox est une plateforme numérique multi-modèle initiée par Fabien Marche pour approcher plusieurs modèles asymptotiques d’écoulements en eau peu profonde en dimension de surface d = 2. Elle combine efficacement les méthodes Hybridized Discontinuous Galerkin (HDG), Hybrid High-Order (HHO), DG/FV subcells monolithiques et DG sur des maillages non structurés généraux, pour les équations de Saint-Venant, Boussinesq et Green-Naghdi.</p>

<p class="software-features__title">Les principales caractéristiques sont :</p>
<ul class="software-features">
  <li>Co-calcul CPU–GPU entre sous-modèles ;</li>
  <li>Ordre de précision arbitraire (h-adaptivity et p-adaptivity) ;</li>
  <li>Traitement robuste du run-up et des phénomènes d’inondation, avec respect strict du principe du maximum ;</li>
  <li>Well-balancing pour les états stationnaires au repos ;</li>
  <li>Subdivision de maillages non structurés et mouvement ALE ;</li>
  <li>Traitement du déferlement par stratégie de commutation dynamique.</li>
</ul>

<div class="media-strip" style="justify-content: space-between;">
      <img src="{{ site.baseurl }}/images/cropped_2.gif" alt="WaveBox Image 2" style="width: 55%; height: auto;">
      <img src="{{ site.baseurl }}/images/cropped_1.gif" alt="WaveBox Image 1" style="width: 43%; height: auto;">
</div>

<details class="wavebox-disclosure">
  <summary class="wavebox-disclosure__summary">
    <span class="wavebox-disclosure__text">
      <strong>Simulations numériques</strong>
    </span>
    <span class="wavebox-disclosure__icon" aria-hidden="true">•••</span>
  </summary>

<section class="wavebox-gallery" aria-label="Simulations numériques WaveBox">
  <label class="wavebox-gallery__label" for="wavebox-select">Choisissez une simulation</label>
  <div class="wavebox-gallery__select-wrap">
    <select id="wavebox-select" class="wavebox-gallery__select">
      <option value="{{ site.baseurl }}/images/mesh_ale_evolution_laplacian.gif" data-type="image" data-degree="P² · ALE">Mouvement de maillage autour d'un cylindre oscillant (lissage laplacien)</option>
      <option value="{{ site.baseurl }}/images/mesh_ale_evolution_elasticity.gif" data-type="image" data-degree="P² · ALE">Mouvement du maillage autour d'un cylindre oscillant (pseudo-élasticité)</option>
      <option value="{{ site.baseurl }}/images/spring_beach.avi" data-type="video" data-degree="P¹ · ALE 2D">Vague run-up généré par un piston arrêté de manière impulsive</option>
      <option value="{{ site.baseurl }}/images/spring_ale.mp4" data-type="video" data-degree="P² · ALE 2D">Génération d'ondes périodiques par un piston oscillant</option>
      <option value="{{ site.baseurl }}/images/ale_dual.avi" data-type="video" data-degree="P¹ · ALE 2D">Cylindre de translation et d'oscillation en écoulement en eau peu profonde (1)</option>
      <option value="{{ site.baseurl }}/images/oscillating_cylinder.avi" data-type="video" data-degree="P¹ · ALE 2D">Cylindre de translation et d'oscillation dans un écoulement en eau peu profonde (2)</option>
      <option value="{{ site.baseurl }}/images/rock_wave_P6.mp4" data-type="video" data-degree="P⁶ · 2D">Vague qui s'effondre en interaction avec un rocher</option>
      <option value="{{ site.baseurl }}/images/tidal_P2.avi" data-type="video" data-degree="P² · 2D">Raz-de-marée interagissant avec un rocher (1)</option>
      <option value="{{ site.baseurl }}/images/tidal_P2_2.avi" data-type="video" data-degree="P² · 2D">Raz-de-marée interagissant avec un rocher (2)</option>
      <option value="{{ site.baseurl }}/images/wet_dam_break_P4.avi" data-type="video" data-degree="P⁴ · 2D">Rupture de barrage sur un lit mouillé</option>
      <option value="{{ site.baseurl }}/images/circ_dam_P3.avi" data-type="video" data-degree="P³ · 2D">Rupture de barrage circulaire sur lit mouillé</option>
      <option value="{{ site.baseurl }}/images/cg_periodic_P2.mp4" data-type="video" data-degree="P² · 2D">Solution périodique Carrier-Greenspan</option>
      <option value="{{ site.baseurl }}/images/tsunami_P2.mp4" data-type="video" data-degree="P² · 2D">Tsunami sur trois îles coniques</option>
      <option value="{{ site.baseurl }}/images/single_wave_stationnary.mp4" data-type="video" data-degree="P² · 2D">Vague unique sur ponton stationnaire partiellement immergé</option>
      <option value="{{ site.baseurl }}/images/prescribed_motion_object.avi" data-type="video" data-degree="P² · 2D">Générateur d'ondes 2D</option>
      <option value="{{ site.baseurl }}/images/pontoon_equilibrium_up.avi" data-type="video" data-degree="P² · 2D ">Ponton retour à l'équilibre (vers le haut)</option>
      <option value="{{ site.baseurl }}/images/pontoon_equilibrium_down.avi" data-type="video" data-degree="P² · 2D">Ponton retour à l'équilibre (vers le bas)</option>
      <option value="{{ site.baseurl }}/images/single_wave_newton.avi" data-type="video" data-degree="P⁵ · 2D">Une seule vague sur un ponton en mouvement libre</option>
      <option value="{{ site.baseurl }}/images/shock_wave_newton.avi" data-type="video" data-degree="P² · 2D">Onde de choc sur un ponton en mouvement libre</option>
      <option value="{{ site.baseurl }}/images/single_wave_stationnary_cylinder.avi" data-type="video" data-degree="P² · 2D">Onde unique sur un cylindre stationnaire partiellement immergé</option>
      <option value="{{ site.baseurl }}/images/single_wave_cylinder_beach.avi" data-type="video" data-degree="P¹ · 2D">Vague unique sur un cylindre fixe et une plage</option>
      <option value="{{ site.baseurl }}/images/GN_dispersive.gif" data-type="image" data-degree="P³ · 1D">Green–Naghdi rupture de barrage avec choc dispersif</option>
      <option value="{{ site.baseurl }}/images/1d_boat.gif" data-type="image" data-degree="P³ · 1D">Générateur d'ondes 1D</option>
      <option value="{{ site.baseurl }}/images/fixed_obj_topo.gif" data-type="image" data-degree="P⁶ · 1D">Vague interagissant avec un objet fixe et une topographie</option>
    </select>
  </div>

  <div class="wavebox-gallery__stage" id="wavebox-stage" aria-live="polite">
    <img src="{{ site.baseurl }}/images/single_wave_newton.avi" alt="Single wave on a freely moving pontoon">
  </div>

  <div class="wavebox-gallery__footer">
    <div class="wavebox-gallery__caption">
      <span id="wavebox-meta">P⁵ · 2D</span>
      <strong id="wavebox-caption">Une seule vague sur un ponton en mouvement libre</strong>
    </div>
    <div class="wavebox-gallery__nav" aria-label="Navigation entre les simulations">
      <button type="button" id="wavebox-prev" aria-label="Simulation précédente">←</button>
      <button type="button" id="wavebox-next" aria-label="Simulation suivante">→</button>
    </div>
  </div>
</section>
</details>

<style>
.wavebox-disclosure { margin: 1.4rem 0 2rem; }
.wavebox-disclosure__summary { display: flex; align-items: center; justify-content: space-between; gap: 1rem; min-height: 42px; padding: .45rem .2rem; border-top: 1px solid rgba(127,127,127,.2); border-bottom: 1px solid rgba(127,127,127,.2); color: var(--global-text-color-light); cursor: pointer; list-style: none; user-select: none; transition: color .18s ease, padding .18s ease; }
.wavebox-disclosure__summary::-webkit-details-marker { display: none; }
.wavebox-disclosure__summary:hover { padding-left: .4rem; color: var(--global-text-color); }
.wavebox-disclosure__text strong { font-size: .8rem; font-weight: 600; letter-spacing: .035em; text-transform: uppercase; }
.wavebox-disclosure__icon { flex: 0 0 auto; color: #899198; font-size: .78rem; letter-spacing: .16em; line-height: 1; transition: transform .2s ease; }
.wavebox-disclosure[open] .wavebox-disclosure__icon { transform: rotate(90deg); }
.wavebox-gallery { margin-top: .75rem; overflow: hidden; border: 1px solid rgba(127,127,127,.24); border-radius: 14px; background: var(--global-bg-color, #fff); box-shadow: 0 12px 34px rgba(0,0,0,.07); }
.wavebox-gallery__footer { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 1.15rem 1.35rem; }
.wavebox-gallery__label { margin: 0; color: #65717d; font-size: .68rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
.wavebox-gallery__count { color: #78838e; font-size: .72rem; font-variant-numeric: tabular-nums; white-space: nowrap; }
.wavebox-gallery__count strong { color: inherit; font-size: .95rem; }
.wavebox-gallery__label { display: block; padding: 1rem 1.35rem .45rem; }
.wavebox-gallery__select-wrap { position: relative; margin: 0 1.35rem 1rem; }
.wavebox-gallery__select-wrap::after { content: "⌄"; position: absolute; top: 50%; right: 1rem; transform: translateY(-56%); pointer-events: none; font-size: 1.1rem; }
.wavebox-gallery__select { width: 100%; min-height: 46px; padding: .65rem 2.7rem .65rem .85rem; border: 1px solid rgba(127,127,127,.32); border-radius: 9px; background: var(--global-bg-color, #fff); color: inherit; font: inherit; font-size: .84rem; appearance: none; cursor: pointer; }
.wavebox-gallery__select:focus-visible, .wavebox-gallery__nav button:focus-visible { outline: 3px solid rgba(82,146,204,.35); outline-offset: 2px; }
.wavebox-gallery__stage { display: grid; place-items: center; min-height: 300px; aspect-ratio: 16 / 9; background: var(--global-bg-color, #fff); overflow: hidden; }
.wavebox-gallery__stage img, .wavebox-gallery__stage video { display: block; width: 100%; height: 100%; max-height: 580px; object-fit: contain; margin: 0; }
.wavebox-gallery__caption { display: grid; gap: .2rem; min-width: 0; }
.wavebox-gallery__caption span { color: #65717d; font-size: .68rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
.wavebox-gallery__caption strong { font-size: .83rem; line-height: 1.35; }
.wavebox-gallery__nav { display: flex; gap: .45rem; flex: 0 0 auto; }
.wavebox-gallery__nav button { width: 38px; height: 38px; border: 1px solid rgba(127,127,127,.3); border-radius: 50%; background: transparent; color: inherit; font-size: 1rem; cursor: pointer; transition: transform .18s ease, background .18s ease; }
.wavebox-gallery__nav button:hover { transform: translateY(-1px); background: rgba(127,127,127,.1); }
@media (max-width: 600px) { .wavebox-gallery__footer { padding: 1rem; } .wavebox-gallery__label { padding: .85rem 1rem .4rem; } .wavebox-gallery__select-wrap { margin: 0 1rem 1rem; } .wavebox-gallery__stage { min-height: 210px; } }
@media (prefers-reduced-motion: reduce) { .wavebox-disclosure__summary, .wavebox-disclosure__icon, .wavebox-gallery__nav button { transition: none; } }
</style>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var select = document.getElementById('wavebox-select');
  if (!select) return;
  var stage = document.getElementById('wavebox-stage');
  var caption = document.getElementById('wavebox-caption');
  var meta = document.getElementById('wavebox-meta');
  var disclosure = document.querySelector('.wavebox-disclosure');
  disclosure.open = false;

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
  }

  select.addEventListener('change', function () { showSimulation(select.selectedIndex); });
  document.getElementById('wavebox-prev').addEventListener('click', function () { showSimulation(select.selectedIndex - 1); });
  document.getElementById('wavebox-next').addEventListener('click', function () { showSimulation(select.selectedIndex + 1); });
  disclosure.addEventListener('toggle', function () {
    if (!disclosure.open) {
      var video = stage.querySelector('video');
      if (video) video.pause();
    }
  });
  showSimulation(select.selectedIndex);
});
</script>
</section>

<section class="software-card">
<h2 class="software-entry__title">ManicoreFV — Code discontinuous Galerkin pour les lois de conservation sur surfaces</h2>
<dl class="software-facts">
  <div><dt>Mots-clés</dt><dd>Discontinuous Galerkin · Volumes finis · Lois de conservation · EDP de surface · Maillages courbes</dd></div>
  <div><dt>Stack</dt><dd>C++ · Python</dd></div>
  <div><dt>Équipe</dt><dd>Marien Hanot · Sacha Cardonna</dd></div>
</dl>

<p>ManicoreFV est une plateforme C++ consacrée à l’approximation numérique de lois de conservation sur des surfaces courbes par des méthodes discontinuous Galerkin et volumes finis. Il s’agit d’un fork de <a href="https://mlhanot.github.io/Manicore/">Manicore</a>, le code développé par Marien Hanot pour implémenter des schémas numériques sur des variétés munies de métriques riemanniennes générales.</p>

<p class="software-features__title">Les principales caractéristiques sont :</p>
<ul class="software-features">
  <li>Formulations tenant compte de la géométrie basées sur les cartes locales, les paramétrisations et les métriques riemanniennes fournies par le framework Manicore ;</li>
  <li>Discrétisations discontinuous Galerkin de lois de conservation scalaires sur surfaces courbes, du degré zéro aux approximations polynomiales d’ordre élevé ;</li>
  <li>Intégration temporelle explicite de Runge–Kutta avec choix du pas de temps fondé sur une condition CFL ;</li>
  <li>Limiteur préservant les bornes pour les solutions discontinues, tout en conservant les moyennes locales et la masse globale.</li>
</ul>

<div class="media-strip" style="justify-content: space-between;">
      <img src="{{ site.baseurl }}/images/limDG.gif" alt="manicore Image 2" style="width: 55%; height: auto;">
      <img src="{{ site.baseurl }}/images/slice_limDG.gif" alt="manicore Image 1" style="width: 43%; height: auto;">
</div>

<details class="wavebox-disclosure manicore-disclosure">
  <summary class="wavebox-disclosure__summary">
    <span class="wavebox-disclosure__text">
      <strong>Simulations numériques</strong>
    </span>
    <span class="wavebox-disclosure__icon" aria-hidden="true">•••</span>
  </summary>

  <section class="wavebox-gallery" aria-label="Simulations numériques ManicoreFV">
    <label class="wavebox-gallery__label" for="manicore-select">Choisissez une simulation</label>
    <div class="wavebox-gallery__select-wrap">
      <select id="manicore-select" class="wavebox-gallery__select">
        <option value="{{ site.baseurl }}/images/code_manicore/equatorial_slice_crenel_DG.gif" data-type="image" data-meta="P³ · Equatorial slice">Advection linéaire (créneau) - Profil équatorial DG</option>
        <option value="{{ site.baseurl }}/images/code_manicore/equatorial_slice_crenel_limDG.gif" data-type="image" data-meta="P³ · Equatorial slice">Advection linéaire (créneau) - Profil équatorial DG limité</option>
        <option value="{{ site.baseurl }}/images/code_manicore/equatorial_slice_gaussian.gif" data-type="image" data-meta="P³ · Equatorial slice">Advection linéaire (gaussienne) - Profil équatorial DG</option>
        <option value="{{ site.baseurl }}/images/code_manicore/shallow_water_equatorial_slice.gif" data-type="image" data-meta="P¹ · Equatorial slice">Eaux peu profondes (rupture de barrage circulaire) - Profil équatorial DG limité</option>
        <option value="{{ site.baseurl }}/images/code_manicore/dg.avi" data-type="video" data-meta="P³ · Surface view">Advection linéaire (créneau) - Solution DG</option>
        <option value="{{ site.baseurl }}/images/code_manicore/limDG.avi" data-type="video" data-meta="P³ · Surface view">Advection linéaire (créneau) - Solution DG limitée</option>
        <option value="{{ site.baseurl }}/images/code_manicore/gaussian.avi" data-type="video" data-meta="P³ · Surface view">Advection linéaire (gaussienne) - Solution DG</option>
        <option value="{{ site.baseurl }}/images/code_manicore/dam_break_P1.avi" data-type="video" data-meta="P¹ · Surface view">Eaux peu profondes (rupture de barrage circulaire) - Solution DG limitée</option>
      </select>
    </div>

    <div class="wavebox-gallery__stage" id="manicore-stage" aria-live="polite">
      <img src="{{ site.baseurl }}/images/code_manicore/equatorial_slice_crenel_DG.gif" alt="Discontinuous Galerkin square profile simulation">
    </div>

    <div class="wavebox-gallery__footer">
      <div class="wavebox-gallery__caption">
        <span id="manicore-meta">Tranche équatoriale · GIF</span>
        <strong id="manicore-caption">Discontinuous Galerkin profil carré</strong>
      </div>
      <div class="wavebox-gallery__nav" aria-label="Navigation entre les simulations ManicoreFV">
        <button type="button" id="manicore-prev" aria-label="Simulation précédente">←</button>
        <button type="button" id="manicore-next" aria-label="Simulation suivante">→</button>
      </div>
    </div>
  </section>
</details>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var select = document.getElementById('manicore-select');
  if (!select) return;

  var stage = document.getElementById('manicore-stage');
  var caption = document.getElementById('manicore-caption');
  var meta = document.getElementById('manicore-meta');
  var disclosure = document.querySelector('.manicore-disclosure');
  disclosure.open = false;

  function showManicoreSimulation(index) {
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
      media.alt = option.text + ' simulation';
    }

    media.src = option.value;
    media.setAttribute('aria-label', option.text + ' simulation');
    stage.appendChild(media);
    caption.textContent = option.text;
    meta.textContent = option.dataset.meta;
  }

  select.addEventListener('change', function () {
    showManicoreSimulation(select.selectedIndex);
  });
  document.getElementById('manicore-prev').addEventListener('click', function () {
    showManicoreSimulation(select.selectedIndex - 1);
  });
  document.getElementById('manicore-next').addEventListener('click', function () {
    showManicoreSimulation(select.selectedIndex + 1);
  });
  disclosure.addEventListener('toggle', function () {
    if (!disclosure.open) {
      var video = stage.querySelector('video');
      if (video) video.pause();
    }
  });
  showManicoreSimulation(select.selectedIndex);
});
</script>
</section>

<section class="software-card">
<h2 class="software-entry__title">Bfree — Solveur volumes finis préservant la structure pour une magnétohydrodynamique idéale</h2>
<dl class="software-facts">
  <div><dt>Mots-clés</dt><dd>Magnétohydrodynamique · Schémas sans divergence · Volumes finis · Méthodes semi-implicites · ALE</dd></div>
  <div><dt>Stack</dt><dd>Fortran · Python</dd></div>
  <div><dt>Équipe</dt><dd>Walter Boscheri <span class="software-role">lead</span> · Mattia Lupi · Elena Bernardelli · Lidia Gude Vila · Sacha Cardonna</dd></div>
</dl>

<p>Bfree est une plateforme numérique de recherche pour la simulation bidimensionnelle de la magnétohydrodynamique idéale et des écoulements Euler–Heat. Elle vise à concevoir des méthodes de volumes finis structure-preserving qui maintiennent au niveau discret les contraintes différentielles fondamentales : la condition de divergence nulle du champ magnétique en MHD idéale et la condition de rotationnel nul de l’impulsion thermique pour le modèle Euler–Heat.</p>

<p class="software-features__title">Les principales caractéristiques sont :</p>
<ul class="software-features">
  <li>Discrétisations sans divergence pour le champ magnétique en MHD idéal ;</li>
  <li>Discrétisations à rotationnel nul pour l’impulsion thermique dans le système Euler–Heat ;</li>
  <li>Schémas explicites de volumes finis Arbitrary Lagrangian–Eulerian (ALE) sur maillages mobiles ;</li>
  <li>Schémas volumes finis semi-implicites pour les régimes à faible nombre de Mach et à faible nombre d'Alfvén ;</li>
  <li>Évolution structure-preserving des contraintes différentielles discrètes ;</li>
  <li>Discrétisations spatiales d’ordre un et deux ;</li>
  <li>Suivi conservatif de la masse et de l’énergie totale.</li>
</ul>

<div class="media-strip" style="justify-content: space-between;">
      <img src="{{ site.baseurl }}/images/bfree2.gif" alt="bfree Image 2" style="width: 32%; height: auto;">
      <img src="{{ site.baseurl }}/images/bfree1.gif" alt="bfree Image 1" style="width: 32%; height: auto;">
      <img src="{{ site.baseurl }}/images/bfree3.gif" alt="bfree Image 4" style="width: 32%; height: auto;">
</div>
</section>

<section class="software-card">
<h2 class="software-entry__title">ShoreVPINN - Solveur neuronal variationnel basé sur la physique pour les écoulements en eaux peu profondes</h2>
<dl class="software-facts">
  <div><dt>Mots-clés</dt><dd>Variational PINNs · Équations de Saint-Venant · Interfaces sec-mouillé · Run-up</dd></div>
  <div><dt>Stack</dt><dd>Python · PyTorch</dd></div>
  <div><dt>Équipe</dt><dd>Ali Haidar · Sacha Cardonna</dd></div>
</dl>

<p>ShoreVPINN est un code de recherche en Python qui explore les Variational Physics-Informed Neural Networks (VPINNs) pour approcher les équations non linéaires de Saint-Venant en dimension un. Plutôt que de s’appuyer uniquement sur des évaluations ponctuelles des équations, les résidus physiques sont intégrés contre des fonctions tests locales sur un maillage spatial. Cette formulation faible est particulièrement adaptée aux écoulements avec topographie variable et interfaces sec-mouillé mobiles.</p>

<p class="software-features__title">Les principales caractéristiques sont :</p>
<ul class="software-features">
  <li>Application variationnelle des équations de masse et de quantité de mouvement à l'aide de fonctions de test locales par éléments finis ;</li>
  <li>Préservation exacte de la condition initiale grâce à un ansatz neuronal fortement contraint ;</li>
  <li>Traitement préservant la positivité de la profondeur de l'eau ;</li>
  <li>Formulation robuste du flux de quantité de mouvement au voisinage des interfaces sec-mouillé ;</li>
  <li>Maillages spatiaux non uniformes avec raffinement local optionnel dans la région de run-up ;</li>
  <li>Quadrature de Gauss-Legendre et batching stochastique sur des tranches de temps ;</li>
  <li>Exécution automatique sur CPU, CUDA GPUs et Apple Silicon GPUs.</li>
</ul>

<div class="media-strip" style="justify-content: space-between;">
      <img src="{{ site.baseurl }}/images/shorevpinn1.gif" alt="WaveBox Image 2" style="width: 48%; height: auto;">
      <img src="{{ site.baseurl }}/images/shorevpinn2.gif" alt="WaveBox Image 1" style="width: 48%; height: auto;">
</div>
</section>

<section class="software-card">
<h2 class="software-entry__title">DG4SCL - Code compact et convivial pour les étudiants pour les méthodes DG sur 1D SCL</h2>
<dl class="software-facts">
  <div><dt>Mots-clés</dt><dd>Discontinuous Galerkin · Lois de conservation scalaires</dd></div>
  <div><dt>Stack</dt><dd>C++ · Python</dd></div>
  <div><dt>Développeur</dt><dd>Sacha Cardonna</dd></div>
</dl>

<p>Au début de mon stage avec F. Vilar et F. Marche, j’ai développé un code C++ compact consacré aux schémas discontinuous Galerkin (DG) pour les lois de conservation en dimension un.</p>
<p>Ce code est un travail en cours, loin d'être complet ou impeccable. Sa création a été motivée par mon engagement envers la simplicité et la compréhensibilité. Je me suis efforcé de faire en sorte que la structure et la mise en œuvre du code soient aussi simples que possible, permettant aux utilisateurs de comprendre facilement les concepts sous-jacents.</p>
<p>En élargissant ses fonctionnalités et en la rendant plus complète, mon objectif est de créer une ressource précieuse pour les étudiants à la recherche d'un exemple simplifié de régimes DG. Cet effort découle de mes propres expériences en tant qu'étudiant, où l'accès à une telle ressource aurait grandement facilité ma compréhension et mon processus d'apprentissage.</p>
<p>Contactez-moi pour obtenir la source.</p>

</section>
