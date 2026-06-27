---
role: proof
locale: en
of_concept: prop-there-is-a-constant-such-that
source_book: gtm034
source_chapter: "5"
source_section: "012"
---

Proof: In view of P4 we can choose $M$ such that $0 \leq u(x) \leq M, 0 \leq v(x) \leq M$, for all $x \geq 0$. But it is probabilistically obvious that

$$g_N(x,y) \leq g(x,y) \leq M \min(1+x,1+y) = M[1 + \min(x,y)].$$

On the other hand, we have

$$g_N(x,y) = g_N(N-y,N-x).$$

This is not a mistake! To verify it one need not even introduce the reversed random walk, as this simple identity follows directly from the definition of $g_N(x,y)$ in D21.1. Therefore we also have

$$g_N(x,y) \leq g(N-y,N-x) \leq M \min[1+N-y,1+N-x]$$

which completes the proof of P5.

Now we take up the study of the hitting probabilities $R_N(x,k)$ and $L_N(x,k)$ of the two components of the complement of the interval $[0,N]$.
