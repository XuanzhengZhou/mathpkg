---
role: proof
locale: en
of_concept: whitney-ctopology-composition-continuity
source_book: gtm014
source_chapter: "II"
source_section: "3"
---

**Proof.** Let $D$ be the fiber product $J^k(X, Y) \times_Y J^k(Y, Z)$ described in Lemma 3.7, where $A = J^k(X, Y)$, $B = J^k(Y, Z)$, $P = Y$, $\pi_A = \beta$ (the target mapping), and $\pi_B = \alpha$ (the source mapping). The composition of jets induces a mapping $\gamma: D \to J^k(X, Z)$ defined by $(\sigma, \tau) \mapsto \tau \cdot \sigma$, which is continuous. (Note that $\tau \cdot \sigma = j^k(g \circ f)(\alpha(\sigma))$ where $f$ represents $\sigma$ in $J^k(X, Y)$ and $g$ represents $\tau$ in $J^k(Y, Z)$.)

To prove the proposition it suffices to show: if $f \in C^\infty(X, Y)$, $g \in C^\infty(Y, Z)$, and $S \subset J^k(X, Z)$ is open with $g \circ f \in M(S)$, then there exist open sets $V \subset J^k(X, Y)$ and $W \subset J^k(Y, Z)$ with $\gamma(V \times_Y W) \subset S$. For then if $f' \in M(V)$ and $g' \in M(W)$, we have $g' \circ f' \in M(S)$, establishing continuity of composition in the Whitney $C^k$ topology for arbitrary $k$, and hence in the Whitney $C^\infty$ topology.

The existence of such $V$ and $W$ follows from Lemma 3.7. Since $X$ is compact, the $k$-jet extensions $j^k f(X) \subset J^k(X, Y)$ and $j^k g(\beta(j^k f(X))) \subset J^k(Y, Z)$ have compact closures, and the restrictions of the source/target projections to these compact sets are proper. Let $K = j^k f(X)$ and $L = j^k g(Y)$. The set $U = \gamma^{-1}(S) \cap D$ is an open neighborhood of $K \times_Y L$ in $D = J^k(X, Y) \times_Y J^k(Y, Z)$. Applying Lemma 3.7 yields neighborhoods $V$ of $K$ in $J^k(X, Y)$ and $W$ of $L$ in $J^k(Y, Z)$ such that $V \times_Y W \subset U = \gamma^{-1}(S)$, i.e., $\gamma(V \times_Y W) \subset S$, completing the proof.
