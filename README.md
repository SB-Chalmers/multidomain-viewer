# Multidomain Urban Design Viewer

![JavaScript](https://img.shields.io/badge/JavaScript-Three.js-blue)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Paper DOI](https://img.shields.io/badge/Paper_DOI-10.1080%2F19401493.2024.2320112-blue)](https://doi.org/10.1080/19401493.2024.2320112)

Explore urban design alternatives through combined energy, wind, noise, and solar radiation results in a browser.

## Context and aim

This Three.js viewer is the web visualization accompanying [Gonzalez-Caceres et al.'s Gothenburg multi-domain study](https://research.chalmers.se/publication/546286). It compares simulated design alternatives and provides an experimental WebXR mode. The article links directly to the viewer's original URL.

The work connects to [decarbonAIte](https://github.com/SB-Chalmers/decarbonAIte) through the group's wider DTCC and urban digital-twin research. See [publication provenance, funding and the documented connection](docs/research-context.md).

**Project status:** migrated research prototype. The migration preserves the original rendering and simulation assumptions; it is not a new validation of the case-study results.

## People and research outputs

Joakim Bohlin is credited for web development in the source project. Joakim Bohlin and Sanjay Somanath appear in the retained software commit history. The paper's complete research author list is preserved separately.

- **Paper:** [Towards digital twinning for multi-domain simulation workflows in urban design: a case study in Gothenburg](https://doi.org/10.1080/19401493.2024.2320112).
- **How to cite:** [CITATION.cff](CITATION.cff) distinguishes the software contributors from the associated paper.
- **Software/data archive DOI:** not established in the source; see [data provenance](data/README.md).

## Getting started

From the repository root, using Python 3 for data retrieval and the local HTTP server:

```sh
python3 scripts/fetch_archived_data.py
python3 -m http.server 8000
```

Open [the local viewer](http://localhost:8000/?option=0). At the CityModel prompt, choose **Ignore** to view the supplied environmental results without a city model. To include building energy colors, supply a compatible DTCC CityModel JSON file. Internet access is needed for the import-map shim in `index.html`.

See [docs/reproduce.md](docs/reproduce.md) for data checks, all alternatives, hosting, and limitations.

## Repository structure

`index.html` and `main.js` start the viewer; `src/` contains data loaders and rendering helpers; `libs/` contains the original browser libraries; `data/` contains small inputs and describes larger downloadable files; `docs/` holds methods and reproduction guidance. [migration.json](migration.json) records source paths and checksums.

## License and funding

Project code is licensed under [MIT](LICENSE); bundled third-party notices are retained. Input data provenance and terms are documented separately in [data/README.md](data/README.md). Funding references and remaining maintainer questions are in [docs/README.md](docs/README.md).
