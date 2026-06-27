---
role: proof
locale: en
of_concept: liouvilles-theorem
source_book: gtm051
source_chapter: "5"
source_section: "5.7"
---

Outline of the proof: For an appropriate choice of a constant $c$, define new coordinates

$$u' := \int A_1 \sqrt{A - c} \, du + \int B_1 \sqrt{c - B} \, dv,$$

$$v' := \int \frac{A_1}{\sqrt{A - c}} \, du - \int \frac{B_1}{\sqrt{c - B}} \, dv.$$

In this new coordinate system $(u', v')$, the line element takes the form

$$ds^2 = du'^2 + (A - c)(c - B) \, dv'^2.$$

In these coordinates, the $v'$-parameter curves (with $u'$ held constant) are geodesics parametrized by arc length. The condition $\Phi(\dot{c}(t)) = \text{constant}$ characterizes precisely those curves that can be reparametrized to become $v'$-coordinate curves.
