---
role: proof
locale: en
of_concept: elementary-chain
source_book: gtm053
source_chapter: "X"
source_section: "3"
---

# Proof of Elementary Chain Theorem

**Theorem 3.5 (Tarski's Elementary Chain Theorem).** Let, for an ordinal $\kappa$,

$$\mathbf{A}_0 \preceq \mathbf{A}_1 \preceq \cdots \preceq \mathbf{A}_\alpha \preceq \cdots \quad (\alpha < \kappa)$$

be a $\kappa$-sequence of $L$-structures forming an elementary chain. For each limit ordinal $\delta \leq \kappa$, define $\mathbf{A}_\delta$ as the union of the chain:

- Domain: $A_\delta = \bigcup_{\alpha < \delta} A_\alpha$,
- Relations and functions are interpreted in the natural way: $p^{\mathbf{A}_\delta} = \bigcup_{\alpha < \delta} p^{\mathbf{A}_\alpha}$, and similarly for functions and constants.

Then for every $\alpha < \delta$, $\mathbf{A}_\alpha \preceq \mathbf{A}_\delta$. Moreover, if $\mathbf{A}_\alpha \preceq \mathbf{B}$ for all $\alpha < \delta$, then $\mathbf{A}_\delta \preceq \mathbf{B}$.

*Proof.* We prove by induction on the complexity of an $L$-formula $P(x_1, \ldots, x_n)$ that for any $\bar{a} = (a_1, \ldots, a_n) \in A_\alpha^n$ and any $\beta$ with $\alpha \leq \beta < \delta$,

$$\mathbf{A}_\alpha \models P(\bar{a}) \iff \mathbf{A}_\beta \models P(\bar{a}).$$

The base case (atomic formulas) and the cases for Boolean connectives are straightforward.

For the existential case $P = \exists y\, Q(\bar{x}, y)$:

($\Rightarrow$): If $\mathbf{A}_\alpha \models \exists y\, Q(\bar{a}, y)$, then there exists $b \in A_\alpha$ such that $\mathbf{A}_\alpha \models Q(\bar{a}, b)$. By induction hypothesis, $\mathbf{A}_\beta \models Q(\bar{a}, b)$, hence $\mathbf{A}_\beta \models \exists y\, Q(\bar{a}, y)$.

($\Leftarrow$): Suppose $\mathbf{A}_\delta \models \exists y\, P(\bar{a}, y)$ with $\bar{a} \in A_\alpha^n$. Then $\mathbf{A}_\delta \models P(\bar{a}, b)$ for some $b \in A_\delta$. Since $A_\delta = \bigcup_{\alpha < \delta} A_\alpha$, we have $b \in A_\beta$ for some $\alpha < \beta < \delta$. By the induction hypothesis (applied downward along the chain), $\mathbf{A}_\beta \models P(\bar{a}, b)$. This implies $\mathbf{A}_\beta \models \exists y\, P(\bar{a}, y)$, and since $\mathbf{A}_\alpha \preceq \mathbf{A}_\beta$, we obtain $\mathbf{A}_\alpha \models \exists y\, P(\bar{a}, y)$.

By induction, the equivalence holds for all formulas, establishing $\mathbf{A}_\alpha \preceq \mathbf{A}_\delta$ for all $\alpha < \delta$. The second claim follows similarly by considering the chain $\mathbf{A}_\alpha \preceq \mathbf{B}$. $\square$
