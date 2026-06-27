---
role: proof
locale: en
of_concept: lambda-partial-geometry-f5
source_book: gtm054
source_chapter: "9"
source_section: "Section 44"
---

Equation (a) is precisely C7 and (b) is immediate. To prove (c), let $L_0 \in \mathcal{L}$ and $x_0 \in V + L_0$. By F2, $x_0$ lies on at least $t$ lines. Hence, $t \leq r$. By F3, no two of these lines can intersect in any point other than $x_0$. Hence they meet $L_0$ in $t$ distinct points, and so $t \leq k$.

To prove (d), we fix $L_0 \in \mathcal{L}$ and enumerate the set

$$\{(x, L): x \in L \cap (V + L_0); L \cap L_0 \neq \emptyset\}$$

in two ways. First we may choose $x \in V + L_0$ in $(v - k)$ ways

for each $x \in V$. Let $L_0 \in \mathcal{L}$ and let $x_0^*$ be a dual line such that $L_0 \notin x_0^*$. Since $x_0 \notin L_0$, there exists a $t$-set $\mathcal{T}$ of lines through $x_0$ which meet $L_0$. For each $L \in \mathcal{T}$, let $x_L \in L \cap L_0$. By F3, these points $x_L$ are all distinct. It is clear then that each of the $t$ dual lines in $\{x_L^* : L \in \mathcal{T}\}$ contains $L_0$ and meets $x_0^*$. Also no other dual lines through $L_0$ meet $x_0^*$. We have proved:
