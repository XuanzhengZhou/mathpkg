---
role: proof
locale: en
of_concept: thm-4
source_book: gtm095
source_chapter: "3"
source_section: "5"
---

# Proof of Theorem 4 (Coupling Bound for Lévy–Prokhorov Metric)

*Note: The OCR source for this section is partially truncated; the statement of Theorem 4 as it appears in the text begins with "Theorem 4. For each..." followed by an incomplete formula. The following reconstruction is based on the surrounding text (the corollary, Remarks 4–5, and the general theory of §3.5) and follows Shiryaev's Probability-1 (3rd ed.).*

**Theorem 4.** For any two probability measures $P$ and $\tilde{P}$ on a separable metric space $(E, \mathcal{E}, \rho)$, suppose there exist random elements $X$ and $\tilde{X}$ defined on a common probability space $(\Omega^*, \mathcal{F}^*, \mathbb{P}^*)$ such that $X \sim P$ and $\tilde{X} \sim \tilde{P}$. Then for every $\varepsilon > 0$,

$$L(P, \tilde{P}) \leq \varepsilon + \mathbb{P}^*\{\omega^* : \rho(X(\omega^*), \tilde{X}(\omega^*)) \geq \varepsilon\}.$$

Consequently,

$$L(P, \tilde{P}) \leq \inf\{\varepsilon > 0 : \mathbb{P}^*(\rho(X, \tilde{X}) \geq \varepsilon) \leq \varepsilon\} = d_{\mathbb{P}^*}(X, \tilde{X}).$$

*Proof.* The proof is a direct application of the coupling method (the "method of a single probability space") already used in Theorem 1.

Fix $\varepsilon > 0$ and let $F$ be any closed subset of $E$. Define the $\varepsilon$-neighborhood $F^\varepsilon = \{x \in E : \rho(x, F) < \varepsilon\}$. Consider the event inclusion

$$\{X \in F\} \subseteq \{\tilde{X} \in F^\varepsilon\} \cup \{\rho(X, \tilde{X}) \geq \varepsilon\}.$$

Indeed, if $X(\omega^*) \in F$ and $\rho(X(\omega^*), \tilde{X}(\omega^*)) < \varepsilon$, then by the triangle inequality (or directly by definition of $F^\varepsilon$), $\tilde{X}(\omega^*) \in F^\varepsilon$.

Taking $\mathbb{P}^*$-probability of both sides,

$$P(F) = \mathbb{P}^*(X \in F) \leq \mathbb{P}^*(\tilde{X} \in F^\varepsilon) + \mathbb{P}^*(\rho(X, \tilde{X}) \geq \varepsilon) = \tilde{P}(F^\varepsilon) + \mathbb{P}^*(\rho(X, \tilde{X}) \geq \varepsilon).$$

This inequality holds for every closed set $F \subset E$. Therefore, by definition of the Lévy–Prokhorov metric,

$$L(P, \tilde{P}) = \inf\{\delta > 0 : P(F) \leq \tilde{P}(F^\delta) + \delta \text{ for all closed } F\}.$$

Choosing $\delta = \varepsilon + \mathbb{P}^*(\rho(X, \tilde{X}) \geq \varepsilon)$, we have $P(F) \leq \tilde{P}(F^\varepsilon) + \varepsilon + \mathbb{P}^*(\rho(X, \tilde{X}) \geq \varepsilon) \leq \tilde{P}(F^\delta) + \delta$ (since $F^\varepsilon \subseteq F^\delta$ when $\varepsilon \leq \delta$). Hence $L(P, \tilde{P}) \leq \delta$, which proves the first inequality.

Taking the infimum over all $\varepsilon > 0$ yields the second bound.

$\square$

**Remark 4 (from the text).** The proof shows that in fact the bound is valid whenever we can exhibit, on *any* probability space $(\Omega^*, \mathcal{F}^*, \mathbb{P}^*)$, random elements $X$ and $\tilde{X}$ with values in $E$ whose distributions coincide with $P$ and $\tilde{P}$ and for which the set $\{\omega^* : \rho(X(\omega^*), \tilde{X}(\omega^*)) \geq \varepsilon\} \in \mathcal{F}^*$ for $\varepsilon > 0$. Hence, the quality of the bound depends in an essential way on how well the coupling $(X, \tilde{X})$ is constructed. The trivial choice $\mathbb{P}^* = P \otimes \tilde{P}$ (independent coupling) would, as a rule, not lead to a good estimate.

**Remark 5 (from the text).** It is natural to ask when equality can be achieved. Without proof, we state the following: Let $P$ and $\tilde{P}$ be two probability measures on a separable metric space $(E, \mathcal{E}, \rho)$. Then there exist $(\Omega^*, \mathcal{F}^*, \mathbb{P}^*)$ and $X, \tilde{X}$ such that

$$L(P, \tilde{P}) = d_{\mathbb{P}^*}(X, \tilde{X}) = \inf_{\text{couplings}} d(X, \tilde{X}),$$

i.e., the Lévy–Prokhorov distance equals the minimal possible Ky Fan distance over all couplings. This optimal coupling theorem is a deep result in the theory of probability metrics.
