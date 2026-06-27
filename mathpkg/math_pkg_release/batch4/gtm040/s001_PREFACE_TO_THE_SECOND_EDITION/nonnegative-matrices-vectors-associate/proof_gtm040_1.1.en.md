---
role: proof
locale: en
of_concept: nonnegative-matrices-vectors-associate
source_book: gtm040
source_chapter: "1"
source_section: "1"
---

Consider $f^+$ and $f^-$ separately and apply Proposition 1-4. Since $f = f^+ - f^-$ and both $f^+ \geq 0$ and $f^- \geq 0$, Proposition 1-4 gives $A(Bf^+) = (AB)f^+$ and $A(Bf^-) = (AB)f^-$. By distributivity (Proposition 1-2),

$$A(Bf) = A(B(f^+ - f^-)) = A(Bf^+ - Bf^-) = A(Bf^+) - A(Bf^-) = (AB)f^+ - (AB)f^- = (AB)(f^+ - f^-) = (AB)f.$$

For the second assertion, set $A = C$ and $B = C^{\,n-1}$ and apply the first part.
