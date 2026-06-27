---
role: proof
locale: en
of_concept: optional-sampling-theorem
source_book: gtm017
source_chapter: "VIII"
source_section: "b"
---
For $S \leq T$ bounded by $k$, define $Y_n = X_{\min(T,n)} - X_{\min(S,n)}$. Then $Y_0 = 0$, $Y_k = X_T - X_S$, and
$$E[Y_{n+1}-Y_n|\mathcal{B}_n] = I_{\{S < n+1 \leq T\}} E[X_{n+1}-X_n|\mathcal{B}_n] \leq 0,$$
so $Y$ is a supermartingale. Hence $0 \geq EY_k = E(X_T - X_S)$. For any $A \in \mathcal{B}_S$, apply this to $S = \min(S_A, k)$ and $T = \min(T_A, k)$ to get $\int_A (X_T - X_S) dP \leq 0$, which gives $E[X_T|\mathcal{B}_S] \leq X_S$ by definition of conditional expectation. For a martingale, equality holds throughout.
