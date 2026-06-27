---
role: proof
locale: en
of_concept: irreducible-divisibility-lemma
source_book: gtm023
source_chapter: "XII"
source_section: "2"
---

The "if" direction is trivial: if $h^p \mid f$ and $h^{m-p} \mid g$, then $h^m = h^p \cdot h^{m-p} \mid fg$.

For the "only if" direction, suppose $h^m \mid fg$. Let $p$ be the largest integer such that $h^p \mid f$ (so $f = h^p f_1$ with $h \nmid f_1$). Then $h^m \mid h^p f_1 g$, so $h^{m-p} \mid f_1 g$. Since $h$ is irreducible and $h \nmid f_1$, $h$ and $f_1$ are relatively prime. By the corollary to Proposition II, there exist $u, v$ such that $uh + v f_1 = 1$. Set $g_1 = ug + v h^{m-p-1} k$ (where $f_1 g = h^{m-p}k$). Then $h g_1 = hug + v h^{m-p} k = hug + f_1 v g = (hu + f_1 v)g = g$. So $h \mid g$. Repeating this argument $m-p$ times shows $h^{m-p} \mid g$.
