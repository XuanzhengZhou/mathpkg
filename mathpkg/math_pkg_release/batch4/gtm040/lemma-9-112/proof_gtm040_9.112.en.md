---
role: proof
locale: en
of_concept: lemma-9-112
source_book: gtm040
source_chapter: "9"
source_section: "112"
---

**Proof:** By hypothesis and by Propositions 9-109 and 9-110,

$$0 \geq \lambda^E(g' - g) \geq (-\alpha f')k(E) + (\alpha f)k(E).$$

From this it follows that $\alpha f

discuss the effect of the change after proving that equilibrium potentials exist.

Theorem 9-114: Any set $E$ in $\mathcal{L}$ has a unique equilibrium potential. The equilibrium charge is $l^E$ and the value of the equilibrium potential on the set is $-k(E)$. For $j$ not in $E$ it has the value $-k(E) - E d_j$.

Proof: Lemma 9-95, together with the fact that $\alpha l^E = 1$, shows that $-K l^E$ is an equilibrium potential and has the values specified in the theorem.

Conversely, if $f$ is an equilibrium charge, then by Proposition 9-109, $f_E = (I - P^E)g_E + (\alpha f)l^E = (I - P^E)g_E + l^E$. Since $g_E$ is constant and $P^E = 1$, $(I - P^E)g_E = 0$. Thus $f_E = l^E$, and the equilibrium potential is unique.

If we renormalize the equilibrium potential for $E$ so that its value is one on $E$, then its total charge becomes $-1/k(E)$. Thus if we were following the definitions of transient potential theory, we would define $-1/k(E)$ to be the capacity of $E$. The set function $-1/k(E)$ is a monotone function, as is $k(E)$, but it does not have as nice a probabilistic interpretation as our choice.

We shall now prove the recurrent Principle of Balayage.

Theorem 9-115: If $g$ is a pure potential and if $E \in \mathcal{L}$ then there is a unique pure potential $g'$ with support in $E$ such that

(1) $g'_E = g_E$,
(2) $g' \leq g$,
(3) $\alpha f' \geq \alpha f$,
(4) $\alpha f' = -k(E)^{-1} \lambda^E g$,

and this unique potential is $B^E g + (\lambda^E g/k(E))^E d$.

Proof: Since $g'$ is determined by its values on $E$, there is

$\alpha f' \geq \alpha f$, by Lemma 9-112, and we have (3). Result (4) follows by multiplying the second equation above by $\alpha$. Furthermore

$$g' = B^E g' - (\alpha f')^E d \quad \text{by Proposition 9-109}$$
$$\leq B^E g - (\alpha f')^E d \quad \text{by (1) and (3)}$$
$$\leq g \quad \text{by Proposition 9-110}.$$

Hence we have (2). The formula for $g'$ follows from (4) and the second part of Proposition 9-109.

The potential $g'$ is, as in the transient case, referred to as the balayage potential of $g$ on $E$.

Next, we prove the recurrent Principle of Domination.
