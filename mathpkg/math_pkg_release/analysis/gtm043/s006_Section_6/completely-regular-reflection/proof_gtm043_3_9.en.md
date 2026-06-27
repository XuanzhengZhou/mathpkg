---
role: proof
locale: en
of_concept: completely-regular-reflection
source_book: gtm043
source_chapter: "3"
source_section: "3.9"
---

Define $x \equiv x'$ in $X$ to mean that $f(x) = f(x')$ for every $f \in C(X)$. Evidently, this is an equivalence relation. Let $Y$ be the set of all equivalence classes. We define a mapping $\tau$ of $X$ onto $Y$ as follows: $\tau x$ is the equivalence class that contains $x$.

With each $f \in C(X)$, associate a function $g \in \mathbf{R}^Y$ as follows: $g(y)$ is the common value of $f(x)$ at every point $x \in y$. Thus, $f = g \circ \tau$. Let $C'$ denote the family of all such functions $g$, i.e., $g \in C'$ if and only if $g \circ \tau \in C(X)$. Now endow $Y$ with the weak topology induced by $C'$. By definition, every function in $C'$ is continuous on $Y$, i.e., $C' \subset C(Y)$. The continuity of $\tau$ now follows from Theorem 3.8.

It is evident that if $y$ and $y'$ are distinct points of $Y$, then there exists $g \in C'$ such that $g(y) \neq g(y')$. This proves that $Y$ is a Hausdorff space. Hence $Y$ is completely regular, by Theorem 3.7.

Finally, consider any function $h \in C(Y)$. Since $\tau$ is continuous, $h \circ \tau$ is continuous on $X$. But this says that $h \in C'$. Therefore, $C' \supset C(Y)$. Thus, $C' = C(Y)$; and it is clear that the mapping $g \mapsto g \circ \tau$ is an isomorphism. This completes the proof.
