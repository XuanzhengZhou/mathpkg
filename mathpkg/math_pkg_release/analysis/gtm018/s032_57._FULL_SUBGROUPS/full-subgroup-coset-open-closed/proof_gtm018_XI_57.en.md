---
role: proof
locale: en
of_concept: full-subgroup-coset-open-closed
source_book: gtm018
source_chapter: "XI"
source_section: "57"
---

Since the complement of any union of left cosets is itself a union of left cosets, and since a set whose complement is open is closed, it is sufficient to prove that every union of left cosets of $Z$ is open. Since a union of open sets is open, it is sufficient to prove that each left coset of $Z$ is open. By translation invariance of the topology, this reduces to proving that $Z$ itself is open.

Let $Z^0$ denote the interior of $Z$. Since $Z$ is full, $Z^0 \neq \varnothing$, so there exists an element $z_0 \in Z^0$. If $z$ is any element of $Z$, then $z z_0^{-1} \in Z$ (since $Z$ is a subgroup) and therefore

$$z z_0^{-1} Z = Z.$$

Multiplying by $Z^0$, we obtain $z z_0^{-1} Z^0 = Z^0$, which implies

$$z = (z z_0^{-1}) z_0 \in Z^0.$$

Since $z$ was an arbitrary element of $Z$, we have proved $Z \subset Z^0$, i.e., $Z$ is open. Every left coset $xZ$ is then open as the translate of the open set $Z$, and the result follows.
