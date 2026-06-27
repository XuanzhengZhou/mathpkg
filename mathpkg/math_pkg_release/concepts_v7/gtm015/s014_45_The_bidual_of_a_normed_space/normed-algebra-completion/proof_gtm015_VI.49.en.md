---
role: proof
locale: en
of_concept: normed-algebra-completion
source_book: gtm015
source_chapter: "VI"
source_section: "49"
---

# Proof of Completion of a Normed Algebra

Viewing $A$ as a normed space, one first constructs a Banach space $B$ and an isometric linear mapping $\varphi: A \to B$ such that $\varphi(A)$ is dense in $B$. (A fast proof is available via the Hahn-Banach theorem (40.15), embedding $A$ isometrically into its bidual; a more elementary proof is indicated in (16.18), using equivalence classes of Cauchy sequences.)

Identifying $A$ with $\varphi(A)$, i.e., viewing $A$ as a dense linear subspace of the Banach space $B$, there remains the task of extending the multiplication of $A$ to all of $B$. Assuming $u, v \in B$, we are to define the product $uv$. Choose sequences $(x_n)$, $(y_n)$ in $A$ with $x_n \to u$ and $y_n \to v$. Since $(x_n y_n)$ is Cauchy (by Proposition 49.2(ii)), it converges to a limit $w$ in $B$. One verifies that this limit is independent of the choice of sequences: if $x_n' \to u$ and $y_n' \to v$, then
$$\|x_n y_n - x_n' y_n'\| \leq \|x_n\|\|y_n - y_n'\| + \|x_n - x_n'\|\|y_n'\| \to 0,$$
so the limits coincide. Define $uv = w$.

The verification that this multiplication makes $B$ into an algebra (associative, bilinear) and that the norm satisfies $\|uv\| \leq \|u\|\|v\|$ follows by taking limits of the corresponding relations in $A$. If $A$ has a unity element $e$, then $\varphi(e)$ is a unity element for $B$ because $\varphi(e) \cdot \lim x_n = \lim \varphi(e) x_n = \lim \varphi(x_n) = \lim x_n$ for any $\lim x_n \in B$, and similarly on the right. The mapping $\varphi$ is then an algebra monomorphism. $\square$
