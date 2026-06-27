---
role: proof
locale: en
of_concept: upper-semicontinuity-of-local-ring-dimension
source_book: gtm014
source_chapter: "VII. The Local Ring of a Singularity"
source_section: "2. Finite Mappings"
---

**Proof.** Let $x_1, \ldots, x_n$ be a coordinate system centered at $x$, and $y_1, \ldots, y_m$ a coordinate system centered at the image point $f(x)$. Let $p_1, \ldots, p_k$ be elements of $C_x^\infty$ projecting onto a basis of $\mathcal{R}_f(x)$ over $\mathbf{R}$. By the Malgrange Preparation Theorem, $p_1, \ldots, p_k$ generate $C_x^\infty$ as a module over $C_y^\infty$. We can assume that the functions $p_1, \ldots, p_k$ are polynomials in the $x_i$'s of degree $< N$.

We will show that there exists a fixed open set $U$ about $x$ such that on $U$ every polynomial in the $x_i$'s can be written as a linear combination of the $p_i$'s with smooth functions of the $y_i$'s as coefficients.

First note that this statement is true for some $U$ and for all polynomials of degree $\leq N$. Indeed, for any monomial we can find an open set $U$ since the statement is true for germs at $x$. Thus we can find an open set $U$ which works for all monomials of degree $\leq N$. By linearity, $U$ works for all polynomials of degree $\leq N$.

Now consider a polynomial of the form $x^\alpha p$ where $\deg p = N$. The polynomial $x^\alpha p$ can be written as a linear combination of the $x^\alpha p_i$'s and, hence, by induction on the degree, every polynomial in the $x_i$'s admits such a representation on $U$.

It follows that for every $x' \in U$, the elements $p_1, \ldots, p_k$ project onto a spanning set of $\mathcal{R}_f(x')$, so
$$\dim_{\mathbf{R}} \mathcal{R}_f(x') \leq k = \dim_{\mathbf{R}} \mathcal{R}_f(x).$$
This proves upper semi-continuity. If $f$ is finite at $x$, then $k < \infty$, and the inequality shows finiteness at all points of $U$.
