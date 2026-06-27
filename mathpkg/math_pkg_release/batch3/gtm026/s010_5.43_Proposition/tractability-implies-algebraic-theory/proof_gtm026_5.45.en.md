---
role: proof
locale: en
of_concept: tractability-implies-algebraic-theory
source_book: gtm026
source_chapter: "5"
source_section: "5.45"
---

The text provides informal comments in lieu of a full proof. The construction proceeds by defining, for each small set $A$, a (possibly large) set $A\Omega$ inductively:

$$a \in A\Omega \text{ for all } a \in A$$

and whenever $\omega \in \Omega_n$ and $(p_i : i \in n)$ is an $n$-tuple in $A\Omega$, the formal composite $(\omega, (p_i))$ also lies in $A\Omega$. The tractability hypothesis ensures that this inductive construction yields a small set rather than a proper class. The algebraic theory $T$ is then obtained by quotienting this free construction by the equations $E$, using the techniques developed in 5.34-5.42.
