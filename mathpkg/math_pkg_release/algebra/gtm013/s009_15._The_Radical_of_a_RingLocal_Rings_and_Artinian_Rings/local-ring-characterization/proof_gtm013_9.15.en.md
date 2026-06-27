---
role: proof
locale: en
of_concept: local-ring-characterization
source_book: gtm013
source_chapter: "9"
source_section: "15"
---
\textbf{(b) $\Leftrightarrow$ (c).} Immediate from the definition of $J(R)$ as the intersection of all maximal left ideals.

\textbf{(c) $\Rightarrow$ (d).} Assume (c). Then $J(R)$ is the unique maximal left ideal of $R$. Let $x, y \in R$ be non-left-invertible. Then every proper left ideal is contained in a maximal one (10.5), so $Rx, Ry \leq J(R)$, whence $x + y \in J(R)$. Thus $x + y$ is not left invertible.

\textbf{(d) $\Rightarrow$ (e).} Assume (d). Since $J(R)$ is a proper left ideal, it suffices to prove that if $x \in R$ with $Rx \neq R$, then $x \in J(R)$. For each $r \in R$, $rx$ does not have a left inverse and $1 = rx + (1 - rx)$. By (d), $1 - rx$ has a left inverse. Thus by (15.3), $x \in J_4 = J(R)$.

\textbf{(e) $\Rightarrow$ (f).} Assuming (e), every non-zero element of $R/J(R)$ has a left inverse. Hence $R/J(R)$ is a division ring.

\textbf{(f) $\Rightarrow$ (g).} If $R/J(R)$ is a division ring, then $x \notin J(R)$ iff $x + J(R)$ is invertible in $R/J(R)$ iff $x$ is invertible modulo $J(R)$ iff $x$ is invertible in $R$.

\textbf{(g) $\Rightarrow$ (h).} If neither $x$ nor $1-x$ were invertible, then both would lie in $J(R)$ by (g), so $1 = x + (1-x) \in J(R)$, contradicting $J(R) \neq R$.

\textbf{(h) $\Rightarrow$ (a).} If (h) holds and $x, y$ are non-invertible, then $x+y$ cannot be invertible (otherwise $1 = (x+y)z$ would force a contradiction), and the sum of non-invertibles is non-invertible, which is the definition of a local ring.
