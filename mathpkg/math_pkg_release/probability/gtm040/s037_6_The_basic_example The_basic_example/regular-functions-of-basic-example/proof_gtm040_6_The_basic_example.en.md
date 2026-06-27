---
role: proof
locale: en
of_concept: regular-functions-of-basic-example
source_book: gtm040
source_chapter: "6"
source_section: "The basic example"
---

If $r$ is a $P$-regular function, then $r_i = (Pr)_i$ for all $i$. For the basic example:
$$r_i = p_{i+1} r_{i+1} + q_{i+1} r_0.$$

For $i = 0$:
$$r_0 = p_1 r_1 + q_1 r_0,$$
which implies $p_1 r_0 = p_1 r_1$. Since $p_1 > 0$, we have $r_0 = r_1$.

By induction, suppose $r_k = r_0$ for all $k \leq i$. Then from the regularity equation for $i$:
$$r_i = p_{i+1} r_{i+1} + q_{i+1} r_0.$$

Since $r_i = r_0$ by induction hypothesis, and $p_{i+1} + q_{i+1} = 1$:
$$r_0 = p_{i+1} r_{i+1} + q_{i+1} r_0,$$
so $p_{i+1} r_0 = p_{i+1} r_{i+1}$, hence $r_{i+1} = r_0$.

Thus $r_i = r_0$ for all $i$, and only the constant functions are $P$-regular.

By duality, the regular signed measures for $\hat{P}$ are multiples of the regular measure $\beta$ (since $\beta \hat{P} = \beta$). Since $P$ has no regular signed measures (the chain has no finite invariant measure when $\sum \beta_i = \infty$), dually $\hat{P}$ has no non-zero regular functions.

The final statement about non-negative superregular functions follows from the Riesz decomposition: every non-negative superregular function is the sum of a potential and a regular function. For $P$, the regular part must be a non-negative constant. For $\hat{P}$, the regular part must be zero, leaving only pure potentials.
