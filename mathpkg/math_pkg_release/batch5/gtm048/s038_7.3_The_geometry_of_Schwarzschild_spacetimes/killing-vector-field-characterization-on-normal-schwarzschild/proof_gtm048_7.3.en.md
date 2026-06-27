---
role: proof
locale: en
of_concept: killing-vector-field-characterization-on-normal-schwarzschild
source_book: gtm048
source_chapter: "7"
source_section: "7.3"
---

The vector field $\partial/\partial t$ is Killing on $N$ by construction of the Schwarzschild metric, since the metric components are independent of $t$. Moreover, $g(\partial/\partial t, \partial/\partial t) = -(1 - 2\mu/r) < 0$ on $N$ (since $r > 2\mu$ on $N$), so $\partial/\partial t$ is timelike and future-pointing. Thus any scalar multiple $a \partial/\partial t$ with $a > 0$ is also Killing and future-pointing.

Conversely, suppose $X$ is a Killing vector field on $N$ that is future-pointing. Since the isometry group of $N$ contains the rotation group $\mathrm{SO}(3)$ acting on the $\mathcal{S}^2$ factor, and the metric is static, the Killing algebra decomposes. The Lemma (scaling-of-nowhere-zero-killing-vector-field) shows that any Killing field must be proportional to $\partial/\partial t$ on each $r = \text{const}$ slice, and continuity plus the connectedness of $N$ forces the proportionality constant to be global. Hence $X = a \partial/\partial t$ for some $a \in \mathbb{R}$.
