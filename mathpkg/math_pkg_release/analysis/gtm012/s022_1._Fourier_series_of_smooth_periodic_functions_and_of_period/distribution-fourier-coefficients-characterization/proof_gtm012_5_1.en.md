---
role: proof
locale: en
of_concept: distribution-fourier-coefficients-characterization
source_book: gtm012
source_chapter: "5"
source_section: "§1. Fourier series of smooth periodic functions and of periodic distributions"
---

# Proof of Characterization of Fourier Coefficients of Periodic Distributions

**Theorem 1.2.** A sequence $(a_n)_{-\infty}^{\infty} \subset \mathbb{C}$ is the sequence of Fourier coefficients of a distribution $F \in \mathcal{P}'$ if and only if it is of slow growth.

**Proof.** Suppose first that $F \in \mathcal{P}'$ has $(a_n)_{-\infty}^{\infty}$ as its sequence of Fourier coefficients. Recall that for some integer $k$, $F$ is of order $k$. Thus for $u \in \mathcal{P}$

$$|F(u)| \leq c(|u| + |Du| + \cdots + |D^k u|).$$

With $u = e_{-n}$ this means

$$|a_n| = |F(u)| \leq c(1 + |n| + \cdots + |n|^k) < 2c|n|^k.$$

Thus $(a_n)_{-\infty}^{\infty}$ is of slow growth.

Conversely, suppose $(a_n)_{-\infty}^{\infty} \subset \mathbb{C}$ is a sequence which is of slow growth. Then there is an integer $k > 0$ such that

$$|a_n| \leq c|n|^k, \quad n \neq 0.$$

Let $b_0 = 0$ and

$$b_n = a_n/(in)^k, \quad n \neq 0.$$

Let

$$v_N(x) = \sum_{-N}^{N} b_n \exp(inx).$$

From (5) we get

$$\sum_{-\infty}^{\infty} |b_n| < \infty.$$

Therefore $v_N$ converges uniformly to $v \in \mathcal{C}$. Let

$$F = D^k F_v + F_f, \quad f = a_0 e_0.$$

This is a distribution; we claim that its Fourier coefficients are the $(a_n)_{-\infty}^{\infty}$. In fact, for $n \neq 0$,

$$F(e_{-n}) = D^k F_v(e_{-n}) = F_v((-D)^k e_{-n})$$
$$= (in)^k F_v(e_{-n}) = (in)^k b_n = a_n.$$

Also

$$F(e_0) = D^k F_v(e_0) + F_f(e_0) = 0 + a_0.$$

$\square$

In the course of the preceding proof we gave a second proof of the characterization theorem for periodic distributions, Theorem 6.1 of Chapter 3. In fact, the whole theory of $\mathcal{P}$ and $\mathcal{P}'$ in Chapter 3 can be derived from the point of view of Fourier series.
