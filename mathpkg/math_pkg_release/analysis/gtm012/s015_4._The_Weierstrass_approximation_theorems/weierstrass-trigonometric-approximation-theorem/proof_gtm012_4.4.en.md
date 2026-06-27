---
role: proof
locale: en
of_concept: weierstrass-trigonometric-approximation-theorem
source_book: gtm012
source_chapter: "4"
source_section: "4. The Weierstrass approximation theorems"
---

# Proof of Theorem 4.3: Weierstrass Trigonometric Approximation Theorem

Let $u \in \mathbb{C}$ be a continuous $2\pi$-periodic function and let $v \in \mathcal{P}$ be a smooth $2\pi$-periodic function.

Let $(\varphi_n)_{1}^{\infty}$ be a sequence of trigonometric polynomials which is an approximate identity, as constructed in Lemma 4.1. Define

$$u_n = \varphi_n * u, \quad v_n = \varphi_n * v.$$

By Lemma 4.2, the functions $u_n$ and $v_n$ are trigonometric polynomials. (Lemma 4.2 states that the convolution of a trigonometric polynomial with any periodic distribution is again a trigonometric polynomial.)

By Theorem 3.6 (which establishes that convolution with an approximate identity gives uniform convergence for continuous functions and $\mathcal{P}$-convergence for smooth functions), we obtain:

- $u_n \to u$ uniformly on $[0, 2\pi]$,
- $v_n \to v$ in the sense of $\mathcal{P}$ (i.e., all derivatives converge uniformly).

Thus $(u_n)_{1}^{\infty}$ and $(v_n)_{1}^{\infty}$ are the desired sequences of trigonometric polynomials approximating $u$ and $v$ respectively.

**Note.** If $u$ and $v$ are real-valued, then the sequences $(u_n)_{1}^{\infty}$ and $(v_n)_{1}^{\infty}$ constructed here are also real-valued, since the approximate identity $(\varphi_n)_{1}^{\infty}$ from Lemma 4.1 consists of real-valued functions.
