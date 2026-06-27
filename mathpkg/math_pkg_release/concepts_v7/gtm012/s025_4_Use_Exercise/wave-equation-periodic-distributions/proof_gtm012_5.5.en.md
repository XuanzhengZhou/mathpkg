---
role: proof
locale: en
of_concept: wave-equation-periodic-distributions
source_book: gtm012
source_chapter: "5"
source_section: "5. The wave equation"
---

# Proof of Existence and Uniqueness for the Wave Equation on Periodic Distributions

**Theorem 5.1.** For each $G, H \in \mathcal{P}'$ there is a unique family $(F_t)_{t > 0} \subset \mathcal{P}'$ with the following properties:

1. $\frac{d}{dt} F_t \big|_s$ exists for each $s > 0$,
2. $\left( \frac{d}{dt} \right)^2 F_t \big|_s = D^2 F_s$ for all $s > 0$,
3. $F_t \to G$ in $\mathcal{P}'$ as $t \to 0$,
4. $\frac{d}{dt} F_t \big|_s \to H$ in $\mathcal{P}'$ as $s \to 0$.

*Proof.* Let $(b_n)_{n=-\infty}^{\infty}$ be the sequence of Fourier coefficients of $G$, and let $(c_n)_{n=-\infty}^{\infty}$ be the sequence of Fourier coefficients of $H$. If $(F_t)_{t > 0}$ is such a family of distributions, let the Fourier coefficients of $F_t$ be $(a_n(t))_{n=-\infty}^{\infty}$.

As in the proof of Theorem 3.1, conditions (2), (3), (4) imply that for each $n$, the function $a_n$ is twice continuously differentiable for $t > 0$, and $a_n$ and $Da_n$ have limits as $t \to 0$, and

$$D^2 a_n(t) = -n^2 a_n(t), \quad t > 0,$$
$$a_n(0) = b_n, \quad Da_n(0) = c_n.$$

The unique function satisfying these conditions (see §6 of Chapter 2) is

$$a_n(t) = b_n \cos nt + n^{-1}c_n \sin nt, \quad n \neq 0,$$
$$a_0(t) = b_0 + c_0 t.$$

In particular, for each $t > 0$, the sequence $(a_n(t))_{n=-\infty}^{\infty}$ is a sequence of slowly growing type, so it defines a periodic distribution $F_t \in \mathcal{P}'$. The sequence $(Da_n(t))_{n=-\infty}^{\infty}$ is also of slowly growing type. Moreover,

$$\frac{d}{dt} F_t \bigg|_{t=s}$$

exists for $s > 0$ and has Fourier coefficients $(Da_n(s))_{n=-\infty}^{\infty}$, which gives condition (4).

To verify condition (2), we estimate:

$$|D^2 a_n(t)| = |n^2 b_n \cos nt + n c_n \sin nt| \leq |n^2 b_n| + |n c_n|, \quad \text{for all } n.$$

Since $(b_n)$ and $(c_n)$ are slowly growing sequences, the sequence $(n^2 b_n + n c_n)_{n=-\infty}^{\infty}$ is also slowly growing. It follows that

$$\left( \frac{d}{dt} \right)^2 F_t \bigg|_{t=s}$$

exists for each $s > 0$, and its Fourier coefficients are $(D^2 a_n(s))_{n=-\infty}^{\infty} = (-n^2 a_n(s))_{n=-\infty}^{\infty}$, which are precisely the Fourier coefficients of $D^2 F_s$. Thus

$$\left( \frac{d}{dt} \right)^2 F_t \bigg|_{t=s} = D^2 F_s, \quad \text{for all } s > 0.$$

The uniqueness follows from the uniqueness of the solution to the initial value problem for the ordinary differential equation $D^2 a_n(t) = -n^2 a_n(t)$ with given initial data $(b_n, c_n)$, together with the fact that a periodic distribution is uniquely determined by its Fourier coefficients. $\square$
