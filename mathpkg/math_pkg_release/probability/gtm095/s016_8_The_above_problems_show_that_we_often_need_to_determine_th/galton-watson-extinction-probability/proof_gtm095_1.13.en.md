---
role: proof
locale: en
of_concept: galton-watson-extinction-probability
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of Galton–Watson Extinction Probability

Consider the Galton–Watson branching process defined by the recurrence

$$\xi_{k+1} = \sum_{i=1}^{\xi_k} \eta_i^{(k)}, \quad \xi_0 = 1,$$

where $\{\eta_i^{(k)},\; i \geq 1,\; k \geq 0\}$ is a sequence of independent identically distributed random variables having the same distribution as a random variable $\eta$, with offspring probabilities

$$p_k = P(\eta = k), \quad k \geq 0, \quad \sum_{k=0}^{\infty} p_k = 1.$$

It is assumed that for each $k$, the random variables $\eta_i^{(k)}$ are independent of $\xi_1, \ldots, \xi_k$. Thus each particle independently of others and of the prehistory turns into $j$ particles with probability $p_j$, $j \geq 0$.

Let $\tau = \inf\{k \geq 0 : \xi_k = 0\}$ be the extinction time, with the convention $\tau = \infty$ if $\xi_k > 0$ for all $k \geq 0$.

Define the generating function of the offspring distribution:

$$G(x) = \sum_{k=0}^{\infty} p_k x^k, \quad |x| \leq 1,$$

so that $G(x) = \mathbb{E}\, x^{\eta}$. Let $F_k(x) = \mathbb{E}\, x^{\xi_k}$ be the generating function of the population size at the $k$-th generation.

Using the recurrence for $\xi_{k+1}$ and the properties of conditional expectations together with the independence assumption, we obtain for $k \geq 0$:

$$F_{k+1}(x) = \mathbb{E}\, x^{\xi_{k+1}} = \mathbb{E}\Bigl[ \mathbb{E}\bigl( x^{\xi_{k+1}} \mid \xi_k \bigr) \Bigr] = \mathbb{E}\bigl[ G(x)^{\xi_k} \bigr] = F_k(G(x)).$$

By the same reasoning, one also has the symmetric relation $F_{k+1}(x) = G(F_k(x))$.

Starting from $\xi_0 = 1$, we have $F_0(x) = x$. Iterating the relation $F_{k+1} = G \circ F_k$ yields

$$F_1(x) = G(x), \quad F_2(x) = G(G(x)), \quad \ldots, \quad F_N(x) = \underbrace{G \circ G \circ \cdots \circ G}_{N}(x).$$

The ultimate extinction probability $q$ is

$$q = P(\tau < \infty) = P\!\left(\bigcup_{N=1}^{\infty} \{\xi_N = 0\}\right) = \lim_{N \to \infty} P(\xi_N = 0).$$

Since $P(\xi_N = 0) = F_N(0)$, we have

$$q = \lim_{N \to \infty} F_N(0).$$

From the recurrence $F_N(x) = G(F_{N-1}(x))$, evaluating at $x = 0$ gives $F_N(0) = G(F_{N-1}(0))$. Passing to the limit as $N \to \infty$ and using the continuity of $G$ on $[0,1]$ yields the fixed-point equation

$$q = G(q), \quad 0 \leq q \leq 1.$$

The analysis of the solutions to $q = G(q)$ on $[0,1]$ shows that the extinction probability $q$ is the smallest nonnegative root of this equation. Moreover:

**(a)** If $\mathbb{E}\,\eta = G'(1) > 1$ (supercritical case), then $0 < q < 1$; the extinction probability is strictly between $0$ and $1$.

**(b)** If $\mathbb{E}\,\eta = G'(1) \leq 1$ (critical or subcritical case), then $q = 1$; extinction is almost sure.

Thus the fate of the branching process is determined by the mean offspring number $\mathbb{E}\,\eta$ and the smallest fixed point of the generating function $G$ in $[0,1]$.
