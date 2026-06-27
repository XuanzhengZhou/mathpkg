---
role: proof
locale: en
of_concept: linear-map-circled-radial
source_book: gtm003
source_chapter: ""
source_section: "3"
---

**Circled sets.** Let $C \subset L_1$ be circled and $|\lambda| \leq 1$. For any $y \in f(C)$, there exists $x \in C$ such that $y = f(x)$. Since $C$ is circled, $\lambda x \in C$, hence $\lambda y = \lambda f(x) = f(\lambda x) \in f(C)$. Thus $\lambda f(C) \subset f(C)$, proving $f(C)$ is circled.

For the preimage: let $D \subset L_2$ be circled and $x \in f^{-1}(D)$, i.e., $f(x) \in D$. For $|\lambda| \leq 1$, since $D$ is circled, $\lambda f(x) \in D$. By linearity, $f(\lambda x) = \lambda f(x) \in D$, so $\lambda x \in f^{-1}(D)$. Thus $\lambda f^{-1}(D) \subset f^{-1}(D)$, proving $f^{-1}(D)$ is circled.

**Radial sets.** Let $B \subset L_2$ be radial. For any finite subset $\{x_1, \ldots, x_n\} \subset L_1$, the set $\{f(x_1), \ldots, f(x_n)\}$ is a finite subset of $L_2$. Since $B$ is radial, there exists $\lambda_0 \in K$ such that $\{f(x_1), \ldots, f(x_n)\} \subset \lambda B$ whenever $|\lambda| \geq |\lambda_0|$. Then $\{x_1, \ldots, x_n\} \subset \lambda f^{-1}(B)$ under the same condition, proving $f^{-1}(B)$ is radial.

Now let $A \subset L_1$ be radial and $f$ surjective. Let $\{y_1, \ldots, y_n\} \subset L_2$ be any finite subset. By surjectivity, choose $x_i \in L_1$ with $f(x_i) = y_i$ for each $i$. Since $A$ is radial, there exists $\lambda_0 \in K$ such that $\{x_1, \ldots, x_n\} \subset \lambda A$ whenever $|\lambda| \geq |\lambda_0|$. Applying $f$, we obtain $\{y_1, \ldots, y_n\} = f(\{x_1, \ldots, x_n\}) \subset f(\lambda A) = \lambda f(A)$. Thus $f(A)$ is radial.
