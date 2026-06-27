---
role: proof
locale: en
of_concept: proposition-6-9-degree-of-pullback-divisor
source_book: gtm052
source_chapter: "II"
source_section: "6"
---
It suffices to show $\deg f^*Q = \deg f$ for any closed point $Q \in Y$. Let $V = \text{Spec } B$ be an open affine containing $Q$. Let $A$ be the integral closure of $B$ in $K(X)$, so $U = \text{Spec } A = f^{-1}V$. Let $\mathfrak{m}_Q$ be the maximal ideal of $Q$ in $B$. Localizing with respect to $S = B - \mathfrak{m}_Q$, we obtain $C_Q \hookrightarrow A'$ where $A'$ is a finitely generated $C_Q$-module, torsion-free, rank $r = [K(X):K(Y)] = \deg f$, hence $A'$ is a free $C_Q$-module of rank $r$. If $t$ is a local parameter at $Q$, then $A'/tA'$ is a $k$-vector space of dimension $r$.

The points $P_i$ with $f(P_i) = Q$ correspond to maximal ideals $\mathfrak{m}_i$ of $A'$ with $A'_{\mathfrak{m}_i} = \mathcal{O}_{P_i}$. Then $tA' = \bigcap_i (tA'_{\mathfrak{m}_i} \cap A')$, so by the Chinese remainder theorem,
$$\dim_k A'/tA' = \sum_i \dim_k A'/(tA'_{\mathfrak{m}_i} \cap A') = \sum_i \dim_k \mathcal{O}_{P_i}/t\mathcal{O}_{P_i} = \sum_i v_{P_i}(t) = \deg f^*Q.$$
Thus $\deg f^*Q = r = \deg f$.
