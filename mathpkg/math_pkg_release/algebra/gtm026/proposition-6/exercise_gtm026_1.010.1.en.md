---
role: exercise
locale: en
chapter: "1"
section: "010"
exercise_number: 1
---

Recall that "characteristic function" establishes a bijection between subsets of $X$ and functions $X \rightarrow 2$, where $2 = \{0, 1\}$ so that, in particular, a collection of subsets of $X$ is a function $2^X \rightarrow 2$. Also recall that an $I$-indexed family of functions $(f_i: X \rightarrow Y)$ corresponds to the single function $f: X \rightarrow Y^I$.

(a) Let $T$ be the double power-set theory of 3.19. Thinking of $XT$ as the set of functions from $2^X$ to 2, show that $\eta$ sends $x$ to the $x$th projection $pr_x: 2^X \rightarrow 2$ and that the characteristic function of $x(\alpha \circ \beta)$ is given by

$$2^Z \xrightarrow{(\chi_{\beta}: y \in Y)} 2^Y \xrightarrow{\chi_{xa}} 2$$

(b) (Kock-Lawvere) Let $S$ be any algebraic theory in Set and let $(2, \xi)$ be an $S$-algebra structure on 2. Define $XS_\xi$ to be the set of $S$-homomorphisms from the (cartesian power) algebra $(2, \xi)^X$ to $(2, \xi)$. Show that $S$ is a subtheory of the double power-set theory as in (a). See also exercise 11 of 2.3.
