---
role: proof
locale: en
of_concept: ionescu-tulceas-theorem-on-extending-a-measure-and-the-existence-of-a-random-seq
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Ionescu Tulcea's Theorem on Extending a Measure and the Existence of a Random Sequence

**Theorem 2 (Ionescu Tulcea&#x2019;s Theorem).** Let $(\Omega_n, \mathcal{F}_n)$, $n = 1, 2, \ldots$, be arbitrary measurable spaces and $\Omega = \prod_{n \geq 1} \Omega_n$, $\mathcal{F} = \bigotimes_{n \geq 1} \mathcal{F}_n$. Suppose that a probability measure $P_1$ is given on $(\Omega_1, \mathcal{F}_1)$ and that, for every $(\omega_1, \ldots, \omega_n) \in \Omega_1 \times \cdots \times \Omega_n$, $n \geq 1$, probability measures $P(\omega_1, \ldots, \omega_n; \cdot)$ are given on $(\Omega_{n+1}, \mathcal{F}_{n+1})$. Suppose that for every $B \in \mathcal{F}_{n+1}$ the functions $P(\omega_1, \ldots, \omega_n; B)$ are $\mathcal{F}^n \equiv \mathcal{F}_1 \otimes \cdots \otimes \mathcal{F}_n$-measurable functions of $(\omega_1, \ldots, \omega_n)$ and let, for $A_i \in \mathcal{F}_i$, $n \geq 1$,

$$P_n(A_1 \times \cdots \times A_n) = \int_{A_1} P_1(d\omega_1) \int_{A_2} P(\omega_1; d\omega_2) \cdots \int_{A_n} P(\omega_1, \ldots, \omega_{n-1}; d\omega_n).$$

Then there is a unique probability measure $P$ on $(\Omega, \mathcal{F})$ such that

$$P\{\omega : \omega_1 \in A_1, \ldots, \omega_n \in A_n\} = P_n(A_1 \times \cdots \times A_n)$$

for every $n \geq 1$.

*Proof.* The construction defines an additive measure on the algebra of cylindrical sets via the iterated integrals. It remains to verify its countable additivity and apply Carath\'eodory's theorem.

Let $\{\hat{B}_n\}_{n \geq 1}$ be a sequence of cylindrical sets $\hat{B}_n = \{\omega : (\omega_1, \ldots, \omega_n) \in B_n\}$ that decrease to $\varnothing$, but $\lim_n P(\hat{B}_n) > 0$.

For $n > 1$, $P(\hat{B}_n) = \int_{\Omega_1} f_n^{(1)}(\omega_1) P_1(d\omega_1)$, where $f_n^{(1)}$ is defined via iterated integrals. The sequence $\{f_n^{(1)}\}$ decreases. Let $f^{(1)} = \lim f_n^{(1)}$. Since $\lim_n P(\hat{B}_n) > 0$, there exists $\omega_1^0$ with $f^{(1)}(\omega_1^0) > 0$.

Continuing inductively, we construct $\omega^0 = (\omega_1^0, \omega_2^0, \ldots)$ with $(\omega_1^0, \ldots, \omega_n^0) \in B_n$ for all $n$, hence $\omega^0 \in \bigcap \hat{B}_n = \varnothing$, a contradiction. Therefore $\lim_n P(\hat{B}_n) = 0$, proving countable additivity. Carath\'eodory's theorem yields the unique extension $P$.

The random sequence is obtained by $X_n(\omega) = \omega_n$, $n \geq 1$. $\square$
