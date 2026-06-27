---
role: proof
locale: en
of_concept: thm-for-arbitrary-one-dimensional-random-walk
source_book: gtm034
source_chapter: "5"
source_section: "012"
---

Proof: To facilitate the use of T1 we shall assume the random walk to be aperiodic, keeping in mind that this assumption may be removed by an argument similar to that in the proof of T22.1. The proof will require several preliminary lemmas, the first of which concerns the moments of the distribution $F(x)$ in T2.

$$m_p = \int_0^\infty x^p f(x) \, dx = p! \frac{\pi}{2} \left( \frac{8}{\pi^2} \right)^{p+1} \sum_{k=0}^{\infty} (-1)^k \left( \frac{1}{2k+1} \right)^{2p+1}, \quad p \geq 0,$$

where $f(x)$ is the density $F'(x)$. Moreover, if $G(x)$ is any distribution function such that

$$\int_{-\infty}^{\infty} x^p dG(x) = m_p \text{ for all } p = 0, 1, 2, \ldots,$$

then $G(x) = F(x)$.

Proof: The first part of P3 involves only straightforward calculation of the moments $m_p$ of the distribution $F(x)$ defined in T2. The second part, which amounts to saying that the moment problem for the particular moment sequence $m_p$ has a unique solution may be deduced from a well known criterion. If

$$c_p = \int_{-\infty}^{\infty} x^p dH(x), \quad p \geq 0,$$

is a sequence of moments of a probability distribution $H(x)$, and if

$$\sum_{k=0}^{\infty} \frac{c_k}{k!} r^k < \infty \text{ for some } r > 0$$

then $H(x)$ is the only distribution with these moments (the moment problem for the sequence $c_k$ has a unique solution). The moments $m_p$ are easily seen to satisfy the above condition for all $r < \pi^2/8$.

We need one more result from the general theory of distribution functions. If $H_n(x)$ is a sequence of distribution functions, such that

$$\int_{-\infty}^{\infty} x^p dH_n(x) = c_p(n), \

and if there is one unique distribution function $H(x)$ such that

$$c_p = \int_{-\infty}^{\infty} x^p dH(x), \quad p \geq 0,$$

then

$$\lim_{n \to \infty} H_n(x) = H(x)$$

at every point of continuity of $H(x)$.

This theorem permits us to conduct the proof of T2 by showing that the moments of $T_N$ have the proper limiting behavior. In view of P3 we may record this state of affairs as
