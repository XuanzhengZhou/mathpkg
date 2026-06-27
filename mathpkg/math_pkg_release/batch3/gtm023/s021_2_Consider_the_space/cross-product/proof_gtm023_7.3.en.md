---
role: proof
locale: en
of_concept: cross-product
source_book: gtm023
source_chapter: "7"
source_section: "3. Normed determinant functions"
---

**Existence and uniqueness.** Since \(\Delta\) is a determinant function on the 3-dimensional space, for fixed \(x, y\), the map \(z \mapsto \Delta(x, y, z)\) is a linear functional on \(E\). By the Riesz representation theorem (valid in any finite-dimensional inner product space), there exists a unique vector \(u\) such that \((u, z) = \Delta(x, y, z)\) for all \(z\). This vector is defined to be \(x \times y\).

**Orthogonality.** Setting \(z = x\) gives \((x \times y, x) = \Delta(x, y, x) = 0\) by the skew-symmetry of \(\Delta\). Similarly \((x \times y, y) = \Delta(x, y, y) = 0\).

**Skew-symmetry.** \((y \times x, z) = \Delta(y, x, z) = -\Delta(x, y, z) = -(x \times y, z)\) for all \(z\), hence \(y \times x = -x \times y\).

**Linear independence criterion.** If \(y = \lambda x\), then by skew-symmetry and bilinearity, \(x \times (\lambda x) = \lambda (x \times x) = 0\). Conversely, if \(x, y\) are linearly independent, choose \(z\) such that \(x, y, z\) form a basis. Then \((x \times y, z) = \Delta(x, y, z) \neq 0\), hence \(x \times y \neq 0\).

**Norm formula.** Setting \(z = x \times y\) gives \(\Delta(x, y, x \times y) = |x \times y|^2\). On the other hand, formula (7.38) yields

$$|x \times y|^2 = |x|^2 |y|^2 - (x, y)^2.$$

If \(\theta \in [0, \pi]\) denotes the angle between \(x\) and \(y\) (with \(\cos \theta = (x,y)/(|x||y|)\)), then

$$|x \times y|^2 = |x|^2 |y|^2 (1 - \cos^2 \theta) = |x|^2 |y|^2 \sin^2 \theta.$$

Since \(\sin \theta \geq 0\) for \(\theta \in [0, \pi]\), taking square roots yields \(|x \times y| = |x| |y| \sin \theta\).
