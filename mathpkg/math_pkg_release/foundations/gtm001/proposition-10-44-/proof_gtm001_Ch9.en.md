---
role: proof
locale: en
of_concept: proposition-10-44-
source_book: gtm001
source_chapter: "9"
source_section: ""
---

We define a function $h$ on $2^a$ in the following way

$$h'f = \{x \in a | f'x = 1\}, \quad f \in 2^a.$$

Then $h \colon 2^a \to \mathcal{P}(a)$. We wish to prove that $h$ is one-to-one and onto.

If $b \in \mathcal{P}(a)$ and if $f$ is defined on $a$ by

$$f'x = 1, \quad x \in b$$

$$= 0, \quad x \in a - b.$$

Then $f \in 2^a$ and $h'f = b$. Thus $h$ is onto.

Suppose that $f \in 2^a$, $g \in 2^a$, and $h'f = h'g$, then

$$\{x \in a | f'x = 1\} = \{x \in a | g'x =

then $\tilde{f}_y \in a^b$. Therefore if

$$f' y = \tilde{f}_y, \quad y \in c,$$

then $f \in (a^b)^c$ and $g' \langle x, y \rangle = (f' y)' x$. Consequently $F' f = g$ and $F$ is onto.

If $f_1 \in (a^b)^c, f_2 \in (a^b)^c$, and $F' f_1 = F' f_2$, then

$(\forall y \in c)(\forall x \in b)[(f'_1 y)' x = (f'_2 y)' x]$

$(\forall y \in c)[f'_1 y = f'_2 y]$

$f_1 = f_2$.

Therefore $F$ is one-to-one.

Since $F$ maps $(a^b)^c$ one-to-one onto $a^{b \times c}$ it follows that $(a^b)^c \simeq a^{b \times c}$. $\square$

Remark. Proposition 10.45 tells us that powers of cardinals obey a law of finite cardinals that we have known since we first studied powers of integers:

$$\overline{(\aleph_\alpha^{\aleph_\beta})^{\aleph_y}} = \overline{\aleph_\alpha^{\aleph_\beta \times \aleph_y}}.$$

From our studies of integers we know that, at least in principle, we can compute any finite power of any finite cardinal. But alas we cannot compute even such a simple infinite power as

(1) $$\overline{2^{\aleph_0}}.$$

Indeed Cohen has shown that the question of what (1) is, is undecidable in ZF.

In the next section we will introduce the Generalized Continuum Hypothesis from which we will show how to compute powers of cardinals. But before we do that we wish to prove two more results on the cardinality of unions. For their proof we need the following result.
