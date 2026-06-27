---
role: proof
locale: en
of_concept: minimum-polynomial-of-dual-transformation
source_book: gtm023
source_chapter: "13"
source_section: "13.8"
---
From sec. 2.25, for any polynomial $f(t) = \sum a_k t^k$, we have
$$f(\varphi^*) = \sum a_k (\varphi^*)^k = \sum a_k (\varphi^k)^* = \left(\sum a_k \varphi^k\right)^* = [f(\varphi)]^*.$$
Now $f(\varphi^*) = 0$ if and only if $[f(\varphi)]^* = 0$, which (since the dual of a transformation is zero iff the transformation is zero) is equivalent to $f(\varphi) = 0$. Thus $\varphi$ and $\varphi^*$ are annihilated by exactly the same polynomials. Therefore their minimum polynomials, being the monic polynomials of least degree that annihilate each transformation, must coincide.
