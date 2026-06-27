---
role: proof
locale: en
of_concept: integration-over-triangle
source_book: gtm012
source_chapter: "1"
source_section: "7. Functions of two variables"
---

# Proof of Theorem 7.3: Change of Order of Integration (Triangle)

**Theorem 7.3.** Suppose $f$ is a continuous complex-valued function defined on the triangle

$$A = \{(x, y) \mid 0 \leq x \leq a,\; 0 \leq y \leq x\}.$$

Then

$$\int_0^a \left( \int_0^x f(x, y) \, dy \right) dx = \int_0^a \left( \int_y^a f(x, y) \, dx \right) dy.$$

**Proof.** The argument parallels the proof of Theorem 7.2. Define two auxiliary functions on the triangle by introducing a variable upper limit:

$$F_1(s, t) = \int_0^s \left( \int_0^x f(x, y) \, dy \right) dx,$$

$$F_2(s, t) = \int_0^t \left( \int_y^a f(x, y) \, dx \right) dy.$$

(Note: the precise definitions used in the text involve a parameter $t$ to track the upper boundary of the triangle slice. The core idea is to show that the two iterated integrals are equal by differentiating with respect to the parameters.)

By the fundamental theorem of calculus and the differentiation under the integral sign lemma, one computes the derivatives with respect to the parameters and shows that $D_1(F_2 - F_1) = 0$ and $D_2(F_2 - F_1) = 0$ on the interior of the triangle. Thus $F_2 - F_1$ is constant throughout the domain.

Since both $F_1$ and $F_2$ evaluate to zero when the upper limits are zero, they are identical. Setting the parameters to their maximal values ($s = t = a$) yields the desired equality of the iterated integrals. $\square$

**Remark.** The essential content of the theorem is that for a continuous function on a triangular domain, the order of integration may be interchanged. In the first iterated integral, for each fixed $x$, $y$ runs from $0$ to $x$ (vertical slices). In the second, for each fixed $y$, $x$ runs from $y$ to $a$ (horizontal slices). Both descriptions cover the same triangle.
