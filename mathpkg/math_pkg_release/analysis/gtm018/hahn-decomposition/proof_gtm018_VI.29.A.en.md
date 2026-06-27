---
role: proof
locale: en
of_concept: hahn-decomposition
source_book: gtm018
source_chapter: "VI"
source_section: "29"
---

Since $\mu$ assumes at most one of the values $+\infty$ and $-\infty$, we may assume that, say

$$-\infty < \mu(E) \leq \infty$$

for every measurable set $E$. Since the difference of two negative sets, and a disjoint, countable union of negative sets are obviously negative, it follows that every countable union of negative sets is negative. We write $\beta = \inf \mu(B)$ for all measurable negative sets $B$. Let $\{B_i\}$ be a sequence of measurable negative sets such that $\lim_i \mu(B_i) = \beta$; if $B = \bigcup_{i=1}^{\infty} B_i$, then $B$ is a measurable negative set for which $\mu(B)$ is minimal.

We shall prove that the set $A = X - B$ is a positive set. Suppose that, on the contrary, $E_0$ is a measurable subset of $A$ for which $\mu(E_0) < 0$. The set $E_0$ cannot be a negative set, for then $B \cup E_0$ would be a negative set with a smaller value of $\mu$ than $\mu(B)$, which is impossible. Let $k_1$ be the smallest positive integer with the property that $E_0$ contains a measurable set $E_1$ for which $\mu(E_1) \geq 1/k_1$. (Observe that, since $\mu(E_0) < 0$, $\mu(E_0)$ and $\mu(E_1)$ are both finite.) Since

$$\mu(E_0 - E_1) = \mu(E_0) - \mu(E_1) \leq \mu(E_0) - \frac{1}{k_1} < 0,$$

we may repeat the argument with $E_0 - E_1$ in place of $E_0$. Proceeding by induction, we obtain a disjoint sequence $\{E_j\}$ of measurable subsets of $E_0$ and a sequence $\{k_j\}$ of positive integers such that

$$\mu(E_j) \geq \frac{1}{k_j}.$$

Since the terms of $\{E_j\}$ are disjoint measurable subsets of $E_0$ and all their measures are positive, and since $\mu(E_0)$ is finite (28.A), the series $\sum \mu(E_j)$ converges, whence $\lim_j \mu(E_j) = 0$. By the definition of $k_j$ as minimal, we must have $\lim_j 1/k_j = 0$. It follows that, for every measurable subset $F$ of

$$F_0 = E_0 - \bigcup_{j=1}^{\infty} E_j,$$

we have $\mu(F) \leq 0$, i.e. that $F_0$ is a measurable negative set. Since $F_0$ is disjoint from $B$, and since

$$\mu(F_0) = \mu(E_0) - \sum_{j=1}^{\infty} \mu(E_j) \leq \mu(E_0) < 0,$$

this contradicts the minimality of $B$, and we conclude that the hypothesis $\mu(E_0) < 0$ is untenable. Hence $A$ is positive and $\{A, B\}$ is a Hahn decomposition.
