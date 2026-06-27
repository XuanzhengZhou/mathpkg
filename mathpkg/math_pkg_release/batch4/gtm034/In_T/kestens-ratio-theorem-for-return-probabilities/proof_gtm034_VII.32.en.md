---
role: proof
locale: en
of_concept: kestens-ratio-theorem-for-return-probabilities
source_book: gtm034
source_chapter: "VII"
source_section: "32"
---

The proof proceeds through Propositions P5-P8.

**P5 (Exponential lower bound).** For every $\epsilon > 0$, $F_n \geq (1-\epsilon)^n/(n-2)$ for sufficiently large $n$. Choose $a_1 > 0$, $a_2 > 0$ with $P(0,a_1) > 0$ and $P(0,-a_2) > 0$. Then $P[S_1 = a_1, S_{n-1} - S_1 = a_2 - a_1, S_n = 0] \geq (1-\epsilon)^n$. Using cyclic permutations of $X_2,\ldots,X_{n-1}$, at least one of $n-2$ polygonal paths lies above its chord; the identity permutation gives $F_n \geq (1-\epsilon)^n/(n-2)$.

**P6 (Conditional bound).** For every $m$ and $\epsilon > 0$, there exists $M = M(m,\epsilon)$ such that $\lim_{n \to \infty} \frac{1}{n}\sum_{k=1}^{n-M} P[|S_k| \leq A \text{ or } S_{k+j} \neq S_k \text{ for } m \leq j \leq M \mid T=n] \leq \epsilon$.

**P7 (Ratio approximation).** Given $\epsilon_1 > 0$, $m$, $A$, there exist $k$ and $M$ such that $|q_n/F_n - 1| \leq \epsilon_1$ for large $n$, where $q_n = P[T=n, |S_k| > A, S_{k+j} = S_k \text{ for some } m \leq j \leq M]$.

**P8 (Difference inequality).** $|q_n - \tilde{q}_{n+1}| \leq \epsilon_1 q_n$ using decomposition of $q_n$ and bounds on $|c_{k,j+1} - c_{k,j}|$.

Since $\tilde{q}_{n+1} \leq F_{n+1}$, P8 and P7 give $F_{n+1} \geq (1-\epsilon_1)^2 F_n$, so $\liminf F_{n+1}/F_n \geq 1$. A symmetric argument yields $\limsup F_{n+1}/F_n \leq 1$, proving $\lim F_{n+1}/F_n = 1$.
