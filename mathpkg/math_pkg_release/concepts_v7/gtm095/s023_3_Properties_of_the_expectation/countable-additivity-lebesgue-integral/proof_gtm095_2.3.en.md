---
role: proof
locale: en
of_concept: countable-additivity-lebesgue-integral
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Countable Additivity of the Lebesgue Integral as a Set Function

**Proposition.** Let $\xi$ be a random variable for which $E\xi$ is defined. Then the set function

$$Q(A) \equiv \int_A \xi \, dP, \quad A \in \mathcal{F},$$

is countably additive (i.e., a signed measure).

*Proof.* First suppose that $\xi \geq 0$. If $A_1, A_2, \ldots$ are pairwise disjoint sets from $\mathcal{F}$ and $A = \bigcup_{n} A_n$, the corollary to Theorem 1 (monotone convergence) implies that

$$Q(A) = E(\xi \cdot I_A) = E\left(\xi \cdot I_{\bigcup_n A_n}\right) = E\left(\sum_{n=1}^{\infty} \xi \cdot I_{A_n}\right)$$
$$= \sum_{n=1}^{\infty} E(\xi \cdot I_{A_n}) = \sum_{n=1}^{\infty} Q(A_n),$$

where the interchange of expectation and summation is justified by the corollary to the Monotone Convergence Theorem, since $\xi \cdot I_{A_n} \geq 0$ for all $n$.

If $\xi$ is an arbitrary random variable for which $E\xi$ is defined, write $Q(A) = Q^+(A) - Q^-(A)$, where

$$Q^+(A) = \int_A \xi^+ dP, \quad Q^-(A) = \int_A \xi^- dP.$$

Both $Q^+$ and $Q^-$ are countably additive by the nonnegative case. Since $E\xi$ is defined, at least one of $Q^+(\Omega)$ and $Q^-(\Omega)$ is finite, so the difference $Q = Q^+ - Q^-$ is a well-defined signed measure.

Thus if $E\xi$ is defined, the set function $Q = Q(A)$ is a signed measure — a countably additive set function representable as the difference of two measures, at least one of which is finite. Moreover, $Q$ is absolutely continuous with respect to $P$: if $P(A) = 0$ then $Q(A) = 0$. $\square$
