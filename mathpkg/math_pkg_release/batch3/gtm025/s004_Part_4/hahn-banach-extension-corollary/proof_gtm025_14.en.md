---
role: proof
locale: en
of_concept: hahn-banach-extension-corollary
source_book: gtm025
source_chapter: "4"
source_section: "14"
---

Apply the Hahn-Banach theorem (14.9) with $p(x) = \|f\| \cdot \|x\|$, which is a sublinear functional. The extension $g$ satisfies $g(x) \le \|f\| \cdot \|x\|$ and $-g(x) = g(-x) \le \|f\| \cdot \|x\|$, so $|g(x)| \le \|f\| \cdot \|x\|$. Thus $\|g\| \le \|f\|$. Since $g$ extends $f$, $\|g\| \ge \|f\|$, giving equality.
