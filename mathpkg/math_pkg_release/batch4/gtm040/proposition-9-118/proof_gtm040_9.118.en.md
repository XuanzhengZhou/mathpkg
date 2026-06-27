---
role: proof
locale: en
of_concept: proposition-9-118
source_book: gtm040
source_chapter: "9"
source_section: "118"
---

Proof: By Proposition 9-109,

$$(I - P^E)g_E = f_E - (\alpha f)l_E^E.$$

Hence

$$\nu_E(I - P^E)g_E = I(g) - (\alpha f)(\nu_E l_E^E) = I(g) - (\alpha f)(\hat{\lambda}^E g).$$

If $P = \hat{P}$, then $\hat{\lambda}^E g = \lambda^E g = -(\alpha f)k(E)$ by Proposition 9-109.

Lemma 9-121: $\nu_E(I - P^E)g_E = \frac{1}{2} \sum_{i,j \in E} \alpha_i P_{ij}^E(g_i - g_j)^2 \geq 0$, and the value is 0 only if $g$ is constant on $E$.

Proof: The proof proceeds as in Lemma 8-54, but $P^E1 = 1$ and $\alpha_E P^E = \alpha_E$; hence $m_i = 0$ and $\pi_i = 0$. Let $F$ be the subset of all states of $E$ on which $g = g_0$. If $F \neq E$, there are states $i \in F$ and $j \in \tilde{F}$ such that $P_{ij}^E > 0$, since the states of $E$ communicate. Then

$$\nu_E(I - P^E)g_E \geq \frac{1}{2} \alpha_i P_{

is no connection between $i$ and $j$, we let $c_{ij} = 0$; also we define $c_{ii} = 0$. We shall assume that:

(1) For each $i$, $\sum_j c_{ij} < \infty$. This condition is satisfied, for example, if each terminal is connected to only finitely many other terminals.

(2) The circuit is connected.

From physics we have the following two laws. In the present context the first one may be taken as a definition of current in terms of voltage:

(1) (Ohm) If $i$ is at voltage $v_i$ and $j$ is at voltage $v_j$, the current flowing from $j$ to $i$ is $(v_i - v_j)c_{ij}$.

(2) (Kirchhoff) The sum of all currents flowing into a given terminal is 0.

If an outside source is attached to a certain terminal, then the Kirchhoff Law (2) does not apply unless account is taken of current flowing from the outside source. But for all terminals $i$ which are not attached to any outside sources, Ohm’s Law and Kirchhoff’s Law imply:

(3) $\sum_k (v_i - v_k)c_{ik} = 0$.

If a finite set $E$ of terminals is kept at prescribed non-zero voltages by an outside source and if there is a finite set $F$ with $E \subset F$ such that all points in the set $\tilde{F}$ are grounded (kept at 0 voltage), then we shall call the problem of finding voltages at the points $i$ of $F - E$ in such a way that (3) holds a standard voltage problem. Note that for finite circuits the voltages may be prescribed at an arbitrary subset $E$ of terminals.
