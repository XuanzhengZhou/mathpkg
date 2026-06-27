---
role: proof
locale: en
of_concept: random-variable-20
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Corollary 4: Existence of Independent Random Variables with Given Distributions

**Corollary 4.** Let $(E_n, \mathcal{E}_n)_{n \geq 1}$ be any measurable spaces and $(P_n)_{n \geq 1}$ be probability measures on them. Then there exist a probability space $(\Omega, \mathcal{F}, P)$ and a sequence of independent random variables $X = (X_n)_{n \geq 1}$ defined on it such that the distribution of $X_n$ is $P_n$, i.e.,

$$P\{X_n \in B\} = P_n(B), \quad B \in \mathcal{E}_n,$$

for each $n \geq 1$, and the $X_n$ are independent.

*Proof.* This follows from the Ionescu Tulcea theorem (Theorem 2) by taking the transition probabilities to be independent of the past: define

$$P(\omega_1, \ldots, \omega_n; B) = P_{n+1}(B)$$

for all $(\omega_1, \ldots, \omega_n)$ and all $B \in \mathcal{E}_{n+1}$. The measurability condition is trivially satisfied since these are constant functions of $(\omega_1, \ldots, \omega_n)$. The finite-dimensional distributions then factor:

$$P_n(A_1 \times \cdots \times A_n) = \int_{A_1} P_1(d\omega_1) \int_{A_2} P_2(d\omega_2) \cdots \int_{A_n} P_n(d\omega_n) = \prod_{k=1}^n P_k(A_k).$$

The Ionescu Tulcea theorem yields a unique probability measure $P$ on $(\prod E_n, \bigotimes \mathcal{E}_n)$ with these finite-dimensional distributions. This is precisely the product measure $\bigotimes_{n \geq 1} P_n$. The coordinate projections $X_n(\omega) = \omega_n$ are then independent random variables with distributions $P_n$, since for any $B_k \in \mathcal{E}_k$,

$$P\{X_1 \in B_1, \ldots, X_n \in B_n\} = P(B_1 \times \cdots \times B_n \times \prod_{k > n} E_k) = \prod_{k=1}^n P_k(B_k).$$

This completes the proof. $\square$
