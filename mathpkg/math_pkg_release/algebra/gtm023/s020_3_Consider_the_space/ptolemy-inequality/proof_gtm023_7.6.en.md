---
role: proof
locale: en
of_concept: ptolemy-inequality
source_book: gtm023
source_chapter: "7"
source_section: "7.6"
---

The inequality is trivial if one of the three vectors is zero, so assume $x \neq 0$, $y \neq 0$, and $z \neq 0$. Define the vectors

$$x' = \frac{x}{|x|^2}, \quad y' = \frac{y}{|y|^2}, \quad z' = \frac{z}{|z|^2}.$$

Compute the squared distance between $x'$ and $y'$:

$$|x' - y'|^2 = \left|\frac{x}{|x|^2} - \frac{y}{|y|^2}\right|^2 = \frac{1}{|x|^2} - \frac{2(x, y)}{|x|^2 |y|^2} + \frac{1}{|y|^2} = \frac{|x - y|^2}{|x|^2 |y|^2}.$$

Taking square roots, $|x' - y'| = |x - y| / (|x| |y|)$. Applying the triangle inequality in the form $|x' - y'| \leq |x' - z'| + |z' - y'|$ to the vectors $x', y', z'$ we obtain

$$\frac{|x - y|}{|x| |y|} \leq \frac{|y - z|}{|y| |z|} + \frac{|z - x|}{|z| |x|}.$$

Multiplying both sides by $|x| |y| |z|$ yields the Ptolemy inequality

$$|x - y| |z| \leq |y - z| |x| + |z - x| |y|.$$
