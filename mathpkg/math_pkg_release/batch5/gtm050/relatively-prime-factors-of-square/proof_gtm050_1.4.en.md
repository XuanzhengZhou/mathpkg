---
role: proof
locale: en
of_concept: relatively-prime-factors-of-square
source_book: gtm050
source_chapter: "1"
source_section: "1.4"
---

The proof uses the method of infinite descent. Assume there exist relatively prime positive integers $v, w$ such that:
(1) $vw$ is a square,
(2) $v$ is not a square,
(3) $w$ is not a square.

Let $v$ be the smallest positive integer for which such a $w$ exists. Since $vw$ is a square, say $vw = m^2$, and $v, w$ are relatively prime, any prime $P$ dividing $v$ must divide $m^2$ but not $w$. Write $v = Pk$ where $P$ does not divide $k$ (since $P^2$ divides $vw = m^2$, $P^2$ must divide $v$). Then $v = P^2 v'$ for some integer $v'$.

From $v'w = (m/P)^2$, we see $v'w$ is a square, $v'$ and $w$ are relatively prime, and $v' < v$. Moreover, $v'$ cannot be a square (otherwise $v = P^2 v'$ would be a square). Thus $v', w$ satisfy the same three properties but with $v' < v$, contradicting the minimality of $v$. Therefore no such $v, w$ exist.
