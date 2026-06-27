---
role: proof
locale: en
of_concept: regular-functions-basic-example
source_book: gtm040
source_chapter: "8"
source_section: "6"
---

**(i) $P$-regular functions.** A function $r$ is $P$-regular if $r = Pr$, i.e., for all $i \geq 0$,
$$r_i = (Pr)_i = p_{i+1} r_{i+1} + q_{i+1} r_0.$$
For $i = 0$, this gives
$$r_0 = p_1 r_1 + q_1 r_0.$$
Since $p_1 + q_1 = 1$, we have $p_1 r_0 = p_1 r_1$, and since $p_1 > 0$, we obtain $r_0 = r_1$.

Now assume by induction that $r_0 = r_1 = \cdots = r_k$. For $i = k$, the regularity condition gives
$$r_k = p_{k+1} r_{k+1} + q_{k+1} r_0.$$
Since $r_k = r_0$ and $p_{k+1} + q_{k+1} = 1$,
$$r_0 = p_{k+1} r_{k+1} + q_{k+1} r_0 \implies p_{k+1} r_0 = p_{k+1} r_{k+1} \implies r_0 = r_{k+1}.$$
Thus $r_i = r_0$ for all $i$, so $r$ is a constant function. Conversely, any constant function is $P$-regular since $P1 = 1$.

**(ii) $\hat{P}$-regular signed measures.** A row vector $\mu$ satisfies $\mu = \mu \hat{P}$ if and only if its dual $r_i = \mu_i / \beta_i$ satisfies $r_i = (Pr)_i$ (this is the general duality between regular functions and signed measures). From (i), $r$ must be constant, so $r_i = c$ for all $i$, giving $\mu_i = c \beta_i$. Thus the $\hat{P}$-regular signed measures are exactly the multiples of $\beta$.

**(iii) $P$ has no non-zero regular signed measures.** A signed measure $\nu$ is $P$-regular if $\nu = \nu P$. The dual function $h_j = \nu_j / \beta_j$ would satisfy $h = \hat{P}h$. But $\hat{P}1 \neq 1$ (since $\sum_j \hat{P}_{0j} = 1 - \beta_\infty < 1$ in the transient case), so the constant function $1$ is not $\hat{P}$-regular. Any $\hat{P}$-regular function would, by an argument dual to (i), need to be constant, yielding a contradiction. Hence the only $P$-regular signed measure is the zero measure.

**(iv) $\hat{P}$ has no non-zero regular functions.** Dual to (iii): a $\hat{P}$-regular function would correspond to a $P$-regular signed measure, which we just showed must be zero.

**Superregular functions.** A non-negative function is $P$-superregular if $g \geq Pg$. By the Riesz decomposition, any non-negative superregular function decomposes as a potential plus a regular function. For $P$, the regular functions are constants, so non-negative $P$-superregular functions are pure potentials plus non-negative constants. For $\hat{P}$, there are no non-zero regular functions, so every non-negative $\hat{P}$-superregular function is a pure potential.
