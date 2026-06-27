---
role: proof
locale: en
of_concept: factor-group
source_book: gtm023
source_chapter: "0"
source_section: "0.4"
---
Let $x', y'$ be two other elements satisfying $\pi x' = \bar{x}$ and $\pi y' = \bar{y}$. Then $x' - x \in H$ and $y' - y \in H$. It follows that
$$(x' + y') - (x + y) = (x' - x) + (y' - y) \in H,$$
so $\pi(x' + y') = \pi(x + y)$. Hence $\bar{x} + \bar{y} = \pi(x + y)$ is well-defined. The group axioms are verified by lifting them from $G$:
\begin{itemize}
  \item Associativity follows from associativity in $G$.
  \item The coset $H$ (the class of $0$) serves as the identity.
  \item The inverse of $\bar{x}$ is $\overline{-x}$.
\end{itemize}
The unit element is $H$ because $0 \in H$ and $\pi(0) = H$.
