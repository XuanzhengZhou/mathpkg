---
role: proof
locale: en
of_concept: anticommutator-in-q1
source_book: gtm023
source_chapter: "11"
source_section: "4"
---

From $\varphi^2 = -(\varphi, \varphi) \iota$ (proved above), we polarize. Replace $\varphi$ by $\varphi + \psi$:
$$
(\varphi + \psi)^2 = -(\varphi + \psi, \varphi + \psi) \iota.
$$
Expanding both sides:
$$
\varphi^2 + \varphi \circ \psi + \psi \circ \varphi + \psi^2 = -\big((\varphi, \varphi) + 2(\varphi, \psi) + (\psi, \psi)\big) \iota.
$$
Using $\varphi^2 = -(\varphi, \varphi) \iota$ and $\psi^2 = -(\psi, \psi) \iota$, these terms cancel, leaving
$$
\varphi \circ \psi + \psi \circ \varphi = -2(\varphi, \psi) \iota,
$$
which is the desired formula.
