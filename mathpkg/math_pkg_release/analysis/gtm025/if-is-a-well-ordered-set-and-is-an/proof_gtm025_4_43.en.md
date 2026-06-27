---
role: proof
locale: en
of_concept: "if-is-a-well-ordered-set-and-is-an"
source_book: gtm025
source_chapter: "Unknown Chapter"
source_section: "4.43"
---

Assume that there is an $x$ in $A$ such that $f(x) < x$ and let $a$ be the smallest such $x$. Then $f(a) < a$ so $f(f(a)) < f(a)$

initial segment of $B$ or $B$ itself [we may obviously suppose that $A \neq \varnothing \neq B$]. If $a$ is the least element of $A$ and $b$ is the least element of $B$, then $\{(a, b)\} \in \mathfrak{F}$, and so $\mathfrak{F} \neq \varnothing$. By the Hausdorff Maximality Principle, there is a maximal chain $\mathfrak{C} \subset \mathfrak{F}$. [Actually $\mathfrak{C} = \mathfrak{F}$, but we do not need this fact.] Let $h = \cup \mathfrak{C}$. It is easy to check that $h$ belongs to $\mathfrak{F}$. If $dom h$ and $rng h$ are initial segments $A_x$ and $B_y$ of $A$ and $B$, respectively, then $h \cup \{(x, y)\}$ can be adjoined to $\mathfrak{C}$, and this violates the maximality of $\mathfrak{C}$. Thus we have either $dom h = A$ or $rng h = B$. If $dom h = A$, then either $rng h = B$ [i.e., $\alpha = \beta$], or $rng h$ is an initial segment of $B$ [i.e., $\alpha < \beta$]. If $dom h \neq A$, then $dom h$ is an initial segment of $A$ and $rng h = B$, and so the existence of $h^{-1}$ shows in this case that $\beta < \alpha$.
