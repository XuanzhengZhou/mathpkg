---
role: proof
locale: en
of_concept: derived-plane-coordinates
source_book: gtm006
source_chapter: "X"
source_section: "4. General Derivation"
---

We coordinatize $\mathcal{A}_1$ so that $[0, 0]'$ is the Baer subplane $\mathcal{B}(1, 0, 0)$ and $[0]'$ is $\mathcal{B}(t, 0, 0)$. Then we label the points of $[0, 0]'$ so that $(\alpha + \beta t, 0)'$ corresponds to $(\alpha, \beta)$, and we put $(0, 1)' = (t, 0)$. (Note that this is all the choice we have in setting up the coordinate system for $\mathcal{A}_1$.)

Since $[1, 0]' = (1, 0) = (0(t-1) + 1, 0(t-1) + 0)$ and $(0, 1)' = (t, 0) = ((t-1) + 1, 0(t-1) + 0)$, the line $[1, 1]'$ is $\mathcal{B}(t-1, 1, 0)$. Thus, by Exercise 10.5, the lines $[1, k]'$ have the form $\mathcal{B}(t-1, b, c)$.

A point $(\alpha + \beta t, 0)'$ is on $\mathcal{B}(t-1, b, c)$ if and only if $(\alpha, \beta)$ lies in $\mathcal{B}(t-1, b, c)$, which yields the defining relations for $T_1$. Properties (1) through (5) then follow by analyzing the incidence relations between the Baer subplanes $\mathcal{B}(x, y, z)$ and the points of $\mathcal{A}_1$. The verification of (5) in particular involves showing that $\eta + \mu t = \lambda(\alpha + \beta t) + \gamma + \delta t$ using the imitative computation described in the text. $\square$
