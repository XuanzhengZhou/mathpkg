---
role: proof
locale: en
of_concept: cross-ratio-formula
source_book: gtm049
source_chapter: "VI"
source_section: "6.2"
---
Given $$B_i = [y_i a_0 + z_i a_1]$$ ($$i = 0, 1, 2, 3$$), we need to express $$B_3$$ in terms of a basis where $$B_0, B_1$$ correspond to basis vectors and $$B_2$$ to their sum.

Choose new basis vectors $$b_0 = y_0 a_0 + z_0 a_1$$ and $$b_1 = y_1 a_0 + z_1 a_1$$ (which are linearly independent since $$B_0 \neq B_1$$). Then solve for $$a_0, a_1$$ in terms of $$b_0, b_1$$ using the inverse transformation. Calculate $$B_2$$ as a combination of $$b_0, b_1$$ to find the scaling factor needed to make it $$b_0 + b_1$$; then express $$B_3$$ accordingly to obtain the cross-ratio.

The computation yields the determinant formula:
$$\operatorname{cr}(B_0, B_1; B_2, B_3) = \frac{(y_0 z_2 - y_2 z_0)(y_1 z_3 - y_3 z_1)}{(y_0 z_3 - y_3 z_0)(y_1 z_2 - y_2 z_1)}.$$
