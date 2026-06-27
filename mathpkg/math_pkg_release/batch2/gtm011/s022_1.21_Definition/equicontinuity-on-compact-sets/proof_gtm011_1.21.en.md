---
role: proof
locale: en
of_concept: equicontinuity-on-compact-sets
source_book: gtm011
source_chapter: "1"
source_section: "1.21"
---

Let \(K \subset G\) be compact and let \(\epsilon > 0\). For each \(z_0 \in K\), since \(\mathcal{F}\) is equicontinuous at \(z_0\), there exists \(\delta(z_0) > 0\) such that for all \(f \in \mathcal{F}\) and all \(z \in G\) with \(|z - z_0| < \delta(z_0)\),

\[
d(f(z), f(z_0)) < \frac{\epsilon}{2}.
\]

The collection \(\{B(z_0, \delta(z_0)/2) : z_0 \in K\}\) forms an open cover of \(K\). By compactness of \(K\), there exist finitely many points \(z_1, \ldots, z_n \in K\) such that

\[
K \subset \bigcup_{i=1}^{n} B(z_i, \delta(z_i)/2).
\]

Set \(\delta = \min\{\delta(z_1)/2, \ldots, \delta(z_n)/2\} > 0\). Now let \(z, z' \in K\) with \(|z - z'| < \delta\). Choose \(i\) such that \(z \in B(z_i, \delta(z_i)/2)\). Then

\[
|z' - z_i| \leq |z' - z| + |z - z_i| < \delta + \frac{\delta(z_i)}{2} \leq \frac{\delta(z_i)}{2} + \frac{\delta(z_i)}{2} = \delta(z_i).
\]

Thus both \(z\) and \(z'\) lie in \(B(z_i, \delta(z_i))\). For any \(f \in \mathcal{F}\),

\[
d(f(z), f(z')) \leq d(f(z), f(z_i)) + d(f(z_i), f(z')) < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.
\]

Since \(z, z' \in K\) with \(|z - z'| < \delta\) were arbitrary and the estimate holds for every \(f \in \mathcal{F}\), \(\mathcal{F}\) is equicontinuous on \(K\).
