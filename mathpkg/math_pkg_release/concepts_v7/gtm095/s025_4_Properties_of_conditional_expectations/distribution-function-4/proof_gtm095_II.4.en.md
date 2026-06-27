---
role: proof
locale: en
of_concept: distribution-function-4
source_book: gtm095
source_chapter: "II"
source_section: "4"
---

# Proof of Theorem 4 (Existence of a Regular Distribution Function)

**Theorem 4.** A regular distribution function for a random variable $\xi$ with respect to a $\sigma$-subalgebra $\mathcal{G} \subseteq \mathcal{F}$ always exists.

*Proof.* Let $\{r_k\}$ be the set of rational numbers on $R$. For each $k \geq 1$, choose a version $F_{r_k}(\omega)$ of the conditional probability $P(\xi \leq r_k \mid \mathcal{G})(\omega)$, i.e.,

$$F_{r_k}(\omega) = P(\xi \leq r_k \mid \mathcal{G})(\omega) \quad \text{(a.s.)}.$$

If $r_i < r_j$, let $A_{ij} = \{\omega : F_{r_i}(\omega) > F_{r_j}(\omega)\}$. From the properties of conditional probabilities we have $P(A_{ij}) = 0$. Set

$$A = \bigcup_{r_i < r_j} A_{ij}.$$

Then $P(A) = 0$. Hence there exist modifications $\tilde{F}_{r_k}(\omega)$ such that $\tilde{F}_{r_k}(\omega) \leq \tilde{F}_{r_j}(\omega)$ for all $\omega \in \Omega$ whenever $r_k < r_j$, and $\tilde{F}_{r_k}(\omega) = F_{r_k}(\omega)$ (a.s.).

For rational $r_k$, let

$$B_k = \{\omega : \lim F_{r_k+1/n}(\omega) \neq F_{r_k}(\omega)\}, \quad B = \bigcup_k B_k.$$

By conclusion (a) of Theorem 2, $P(B) = 0$. Finally, let

$$C_k = \{\omega : \lim_{n \to \infty} F_n(\omega) \neq 1 \text{ or } \lim_{m \to -\infty} F_{-m}(\omega) \neq 0\}, \quad C = \bigcup_k C_k.$$

Again $P(C) = 0$.

Now put

$$F(\omega; x) = \begin{cases} \lim_{r \downarrow x} \tilde{F}_r(\omega), & \omega \notin A \cup B \cup C, \\ G(x), & \omega \in A \cup B \cup C, \end{cases}$$

where $G(x)$ is any distribution function on $R$; we show that $F(\omega; x)$ satisfies the conditions of Definition 8.

Let $\omega \notin A \cup B \cup C$. Then it is clear that $F(\omega; x)$ is a nondecreasing function of $x$. If $x < x' \leq r$, then $F(\omega; x) \leq F(\omega; x') \leq \tilde{F}_r(\omega)$, and $\tilde{F}_r(\omega) \downarrow F(\omega; x)$ when $r \downarrow x$. Consequently $F(\omega; x)$ is continuous on the right. Similarly $\lim_{x \to \infty} F(\omega; x) = 1$, $\lim_{x \to -\infty} F(\omega; x) = 0$. Since $F(\omega; x) = G(x)$ when $\omega \in A \cup B \cup C$, it follows that $F(\omega; x)$ is a distribution function on $R$ for every $\omega \in \Omega$, i.e., condition (a) of Definition 8 is satisfied.

By construction, $P(\xi \leq r \mid \mathcal{G})(\omega) = \tilde{F}_r(\omega) = F(\omega; r)$. If $r \downarrow x$, we have $F(\omega; r) \downarrow F(\omega; x)$ for all $\omega \in \Omega$ by the continuity on the right that we just established. But by conclusion (a) of Theorem 2, we have $P(\xi \leq r \mid \mathcal{G})(\omega) \to P(\xi \leq x \mid \mathcal{G})(\omega)$ (a.s.). Therefore $F(\omega; x) = P(\xi \leq x \mid \mathcal{G})(\omega)$ (a.s.), which establishes condition (b) of Definition 8.

Thus $F(\omega; x)$ is a regular distribution function for $\xi$ with respect to $\mathcal{G}$.
