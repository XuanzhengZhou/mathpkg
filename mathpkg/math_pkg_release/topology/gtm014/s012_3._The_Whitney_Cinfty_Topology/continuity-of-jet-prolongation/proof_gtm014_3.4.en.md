---
role: proof
locale: en
of_concept: continuity-of-jet-prolongation
source_book: gtm014
source_chapter: "I. Preliminaries on Manifolds"
source_section: "3. The Whitney C∞ Topology"
---

*Proof.* Choose a metric $d$ on $J^k(X, Y)$ compatible with its topology (possible since $J^k(X, Y)$ is a smooth manifold and all manifolds are metrizable). Let $d_0$ be a metric on $J^0(X, J^k(X, Y))$ compatible with its topology. For $f \in C^\infty(X, Y)$, a basic open neighborhood of $j^k f$ in the Whitney $C^k$ topology on $C^\infty(X, J^k(X, Y))$ has the form

$$B^{(0)}_\varepsilon(j^k f) = \{\, h \in C^\infty(X, J^k(X, Y)) \mid \forall x \in X,\ d_0(j^0(j^k f)(x), j^0 h(x)) < \varepsilon(x) \,\}$$

for some continuous $\varepsilon: X \to \mathbf{R}^+$. Since $j^0(j^k f)(x) = (x, j^k f(x))$ and $j^0(j^k g)(x) = (x, j^k g(x))$, the metric $d_0$ on $J^0(X, J^k(X, Y))$ induces a comparison of values in $J^k(X, Y)$ via the fiberwise identification. By choosing $d_0$ appropriately (e.g., as a product metric with the source fixed), we may assume that $d_0((x, \sigma), (x, \tau)) = d(\sigma, \tau)$ for all $x \in X$ and $\sigma, \tau \in J^k(X, Y)$ with $\alpha(\sigma) = \alpha(\tau) = x$.

Now take $\delta = \varepsilon$. Then for any $g \in B_\delta(f)$, we have by definition

$$d(j^k f(x), j^k g(x)) < \delta(x) = \varepsilon(x) \quad \text{for all } x \in X.$$

Hence $d_0(j^0(j^k f)(x), j^0(j^k g)(x)) = d(j^k f(x), j^k g(x)) < \varepsilon(x)$ for all $x \in X$, which means $j^k g \in B^{(0)}_\varepsilon(j^k f)$. Thus $j^k(B_\delta(f)) \subseteq B^{(0)}_\varepsilon(j^k f)$, proving that $j^k$ is continuous at $f$. Since $f$ was arbitrary, $j^k$ is continuous. $\square$
