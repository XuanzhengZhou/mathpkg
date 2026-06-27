---
role: proof
locale: en
of_concept: units-form-group
source_book: gtm028
source_chapter: "I"
source_section: "6"
---

\text{If } a \text{ and } b \text{ are units, then by definition there exist } a^{-1}, b^{-1} \text{ such that } a^{-1}a = aa^{-1} = 1 \text{ and } b^{-1}b = bb^{-1} = 1. \text{ We verify:}

\begin{enumerate}
\item a^{-1} \text{ is a unit: Since } (a^{-1})^{-1} = a, \text{ and } a \cdot a^{-1} = a^{-1} \cdot a = 1, \text{ the inverse of } a^{-1} \text{ exists (namely } a\text{).}

\item ab \text{ is a unit: We claim } b^{-1}a^{-1} \text{ is its inverse. Indeed:}
$$(b^{-1}a^{-1})(ab) = b^{-1}(a^{-1}a)b = b^{-1} \cdot 1 \cdot b = b^{-1}b = 1,$$
$$(ab)(b^{-1}a^{-1}) = a(b b^{-1})a^{-1} = a \cdot 1 \cdot a^{-1} = aa^{-1} = 1.$$
\end{enumerate}

\text{The identity element } 1 \text{ is trivially a unit (it is its own inverse), and associativity of multiplication is inherited from the ring. Therefore the set of all units forms a group under multiplication.}
