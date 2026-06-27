---
role: proof
locale: en
of_concept: prop-consider-aperiodic-transient-random-walk-and
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: We know from part (a) of P2 that $f(x) = H_A(x)$ satisfies the Poisson equation

$$f(x) - \sum_{y \in R} P(x,y)f(y) = \begin{cases} E_A(x) & \text{for } x \in A \\ 0 & \text{for } x \in R - A. \end{cases}$$

To prove P4 we therefore study the general Poisson equation

(a) $$f(x) - \sum_{y \in R} P(x,y)f(y) = \psi(x), \quad x \in R,$$

where $\psi(x)$ is assumed to be a given non-negative function on $R$. We require the following three basic properties of equation (a) (which will be encountered in an even more general setting in section 27).

(i) If $f(x)$ is a non-negative solution of (a), then it may be written

$$f(x) = h(x) + \sum_{t \in R} G(x,t)\psi(t) < \infty, \quad x \in R,$$

where

(ii) $$

At no step is there any question about convergence. The sum representing $P\psi(x)$ exists since $Pf(x)$ exists and $P\psi(x) \leq Pf(x)$. Continuing this way, once $P_nf(x)$ exists, the non-negativity of $f$ and $\psi$ together with the inequality $P_n\psi(x) \leq P_nf(x)$ implies that also $P_n\psi$ exists. Similarly $P_{n+1}f(x)$ exists as $P_{n+1}f(x) \leq P_nf(x)$. Now we add the equations $P_kf - P_{k+1}f = P_k\psi$ over $k = 0, 1, \ldots, n$ to obtain

$$f(x) - P_{n+1}f(x) = G_n\psi(x).$$

Since

$$G_n\psi(x) = \sum_{y \in R} G_n(x,y)\psi(y) \leq f(x) < \infty,$$

and since

$$G_n\psi(x) \leq G_{n+1}\psi(x),$$

one has

$$\lim_{n \to \infty} G_n\psi(x) = \sum_{y \in R} G(x,y)\psi(y).$$

Hence also

$$\lim_{n \to \infty} \sum_{y \in R} P_{n+1}(x,y)f(y) < \infty,$$

and if we call the last limit $h(x)$ we have established (i) and (ii). Finally, one has

$$h(x) = \lim_{n \to \infty} \sum_{y \in R} P_{n+1}(x,y)f(y)$$

$$= \sum_{t \in R} P(x,t)\left[ \lim_{n \to \infty} \sum_{y \in R} P_n(t,y)f(y) \right] = \sum_{t \in R} P(x,t)h(t),$$

so that $h(x)$ is regular and (iii) holds.

To complete the proof of P4, we set

$$\psi(x) = E_A(x) \text{ for } x \text{ in } A, \quad \psi(x) = 0

To illuminate the result and the proof of P4 from a nonprobabilistic point of view, let us look at a simple special case. The equation

(b) $f(x) - \sum_{y \in R} P(x,y)f(y) = \delta(x,0), \quad x \in R,$

has the solution $f(x) = G(x,0)$. We have used this observation many times, most recently in several proofs in section 24. It would be interesting to be able to characterize the function $G(x,0)$ by the property that it satisfies (b) together with as few other natural requirements as possible. Now (i) through (iii) in the proof of P4 imply that the only non-negative solutions of (b) are the functions

$$f(x) = h(x) + G(x,0),$$

where $h(x)$ is any regular function. Although we have no information as yet concerning the possible unbounded regular functions (the bounded ones are constant) we are in a position to assert
