# Run and inspect the viewer

## Environment

Use a modern desktop browser with WebGL, ES modules, and Web Workers. The viewer uses the original vendored libraries listed in [the documentation index](README.md); it has no npm build or Python runtime dependency. Python 3 is used only for the standard-library download script and local server. Exact browser/OS support has not been established for the research prototype.

## Restore archived inputs

Run from the repository root:

```sh
python3 scripts/fetch_archived_data.py
python3 scripts/fetch_archived_data.py --check
```

The script restores 17 large CSV files using immutable links to the original source commit and verifies SHA-256 checksums. It refuses to overwrite a locally modified file. Restored files are intentionally ignored by Git. The original source commit remains accessible after its folders are removed from the collection's current branch. See [the data inventory](../data/README.md).

## Local example

```sh
python3 -m http.server 8000
```

1. Open `http://localhost:8000/?option=0`.
2. Choose **Ignore** in the CityModel prompt. The supplied data use the original fallback coordinate origin (319189, 6396991).
3. Wait for the loading overlay to disappear. Toggle radiation, wind, and noise in the Data controls. Use the mouse to move around the scene.
4. Open `http://localhost:8000/` to load all eight alternatives. Select an option in the control panel.
5. To color buildings by energy, reload and upload a compatible DTCC JSON file containing `Origin` and `Buildings` with `UUID`, `Footprint`, `Height`, and `GroundHeight`. This file is not included in the source snapshot. Option 1 contains the supplied energy CSV; other alternatives have no energy file configured.

Useful URL parameters include repeated `option=0&option=1` selectors and repeated `ignoreData=wind` selectors. VR can be requested with `?vr`, but requires a compatible device and secure context and was not validated during migration.

## Expected outputs and scope

The display contains colored point clouds for noise/radiation, a wind mesh, and building options, with legends and controls. Context buildings and their energy colors require the additional city model; supplied option STL meshes can load without it. The source assumptions and original scientific outputs are unchanged. No browser image comparison or numerical revalidation of simulations is claimed.

## GitHub Pages

The `pages.yml` workflow restores large inputs, stages only viewer runtime files, and deploys a Pages artifact. The deployed data are kept out of the repository's Git history. The intended new URL is `https://sb-chalmers.github.io/multidomain-viewer/`.

The original collection provides a 404-page redirect for its previous `/ComputationSustainableDesign/multidomainvis/` URL. Query strings and fragments are retained by that redirect.

## Checks performed during migration

On 2026-10-22, the local browser example for Option 0 loaded after choosing **Ignore** at the city-model prompt. Noise/radiation point clouds, the wind mesh, legends, and controls rendered. JavaScript syntax checks passed; archived input checksums and the static staging command passed. This was a desktop browser smoke check, not a simulation revalidation or WebXR test.
