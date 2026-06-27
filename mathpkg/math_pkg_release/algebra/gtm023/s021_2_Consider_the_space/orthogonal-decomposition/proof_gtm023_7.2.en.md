---
role: proof
locale: en
of_concept: orthogonal-decomposition
source_book: gtm023
source_chapter: "7"
source_section: "2. Orthonormal bases"
---

Since \(E_1 \cap E_1^{\perp} = 0\) (a non-zero vector cannot be orthogonal to itself), it suffices to show that every \(x \in E\) can be written as the sum of a vector in \(E_1\) and a vector in \(E_1^{\perp}\).

Select an orthonormal basis \(y_{\mu}\) (\(\mu = 1, \ldots, m\)) of \(E_1\) (exists by the Schmidt orthogonalization theorem 7.9). Given \(x \in E\), consider

$$y = \sum_{\mu} \eta^{\mu} y_{\mu} \in E_1$$

and the difference \(z = x - y\). Then for each \(\nu\),

$$(z, y_{\nu}) = (x, y_{\nu}) - (y, y_{\nu}) = (x, y_{\nu}) - \sum_{\mu} \eta^{\mu} (y_{\mu}, y_{\nu}) = (x, y_{\nu}) - \eta^{\nu}.$$

Thus \(z \in E_1^{\perp}\) if and only if \(\eta^{\nu} = (x, y_{\nu})\) for all \(\nu = 1, \ldots, m\). Choosing

$$p = \sum_{\mu} (x, y_{\mu}) y_{\mu}, \quad h = x - p,$$

we obtain \(p \in E_1\), \(h \in E_1^{\perp}\), and \(x = p + h\). Hence \(E = E_1 \oplus E_1^{\perp}\).

For the norm decomposition, compute

$$|x|^2 = (p + h, p + h) = (p, p) + (h, h) + 2(p, h).$$

Since \(p \in E_1\) and \(h \in E_1^{\perp}\), we have \((p, h) = 0\). Therefore

$$|x|^2 = |p|^2 + |h|^2,$$

which completes the proof.
