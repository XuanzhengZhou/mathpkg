---
role: proof
locale: en
of_concept: boolean-to-reversible-circuit-claim
source_book: gtm053
source_chapter: "8"
source_section: "8.3"
---
Let $L$ be the sum of sizes of the outputs of all gates in $S$. First replace each gate $f$ in $S$ by its reversible counterpart $\tilde{f}$, inserting extra bits into a new register of total length $L$. The resulting subcircuit calculates a permutation $K : \mathbf{F}_2^{m+L} \rightarrow \mathbf{F}_2^{m+L}$ such that $K(x,0) = (F(x), G(x))$ for some garbage function $G$.

Now add one more register of size $n$ for the variable $y$. Extend $K$ to the permutation $\overline{K} : \mathbf{F}_2^{m+L+n} \rightarrow \mathbf{F}_2^{m+L+n}$ keeping $y$ intact: $\overline{K} : (x, z, y) \mapsto (K(x,z), y)$. Then copy the result $F(x)$ bitwise to $y$ (using controlled-NOT gates), and apply the inverse $K^{-1}$ to erase the garbage. The total gate count is $O((L+m+n)^2)$.
