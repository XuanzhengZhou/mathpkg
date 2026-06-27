---
role: proof
locale: en
of_concept: proposition-15-20-
source_book: gtm001
source_chapter: "15"
source_section: ""
---

(1) (By transfinite induction). If $\beta = K_1'\alpha$, $\gamma = K_2'\alpha$ and $n = K_3'\alpha$ then

$$\alpha = J' \langle \beta, \gamma, n \rangle.$$

If $n = 0$ then $F'\alpha = F''\alpha$ and hence $F'\alpha \subseteq F''\alpha$. If $n \neq 0$ then by Proposition 15.10, $\beta < \alpha$, $\gamma < \alpha$ and hence

$$F'\beta \in F''\alpha \land F'\gamma \in F''\alpha.$$

If $n = 1$ then

$$F'\alpha = \mathcal{F}_1(F'\beta, F'\gamma) = \{F'\beta, F'\gamma\} \subseteq F''\alpha.$$

If $n > 1$ then

$$F'\alpha = \mathcal{F}_n(F'\beta, F'\gamma) \subseteq F'\beta.$$

From the induction hypothesis and the fact that $\beta < \alpha$

(1) If $x \in F''\alpha$, then $(\exists \beta < \alpha)[x = F'\beta]$. But from Proposition 15.20 and the fact that $\beta < \alpha$ we have

$$x = F'\beta \subseteq F''\beta \subseteq F''\alpha.$$

(2) The proof is left to the reader. $\square$
