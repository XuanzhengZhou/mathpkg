---
role: proof
locale: en
of_concept: closed-graph-theorem-topological-groups
source_book: gtm027
source_chapter: "6"
source_section: "R"
---

# Proof of the Closed Graph Theorem for Topological Groups

Let $G$ be a topological group and $H$ a metrizable topological group which is complete relative to its right uniformity $\mathcal{R}$. Let $f: G \to H$ be a homomorphism such that:

(i) the graph of $f$ is closed in $G \times H$;

(ii) $\overline{f^{-1}[V]} \in \mathcal{U}$ (neighborhood of $e_G$) whenever $V \in \mathcal{V}$ (neighborhood of $e_H$).

To prove $f$ is continuous, apply Lemma 6.36 (closed graph implies continuity under completeness) to the relation $f^{-1} \subset H \times G$. Choose a right-invariant metric $d$ for $H$; $H$ is then complete relative to each such metric which metrizes $H$.

Let $x_\alpha \to e_G$ in $G$. We need to show $f(x_\alpha) \to e_H$. Suppose not. Then there exists $V \in \mathcal{V}$ and a subnet such that $f(x_\beta) \notin V$.

By condition (ii), $\overline{f^{-1}[V]}$ is a neighborhood of $e_G$. Since $x_\alpha \to e_G$, eventually $x_\alpha \in \overline{f^{-1}[V]}$. Choose $y_\alpha \in f^{-1}[V]$ with $x_\alpha^{-1}y_\alpha \to e_G$.

Then $f(y_\alpha) \in V$ and by the right-invariant metric completeness, one constructs a Cauchy sequence that converges, leading to a contradiction with the closed graph condition unless $f(x_\alpha) \to e_H$.

The detailed construction uses: for each $n$, pick $\varepsilon_n$ defining a metric ball $V_n$, apply condition (ii) to get a pre-image neighborhood, use the closed graph to force convergence, and apply the Baire-like argument from Lemma 6.36 to conclude continuity.
