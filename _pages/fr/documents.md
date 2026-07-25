---
layout: archive
title: "Documents"
author_profile: true
permalink: /fr/documents/
lang: fr
translation_url: /documents/
---

{% include base_path %}

<div class="document-page">
  <header class="document-intro">
    <p class="document-lead">Une sélection de stages de recherche, de rapports et de projets réalisés au cours de ma formation universitaire.</p>
    <p class="document-note">Ces documents témoignent d’un travail en cours au moment de leur rédaction. Ils peuvent contenir des coquilles ou des arguments incomplets, mais restent disponibles pour retracer l’évolution de mon parcours.</p>
  </header>

  <section class="document-section">
    <div class="document-section__heading"><span>01</span><h2>Stages de recherche</h2></div>
    <div class="document-entries">
      <details class="document-entry">
        <summary>
          <span class="document-entry__index">01</span>
          <span class="document-entry__heading"><h3>Schéma local monolithique DG/FV subcells préservant les propriétés convexes pour les équations non linéaires de Saint-Venant</h3><p>Analyse numérique · Calcul scientifique</p></span>
          <span class="document-entry__arrow" aria-hidden="true">›</span>
        </summary>
        <div class="document-entry__body">
          <p class="document-entry__abstract">Construction et implémentation d’une nouvelle stratégie de stabilisation des méthodes discontinuous Galerkin pour les équations non linéaires de Saint-Venant, fondée sur une approche de type volumes finis subcells. Le travail porte sur un schéma monolithique DG/FV entièrement a priori et préservant les propriétés convexes.</p>
          <p class="document-entry__advisor"><b>Encadrants</b> · François Vilar et Fabien Marche</p>
          <div class="document-entry__actions"><a class="resource-button" href="{{ site.url }}/files/projects/Soutenance DG-FV4SW.pdf">Diapositives</a></div>
        </div>
      </details>

      <details class="document-entry">
        <summary>
          <span class="document-entry__index">02</span>
          <span class="document-entry__heading"><h3>Analyse asymptotique de suites d’EDP et théorie de l’homogénéisation</h3><p>Équations aux dérivées partielles · Homogénéisation</p></span>
          <span class="document-entry__arrow" aria-hidden="true">›</span>
        </summary>
        <div class="document-entry__body">
          <p class="document-entry__abstract">Étude de deux problèmes, dont un problème de Dirichlet posé sur un ouvert variable. La seconde partie modélise la formation du brouillard glacé — condensation de vapeur d’eau en gouttelettes qui gèlent rapidement — comme un problème d’homogénéisation.</p>
          <p class="document-entry__advisor"><b>Encadrant</b> · Michel Bellieud</p>
          <div class="document-entry__actions">
            <a class="resource-button" href="{{ site.url }}/files/projects/Homogeneisation.pdf">Rapport</a>
            <a class="resource-button" href="{{ site.url }}/files/projects/Soutenance homogeneisation.pdf">Diapositives</a>
          </div>
        </div>
      </details>

      <details class="document-entry">
        <summary>
          <span class="document-entry__index">03</span>
          <span class="document-entry__heading"><h3>De la géométrie différentielle au billard mathématique</h3><p>Géométrie différentielle · Systèmes dynamiques</p></span>
          <span class="document-entry__arrow" aria-hidden="true">›</span>
        </summary>
        <div class="document-entry__body">
          <p class="document-entry__abstract">Étude du billard mathématique comme système dynamique élémentaire, avec une caractérisation des trajectoires périodiques à partir de leur angle d’incidence initial. Travail réalisé avec Samuel Raë.</p>
          <p class="document-entry__advisor"><b>Encadrant</b> · Daniel Massart</p>
          <div class="document-entry__actions">
            <a class="resource-button" href="{{ site.url }}/files/projects/Billards.pdf">Rapport</a>
            <a class="resource-button" href="{{ site.url }}/files/projects/Soutenance billards.pdf">Diapositives</a>
          </div>
        </div>
      </details>

      <details class="document-entry">
        <summary>
          <span class="document-entry__index">04</span>
          <span class="document-entry__heading"><h3>Preuve du théorème de progression arithmétique de Dirichlet</h3><p>Théorie des nombres · Analyse complexe</p></span>
          <span class="document-entry__arrow" aria-hidden="true">›</span>
        </summary>
        <div class="document-entry__body">
          <p class="document-entry__abstract">Démonstration du fait que, pour deux entiers <i>a</i> et <i>b</i> premiers entre eux, la progression arithmétique <i>an + b</i> contient une infinité de nombres premiers, à l’aide d’outils issus notamment de l’analyse complexe et de la théorie des groupes.</p>
          <p class="document-entry__advisor"><b>Encadrant</b> · Sylvain Brochard</p>
          <div class="document-entry__actions">
            <a class="resource-button" href="{{ site.url }}/files/projects/Progression arithmetique.pdf">Rapport</a>
            <a class="resource-button" href="{{ site.url }}/files/projects/Soutenance progression arithmetique.pdf">Diapositives</a>
          </div>
        </div>
      </details>
    </div>
  </section>

  <section class="document-section">
    <div class="document-section__heading"><span>02</span><h2>Projets de cours</h2></div>
    <details class="document-projects">
      <summary>
        <span class="document-projects__summary"><strong>Projets et rapports</strong><span>7 éléments · rapports, notes et simulations</span></span>
        <span class="document-projects__arrow" aria-hidden="true">›</span>
      </summary>
      <div class="document-project-grid">
        <article class="document-project">
          <p class="document-project__label">Analyse numérique</p>
          <h3>Méthode Hybrid High-Order pour les opérateurs de Leray–Lions</h3>
          <p>Étude d’une méthode non conforme de type éléments finis et de ses principaux résultats d’analyse fonctionnelle discrète.</p>
          <div class="document-project__actions"><a class="resource-button" href="{{ site.url }}/files/projects/HHO pour Leray-Lions.pdf">Rapport</a></div>
        </article>

        <article class="document-project">
          <p class="document-project__label">Calcul scientifique</p>
          <h3>Implémentation C++ de la méthode SPH de Müller en dynamique des fluides</h3>
          <p>Construction et implémentation d’une méthode Smoothed Particle Hydrodynamics.</p>
          <div class="document-project__actions">
            <a class="resource-button" href="{{ site.url }}/files/projects/RapportSPH.pdf">Rapport</a>
            <a class="resource-button" href="https://drive.google.com/file/d/1cjR-ff4ITVlfS-i6fOHcgMsZEe19j2L_/view?usp=share_link">Simulation</a>
          </div>
        </article>

        <article class="document-project">
          <p class="document-project__label">Théorie de la mesure</p>
          <h3>Quelques résultats de théorie de la mesure</h3>
          <p>Mesures de Radon et théorèmes de Besicovitch, Vitali, Tietze et Lusin.</p>
          <div class="document-project__actions"><a class="resource-button" href="https://drive.google.com/drive/folders/13TeVJGtoIO5Xk9MxeGtBkZnzkxi8J9TG?usp=sharing">Notes</a></div>
        </article>

        <article class="document-project">
          <p class="document-project__label">Estimation d’erreur</p>
          <h3>Projets pour le cours d'estimations a posteriori</h3>
          <p>Résultats théoriques et implémentations en Fortran, Python et C++.</p>
          <div class="document-project__actions"><a class="resource-button" href="https://drive.google.com/drive/folders/1z1DtewZAjelfo_tHnjh6TZzA_A_a4aCj?usp=sharing">Rapports</a></div>
        </article>

        <article class="document-project">
          <p class="document-project__label">Analyse</p>
          <h3>Rapports pour les cours d'analyse</h3>
          <p>Résultats choisis sur les fonctions hölderiennes et la théorie des distributions.</p>
          <div class="document-project__actions"><a class="resource-button" href="https://drive.google.com/drive/folders/1pF1-KXYOm8rfycXRVeirWSbSoufYTr0s?usp=sharing">Rapports</a></div>
        </article>

        <article class="document-project">
          <p class="document-project__label">Algèbre</p>
          <h3>Rapports pour les cours d'algèbre</h3>
          <p>Automorphismes du cube, anneaux euclidiens et équations diophantiennes.</p>
          <div class="document-project__actions"><a class="resource-button" href="https://drive.google.com/drive/folders/12k5KvgNMU8iEU9qYQoFYRyaJ8ebhsgBu?usp=sharing">Rapports</a></div>
        </article>

        <article class="document-project">
          <p class="document-project__label">Apprentissage automatique</p>
          <h3>Projets de cours d'apprentissage automatique et d'optimisation</h3>
          <p>Analyse de jeux de données et implémentation de méthodes de régression en Python.</p>
          <div class="document-project__actions"><a class="resource-button" href="https://drive.google.com/drive/folders/1eqYNW_TL_0TBVxVPYGF3PJ686cYDTE3d?usp=sharing">Rapports</a></div>
        </article>
      </div>
    </details>
  </section>
</div>
