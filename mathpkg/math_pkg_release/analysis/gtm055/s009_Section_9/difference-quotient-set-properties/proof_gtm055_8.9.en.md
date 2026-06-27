---
role: proof
locale: en
of_concept: difference-quotient-set-properties
source_book: gtm055
source_chapter: "8"
source_section: "9"
---

It suffices to treat the case where $U$ is a single open interval $(a, b)$. Let $g(t) = f(t) - mt$, $a \leq t \leq b$. The difference quotient of $g$ across any subinterval is less than that of $f$ by exactly $m$, so $R_m(f; (a,b)) = R_0(g; (a,b))$ and $L_m(f; (a,b)) = L_0(g; (a,b))$. Thus it suffices to prove the proposition for $m = 0$. The left-hand version follows from the right-hand version by applying it to $\tilde{f}(t) = f(-t)$ on $[-b, -a]$. Hence the proof reduces to Lemma 8.10 (Riesz).
