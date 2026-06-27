---
role: proof
locale: en
of_concept: covering-path-uniqueness
source_book: gtm057
source_chapter: "II"
source_section: "5"
---
Uniqueness: If $\bar{h}$ and $\bar{h}'$ both satisfy the conditions, let $E_0 = \{(s,t) \in E : \bar{h}(s,t) = \bar{h}'(s,t)\}$. Then $E_0$ is closed (since $\mathbb{R}$ is Hausdorff), nonvoid (contains $(0,0)$), and open (by local homeomorphism property of $\phi$). Since $E$ is connected, $E_0 = E$.

Existence: Construct $\bar{h}$ by partitioning $E$ into small rectangles $E_{ij}$ and extending piece by piece using the local inverses $\psi_n$. The construction proceeds from $E_{11}$ outward, using the property that $\psi_n$ and $\psi_m$ agree on overlaps when $|n-m| < 2$.
