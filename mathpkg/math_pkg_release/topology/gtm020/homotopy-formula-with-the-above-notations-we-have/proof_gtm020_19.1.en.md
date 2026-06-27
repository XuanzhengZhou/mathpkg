---
locale: en
of_concept: homotopy-formula-with-the-above-notations-we-have
role: proof
source_book: gtm020
source_chapter: 19. Characteristic Classes and Connections
source_section: '1'
---

Since $d_x$ and $\int dt$ commute, it follows that the sign in the definition of $Q$ gives $Qd_x + d_xQ = 0$. Now we consider $d_tQ + Qd_t$ on each summand of $\omega = \alpha + \beta dt$. Firstly, $(d_tQ + Qd_t)(\beta dt) = 0 = j_1(\beta dt) - j_0(\beta dt)$. Now we decompose $\alpha = \sum_I a_I(x,t)dx_I$ with $I = \{i(1) < \cdots < i(q)\}$ and $dx_I = dx_{i(1)} \wedge \cdots \wedge dx_{i(q)}$. Using the fundamental theorem of calculus, we calculate the following expression

$$(d_tQ + Qd_t)(\alpha) = Qd_t(\alpha)$$

$$= Q \left( \sum_I \frac{\partial}{\partial t} a_I(x,t) dt dx_I \right)$$

$$= \sum_I \int_0^1 \left\{ \frac{\partial}{\partial t} \{a_I(x,t)\} dx_I \right\} dt$$

$$= \sum_I a_I(x,1) dx_I - \sum_I a_I(x,0) dx_I$$

$$= j_1(\alpha) - j_0(\alpha).$$

Adding up the various results, we obtain the homotopy formula

$$dQ(\omega) + Qd(\omega) = j_1(\omega) - j_0(\omega).$$

This proves the proposition.
