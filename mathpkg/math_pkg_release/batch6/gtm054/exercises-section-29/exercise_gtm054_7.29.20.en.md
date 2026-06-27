---
role: exercise
locale: en
chapter: "7"
section: "29"
exercise_number: 20
---

Prove

separates the graph. Thus lobe “decompositions” of a graph are of interest only when the connectivity of the graph is at most 1. This section presents a method for decomposing a graph which is of interest as well for highly-connected graphs.

Since complete graphs do not admit separating sets, we shall assume for the rest of this section that $\Gamma$ is connected and not complete.

Let $\mathcal{S}(\Gamma)$ denote the set of separating sets of $\Gamma$ and let $\mathcal{S}_0(\Gamma)$ denote the subset of $\mathcal{S}(\Gamma)$ consisting of the smallest separating sets of $\Gamma$. Thus $|S| = \kappa(\Gamma)$ for all $S \in \mathcal{S}_0(\Gamma)$.

If $W \subseteq V$, we write $\overline{W} = V + W + N(W)$. If $W, \overline{W} \neq \varnothing$, then $N(W) \in \mathcal{S}(\Gamma)$, and so

$$\kappa(\Gamma) = \min\{|N(W)| : W, \overline{W} \neq \varnothing\}.$$

A fragment of $\Gamma$ is a subset $W \subseteq V$ such that $W, \overline{W} \neq \varnothing$ and $|N(W)| = \kappa(\Gamma)$.
