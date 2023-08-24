---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.15.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Andreev qubits

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-input]
---
import xarray as xr
import hvplot.xarray
import warnings
warnings.filterwarnings("ignore")

andreev_data = xr.load_dataset("andreev_qubits.nc")

bstruct_plot = andreev_data.sel(phase=0).hvplot.scatter(width=300,
                                                        y="band_structure",
                                                        x="k",
                                                        by="level",
                                                        legend=False,
                                                        size=1,
                                                        c="spin",
                                                        ylim=(-80, 50),
                                                       )
andreev_plot = andreev_data.sel(k=0).hvplot.line(width=300,
                                                 y="andreev_energies",
                                                 x="phase",
                                                 by="level",
                                                 legend=False,
                                                 c="black",
                                                 title="",
                                                )

bstruct_plot + andreev_plot
```

```{code-cell} ipython3

```
