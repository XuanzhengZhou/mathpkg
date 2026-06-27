---
role: proof
locale: en
of_concept: extinction-probability-equation
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of Extinction Probability Equation for Branching Processes

Consider the Galton–Watson branching process defined by the recurrence

$$\xi_{k+1} = \sum_{i=1}^{\xi_k} \eta_i^{(k)}, \quad \xi_0 = 1,$$

where $\{\eta_i^{(k)},\; i \geq 1,\; k \geq 0\}$ is a sequence of independent identically distributed random variables having the same distribution as a random variable $\eta$, with probabilities

$$p_k = P(\eta = k), \quad k \geq 0, \quad \sum_{k=0}^{\infty} p_k = 1,$$

and for each $k$ the random variables $\eta_i^{(k)}$ are independent of $\xi_1, \ldots, \xi_k$. Each particle independently of others and of the prehistory turns into $j$ particles with probabilities $p_j$, $j \geq 0$.

Let

$$G(x) = \sum_{k=0}^{\infty} p_k x^k, \quad |x| \leq 1,$$

be the generating function of the offspring distribution $\eta$ (so $G(x) = \mathbb{E}\, x^{\eta}$), and let

$$F_k(x) = \mathbb{E}\, x^{\xi_k}$$

be the generating function of the population size $\xi_k$ at generation $k$.

Using the recurrence formula for $\xi_{k+1}$ and the property of conditional expectations, together with the independence assumption, one obtains for $k \geq 0$:

$$F_{k+1}(x) = \mathbb{E}\, x^{\xi_{k+1}} = \mathbb{E}\Bigl[ \mathbb{E}\bigl( x^{\xi_{k+1}} \mid \xi_k \bigr) \Bigr] = \mathbb{E}\bigl[ G(x)^{\xi_k} \bigr] = F_k(G(x)).$$

Also, by symmetry,

$$F_{k+1}(x) = G(F_k(x)).$$

Starting from $\xi_0 = 1$, we have $F_0(x) = x$. Iterating the relation $F_{k+1}(x) = G(F_k(x))$ yields

$$F_1(x) = G(x), \quad F_2(x) = G(G(x)), \quad \ldots, \quad F_N(x) = \underbrace{G \circ G \circ \cdots \circ G}_{N}(x).$$

The extinction probability $q$ is defined as

$$q = P(\text{ultimate extinction}) = \lim_{N \to \infty} P(\xi_N = 0).$$

Since $P(\xi_N = 0) = F_N(0)$, we obtain

$$q = \lim_{N \to \infty} F_N(0).$$

Now from the recurrence $F_N(x) = G(F_{N-1}(x))$ it follows that $F_N(0) = G(F_{N-1}(0))$. Passing to the limit as $N \to \infty$ and using the continuity of $G$ on $[0,1]$,

$$q = G(q), \quad 0 \leq q \leq 1.$$

The examination of the solutions to this fixed-point equation $q = G(q)$ shows that:

(a) if $\mathbb{E}\,\eta = G'(1) > 1$, then the extinction probability satisfies $0 < q < 1$;

(b) if $\mathbb{E}\,\eta = G'(1) \leq 1$, then the extinction probability is $q = 1$.

Thus the extinction probability is the smallest nonnegative root of the equation $q = G(q)$ in $[0,1]$.
