# Documentation

- [Run the viewer and inspect outputs](reproduce.md).
- [Publication, funding and relationship to decarbonAIte](research-context.md).
- [Original research workflow and credited authors](original-readme.md).
- [Migration, retained history, and source provenance](migration.md).
- [Input data inventory](../data/README.md).

## Research context

The associated paper is *Towards digital twinning for multi-domain simulation workflows in urban design: a case study in Gothenburg*, Journal of Building Performance Simulation, 18(3), 311–332 (2025), DOI [10.1080/19401493.2024.2320112](https://doi.org/10.1080/19401493.2024.2320112). The publication metadata was checked against [Chalmers Research](https://research.chalmers.se/en/publication/546286).

The original README used an earlier title and left the DOI blank. Those historical notes are retained; the root README and citation metadata identify the published article.

## Methods and limits

The viewer renders precomputed results; it does not run CFD, noise, radiation, or EnergyPlus simulations. Coordinate transforms, heights, camera positions, option filenames, and color scales are case-study-specific. Editing them changes the presentation and should be recorded as a separate research change.

Three.js revision 149, lil-gui 0.17.0, and Papa Parse 5.3.2 are vendored in `libs/`. `index.html` also requests es-module-shims 1.3.6 from unpkg. The existing WebXR code is experimental; an undefined `defaultEnvironment` reference remains in its light-estimation shutdown path. This migration does not claim WebXR compatibility.

## Funding and maintainer questions

The [research context](research-context.md) records the published funding acknowledgments and explains the connection to decarbonAIte. Research-project attribution follows the cited sources; repository commit history identifies software contributors.

- TODO: provide the compatible CityModel JSON through an approved data access route and confirm data attribution and terms.
- TODO: supply a dedicated dataset/software archive DOI if one is established; no archive record was invented during migration.
