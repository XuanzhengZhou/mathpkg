---
role: proof
locale: en
of_concept: criterion-for-representing-element-over-qp
source_book: gtm007
source_chapter: "IV"
source_section: "§2. Quadratic forms over Q_p"
---

Let $f_a = f \oplus (-a)Z^2$. The form $f$ represents $a$ if and only if $f_a$ represents $0$ (n° 1.6). The invariants of $f_a$ are:
$$
d(f_a) = -a d, \quad arepsilon(f_a) = (-a, d)\,arepsilon.
$$
Applying Theorem 6 to $f_a$ (which has rank $n+1$) and translating the conditions back to $f$ yields the stated criterion:

egin{itemize}
\item[(i)] $n = 1$: $f_a$ has rank $2$ and represents $0$ iff $d(f_a) = -1$, i.e., $-ad = -1$, so $a = d$.
\item[(ii)] $n = 2$: $f_a$ has rank $3$ and represents $0$ iff $(-1, -d(f_a)) = arepsilon(f_a)$, i.e., $(-1, ad) = (-a, d)arepsilon$. Using Hilbert symbol properties, this simplifies to $(a, -d) = arepsilon$.
\item[(iii)] $n = 3$: $f_a$ has rank $4$ and the criterion from Theorem 6(iii) translates to the stated condition.
\item[(iv)] $n \geq 4$: $f_a$ has rank $\geq 5$, so it always represents $0$ by Theorem 6(iv).
\end{itemize}
