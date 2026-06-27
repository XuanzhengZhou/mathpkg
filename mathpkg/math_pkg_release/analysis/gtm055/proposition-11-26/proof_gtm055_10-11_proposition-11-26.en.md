---
role: proof
locale: en
of_concept: proposition-11-26
source_book: gtm055
source_chapter: "10-11"
source_section: "Section 12_Section_12"
---

Proof. Since the ball $\{x \in \mathcal{E} : \sigma(x) < \varepsilon\}$ is a neighborhood of 0 in the topology induced by $\sigma$, it is clear that (i) implies (ii). To show that (ii) implies (iii) we observe that if $x$ and $x_0$ are vectors in $\mathcal{E}$, then $|\sigma(x) - \sigma(x_0)| \leq \sigma(x - x_0)$. Hence if $V$ is a neighborhood of 0 with respect to $\mathcal{T}$ that is contained in $\{x \in \mathcal{E} : \sigma(x) < \varepsilon\}$, then $x \in x_0 + V$ implies that $|\sigma(x) - \sigma(x_0)| < \varepsilon$. Since $\varepsilon$ is arbitrary, this shows that $\sigma$ is continuous at the arbitrary vector $x_0$, and hence that $\sigma$ is continuous on $\mathcal{E}$ with respect to $\mathcal{T}$. Finally, to see that (iii) implies (i), let $\varepsilon$ be a positive number, and suppose $y \in \{x \in \mathcal{E} : \sigma(x) < \varepsilon\}$. If (iii) holds, then there exists a neighborhood $V$ of 0 with respect to $\mathcal{T}$ such that if $z \in y + V$ then $|\sigma(y) - \sigma(z)| < \varepsilon - \sigma(y)$, and therefore $\sigma(z) < \varepsilon$. Thus $\{

PROOF. According to Example 3M, the collection of all finite intersections of the form

$$V = \{x \in \mathcal{E} : \sigma_{\gamma_1}(x - x_1) < \varepsilon_1\} \cap \cdots \cap \{x \in \mathcal{E} : \sigma_{\gamma_n}(x - x_n) < \varepsilon_n\}$$

constitutes a base for the topology induced on $\mathcal{E}$ by the family $\{\sigma_\gamma\}$. To prove that the collection of all translates $x_0 + U(\gamma_1, \ldots, \gamma_n; \varepsilon)$ also forms a base for this topology, it suffices to show that if $x_0 \in V$, then there exists a positive number $\varepsilon$ such that the set

$$W_\varepsilon = \{x \in \mathcal{E} : \sigma_{\gamma_i}(x - x_0) < \varepsilon, i = 1, \ldots, n\}$$

is contained in $V$ (since $W_\varepsilon = x_0 + U(\gamma_1, \ldots, \gamma_n; \varepsilon)$). To this end, suppose $x_0 \in V$ and let $\delta_i = \sigma_{\gamma_i}(x_0 - x_i)$, $i = 1, \ldots, n$. Then $\delta_i < \varepsilon_i$, so $\varepsilon = \inf_{1 \leq i \leq n} \{\varepsilon_i - \delta_i\}$ is positive, and if $x \in W_\varepsilon$, then

$$\sigma_{\gamma_i}(x - x_i) < \sigma_{\gamma_i}(x - x_0) + \sigma_{\gamma_i}(x_0 - x_i) < \varepsilon + \delta_i < \varepsilon_i, \quad i = 1, \ldots, n$$

so $x \in V$ and therefore $W_\varepsilon \subset V$. The assertion concerning a neighborhood base at 0 follows from this same calculation, and the assertion concerning convergence of nets is a consequence of Proposition 3.20.
