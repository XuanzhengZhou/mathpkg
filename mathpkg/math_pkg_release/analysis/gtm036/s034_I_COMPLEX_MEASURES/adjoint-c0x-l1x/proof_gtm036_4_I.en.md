---
role: proof
locale: en
of_concept: adjoint-c0x-l1x
source_book: gtm036
source_chapter: "4"
source_section: "I (Complex Measures)"
---
For a discrete space $X$, every subset is open and therefore Borel. A regular Borel measure $\mu$ on $X$ is uniquely determined by its values on singletons: let $g(x) = \mu(\{x\})$ for each $x \in X$. Since $\mu$ is countably additive, for any $A \subset X$ we have $\mu(A) = \sum_{x \in A} g(x)$.

By the Riesz representation theorem, every $\phi \in (c_0(X))^*$ corresponds to a finite regular Borel measure $\mu$ with $\phi(f) = \int_X f d\mu$ for all $f \in c_0(X)$. With $\mu$ represented by $g$, the integral becomes the sum $\phi(f) = \sum_{x \in X} f(x) g(x)$. The total variation is $\|\mu\| = \sum_{x \in X} |g(x)|$, giving the isometric isomorphism $(c_0(X))^* \cong l^1(X)$.

For $c(Y)$ where $Y = X \cup \{\infty\}$ is the one-point compactification, functions in $c(Y)$ correspond to sequences $x = \{x_n\}$ converging to $x_\infty$. The dual of $c$ (when $X = \mathbb{N}$) consists of functionals of the form $\{x_n\} \mapsto \sum x_n y_n + (\lim x_n) y_0$ with $\{y_n\}_{n=0}^\infty \in l^1$.
