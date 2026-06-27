---
role: proof
locale: en
of_concept: "let-and-be-normed-linear-spaces-over-and"
source_book: gtm025
source_chapter: "Abstract Banach Spaces"
source_section: "14.4"
---

We prove only that $\mathfrak{B}(A, B)$ is complete if $B$ is complete; the other verifications are routine and we omit them. Suppose that $B$ is complete and let $(T_n)$ be a Cauchy sequence in $\mathfrak{B}(A, B)$. For $x \in A$ we have $\|T_n(x) - T_m(x)\| \leq \|T_n - T_m\| \cdot \|x\|$, and so $(T_n(x))$ is a Cauchy sequence in $B$. Thus for each $x \in A$, there is a vector $T(x) \in B$ such that $\|T_n(x) - T(x)\| \to 0$. This defines a mapping $T$ from $A$ into $B$. For $x, y \in A$, we have $\|T(x + y) - [T(x) + T(y)]\| \leq \|T(x + y) - T_n(x + y)\| + \|T_n(x) - T(x)\| + \|T_n(y) - T(y)\| \to 0$, and thus $T(x + y) = T(x) + T(y)$. We prove similarly that $T(\alpha x) = \alpha T(x)$ for all $x \in A$ and $\alpha \in F$. Thus $T$ is linear.

Since $(T_n)$ is a Cauchy sequence, there is a positive constant $\beta$ such that $\|T_n\| \leq \beta$ for all $n \in N$. For $\|x\| \leq 1$, we have $\|T(x)\| \leq \|T(x) - T_n(x)\| + \|T_n(x)\| \leq

transformation. Also

$$\sup \{ |\hat{x}(f)| : f \in E^*, \|f\| \leq 1 \} = \sup \{ |f(x)| : f \in E^*, \|f\| \leq 1 \}$$

$$\leq \sup \{ \|f\| \|x\| : f \in E^*, \|f\| \leq 1 \} \leq \|x\|$$

for each $x \in E$. Thus the mapping $x \rightarrow \hat{x}$ is a bounded linear transformation from $E$ into $E^*$ of norm $\leq 1$. Several questions arise. (1) Is this mapping one-to-one? (2) Does it preserve norms? (3) Is it onto $E^*$? (4) Indeed, are there any nonzero elements in $E^*$? In general none of these questions have obvious answers; however we are able to answer (1), (2), and (4) with the aid of the Hahn-Banach theorem, which is next on our program. Question (3) will be answered in the exercises.
