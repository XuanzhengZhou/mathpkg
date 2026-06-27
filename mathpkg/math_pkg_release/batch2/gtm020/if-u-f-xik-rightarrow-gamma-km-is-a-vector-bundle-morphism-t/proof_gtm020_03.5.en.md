---
locale: en
of_concept: if-u-f-xik-rightarrow-gamma-km-is-a-vector-bundle-morphism-t
role: proof
source_book: gtm020
source_chapter: 3. Vector Bundles
source_section: '5'
---

The first statement is clear. For the second, let $f(b) = g(p^{-1}(b)) \in G_k(F^m)$, and let $u(x) = (f(p(x)), g(x)) \in E(\gamma_k^m)$ for $x \in E(\xi^k)$. We see that $f$ is continuous by looking at a local coordinate of $\xi$, and from this $u$ is also continuous.

5

If $S$ and $S'$ are two distinct subsets of $I$ each with $m$ elements, then $W(S) \cap W(S')$ is empty. In effect, there exist $i \in S$ with $i \notin S'$ and $j \in S'$ with $j \notin S$. For $b \in W(S)$ we have $\eta_i(b) > \eta_j(b)$, and for $b \in W(S')$ we have $\eta_j(b) > \eta_i(b)$. Therefore, $W(S) \cap W(S')$ is empty.

Let $W_m$ be the union of all $W(S(b))$ such that $S(b)$ has $m$ elements. Since $i \in S(b)$ yields the relation $W(S(b)) \subset V_i$, the bundle $\xi|W(S(b))$ is trivial, and since $W_m$ is a disjoint union, $\xi|W_m$ is trivial. Finally, under the last hypothesis, $W_j$ is empty for $n < j$.
