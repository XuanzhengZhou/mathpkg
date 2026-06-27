---
role: proof
locale: en
of_concept: continuity-theorem
source_book: gtm038
source_chapter: "II. Domains of Holomorphy"
source_section: "1. The Continuity Theorem"
---

Let $f_1 := f|_{\tilde{H}}$. Then $f_1$ is holomorphic in $\tilde{H}$. By the hypothesis on $\tilde{H}$ and $\tilde{P}$, there exists exactly one holomorphic function $f_2$ in $\tilde{P}$ with $f_2|_{\tilde{H}} = f_1$.

Define
$$F(z) := \begin{cases} f(z) & \text{for } z \in B, \\ f_2(z) & \text{for } z \in \tilde{P}. \end{cases}$$

Since $B \cap \tilde{P}$ is a domain (connected) and $f|_{\tilde{H}} = f_2|_{\tilde{H}}$, it follows from the identity theorem for holomorphic functions that $F$ is a well-defined holomorphic function on $B \cup \tilde{P}$. Clearly $F|_{B} = f$.

The uniqueness of the continuation is a further consequence of the identity theorem: if $F_1$ and $F_2$ are two holomorphic extensions of $f$ to $B \cup \tilde{P}$, then $F_1 = F_2$ on $B$, and by the identity theorem on the domain $B \cup \tilde{P}$, they coincide everywhere.
