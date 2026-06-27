---
role: proof
locale: en
of_concept: isthmus-removal-dimension-formulas
source_book: gtm054
source_chapter: "III"
source_section: "C"
---

By IIA10, $\dim(\mathcal{Z}(\Gamma)) = \dim(\pi_e[\mathcal{Z}(\Gamma)]) + \dim(\mathcal{P}(E + \{e\}) \cap \mathcal{Z}(\Gamma))$. By B4a, $\mathcal{P}(E + \{e\}) \cap \mathcal{Z}(\Gamma) = \mathcal{Z}(\Gamma_{(e)})$. Combining these, we get

$$\dim(\mathcal{Z}(\Gamma)) - \dim(\mathcal{Z}(\Gamma_{(e)})) = m,$$

where $m = \dim(\pi_e[\mathcal{Z}(\Gamma)])$. By IIA6, $\dim(\mathcal{Z}(\Gamma)) + \dim(\mathcal{Z}^\perp(\Gamma)) = \nu_1(\Gamma)$ while $\dim(\mathcal{Z}(\Gamma_{(e)})) + \dim(\mathcal{Z}^\perp(\Gamma_{(e)})) = \nu_1(\Gamma) - 1$. Substituting yields

$$\dim(\mathcal{Z}^\perp(\Gamma)) - \dim(\mathcal{Z}^\perp(\Gamma_{(e)})) = 1 - m.$$

By A15a, $\dim(\mathcal{Z}^\perp(\Gamma)) = \nu_0(\Gamma) - \nu_{-1}(\Gamma)$ and the analogous formula holds for $\Gamma_{(e)}$. Substituting yields

$$\nu_{-1}(\Gamma_{(e)}) - \nu_{-1}(\Gamma) = 1 - m.$$

If $e$ is an isthmus, no cycle contains $e$, so $\pi_e[\mathcal{Z}(\Gamma)] = \{\varnothing\}$ and $m = 0$. If $e$ is not an isthmus, some cycle contains $e$, so $\pi_e[\mathcal{Z}(\Gamma)] = \mathcal{P}(\{e\})$ and $m = 1$. The three formulas then give the stated results.
