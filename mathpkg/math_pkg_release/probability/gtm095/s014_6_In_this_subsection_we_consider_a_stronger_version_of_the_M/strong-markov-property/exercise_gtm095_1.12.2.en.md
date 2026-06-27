---
role: exercise
locale: en
chapter: "1"
section: "12"
exercise_number: 2
---

# Exercise 2

Let $\mathbb{P} = \|p_{ij}\|$, $1 \leq i,j \leq r$, be a stochastic matrix (so that $p_{ij} \geq 0$ and $\sum_{j} p_{ij} = 1$ for all $i$) and let $\lambda$ denote an eigenvalue of the matrix, i.e., a root of the characteristic equation $\det\|\mathbb{P} - \lambda E\| = 0$.

(a) Show that $\lambda_1 = 1$ is an eigenvalue and that all the other eigenvalues have moduli not exceeding 1.

(b) If all the eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_r$ are distinct, then the $k$-step transition probability $p_{ij}^{(k)}$ admits the spectral representation

$$
p_{ij}^{(k)} = \pi_j + a_{ij}(2)\lambda_2^k + \cdots + a_{ij}(r)\lambda_r^k,
$$

where $\pi_j, a_{ij}(2), \ldots, a_{ij}(r)$ can be expressed in terms of the elements of the matrix $\mathbb{P}$. Determine these coefficients.

(c) Deduce from this algebraic approach to the study of Markov chains that, when $|\lambda_2| < 1, \ldots, |\lambda_r| < 1$, the limit $\lim_{k \to \infty} p_{ij}^{(k)}$ exists for every $j$ and is independent of the initial state $i$.
