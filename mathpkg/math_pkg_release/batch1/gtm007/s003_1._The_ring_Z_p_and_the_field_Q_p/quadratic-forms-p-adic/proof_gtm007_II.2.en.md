---
role: proof
locale: en
of_concept: quadratic-forms-p-adic
source_book: gtm007
source_chapter: "II. p-Adic Fields"
source_section: "2. p-adic equations"
---

*Proof.* Let $f$ be the quadratic form $\sum a_{ij} X_i X_j$ with $\det(a_{ij}) \in \mathbb{Z}_p^\times$. We apply the $p$-adic Newton method (Hensel's lemma) to show representability. For any element $a \in \mathbb{Z}_p$, we need to find $x \in \mathbb{Z}_p^m$ such that $f(x) = a$.

Consider first the problem modulo $p$: since the discriminant is invertible modulo $p$, the reduced quadratic form $\bar{f}$ over $\mathbb{F}_p$ is nondegenerate. A standard result on quadratic forms over finite fields (proved earlier in the text) shows that a nondegenerate quadratic form in $m \geq 3$ variables over $\mathbb{F}_p$ represents every element of $\mathbb{F}_p$. Thus, for any $a \in \mathbb{Z}_p$, there exists $x^{(1)} \in \mathbb{Z}_p^m$ such that $f(x^{(1)}) \equiv a \pmod{p}$.

Now we lift the solution using the Newton method. Set $g(X) = f(X) - a$. If the gradient $\nabla g(x^{(1)}) = 2\sum_j a_{ij}x_j^{(1)}$ is not the zero vector modulo $p$ (which is guaranteed if we choose $x^{(1)}$ appropriately, using the nondegeneracy of the form), then we are in the situation of a simple zero and Corollary 1 (or directly the Newton lemma with $k=0$) lifts $x^{(1)}$ to a solution $x \in \mathbb{Z}_p^m$ of $g(x) = 0$, i.e., $f(x) = a$. The same argument with scaling by powers of $p$ extends to elements of $\mathbb{Q}_p$. $\square$
