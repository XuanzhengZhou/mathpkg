---
role: proof
locale: en
of_concept: cauchys-theorem
source_book: gtm016
source_chapter: "0.3"
source_section: "0.3.1"
---

By induction on $|G|$. If $|G| = 1$, trivial. For $|G| > 1$, use the class equation $|G| = |C(G)| + \sum |G:G_{x_i}|$. If any centralizer $G_{x_i}$ has order divisible by $p$, it contains an element of order $p$ by induction. Otherwise $p$ divides each index $|G:G_{x_i}|$, and from the class equation $p$ divides $|C(G)|$. Since $C(G)$ is Abelian, it has an element of order $p$ by the structure of finite Abelian groups.
