---
role: proof
locale: en
of_concept: smooth-periodic-fourier-coefficients-characterization
source_book: gtm012
source_chapter: "5"
source_section: "§1. Fourier series of smooth periodic functions and of periodic distributions"
---

# Proof of Characterization of Fourier Coefficients of Smooth Periodic Functions

**Theorem 1.1.** A sequence $(a_n)_{-\infty}^{\infty} \subset \mathbb{C}$ is the sequence of Fourier coefficients of a function $u \in \mathcal{P}$ if and only if it is of rapid decrease.

**Proof.** Suppose first that $u \in \mathcal{P}$ has $(a_n)_{-\infty}^{\infty}$ as its sequence of Fourier coefficients. Given $r > 0$, take an integer $k \geq r$. In proving Theorem 6.4 of Chapter 4 we noted that $(ina_n)_{-\infty}^{\infty}$ is the sequence of Fourier coefficients of $Du$. It follows that

$$((in)^k a_n)_{-\infty}^{\infty}$$

is the sequence of Fourier coefficients of $D^k u$. But then

$$|n|^k |a_n| \leq |D^k u|,$$

which gives (2) with $c = |D^k u|$.

Conversely, suppose $(a_n)_{-\infty}^{\infty} \subset \mathbb{C}$ is a sequence which is of rapid decrease. Define functions $u_N$ by

$$u_N(x) = \sum_{-N}^{N} a_n \exp(inx).$$

From (2) with $r = 2$ we deduce

$$\sum_{-\infty}^{\infty} |a_n| < \infty.$$

By Lemma 6.3 of Chapter 4, the functions $u_N$ converge uniformly to $u \in \mathcal{C}$, and $(a_n)_{-\infty}^{\infty}$ are the Fourier coefficients of $u$. Also

$$D^k u_N = \sum_{-N}^{N} (in)^k a_n e_n.$$

and (2) with $r = k + 2$ implies

$$\sum_{-\infty}^{\infty} |n|^k |a_n| < \infty.$$

Thus each derivative $D^k u_N$ also converges uniformly as $N \to \infty$. Therefore $u \in \mathcal{P}$. $\square$
