---
role: proof
locale: en
of_concept: schwarz-equality-linear-dependence
source_book: gtm049
source_chapter: "6"
source_section: "1"
---

Set $u = b - c$ and $v = a - b$. Compute:
$$\|u + v\|^2 = \|u\|^2 + \|v\|^2 + 2\sigma(u, v).$$
The hypothesis $\|u + v\|^2 = (\|u\| + \|v\|)^2$ gives
$$\|u\|^2 + \|v\|^2 + 2\sigma(u, v) = \|u\|^2 + \|v\|^2 + 2\|u\| \|v\|.$$
Cancelling, we obtain $\sigma(u, v) = \|u\| \|v\|$. By Schwarz's Inequality (Lemma 1 of §6.1), $|\sigma(u, v)| \leq \|u\| \|v\|$ with equality if and only if $u$ and $v$ are linearly dependent. Since $\sigma(u, v) = \|u\| \|v\| > 0$ (assuming $u, v \neq 0$), we have equality in Schwarz's Inequality, hence $u$ and $v$ are linearly dependent. Therefore $a = b + v$ and $c = b - u$ are both expressible in terms of $b$ and the common direction of $u$ and $v$, so $a, b, c$ are collinear (linearly dependent).
