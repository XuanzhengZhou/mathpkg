---
role: proof
locale: en
of_concept: levy-prokhorov-metric-properties
source_book: gtm095
source_chapter: "3"
source_section: "§7. Metrizability of Weak Convergence"
---

# Proof of Properties of the Lévy–Prokhorov Metric

Let $(E, \mathcal{E}, \rho)$ be a metric space and $\mathcal{P}(E)$ the family of probability measures on $(E, \mathcal{E})$. For any two measures $P, \tilde{P} \in \mathcal{P}(E)$, define

$$\sigma(P, \tilde{P}) = \inf \{ \varepsilon > 0 : P(F) \leq \tilde{P}(F^\varepsilon) + \varepsilon \text{ for all closed sets } F \in \mathcal{E} \},$$

and

$$L(P, \tilde{P}) = \max[\sigma(P, \tilde{P}), \sigma(\tilde{P}, P)].$$

The function $L(P, \tilde{P})$ is called the **Lévy–Prokhorov metric**. We prove that it is indeed a metric:

**(a) Symmetry.** $L(P, \tilde{P}) = L(\tilde{P}, P)$, and in fact $\sigma(P, \tilde{P}) = \sigma(\tilde{P}, P)$.

**(b) Triangle inequality.** $L(P, \tilde{P}) \leq L(P, \hat{P}) + L(\hat{P}, \tilde{P})$.

**(c) Positive definiteness.** $L(P, \tilde{P}) = 0$ if and only if $\tilde{P} = P$.

**Proof of (a).** It suffices to show that (with $\alpha > 0$ and $\beta > 0$)

$$P(F) \leq \tilde{P}(F^\alpha) + \beta \quad \text{for all closed sets } F \in \mathcal{E}, \tag{4}$$

if and only if

$$\tilde{P}(F) \leq P(F^\alpha) + \beta \quad \text{for all closed sets } F \in \mathcal{E}. \tag{5}$$

Let $T$ be a closed set in $\mathcal{E}$. Then the set $T^\alpha = \{x : \rho(x, T) < \alpha\}$ is open, and it is easy to verify that

$$T \subseteq E \setminus (E \setminus T^\alpha)^\alpha.$$

If (4) is satisfied, then applying it to the closed set $F = E \setminus T^\alpha$, we obtain

$$P(E \setminus T^\alpha) \leq \tilde{P}\bigl((E \setminus T^\alpha)^\alpha\bigr) + \beta.$$

Taking complements:

$$1 - P(T^\alpha) \leq 1 - \tilde{P}\bigl(E \setminus (E \setminus T^\alpha)^\alpha\bigr) + \beta.$$

Since $T \subseteq E \setminus (E \setminus T^\alpha)^\alpha$, this yields

$$\tilde{P}(T) \leq P(T^\alpha) + \beta,$$

which is precisely condition (5) for the closed set $T$. The reverse implication is symmetric. Therefore $\sigma(P, \tilde{P}) = \sigma(\tilde{P}, P)$, and consequently $L(P, \tilde{P}) = L(\tilde{P}, P)$.

**Proof of (b).** The triangle inequality follows directly from the definition of $\sigma$ and elementary considerations with $\varepsilon$-neighbourhoods. For any $\varepsilon_1 > \sigma(P, \hat{P})$ and $\varepsilon_2 > \sigma(\hat{P}, \tilde{P})$, one has for all closed $F$:

$$P(F) \leq \hat{P}(F^{\varepsilon_1}) + \varepsilon_1 \leq \tilde{P}\bigl((F^{\varepsilon_1})^{\varepsilon_2}\bigr) + \varepsilon_2 + \varepsilon_1 \leq \tilde{P}(F^{\varepsilon_1 + \varepsilon_2}) + \varepsilon_1 + \varepsilon_2.$$

Hence $\sigma(P, \tilde{P}) \leq \sigma(P, \hat{P}) + \sigma(\hat{P}, \tilde{P})$, and the triangle inequality for $L$ follows.

**Proof of (c).** If $\tilde{P} = P$, then clearly $L(P, \tilde{P}) = 0$. Conversely, suppose $L(P, \tilde{P}) = 0$. Then $\sigma(P, \tilde{P}) = 0$, which means that for every $\alpha > 0$ and every closed set $F$,

$$P(F) \leq \tilde{P}(F^\alpha).$$

Since $F^\alpha \downarrow F$ as $\alpha \downarrow 0$, taking the limit yields $P(F) \leq \tilde{P}(F)$. By symmetry, $\tilde{P}(F) \leq P(F)$. Hence $P(F) = \tilde{P}(F)$ for all closed sets $F \in \mathcal{E}$.

For any Borel set $A \in \mathcal{E}$ and every $\varepsilon > 0$, there exist an open set $G_\varepsilon \supseteq A$ and a closed set $F_\varepsilon \subseteq A$ such that $P(G_\varepsilon \setminus F_\varepsilon) \leq \varepsilon$ (regularity of probability measures on metric spaces). It follows that every probability measure $P$ on a metric space $(E, \mathcal{E}, \rho)$ is completely determined by its values on closed sets. Consequently, $\tilde{P}(F) = P(F)$ for all closed sets $F$ implies $\tilde{P}(A) = P(A)$ for all Borel sets $A \in \mathcal{E}$, i.e., $\tilde{P} = P$. $\square$
