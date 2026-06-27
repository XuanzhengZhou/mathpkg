---
role: proof
locale: en
of_concept: numerical-polynomial-binomial-representation
source_book: gtm052
source_chapter: "I"
source_section: "7"
---
Let $\Delta P(z) = P(z+1) - P(z)$ be the difference operator. If $P$ has degree $r$, then $\Delta P$ has degree $r-1$. Moreover, $\Delta \binom{z}{r} = \binom{z}{r-1}$. 

We proceed by induction on the degree. For degree $0$, $P$ is constant, and since $P(n) \in \mathbf{Z}$ for large $n$, the constant is an integer. Assume the result holds for degree $r-1$. Let $P$ have degree $r$ with leading coefficient $a_r$. Then $\Delta P$ has degree $r-1$ with leading coefficient $r a_r$. By induction, $\Delta P(z) = d_0 \binom{z}{r-1} + \ldots + d_{r-1}$ with $d_i \in \mathbf{Z}$.

Let $Q(z) = d_0 \binom{z}{r} + d_1 \binom{z}{r-1} + \ldots + d_{r-1} \binom{z}{1}$. Then $\Delta Q = \Delta P$, so $\Delta(P - Q)(n) = 0$ for all $n \gg 0$, so $(P - Q)(n) = \text{constant } c_r$ for all $n \gg 0$. Thus
$$P(n) = d_0 \binom{n}{r} + d_1 \binom{n}{r-1} + \ldots + d_{r-1} \binom{n}{1} + c_r$$
for all $n \gg 0$. Since both sides are polynomials in $n$, equality holds for all $z$. Moreover, since $P(n) \in \mathbf{Z}$ for large $n$, evaluating at $n$ large gives $c_r \in \mathbf{Z}$. Renaming $c_i = d_{i-1}$ gives the required form.
