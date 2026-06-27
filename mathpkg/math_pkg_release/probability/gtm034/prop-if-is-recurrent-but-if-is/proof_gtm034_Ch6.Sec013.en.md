---
role: proof
locale: en
of_concept: prop-if-is-recurrent-but-if-is
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: The first statement has already been verified, in the course of the proof of P6. We also know, from P4, that $h_A(x)$ is a constant, called $h_A$. Therefore we may assume that $A$ is transient and concentrate on proving that $h_A = 0$. But we shall actually forget about whether or not $A$ is transient and prove an apparently stronger result, namely

(1) $$h_A[1 - H_A(x)] = 0 \text{ for all } x \text{ in } R.$$

Equation (1) will finish the proof of P8, for if $A$ is transient, then $1 - H_A(x) > 0$ for some $x \in R - A

This statement is probabilistically very plausible: $h_A(x)$ gives the probability of infinitely many visits to $A$, starting at $x$. This event is decomposed according to the point $y$ of the first visit to $A$. After this first visit, the random walk, now starting at $y$, is still required to pay an infinite number of visits to $A$. The resulting sum of probabilities is precisely the right-hand side in (2).

In apparently similar cases in the past we have often "declared" a theorem proved after such a heuristic outline of what must obviously be done. Nevertheless, the present argument being by far the most complicated example of its kind we have encountered, we insist on presenting a complete proof. The events $A_n$ will be the same as in the proof of P7, as will $B_n = \bigcup_{k=n}^{\infty} A_k$, and $C_n$ will be the event that $T = n$, where $T$ is the stopping time $T = \min[n \mid n \geq 1, x_n \in A]$.

The right-hand side in (2) is

$$\sum_{y \in A} H_A(x,y)h_A(y) = \lim_{n \to \infty} \sum_{y \in A} H_A(x,y) \sum_{t \in R} P_n(y,t)H_A(t)$$

$$= \lim_{n \to \infty} P_z \left[ \bigcup_{k=1}^{\infty} \left(C_k \cap \bigcup_{j=k+n}^{\infty} A_j\right) \right] = P_z \left[ \bigcup_{k=1}^{\infty} \left(C_k \cap \bigcap_{n=1}^{\infty} B_{k+n}\right) \right]$$

Observing that the sets $B_k$ are decreasing,

$$\bigcap_{n=1}^{\infty} B_{k+n} = \bigcap_{n=1}^{\infty} B_n$$

so that the last probability is

$$P_z \left[ \bigcup_{k=1}^{\infty} \left(C_k \cap \bigcap_{n=1}^{\infty} B_n\right) \right] = P_z \left[ \bigcup_{k=1}^{\infty} C_k \
