---
role: proof
locale: en
of_concept: divisibility-by-integer-in-cyclotomic-integers
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

If $h(\alpha) = a_0 g(\alpha)$, let $g(\alpha) = c_0 + c_1\alpha + \cdots + c_{\lambda-1}\alpha^{\lambda-1}$. Then $b_i = a_0 c_i$ for all $i$, so all $b_i$ are multiples of $a_0$, hence $b_i \equiv b_j \equiv 0 \pmod{a_0}$ in the chosen representation. However, the condition must hold in every representation. If $h(\alpha)$ is represented differently, say as $h(\alpha) = b_0' + b_1'\alpha + \cdots$, then $h(\alpha) - h(\alpha) = 0$ implies $(b_0 - b_0') + (b_1 - b_1')\alpha + \cdots = 0$, which means the difference is an integer multiple of $1 + \alpha + \cdots + \alpha^{\lambda-1}$. Thus $(b_i - b_i') \equiv (b_j - b_j') \pmod{a_0}$ for all $i,j$, so the congruence condition $b_i' \equiv b_j' \pmod{a_0}$ holds in every representation.

Conversely, suppose $b_i \equiv b_j \pmod{a_0}$ for all $i, j$. Let $r$ be the common residue, so $b_i = a_0 c_i + r$ for all $i$. Then
$$h(\alpha) = a_0(c_0 + c_1\alpha + \cdots + c_{\lambda-1}\alpha^{\lambda-1}) + r(1 + \alpha + \cdots + \alpha^{\lambda-1}).$$
Since $1 + \alpha + \cdots + \alpha^{\lambda-1} = 0$, the second term vanishes, giving $h(\alpha) = a_0 g(\alpha)$ with $g(\alpha) = c_0 + c_1\alpha + \cdots + c_{\lambda-1}\alpha^{\lambda-1}$.
