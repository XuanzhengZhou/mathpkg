---
role: proof
locale: en
of_concept: smallest-uniformity-for-bounded-continuous-functions
source_book: gtm027
source_chapter: "6"
source_section: "G"
---

# Proof of Smallest Uniformity for Bounded Continuous Functions

Let $(X, \mathfrak{t})$ be a Tychonoff space and let $\beta X$ be its Stone-Čech compactification with compact uniformity $\mathfrak{u}_{\beta}$. Denote by $\mathfrak{u}_\beta|_X$ the relativization of $\mathfrak{u}_\beta$ to $X$ (i.e., the trace of the entourages on $X \times X$). Let $C_b(X)$ be the set of all bounded real-valued continuous functions on $X$.

First, each $f \in C_b(X)$ extends uniquely to a continuous function $\beta f : \beta X \to \mathbb{R}$ (by the universal property of the Stone-Čech compactification). Since $\beta X$ is compact, $\beta f$ is uniformly continuous with respect to the unique compact uniformity $\mathfrak{u}_\beta$. Consequently, the restriction $f = \beta f|_X$ is uniformly continuous with respect to $\mathfrak{u}_\beta|_X$. Hence every bounded real-valued continuous function on $X$ is uniformly continuous relative to $\mathfrak{u}_\beta|_X$.

Now let $\mathfrak{v}$ be any uniformity on $X$ such that every $f \in C_b(X)$ is uniformly continuous. We must show that $\mathfrak{u}_\beta|_X \subset \mathfrak{v}$ (i.e., $\mathfrak{v}$ is larger than or equal to $\mathfrak{u}_\beta|_X$).

The family $C_b(X)$ separates points from closed sets in $X$ (since $X$ is Tychonoff, and for any closed set $F$ and $x \notin F$, there is a continuous function $f : X \to [0,1]$ with $f(x) = 0$ and $f(F) = \{1\}$, which is bounded). The evaluation map $e : X \to \prod_{f \in C_b(X)} \overline{f(X)}$ is a topological embedding, and the product $\prod_f \overline{f(X)}$ is compact Hausdorff (each $\overline{f(X)}$ is a compact subset of $\mathbb{R}$). The closure of $e(X)$ in this product is homeomorphic to $\beta X$, and the compact uniformity of $\beta X$ is the relativization of the product uniformity.

For each $f \in C_b(X)$, uniform continuity of $f$ with respect to $\mathfrak{v}$ means: for every $\varepsilon > 0$, there exists $V \in \mathfrak{v}$ such that $(x,y) \in V$ implies $|f(x) - f(y)| < \varepsilon$. This is precisely the condition that the identity map $\operatorname{id} : (X, \mathfrak{v}) \to (X, \mathfrak{u}_\beta|_X)$ is uniformly continuous. Since both topologies coincide with $\mathfrak{t}$, this forces $\mathfrak{u}_\beta|_X \subset \mathfrak{v}$.

Therefore $\mathfrak{u}_\beta|_X$ is contained in every uniformity that makes all functions in $C_b(X)$ uniformly continuous, i.e., $\mathfrak{u}_\beta|_X$ is the *smallest* such uniformity. $\square$
