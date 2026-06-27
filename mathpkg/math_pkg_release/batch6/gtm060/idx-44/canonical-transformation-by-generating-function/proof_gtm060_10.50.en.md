---
role: proof
locale: en
of_concept: canonical-transformation-by-generating-function
source_book: gtm060
source_chapter: "10"
source_section: "50"
---

We first assume the function $h(I)$ is known and invertible, so each curve $M_h$ is determined by $I$. For a fixed $I$, the relation $dS|_{I=\text{const}} = p \, dq$ determines a well-defined differential $1$-form on $M_{h(I)}$. Integrating this $1$-form along the curve yields

$$S(I, q) = \int_{q_0}^{q} p \, dq$$

in a neighborhood of $q_0$. The first condition $p = \partial S/\partial q$ is satisfied by construction. 

To verify the second condition $\varphi = \partial S/\partial I$, consider the behavior of $S(I,q)$ "in the large." After a circuit of the closed curve $M_{h(I)}$, the integral increases by

$$\Delta S(I) = \oint_{M_{h(I)}} p \, dq = \Pi(I),$$

the area enclosed by $M_{h(I)}$. Thus $S$ is multi-valued on $M_{h(I)}$ with period $\Pi(I)$. This causes $\varphi = \partial S/\partial I$ to be defined only up to multiples of $d\Pi(I)/dI$. However, the transformation formulas still produce a well-defined canonical transformation: the derivative $\partial S/\partial q$ is single-valued, and the ambiguity in $\varphi$ is an integral multiple of $2\pi$, consistent with $\varphi$ being an angular variable.
