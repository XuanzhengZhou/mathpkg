---
role: proof
locale: en
of_concept: theorem-11-7-no-definable-wellordering
source_book: gtm008
source_chapter: "11"
source_section: "11 The Independence of V = L and the CH"
---

**Proof.** Suppose $\varphi$ is a formula of $\mathcal{L}_0(C(M))$ defining a well-ordering of $\mathcal{P}(\omega)$ in $M[G]$. Then there exists $p \in G$ such that

$$p \Vdash "\varphi \text{ well-orders } \mathcal{P}(\omega)".$$

Since $\tilde{a}(G) \in M[G]$, there is a term $t_0$ of the ramified language such that $\tilde{a}(G) = D_{M[G]}(t_0)$. As $\tilde{a}(G) \subseteq \omega$, there exists $p \in G$ such that

$$p \Vdash "\{t_0 \Delta k \mid k \subseteq \omega \wedge \overline{k} < \omega\} \text{ has a } \varphi\text{-first element}"$$

where $a_1 \Delta a_2 \triangleq (a_1 \cup a_2) - (a_1 \cap a_2)$ is the symmetric difference.

Now one checks that for the automorphism $\pi_k$ defined above,

$$\tilde{a}(\pi_k''(G)) = \tilde{a}(G) \Delta k.$$

Since $\pi_k \in M$ and $\pi_k''(G)$ is also $P$-generic over $M$ (by Theorem 11.5), and $M[\pi_k''G] = M[G]$, the image of the well-order under $\pi_k$ would also be a well-order. But the set $\{t_0 \Delta k \mid k \subseteq \omega \wedge \overline{k} < \omega\}$ is infinite, so having a $\varphi$-first element contradicts the fact that for any $k$, the element $\tilde{a}(G) \Delta k$ is also $\tilde{a}(\pi_k''(G))$ and thus also belongs to the generic extension under the same forcing conditions.

Therefore no such definable well-ordering exists in $M[G]$. $\square$
