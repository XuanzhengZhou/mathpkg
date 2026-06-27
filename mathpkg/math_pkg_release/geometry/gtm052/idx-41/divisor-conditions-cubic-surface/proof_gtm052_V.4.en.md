---
role: proof
locale: en
of_concept: divisor-conditions-cubic-surface
source_book: gtm052
source_chapter: "V"
source_section: "4"
---

$(i) \Rightarrow (ii) \Rightarrow (iii) \Rightarrow (iv)$, using the easy direction of Nakai's criterion (1.10).

The reverse direction $(iv) \Rightarrow (i)$ proceeds as follows. Suppose $D$ is a divisor satisfying $D.L > 0$ for every line $L \subseteq X$. Choose six mutually skew lines $E'_1, \ldots, E'_6$ as follows: choose $E'_6$ so that $D.E'_6$ is equal to the minimum value of $D.L$ for any line $L$; choose $E'_5$ so that $D.E'_5$ is equal to the minimum value of $D.L$ among those lines $L$ which do not meet $E'_6$; and choose $E'_4, E'_3$ similarly. There will be just three remaining lines which do not meet $E'_6, E'_5, E'_4, E'_3$, one of them meeting the other two. Choose $E'_1, E'_2$ so that $D.E'_1 \geq D.E'_2$.

By the symmetry of the configuration of the 27 lines (4.10), there is an automorphism of the configuration sending $E_1, \ldots, E_6$ to $E'_1, \ldots, E'_6$, and this automorphism is realized by a linear automorphism of the cubic surface $X$ (acting on Pic $X$). Under this automorphism, the divisor $D$ transforms to a divisor whose intersection numbers with the standard lines $E_1, \ldots, E_6$ satisfy the inequalities corresponding to $b_1 \geq \cdots \geq b_6 > 0$ and $a \geq b_1 + b_2 + b_5$.

Let $D_0, \ldots, D_6$ be the divisors corresponding to the lines through a point, conic through five points, etc., which form a free basis for $\operatorname{Pic} X \cong \mathbf{Z}^7$. One checks that $|D_1|, |D_2|, |D_3|, |D_4|$ have no base points by (4.1), $|D_5|$ has no base points by (4.3), and $D_6$ is very ample by (4.6). Therefore any linear combination of these, $D = \sum c_i D_i$, with $c_i \geq 0$ and $c_6 > 0$, will be very ample.

Writing $D \sim al - \sum b_i e_i$, we have $b_6 = c_6$, $b_5 = c_5 + c_6$, $\ldots$, $b_1 = c_1 + \cdots + c_6$, $a = c_1 + 2(c_2 + c_3 + c_4) + 3(c_5 + c_6)$. The conditions $c_i \geq 0$, $c_6 > 0$ are equivalent to the conditions $b_1 \geq \cdots \geq b_6 > 0$ and $a \geq b_1 + b_2 + b_5$. Thus all divisors satisfying these conditions are very ample, which completes the proof.
