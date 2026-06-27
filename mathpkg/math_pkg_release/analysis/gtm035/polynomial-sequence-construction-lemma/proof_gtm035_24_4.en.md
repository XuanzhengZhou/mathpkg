---
role: proof
locale: en
of_concept: polynomial-sequence-construction-lemma
source_book: gtm035
source_chapter: "24"
source_section: "24.4"
---
# Proof of Construction of Polynomial Sequences with Controlled Growth

**Lemma 24.4.** There exist two sequences of positive constants $c_j$, $j = 1, 2, \ldots$ and $\epsilon_j$, $j = 1, 2, \ldots$ such that $c_1 = 1/10$, $c_{j+1} \leq (1/10)c_j$, $j = 1, 2, \ldots$, and there exists a sequence of polynomials $P_n$ in $z$ and $w$, $n = 1, 2, \ldots$ such that:

(11) $\{P_n = 0\} = \Sigma(c_1, c_2, \ldots, c_n)$, $n = 1, 2, \ldots$,

(12) $\{|P_n| \leq \epsilon_n\} \subseteq \{|P_{n-1}| \leq \epsilon_{n-1}\}$, $n = 2, 3, \ldots$; and

(13) if $|a| \leq 1/2$ and $|P_n(a, w)| \leq \epsilon_n$, then there exists $w_n$ with

$$P_n(a, w_n) = 0 \text{ and } |w - w_n| < 1/n, \quad n = 1, 2, \ldots.$$

**Proof.** For $j = 1$, we take

$$c_1 = \frac{1}{10}, \quad \epsilon_1 = \frac{1}{4}, \quad P_1(z, w) = w^2 - \frac{1}{100}(z - a_1).$$

Then (11) and (13) hold for $n = 1$, and (12) is vacuous.

Suppose now that $c_j, \epsilon_j, P_j$ have been chosen for $j = 1, 2, \ldots, n$, so that our three conditions are satisfied for each $j$. We shall choose $c_{n+1}, \epsilon_{n+1}, P_{n+1}$.

We denote by $w_j(z)$, $j = 1, 2, \ldots, 2^n$, the $w$-coordinates of the $2^n$ points of $\Sigma_n$ lying over $z$. Write

$$\Sigma(c_1, \ldots, c_n, c) = \{(z, w) : w = \sum_{j=1}^{n} c_j \rho_j B_j(z) + c \rho_{n+1} B_{n+1}(z)\},$$

where each $\rho_j = 1$ or $= -1$, and $\rho_{n+1} = 1$ or $= -1$. For a fixed $z$ and fixed signs $\rho_1, \ldots, \rho_n$, the two choices of $\rho_{n+1}$ give two points lying over $z$ whose $w$-coordinates are

$$w'_j(z) \pm c B_{n+1}(z),$$

where $w'_j(z) = \sum_{v=1}^{n} c_v \rho_v B_v(z)$. The product over all $2^{n+1}$ choices of signs gives

$$P_c(z, w) = \prod_{j=1}^{2^{n+1}} (w - w'_j(z)),$$

where $w'_j(z)$ are the zeros of $P_c(z, \cdot)$.

Now fix $c$ such that (14) holds, and such that $c < (1/10)c_n$. Hence, if $\epsilon > 0$ and if $|P_c(z, w)| < \epsilon$, then $|w - w'_j(z)| < \epsilon^{1/2^{n+1}}$ for some $j$.

It follows that we can choose $\epsilon_{n+1}$ with $\epsilon_{n+1} < \epsilon_n^2/2$ and such that $|P_c(z, w)| < \epsilon_{n+1}$ implies that there exists $w_{n+1}$ with $P_c(z, w_{n+1}) = 0$ and $|w - w_{n+1}| < 1/(n+1)$. Putting $c_{n+1} = c$, and then, putting $P_{n+1} = P_c$ and choosing $\epsilon_{n+1}$ as above, we have that (11), (13), and (12) are satisfied for $j = 1, 2, \ldots, n+1$. The lemma now follows by induction. $\square$
