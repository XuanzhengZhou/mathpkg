---
role: proof
locale: en
of_concept: corollary-8-69
source_book: gtm040
source_chapter: "8"
source_section: "There exists an equilibrium set"
---

By Proposition 8-68,
$$a^{(r)} = N \sum_{m=1}^{r-1} \binom{r}{m} Q a^{(m)} + N\mathbf{1},$$
even if both sides are infinite. Hence
$$a^{(r)} \leq (2^r - 2) N Q a^{(r-1)} + N\mathbf{1} \quad \text{since } a^{(m)} \leq a^{(r-1)}$$
$$= (2^r - 2)(N - I)a^{(r-1)} + N\mathbf{1} \quad \text{since } N - I = NQ$$
$$\leq (2^r - 2)N a^{(r-1)} + N\mathbf{1}$$
$$\leq (2^r - 1) N a^{(r-1)} \quad \text{since } \mathbf{1} \leq a^{(r-1)}.$$
Thus we may take $c = 2^r - 1$ on the right. For the other inequality,
$$a^{(r)} \geq N Q a^{(r-1)}$$
$$= N a^{(r-1)} - a^{(r-1)}$$
$$\geq N a^{(r-1)} - a^{(r)} \quad \text{since } a^{(r-1)} \leq a^{(r)}.$$
Hence $N a^{(r-1)} \leq 2 a^{(r)}$, so we may take $d = \frac{1}{2}$ or, rearranging, $a^{(r)} \geq \frac{1}{2} N a^{(r-1)}$.
