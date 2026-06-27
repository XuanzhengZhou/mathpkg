---
role: proof
locale: en
of_concept: sakai-normal-iff-sigma-continuous
source_book: gtm003
source_chapter: "6"
source_section: "6.9"
---

If $\varphi \in V_+$ then $\varphi$ is normal by (6.3). So suppose that $\varphi$ is normal.

(i) Let $P_0$ be the set of all projections $p$ in $W$ for which $\varphi_p : x \mapsto \varphi(xp)$ is $\sigma(W, V)$-continuous. If $S$ is a directed $(\leq)$ subset of $P_0$, then $r := \sup S$ is in $P_0$; we have $\lim_{q \in S} \varphi(r - q) = 0$ by hypothesis.

(ii) The core of the proof shows that $P_0$ is closed under taking suprema of directed sets and that the maximal element of $P_0$ (by Zorn's lemma) must be the unit $e$. The estimates

$$|\varphi(xp + xq)| \leq |\varphi(xp)| + |\varphi(xq)|,$$
and $$|\varphi(xq)| \leq \sqrt{\varphi(e)} \sqrt{\varphi(qx^*xq)} \leq \sqrt{\varphi(e)} \sqrt{\psi(qx^*xq)}$$

for a suitable $\psi \in V_+$ dominating $\varphi$ on $qWq$, show that $p + q \in P_0$ when $pq = 0$. Since the projections are norm-total in $W$, this forces $e \in P_0$, i.e., $\varphi$ is $\sigma(W, V)$-continuous.

The detailed argument uses the fact that the set of projections for which $\varphi_p$ is $\sigma(W, V)$-continuous contains approximate units and is closed under directed suprema, ultimately reaching the unit.
