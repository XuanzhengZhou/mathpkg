---
role: proof
locale: en
of_concept: proposition-3-3
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Clearly (a) implies both (b

and closed in $G$; by the connectedness of $G$ it will follow that $A$ must be $G$ and so $f \equiv 0$. To see that $A$ is closed let $z \in A^-$ and let $z_k$ be a sequence in $A$ such that $z = \lim z_k$. Since each $f^{(n)}$ is continuous it follows that $f^{(n)}(z) = \lim f^{(n)}(z_k) = 0$. So $z \in A$ and $A$ is closed.

To see that $A$ is open, let $a \in A$ and let $R > 0$ be such that $B(a; R) \subset G$.

Then $f(z) = \sum a_n(z-a)^n$ for $|z-a| < R$ where $a_n = \frac{1}{n!} f^{(n)}(a) = 0$ for each $n \geq 0$. Hence $f(z) = 0$ for all $z$ in $B(a; R)$ and, consequently, $B(a; R) \subset A$. Thus $A$ is open and this completes the proof of the theorem.
