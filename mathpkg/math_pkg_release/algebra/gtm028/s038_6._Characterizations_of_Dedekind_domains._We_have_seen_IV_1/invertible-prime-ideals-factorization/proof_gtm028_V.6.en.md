---
role: proof
locale: en
of_concept: invertible-prime-ideals-factorization
source_book: gtm028
source_chapter: "V"
source_section: "6. Characterizations of Dedekind domains"
---

Suppose $\mathfrak{p} = \prod_{i=1}^n \mathfrak{p}_i$ where the $\mathfrak{p}_i$ are prime ideals, and $\mathfrak{p}$ is invertible. Since $\prod_i \mathfrak{p}_i \subset \mathfrak{p}_1$, the prime ideal $\mathfrak{p}$ is contained in $\mathfrak{p}_1$, so some $\mathfrak{p}_i$, say $\mathfrak{p}_1$, is contained in $\mathfrak{p}$. By symmetry, $\mathfrak{p}$ is contained in some $\mathfrak{p}_j$, say $\mathfrak{p}_r \subset \mathfrak{p} \subset \mathfrak{p}_1$. From the minimality of $\mathfrak{p}_1$ among the $\mathfrak{p}_i$, we deduce $\mathfrak{p}_r = \mathfrak{p} = \mathfrak{p}_1$.

To show each $\mathfrak{p}_i$ is invertible, multiply the equality $\prod_i \mathfrak{p}_i = \mathfrak{p}$ by $\mathfrak{p}^{-1}$ to get $\prod_{i \neq 1} \mathfrak{p}_i = R$ (after absorbing $\mathfrak{p}_1 = \mathfrak{p}$). Thus each $\mathfrak{p}_i$ for $i \neq 1$ divides the unit ideal, hence is invertible. For $\mathfrak{p}_1 = \mathfrak{p}$, invertibility is given. More generally, by induction on $n$: if $n = 1$ the claim is trivial. For $n > 1$, multiply the factorization by $\mathfrak{p}_1^{-1}$ to obtain $\prod_{i \neq 1} \mathfrak{p}_i = \mathfrak{p} \cdot \mathfrak{p}_1^{-1} \subset R$, and the induction hypothesis applied to the remaining $n-1$ factors (after noting that their product is integral) yields that each is invertible.
