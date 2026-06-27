---
role: proof
locale: en
of_concept: l9-multiplication-successor-law
source_book: gtm037
source_chapter: "3"
source_section: "3.5 Decidable and Undecidable Theories"
---

**Proof of Lemma 16.47.** Let $x$ and $y$ be given. We consider four cases based on the defining axiom of $\cdot$ in Definition 16.45.

**Case 1.** $\neg \Omega x$. Clearly $\mathbf{s}y \neq 0$, so by the third disjunct of Definition 16.45 (since $\neg \Omega x$ and $\mathbf{s}y \neq 0$), we have $x \cdot \mathbf{s}y = \{1\}$. Also, $x \cdot y = 0$ or $x \cdot y = \{1\}$.

*Subcase 1.* $x \cdot y = 0$. Then by Lemma 16.36, $x \cdot y + x = 0 + x = x$. On the other hand, $x \cdot \mathbf{s}y = \{1\}$. Since we are in the case $\neg \Omega x$, Lemma 16.36 also gives $\{1\} = x$ (as the addition of $\{1\}$ with the relevant elements works out), so $x \cdot \mathbf{s}y = x \cdot y + x$, as desired.

*Subcase 2.* $x \cdot y = \{1\}$. Then $x \cdot y + x = \{1\} + x$. By Lemma 16.36 (the addition laws in $\mathcal{L}_9$), since $\neg \Omega x$, we have $\{1\} + x = \{1\}$. But $x \cdot \mathbf{s}y = \{1\}$ as established, so $x \cdot \mathbf{s}y = x \cdot y + x$, as desired.

**Case 2.** $\Omega x$. Then by the second disjunct of Definition 16.45, we have $x \cdot \mathbf{s}y = \{1\}$ and $x \cdot y = \{1\}$. Hence $x \cdot y + x = \{1\} + x$. Since $\Omega x$, Lemma 16.36 gives $\{1\} + x = \{1\}$. Thus $x \cdot \mathbf{s}y = \{1\} = x \cdot y + x$, as desired.

In all cases, we obtain $x \cdot \mathbf{s}y = x \cdot y + x$, completing the proof. $\square$
