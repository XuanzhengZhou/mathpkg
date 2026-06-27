---
role: exercise
locale: en
chapter: "9"
section: "48"
exercise_number: 24
---

(a) Under what conditions are complete matroids connected? (b) Under what conditions is the matroid of matched sets (of a multigraph) connected?

Analogous to Tutte connectivity for multigraphs (cf. §VIE), one can define $m$-connectedness for matroids (see [t.8]). If $\Lambda = (V, \mathcal{M})$ is a matroid with rank function $r$, we say that $\Lambda$ is $m$-separated if there exists $U \in \mathcal{P}(V)$ such that
(a) $m < \min\{|U|, |V + U|\}$;
(b) $m = r(U) + r(V + U) - r(V)$.

The connectivity of $\Lambda$ is given by

$$\tau(\Lambda) = \min\{m \in \mathbb{N} : \Lambda is m-separated\}$$

with $\tau(\Lambda) = \infty$ if $\Lambda$ is $m$-separated for no $m \in \mathbb{N}$.
