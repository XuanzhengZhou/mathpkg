---
role: proof
locale: en
of_concept: boundary-of-open-set-empty-interior
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

**1. For open $A$:**
\[
\begin{aligned}
(A^- - A)^0 &= [A^- \cap (X - A)]^{-0} \\
&\subseteq A^{-0} \cap (X - A)^{-0} \\
&= A^{-0} \cap (X - A^{0-}) \\
&\subseteq A^{-0} \cap (X - A^{0-}) \\
&= 0,
\end{aligned}
\]
since $A$ is open.

**2. For closed $A$:**
\[
\begin{aligned}
(A - A^0)^{-0} &= [A \cap (X - A^0)]^{-0} \\
&\subseteq A^0 \cap (X - A^0)^{-0} \\
&= A^0 \cap (X - A^0)^{-0} \\
&= 0,
\end{aligned}
\]
since $A$ is closed.
