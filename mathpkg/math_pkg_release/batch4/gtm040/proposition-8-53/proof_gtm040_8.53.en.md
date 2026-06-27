---
role: proof
locale: en
of_concept: proposition-8-53
source_book: gtm040
source_chapter: "8"
source_section: "53"
---

**Proof:** Since $f$ has support in $E$,

$$(I - P^E)g_E = f_E$$

by Proposition 8-19, and

$$\nu_E[(I - P^E)g_E] = \nu_Ef_E = \nu f = I(g).$$

The other half of the proposition is the dual of the first half.

Classically energy is non-negative. We shall prove shortly that the energy of a potential is non-negative provided it is finite. To do so, we first introduce a definition. If $g = Nf$ and $\bar{g} = N\bar{f}$ are potentials of finite energy, we define

$$(g, \bar{g}) = \frac{1}{2}(\mu \bar{g} + \bar{\mu} g),$$

provided the matrix products are well defined. (We shall show soon that this condition is always satisfied.)

Note that $(g, g) = I(g)$. We wish to show that $(g, \bar{g})$ is an inner product. The reader should verify that $(g, \bar{g})$ satisfies (1), (2), and (4) in general and (3) when all the potentials have finite support. We shall prove (5) and the general case of (3) below.

(1) $(g, \bar{g}) = (\bar{g}, g)$.
(2) For every real number $c$, $(cg, \bar{g}) = c(g, \bar{g})$.
(3) $(g + g', \bar{g}) = (g, \bar{g}) + (g', \bar{g})$.
(4) If $g$ is a pure potential for which $(g

Proof: We shall apply Proposition 8-53. The matrices involved are finite matrices so that distributivity and associativity hold. Hence

$$\mathbf{I}(g) = \nu_E g_E - \nu_E P^E g_E$$
$$= \frac{1}{2} \sum_{i \in E} \left[ \alpha_i g_i^2 + \alpha_i g_i^2 + \sum_{j \in E} \left( -2\alpha_i P^E_{ij} g_i g_j \right) \right]$$
$$= \frac{1}{2} \sum_{i \in E} \left[ \alpha_i \left( 1 - \sum_{j \in E} P^E_{ij} \right) g_i^2 + \left( \alpha_i - \sum_{k \in E} \alpha_k P^E_{ki} \right) g_i^2 \right]$$
$$+ \sum_{j \in E} \left( \alpha_i P^E_{ij} g_i^2 - 2\alpha_i P^E_{ij} g_i g_j + \alpha_i P^E_{ij} g_j^2 \right]$$
$$= \frac{1}{2} \sum_{i \in E} \left[ \left( \alpha_i m_i + \pi_i \right) g_i^2 + \sum_{j \in E} \alpha_i P^E_{ij} \left( g_i - g_j \right)^2 \right].

Since $P^E$ is a transition matrix and $\alpha_E$ is $P^E$-superregular, $m$ and $\pi$ are non-negative. Hence $\mathbf{I}(g) \geq 0$.

From properties (1), (2), and (3), we can prove that Schwarz's inequality holds for $g$ and $\bar{g}$ whenever they have finite support.

Lemma 8-55: If $g = Nf$ and $\bar{g} = N\bar{f}$ are two potentials of finite support, then

$$(g, \bar{g})^2 \leq \mathbf{I}(g)\mathbf{I}(\bar{g}).$$

Proof: By Lemma

be an increasing sequence of finite sets with union the set of all states $S$, and let

$$f^{(n)} = \binom{f_{E_n}}{0}, \quad \bar{f}^{(n)} = \binom{\bar{f}_{E_n}}{0}.$$

$$g^{(n)} = Nf^{(n)}, \quad \text{and} \quad \bar{g}^{(n)} = N\bar{f}^{(n)}.$$

Then $(g, \bar{g}) = \lim_{n \to \infty} (g^{(n)}, \bar{g}^{(n)})$.

Proof: We have $(g, \bar{g}) = \frac{1}{2}(\mu \bar{g} + \bar{\mu} g)$, and by symmetry it is enough to show that $\bar{\mu}^{(n)}g^{(n)}$ converges to $\bar{\mu} g$. By monotone convergence, we have $\lim g^{(n)} = g$, since $0 \leq f^{(1)} \leq f^{(2)} \leq \cdots$. Let

$$h_i^{(n)} = \begin{cases} g_i^{(n)} & \text{if } i \in E_n \\ 0 & \text{otherwise.} \end{cases}$$

Then

$$\bar{\mu}^{(n)}g^{(n)} = \bar{\mu}h^{(n)}$$

and

$$\lim h^{(n)} = \lim g^{(n)} = g.$$

The functions $h^{(n)}$ are non-negative and increasing; also $\bar{\mu}$ is non-negative. Thus by monotone convergence,

$$\lim \bar{\mu}^{(n)}g^{(n)} = \lim \bar{\mu}h^{(n)} = \bar{\mu} \lim h^{(n)} = \bar{\mu}g.$$

Lemma 8-57: If $g$ and $\bar{g}$ are pure potentials of finite energy, then

$$(g, \bar{g})^2 \leq (g, g)(\bar{g}, \bar{g}).$$

Consequently $(g, \bar{g}) < \infty.$

Proof: Form the approximations to $

Proof: Write $g = Nf = Nf^+ - Nf^-$, where $Nf^+$ and $Nf^-$ are pure potentials. Then

$$\mathbf{I}(g) = (g, g) = (Nf^+ - Nf^-, Nf^+ - Nf^-)$$
$$= \mathbf{I}(Nf^+) - 2(Nf^+, Nf^-) + \mathbf{I}(Nf^-)$$
$$\geq \mathbf{I}(Nf^+) - 2\sqrt{\mathbf{I}(Nf^+)\mathbf{I}(Nf^-)} + \mathbf{I}(Nf^-)$$
$$= (\sqrt{\mathbf{I}(Nf^+)} - \sqrt{\mathbf{I}(Nf^-)})^2$$
$$\geq 0.$$

We can finally prove Schwarz's inequality for all potentials of finite energy by proceeding just as in the proof of Lemma 8-55.

We now begin the proof of the fundamental result about energy, the theorem that justifies the name "equilibrium potential." Unfortunately the result fails for the most general transient chain, so that some extra hypothesis is needed. We shall prove the theorem—Theorem 8-61—under the hypothesis $P = \hat{P}$, a condition that is satisfied in the classical case of the three-dimensional symmetric random walk with $\alpha = 1^T$.

Lemma 8-59: The energy of the equilibrium potential on $E$ is the capacity $C(E)$.

Proof: $\mathbf{I}(h^E) = \eta^E h^E = \eta^E h^E = \eta^E 1 = \eta^E 1 = C(E)$.

Lemma 8-60: If $E$ is an equilibrium set, if $g = Nf$ is a potential with support in $E$, and if $P = \hat{P}$, then $(g, h^E) = \alpha f$.

Proof:

$$2(g, h^E) = \mu h^E + \eta^E g$$
$$= \mu h^E + \eta^E Nf$$
