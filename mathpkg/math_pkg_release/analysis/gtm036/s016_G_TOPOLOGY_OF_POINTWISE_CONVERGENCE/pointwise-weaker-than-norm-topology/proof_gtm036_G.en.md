---
role: proof
locale: en
of_concept: pointwise-weaker-than-norm-topology
source_book: gtm036
source_chapter: "G"
source_section: "G"
---

For any finite subset $T \subset S$ and $\varepsilon > 0$, let $x \in U_{T, \varepsilon}$, i.e., $|x(s)| < \varepsilon$ for all $s \in T$. Since $T$ is finite, $\max_{s \in T} |x(s)| < \varepsilon$. If $\|x - y\|_\infty < \delta$ with $\delta = \varepsilon - \max_{s \in T} |x(s)| > 0$, then for every $s \in T$,
$$
|y(s)| \leq |y(s) - x(s)| + |x(s)| \leq \|y - x\|_\infty + |x(s)| < \delta + |x(s)| \leq \varepsilon,
$$
so $y \in U_{T, \varepsilon}$. Thus the norm open ball $B_\delta(x)$ is contained in $U_{T, \varepsilon}$, showing every pointwise-convergence basic neighborhood is open in the norm topology. Hence the pointwise convergence topology is weaker than the norm topology.

The identity mapping $\mathrm{id}: (E, \|\cdot\|_\infty) \to (E, \tau_{\text{ptwise}})$ is therefore continuous. Since $(E, \|\cdot\|_\infty)$ is a Banach space (hence metrizable) while $(E, \tau_{\text{ptwise}})$ is not metrizable, this identity map provides an example of a continuous image of a metrizable linear topological space that is not metrizable.
