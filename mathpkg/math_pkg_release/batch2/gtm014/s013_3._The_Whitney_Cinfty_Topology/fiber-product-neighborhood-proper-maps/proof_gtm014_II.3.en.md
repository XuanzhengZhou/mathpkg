---
role: proof
locale: en
of_concept: fiber-product-neighborhood-proper-maps
source_book: gtm014
source_chapter: "II"
source_section: "3"
---

**Proof.** First note that if $X$ and $Y$ are Hausdorff spaces with $Y$ locally compact and if $f: X \to Y$ is continuous and proper, then $f$ is a closed mapping. For let $Z$ be a closed subset of $X$ and let $y \in \overline{f(Z)}$. Since $Y$ is locally compact, there is a compact neighborhood $C$ of $y$. Then $f^{-1}(C)$ is compact because $f$ is proper. The set $Z \cap f^{-1}(C)$ is closed in the compact set $f^{-1}(C)$, hence compact. Its image $f(Z \cap f^{-1}(C))$ is compact, hence closed, and contains $y$, so $y \in f(Z)$. Thus $f(Z)$ is closed.

Now, since $\pi_A|_K$ and $\pi_B|_L$ are proper, closed, and continuous, for each $x \in P$ we can find open neighborhoods $V_x$ of $K$ in $A$ and $W_x$ of $L$ in $B$ such that $V_x \times_P W_x \subseteq U$, and such that there is an open neighborhood $P_x$ of $x$ in $P$ with the property that $\overline{V_x} \subset A$ has $\pi_A(\overline{V_x}) \subset P_x$ and similarly $\pi_B(\overline{W_x}) \subset P_x$. This is possible using the properness conditions.

The collection $\{P_x\}_{x \in P}$ forms an open cover of $P$. Since $P$ is paracompact, there is a locally finite refinement $\{P_\alpha\}$. For each $\alpha$ choose a point $\alpha(p) \in P$ such that $P_\alpha \subset P_{\alpha(p)}$. Define
$$V_\alpha = V_{\alpha(p)} \cup \pi_A^{-1}(P - P_\alpha), \qquad W_\alpha = W_{\alpha(p)} \cup \pi_B^{-1}(P - P_\alpha).$$
Let
$$V = \bigcap_\alpha V_\alpha, \qquad W = \bigcap_\alpha W_\alpha.$$
To complete the proof we must verify that $K \subset V$, $L \subset W$, $V$ and $W$ are open, and $V \times_P W \subseteq U$.

**(a) $K \subset V$.** It suffices to show $K \subset V_\alpha$ for each $\alpha$. Let $k \in K$. We must show $k \in V_{\alpha(p)}$ or $k \in \pi_A^{-1}(P - P_\alpha)$. If $k \notin V_{\alpha(p)}$, then $\pi_A(k) \notin P_{\alpha(p)}$ and hence $\pi_A(k) \in P - P_{\alpha(p)} \subset P - P_\alpha$ (since $P_\alpha \subset P_{\alpha(p)}$), so $k \in \pi_A^{-1}(P - P_\alpha)$.

**(b) $L \subset W$.** Identical to (a), with $L$, $W$, $B$, $\pi_B$ replacing $K$, $V$, $A$, $\pi_A$.

**(c) $V$ is open.** Let $v \in V$. Since $\{P_\alpha\}$ is locally finite, there exists a neighborhood $U_v$ of $\pi_A(v)$ intersecting only finitely many $P_\alpha$, say $P_{\alpha_1}, \ldots, P_{\alpha_r}$. Set
$$U' = \pi_A^{-1}(U_v) \cap V_{\alpha_1} \cap \cdots \cap V_{\alpha_r}.$$
Then $U'$ is an open neighborhood of $v$. For any $\alpha$, if $U_v \cap P_\alpha = \varnothing$, then $U' \subset \pi_A^{-1}(P - P_\alpha) \subset V_\alpha$. If $U_v \cap P_\alpha \ne \varnothing$, then $\alpha = \alpha_i$ for some $i$ and $U' \subset V_{\alpha_i} = V_\alpha$. Hence $U' \subset V_\alpha$ for all $\alpha$, so $U' \subset V$. Thus $V$ is open. The proof that $W$ is open is identical.

**(d) $V \times_P W \subset U$.** Let $(v, w) \in V \times_P W$, so $\pi_A(v) = \pi_B(w) = p \in P$. Choose $\alpha$ such that $p \in P_\alpha$. Since $p \notin P - P_\alpha$, we have $v \notin \pi_A^{-1}(P - P_\alpha)$. Because $v \in V \subset V_\alpha$, this forces $v \in V_{\alpha(p)}$. Similarly, $w \in W_{\alpha(p)}$. Since $V_{\alpha(p)} \times_P W_{\alpha(p)} \subset U$ by construction, we obtain $(v, w) \in U$.
