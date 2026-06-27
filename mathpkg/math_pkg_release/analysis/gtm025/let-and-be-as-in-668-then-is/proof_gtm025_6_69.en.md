---
role: proof
locale: en
of_concept: "let-and-be-as-in-668-then-is"
source_book: gtm025
source_chapter: "Topology"
source_section: "6.69"
---

Suppose that $f$ is continuous on $X$ and let $V$ be open in $Y$. We must show that $f^{-1}(V)$ is open in $X$. For $x \in f^{-1}(V)$, we know that $f$ is continuous at $x$, so there exists a neighborhood $U_x$ of $x$ such that $f(U_x) \subset V$, i.e., $U_x \subset f^{-1}(V)$. It follows that $f^{-1}(V) = \bigcup \{U_x : x \in f^{-1}(V)\}$ which is a union of open sets, so that $f^{-1}(V)$ is open.

Conversely, suppose that $f^{-1}(V)$ is open in $X$ whenever $V$ is open in $Y$. Let $x \

Conversely, suppose that $f$ is continuous at $x$ and let $(x_n)$ be any sequence in $X$ such that $x_n \to x$. Let $V$ be any neighborhood of $f(x)$. Then there is a neighborhood $U$ of $x$ such that $f(U) \subset V$. Since $x_n \to x$, there exists $n_0 \in N$ such that $n \geq n_0$ implies $x_n \in U$. Then $n \geq n_0$ implies $f(x_n) \in f(U) \subset V$. Thus $f(x_n) \to f(x)$. $\square$
