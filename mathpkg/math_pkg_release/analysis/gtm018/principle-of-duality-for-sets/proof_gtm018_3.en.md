---
role: proof
locale: en
of_concept: principle-of-duality-for-sets
source_book: gtm018
source_chapter: "I"
source_section: "3"
---

The principle follows from the De Morgan identities and the elementary complement formulas. Let an identity be expressed using the operations of union ($\bigcup$), intersection ($\bigcap$), complementation ($'$), the inclusion relation ($\subset$, $\supset$), the empty set ($0$), and the whole space ($X$).

Take the complement of both sides of the identity. By De Morgan's laws:

$$\left(\bigcup E_i\right)' = \bigcap E_i', \quad \left(\bigcap E_i\right)' = \bigcup E_i'.$$

Using the elementary complement identities:

$$0' = X, \quad X' = 0, \quad (E')' = E,$$

and the fact that if $E \subset F$ then $F' \subset E'$ (so $\subset$ and $\supset$ are interchanged), every $\bigcap$ becomes $\bigcup$, every $\bigcup$ becomes $\bigcap$, $\subset$ becomes $\supset$, $0$ becomes $X$, and $X$ becomes $0$, while equality ($=$) and complementation ($'$) are left unchanged. If the original identity holds, its complemented version also holds. Since $(E')' = E$, applying complementation twice recovers the original identity with the symbols interchanged. Hence the dual identity is valid.
