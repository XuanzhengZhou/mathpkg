---
role: proof
locale: en
of_concept: triangle-inequality
source_book: gtm023
source_chapter: "7"
source_section: "7.6"
---

Expand the squared norm of the sum:

$$|x + y|^2 = (x + y, x + y) = |x|^2 + 2(x, y) + |y|^2.$$

Applying the Schwarz inequality $(x, y) \leq |x| |y|$ to the cross term:

$$|x + y|^2 \leq |x|^2 + 2|x| |y| + |y|^2 = (|x| + |y|)^2.$$

Taking the square root of both sides (all quantities are nonnegative) yields

$$|x + y| \leq |x| + |y|.$$

The second form follows by replacing $x$ with $x - z$ and $y$ with $z - y$:

$$|x - y| = |(x - z) + (z - y)| \leq |x - z| + |z - y|.$$
