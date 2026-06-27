---
role: proof
locale: en
of_concept: almost-sure-fundamental-completeness
source_book: gtm095
source_chapter: "2"
source_section: "10"
---

# Proof of Completeness of Almost Sure Convergence

**Theorem 4.** A sequence $(\xi_n)_{n \geq 1}$ of random variables converges almost surely if and only if it is fundamental with probability 1.

*Proof.* If $\xi_n \to \xi$ (P-a.s.), then $|\xi_n - \xi_m| \leq |\xi_n - \xi| + |\xi_m - \xi|$ implies the sequence is fundamental with probability 1.

Conversely, let $(\xi_n)_{n \geq 1}$ be fundamental with probability 1. Let $\mathcal{N} = \{\omega : (\xi_n(\omega)) \text{ is not fundamental}\}$. Then whenever $\omega \in \Omega \setminus \mathcal{N}$ the sequence of numbers $(\xi_n(\omega))_{n \geq 1}$ is fundamental and, by Cauchy's criterion for sequences of real numbers, $\lim \xi_n(\omega)$ exists. Let

$$\xi(\omega) = \begin{cases} \lim\limits_{n \to \infty} \xi_n(\omega), & \omega \in \Omega \setminus \mathcal{N}, \\ 0, & \omega \in \mathcal{N}. \end{cases}$$

The function $\xi$ so defined is a random variable (it is the pointwise limit of measurable functions on a set of full measure), and evidently $\xi_n \xrightarrow{\text{a.s.}} \xi$.

This completes the proof. $\square$
