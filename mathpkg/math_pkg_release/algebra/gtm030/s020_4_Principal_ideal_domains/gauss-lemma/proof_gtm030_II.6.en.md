---
role: proof
locale: en
of_concept: gauss-lemma
source_book: gtm030
source_chapter: "II"
source_section: "6"
---

Let $f(x) = a_0 + a_1x + \cdots + a_nx^n$ and $g(x) = b_0 + b_1x + \cdots + b_mx^m$ be primitive, and suppose $f(x)g(x) = c_0 + c_1x + \cdots + c_{n+m}x^{n+m}$ is not primitive. Then there exists an irreducible element $p \in \mathfrak{A}$ dividing all $c_i$.

Since $f$ is primitive, $p$ does not divide all $a_i$. Let $a_{n'}$ be the last coefficient not divisible by $p$. Similarly, let $b_{m'}$ be the last coefficient of $g$ not divisible by $p$. Consider

$$c_{n'+m'} = a_0b_{n'+m'} + \cdots + a_{n'-1}b_{m'+1} + a_{n'}b_{m'} + a_{n'+1}b_{m'-1} + \cdots + a_{n'+m'}b_0.$$

All terms before $a_{n'}b_{m'}$ have $b_j$ with $j > m'$ (so are divisible by $p$), and all terms after have $a_i$ with $i > n'$ (so are divisible by $p$). Since $p \mid c_{n'+m'}$, we must have $p \mid a_{n'}b_{m'}$. But $p$ is irreducible (hence prime in a Gaussian domain) and $p \nmid a_{n'}$, $p \nmid b_{m'}$, contradiction.
