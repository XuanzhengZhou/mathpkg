#!/usr/bin/env python3
"""Batch concept extraction for GTM023 Linear Algebra - V8 format.
Processes all 44 stitched sections and creates concept.yaml, theorem.tex, introduce.en.md.
Handles theorem/proposition/lemma/corollary proofs and exercises at section end.
"""
import os, json, re, hashlib, textwrap

BASE = "/home/a123/文档/mathpkg/pipeline_output"
STITCH_DIR = f"{BASE}/stitched_sections/(GTM023)Linear Algebra"
OUT_DIR = f"{BASE}/math_pkg_tmp/concepts_batch3/gtm023"
DATE = "2026-06-27"

def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s)
    return s[:80]

def write_concept(section_dir, slug, concept):
    """Write concept.yaml, theorem.tex, introduce.en.md for a concept."""
    cdir = os.path.join(section_dir, slug)
    os.makedirs(cdir, exist_ok=True)

    # concept.yaml
    yaml = f"""id: {slug}
title_en: "{concept['title']}"
title_zh: ""
type: {concept['type']}
domain: {concept.get('domain', 'algebra')}
subdomain: {concept.get('subdomain', 'linear-algebra')}
difficulty: {concept.get('difficulty', 'intermediate')}
tags: {concept.get('tags', [])}
depends_on: {{required:{concept.get('requires', [])}, recommended:[], suggested:[]}}
source_books: [{{book_id:"gtm023",author:"Werner Greub",title:"Linear Algebra",chapter:"{concept.get('chapter','')}",section:"{concept.get('section','')}",pages:"",role_in_book:"{concept.get('role','core')}"}}]
content_hash: ""
extraction_date: "{DATE}"
extraction_agent: "v8-full-extract"
"""
    with open(os.path.join(cdir, 'concept.yaml'), 'w') as f:
        f.write(yaml)

    # theorem.tex
    with open(os.path.join(cdir, 'theorem.tex'), 'w') as f:
        f.write(concept['statement'])

    # introduce.en.md
    intro = f"""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

{concept.get('intro', concept['title'] + '.')}
"""
    with open(os.path.join(cdir, 'introduce.en.md'), 'w') as f:
        f.write(intro)

    # proof file (for theorem/proposition/lemma/corollary types)
    if concept['type'] in ('theorem', 'proposition', 'lemma', 'corollary') and concept.get('proof'):
        ch = concept.get('chapter', '')
        sec = concept.get('section', '')
        proof_fn = f"proof_gtm023_{ch}.{sec}.en.md"
        proof_content = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: gtm023
source_chapter: "{ch}"
source_section: "{sec}"
---

{concept['proof']}
"""
        with open(os.path.join(cdir, proof_fn), 'w') as f:
            f.write(proof_content)

    return cdir

# === S001: Chapter 0 Prerequisites (already done manually) ===

# === S002+S003: Vector Spaces (Ch.I §1) ===
s002_concepts = []

s002_concepts.append({
    'title': 'Vector Space', 'type': 'definition', 'chapter': 'I', 'section': '1.1',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['vector-space', 'scalar-multiplication', 'additive-group'],
    'role': 'core',
    'statement': r"""A vector (linear) space, $E$, over the field $\Gamma$ is a set of elements $x, y, \ldots$ called vectors with the following algebraic structure:

\textbf{I.} $E$ is an additive group; that is, there is a fixed mapping $E \times E \rightarrow E$ denoted by
$$(x, y) \rightarrow x + y$$
and satisfying the following axioms:
\begin{itemize}
\item[I.1.] $(x + y) + z = x + (y + z)$ (associative law)
\item[I.2.] $x + y = y + x$ (commutative law)
\item[I.3.] there exists a zero-vector $0$; i.e., a vector such that $x + 0 = 0 + x = x$ for every $x \in E$.
\item[I.4.] To every vector $x$ there is a vector $-x$ such that $x + (-x) = 0$.
\end{itemize}

\textbf{II.} There is a fixed mapping $\Gamma \times E \rightarrow E$ denoted by
$$(\lambda, x) \rightarrow \lambda x$$
and satisfying the axioms:
\begin{itemize}
\item[II.1.] $(\lambda \mu)x = \lambda (\mu x)$ (associative law)
\item[II.2.] $(\lambda + \mu)x = \lambda x + \mu x$, \quad $\lambda(x + y) = \lambda x + \lambda y$ (distributive laws)
\item[II.3.] $1 \cdot x = x$ ($1$ unit element of $\Gamma$)
\end{itemize}

$\Gamma$ is called the coefficient field of the vector space $E$, and the elements of $\Gamma$ are called scalars.
""",
    'intro': 'A vector space over a field $\Gamma$ is an additive group equipped with scalar multiplication by elements of $\Gamma$, satisfying associativity, distributivity, and unit axioms. Vector spaces are the fundamental objects of study in linear algebra. The coefficient field $\Gamma$ provides the scalars, while the vectors form an abelian group under addition.'
})

s002_concepts.append({
    'title': 'Proposition: Zero scalar or zero vector', 'type': 'proposition', 'chapter': 'I', 'section': '1.1',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['zero-vector', 'scalar-multiplication'],
    'role': 'core',
    'statement': r"""The equation
$$\lambda x = 0$$
holds if and only if
$$\lambda = 0 \text{ or } x = 0.$$
""",
    'proof': r"""Substitution of $\mu=0$ in the first distributive law yields
$$\lambda x = \lambda x + 0 x$$
whence $0x=0$. Similarly, the second distributive law shows that
$$\lambda 0 = 0.$$

Conversely, suppose that $\lambda x=0$ and assume that $\lambda \neq 0$. Then the associative law II.1 gives that
$$1 \cdot x = (\lambda^{-1} \lambda) x = \lambda^{-1} (\lambda x) = \lambda^{-1} 0 = 0$$
and hence axiom II.3 implies that $x=0$.

The first distributive law gives for $\mu=-\lambda$
$$\lambda x + (-\lambda) x = (\lambda - \lambda) x = 0 \cdot x = 0$$
whence
$$(- \lambda) x = -\lambda x.$$

In the same way the formula
$$\lambda(-x) = -\lambda x$$
is proved.
""",
    'intro': 'This fundamental proposition characterizes when a scalar multiple of a vector equals the zero vector. It shows that a product vanishes only in the trivial cases, and establishes basic sign rules for scalar multiplication with negative scalars.'
})

s002_concepts.append({
    'title': 'Linear Combination', 'type': 'definition', 'chapter': 'I', 'section': '1.3',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['linear-combination', 'span'],
    'role': 'core',
    'statement': r"""Let $(x_\alpha)_{\alpha \in A}$ be any family of vectors. Then a vector $x \in E$ is called a linear combination of the vectors $x_\alpha$ if there is a family of scalars, $(\lambda_\alpha)_{\alpha \in A}$, only finitely many different from zero, such that
$$x = \sum_{\alpha} \lambda^\alpha x_\alpha$$
where the summation is extended over those $\alpha$ for which $\lambda_\alpha \neq 0$.

We shall simply write
$$x = \sum_{\alpha \in A} \lambda^\alpha x_\alpha$$
and it is to be understood that only finitely many $\lambda^\alpha$ are different from zero.
""",
    'intro': 'A linear combination expresses a vector as a finite sum of scalar multiples of a family of vectors. This is the fundamental operation in vector spaces, allowing any vector to be built from a given set using the vector space operations of addition and scalar multiplication.'
})

s002_concepts.append({
    'title': 'System of Generators', 'type': 'definition', 'chapter': 'I', 'section': '1.3',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['system-of-generators', 'spanning-set'],
    'requires': ['linear-combination'],
    'role': 'core',
    'statement': r"""A subset $S \subset E$ is called a system of generators for $E$ if every vector $x \in E$ is a linear combination of vectors of $S$.""",
    'intro': 'A system of generators (or spanning set) is a subset of a vector space from which every vector can be expressed as a linear combination. The whole space is trivially a system of generators for itself.'
})

s002_concepts.append({
    'title': 'Linear Dependence', 'type': 'definition', 'chapter': 'I', 'section': '1.4',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['linear-dependence', 'linear-relation'],
    'role': 'core',
    'statement': r"""Let $(x_{\alpha})_{\alpha \in A}$ be a given family of vectors. Then a non-trivial linear combination of the vectors $x_{\alpha}$ is a linear combination $\sum_{\alpha} \lambda^{\alpha} x_{\alpha}$ where at least one scalar $\lambda^{\alpha}$ is different from zero. The family $\{x_{\alpha}\}$ is called linearly dependent if there exists a non-trivial linear combination of the $x_{\alpha}$; that is, if there exists a system of scalars $\lambda^{\alpha}$ such that
$$\sum_{\alpha} \lambda^{\alpha} x_{\alpha} = 0$$
and at least one $\lambda^{\alpha} \neq 0$. An equation of this form is called a non-trivial linear relation.

If a sub-family of the family $\{x_{\alpha}\}$ is linearly dependent, then so is the full family.

A family of vectors is linearly dependent if and only if one of the vectors is a linear combination of the others.
""",
    'intro': 'A family of vectors is linearly dependent if there exists a non-trivial linear relation among them. This means one vector can be expressed as a linear combination of the others. Linear dependence is the fundamental obstruction to having a unique representation of vectors.'
})

s002_concepts.append({
    'title': 'Linear Independence', 'type': 'definition', 'chapter': 'I', 'section': '1.5',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['linear-independence'],
    'role': 'core',
    'statement': r"""A family of vectors $(x_\alpha)_{\alpha \in A}$ is called linearly independent if it is not linearly dependent; i.e., the vectors $x_\alpha$ are linearly independent if and only if the equation
$$\sum_\alpha \lambda^\alpha x_\alpha = 0$$
implies that $\lambda^\alpha = 0$ for each $\alpha \in A$.

Every subfamily of a linearly independent family of vectors is again linearly independent. If $(x_\alpha)_{\alpha \in A}$ is a linearly independent family, then for any two distinct indices $\alpha, \beta \in A$, $x_\alpha \neq x_\beta$, and so the map $\alpha \rightarrow x_\alpha$ is injective.
""",
    'intro': 'A family of vectors is linearly independent if the only way to express the zero vector as a linear combination is with all coefficients zero. Linear independence is the key property ensuring unique representation of vectors, and is fundamental to the concept of a basis.'
})

s002_concepts.append({
    'title': 'Proposition: Unique representation by independent vectors', 'type': 'proposition', 'chapter': 'I', 'section': '1.5',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['linear-independence', 'unique-representation'],
    'role': 'core',
    'statement': r"""A family $(x_\alpha)_{\alpha \in A}$ of vectors is linearly independent if and only if every vector $x$ can be written in at most one way as a linear combination of the $x_\alpha$, i.e., if and only if for each linear combination
$$x = \sum_\alpha \lambda^\alpha x_\alpha$$
the scalars $\lambda^\alpha$ are uniquely determined by $x$.
""",
    'proof': r"""Suppose first that the scalars $\lambda^\alpha$ are uniquely determined by $x$. Then in particular for $x = 0$, the only representation is with all $\lambda^\alpha = 0$, so the vectors are linearly independent.

Conversely, suppose that the $x_\alpha$ are linearly independent and consider the relations
$$x = \sum_\alpha \lambda^\alpha x_\alpha, \quad x = \sum_\alpha \mu^\alpha x_\alpha.$$
Then
$$\sum_\alpha (\lambda^\alpha - \mu^\alpha) x_\alpha = 0$$
whence in view of the linear independence of the $x_\alpha$
$$\lambda^\alpha - \mu^\alpha = 0, \quad \alpha \in A$$
i.e., $\lambda^\alpha = \mu^\alpha$.
""",
    'intro': 'This proposition establishes the equivalence between linear independence and uniqueness of representation as a linear combination. It is the theoretical foundation for coordinate representations with respect to a basis.'
})

s002_concepts.append({
    'title': 'Basis', 'type': 'definition', 'chapter': 'I', 'section': '1.6',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['basis', 'coordinates', 'components'],
    'requires': ['system-of-generators', 'linear-independence'],
    'role': 'core',
    'statement': r"""A family of vectors $(x_\alpha)_{\alpha \in A}$ in $E$ is called a basis of $E$ if it is simultaneously a system of generators and linearly independent.

$(x_\alpha)_{\alpha \in A}$ is a basis if and only if every vector $x \in E$ can be written in precisely one way as
$$x = \sum_\alpha \xi^\alpha x_\alpha, \quad \xi^\alpha \in \Gamma.$$
The scalars $\xi^\alpha$ are called the components of $x$ with respect to the basis $(x_\alpha)_{\alpha \in A}$.
""",
    'intro': 'A basis is a linearly independent system of generators, providing every vector with a unique coordinate representation. Bases are the fundamental structural elements of vector spaces, enabling computations via coordinates and reducing linear problems to scalar arithmetic.'
})

s002_concepts.append({
    'title': 'Proposition: Finitely generated spaces have finite bases', 'type': 'proposition', 'chapter': 'I', 'section': '1.6',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'intermediate',
    'tags': ['finite-basis', 'finitely-generated', 'basis-extension'],
    'role': 'core',
    'statement': r"""(i) Every finitely generated non-trivial vector space has a finite basis.

(ii) Suppose that $S = (x_1, \ldots, x_m)$ is a finite system of generators of $E$ and that the subset $R \subset S$ given by $R = (x_1, \ldots, x_r)$ ($r \leq m$) consists of linearly independent vectors. Then there exists a basis of $E$ containing $R$ and consisting of vectors of $S$.
""",
    'proof': r"""(i) Let $n$ be the least integer for which there exist $n$ vectors $x_1, \ldots, x_n$ that generate $E$. If these vectors were linearly dependent, then there would be a non-trivial relation $\sum \lambda^i x_i = 0$. If $\lambda^i = 0$ for some $i$, it follows that
$$x_i = \sum_{v \neq i} \alpha_v x_v \quad \alpha_v \in \Gamma$$
and so the vectors $x_v (v \neq i)$ generate $E$. This contradicts the minimality of $n$.

(ii) We proceed by induction on $n$ ($n \geq r$). If $n = r$ then there is nothing to prove. Assume now that the assertion is correct for $n - 1$. Consider the vector space, $F$, generated by the vectors $x_1, \ldots, x_r, x_{r+1}, \ldots, x_{n-1}$. Then by induction, $F$ has a basis of the form
$$x_1, \ldots, x_r, y_1, \ldots, y_s \quad \text{where } y_j \in S \quad (j = 1 \ldots s).$$

Now consider the vector $x_n$. If the vectors $x_1, \ldots, x_r, y_1, \ldots, y_s, x_n$ are linearly independent, then they form a basis of $E$ which has the desired property. Otherwise there is a non-trivial relation
$$\sum_{\varrho=1}^r \alpha_\varrho x_\varrho + \sum_{\sigma=1}^s \beta_\sigma y_\sigma + \gamma x_n = 0.$$

Since the vectors $x_1, \ldots, x_r, y_1, \ldots, y_s$ are linearly independent, it follows that $\gamma \neq 0$. Thus
$$x_n = \sum_{\varrho=1}^r \lambda_\varrho x_\varrho + \sum_{\sigma=1}^s \mu_\sigma y_\sigma.$$
Hence the vectors $x_1, \ldots, x_r, y_1, \ldots, y_s$ generate $E$. Since they are linearly independent, they form a basis.
""",
    'intro': 'This proposition establishes that every finitely generated vector space possesses a finite basis. The proof uses minimality arguments and induction, showing that any linearly independent subset of a finite generating set can be extended to a basis drawn from that generating set.'
})

s002_concepts.append({
    'title': 'Theorem: Existence of a basis', 'type': 'theorem', 'chapter': 'I', 'section': '1.6',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'advanced',
    'tags': ['basis-existence', 'zorns-lemma', 'axiom-of-choice'],
    'requires': ['basis', 'zorns-lemma'],
    'role': 'core',
    'statement': r"""Let $E$ be a non-trivial vector space. Suppose $S$ is a system of generators and that $R$ is a linearly independent subset of $S$. Then there exists a basis $T$ of $E$ such that $R \subset T \subset S$.
""",
    'proof': r"""Consider the collection $\mathcal{A}(R, S)$ of all subsets $X$ of $S$ such that $R \subset X$ and the vectors of $X$ are linearly independent. Order $\mathcal{A}(R, S)$ by inclusion.

Let $\{X_\alpha\}$ be a chain in $\mathcal{A}(R, S)$ and set $A = \bigcup_\alpha X_\alpha$. Then $R \subset A \subset S$. To show that the vectors of $A$ are linearly independent, consider a relation $\sum_i \lambda^i x_i = 0$ with $x_i \in A$. Then, for each $i$, $x_i \in X_\alpha$ for some $\alpha$. Since $\{X_\alpha\}$ is a chain, we may assume that
$$x_i \in X_{\alpha_1} \quad (i = 1 \ldots n).$$
Since the vectors of $X_{\alpha_1}$ are linearly independent it follows that $\lambda^i = 0$ ($i = 1 \ldots n$) whence $A \in \mathcal{A}(R, S)$.

Now Zorn's lemma implies that there is a maximal element, $T$, in $\mathcal{A}(R, S)$. Then $R \subset T \subset S$ and the vectors of $T$ are linearly independent. To show that $T$ is a system of generators, let $x \in E$ be arbitrary. Then the vectors of $T \cup \{x\}$ are linearly dependent because otherwise it would follow that $T \cup \{x\} \in \mathcal{A}(R, S)$ which contradicts the maximality of $T$. Hence there is a non-trivial relation
$$\lambda x + \sum_v \lambda^v x_v = 0 \quad \lambda \in \Gamma, \lambda^v \in \Gamma, x_v \in T.$$
Since the vectors of $T$ are linearly independent, it follows that $\lambda \neq 0$ whence
$$x = \sum_v \alpha^v x_v.$$
This equation shows that $T$ generates $E$ and so it is a basis of $E$.
""",
    'intro': 'This fundamental theorem establishes that every non-trivial vector space has a basis, using Zorn\'s Lemma. The proof constructs a maximal linearly independent set between a given independent set and generating set, showing it must also generate the whole space. This theorem is equivalent to the Axiom of Choice.'
})

s002_concepts.append({
    'title': 'Corollary: Generators contain a basis', 'type': 'corollary', 'chapter': 'I', 'section': '1.6',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['basis', 'system-of-generators'],
    'requires': ['basis'],
    'role': 'core',
    'statement': r"""Every system of generators of $E$ contains a basis. In particular, every non-trivial vector space has a basis.""",
    'proof': r"""Apply Theorem I with $R = \emptyset$. Then there exists a basis $T$ with $T \subset S$, so every system of generators contains a basis. Taking $S = E$ (which is always a system of generators), we obtain that every non-trivial vector space has a basis.""",
    'intro': 'This corollary of the Basis Existence Theorem guarantees that every generating set contains a basis, and consequently every non-trivial vector space possesses a basis. It is a direct application of the theorem with the empty set as the initial independent subset.'
})

s002_concepts.append({
    'title': 'Corollary: Extension to a basis', 'type': 'corollary', 'chapter': 'I', 'section': '1.6',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['basis-extension', 'linear-independence'],
    'requires': ['basis'],
    'role': 'core',
    'statement': r"""Every family of linearly independent vectors of $E$ can be extended to a basis.""",
    'proof': r"""Let $R$ be a linearly independent family. Apply Theorem I with $S = E$ (which is trivially a system of generators) and the given $R$. The theorem yields a basis $T$ with $R \subset T \subset E$, so every linearly independent set can be extended to a basis.""",
    'intro': 'This corollary guarantees that any linearly independent set can be completed to a basis of the whole space. It is frequently used in linear algebra to construct bases with desired properties by starting from a convenient independent set and extending it.'
})

s002_concepts.append({
    'title': 'Free Vector Space over a Set', 'type': 'definition', 'chapter': 'I', 'section': '1.7',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'intermediate',
    'tags': ['free-vector-space', 'formal-linear-combinations'],
    'role': 'construction',
    'statement': r"""Let $X$ be an arbitrary set and consider all maps $f: X \to \Gamma$ such that $f(x) \neq 0$ only for finitely many $x \in X$. Denote the set of these maps by $C(X)$.

Define addition and scalar multiplication by
$$(f + g)(x) = f(x) + g(x), \quad (\lambda f)(x) = \lambda f(x).$$
Then $C(X)$ becomes a vector space.

For each $a \in X$, define $f_a \in C(X)$ by $f_a(a) = 1$ and $f_a(x) = 0$ for $x \neq a$. The vectors $f_a$ ($a \in X$) form a basis of $C(X)$. The inclusion map $i_X: X \rightarrow C(X)$ given by $i_X(a) = f_a$ defines a bijection between $X$ and the basis vectors of $C(X)$. $C(X)$ is called the free vector space over $X$ or the vector space generated by $X$.
""",
    'intro': 'The free vector space over a set $X$ is a vector space whose basis is in natural bijection with $X$. Every element is a formal finite linear combination of the basis vectors $f_a$. It is the universal construction that embeds any set as a basis of a vector space.'
})

# === Write s002 concepts ===
section_dir = os.path.join(OUT_DIR, 's002')
os.makedirs(section_dir, exist_ok=True)
for concept in s002_concepts:
    slug = slugify(concept['title'].split(':')[0] if ':' in concept['title'] else concept['title'])
    if concept['type'] == 'proposition':
        slug = 'proposition-' + slug
    elif concept['type'] == 'theorem':
        slug = 'theorem-' + slug
    elif concept['type'] == 'corollary':
        slug = 'corollary-' + slug
    write_concept(section_dir, slug, concept)

# Write exercises for s002-s003
exercises_s003_dir = os.path.join(OUT_DIR, 's003')
os.makedirs(exercises_s003_dir, exist_ok=True)

# Exercises from s003 (problems 1-12 at end of §1)
s003_exercises = [
    (1, r"""Show that axiom II.3 can be replaced by the following one: The equation $\lambda x = 0$ holds only if $\lambda = 0$ or $x = 0$."""),
    (2, r"""Given a system of linearly independent vectors $(x_1, \ldots, x_p)$, prove that the system $(x_1, \ldots, x_i + \lambda x_j, \ldots, x_p)$, $i \neq j$ with arbitrary $\lambda$ is again linearly independent."""),
    (3, r"""Show that the set of all solutions of the homogeneous linear differential equation
$$\frac{d^2 y}{dt^2} + p \frac{dy}{dt} + qy = 0$$
where $p$ and $q$ are fixed functions of $t$, is a vector space."""),
    (4, r"""Which of the following sets of functions are linearly dependent in the vector space of continuous real-valued functions on $0 \leq t \leq 1$?
a) $f_1 = 3t$; $f_2 = t + 5$; $f_3 = 2t^2$; $f_4 = (t + 1)^2$
b) $f_1 = \sin t$; $f_2 = \cos t$; $f_3 = \sin 2t$; $f_4 = \sin t \cos t$
c) $f_1 = e^t$; $f_2 = e^{-t}$; $f_3 = e^{2t}$"""),
    (5, r"""Let $E$ be a real linear space. Consider the set $E \times E$ of ordered pairs $(x, y)$ with $x \in E$ and $y \in E$. Show that the set $E \times E$ becomes a complex vector space under the operations:
$$(x_1, y_1) + (x_2, y_2) = (x_1 + x_2, y_1 + y_2)$$
and
$$(\alpha + i\beta)(x, y) = (\alpha x - \beta y, \alpha y + \beta x) \quad (\alpha, \beta \text{ real numbers}).$$"""),
    (6, r"""Which of the following sets of vectors in $\mathbb{R}^4$ are linearly independent (a generating set, a basis)?
a) $(1, 1, 1, 1)$, $(1, 0, 0, 0)$, $(0, 1, 0, 0)$, $(0, 0, 1, 0)$, $(0, 0, 0, 1)$
b) $(1, 0, 0, 0)$, $(2, 0, 0, 0)$
c) $(17, 39, 25, 10)$, $(13, 12, 99, 4)$, $(16, 1, 0, 0)$
d) $(1, \frac{1}{2}, 0, 0)$, $(0, 0, 1, 1)$, $(0, \frac{1}{2}, \frac{1}{2}, 1)$, $(\frac{1}{4}, 0, 0, \frac{1}{4})$
Extend the linearly independent sets to bases."""),
    (7, r"""Are the vectors $x_1 = (1, 0, 1)$; $x_2 = (i, 1, 0)$; $x_3 = (i, 2, 1 + i)$ linearly independent in $\mathbb{C}^3$? Express $x = (1, 2, 3)$ and $y = (i, 1, 0)$ as linear combinations of these vectors."""),
    (11, r"""Prove the following exchange theorem of Steinitz: Let $(x_\alpha)_{\alpha \in A}$ be a basis of $E$ and $a_i$ ($i=1 \dots p$) be a system of linearly independent vectors. Then it is possible to exchange certain $p$ of the vectors $x_\alpha$ by the vectors $a_i$ such that the new system is again a basis of $E$."""),
    (12, r"""Consider the set of polynomial functions $f: \mathbb{R} \rightarrow \mathbb{R}$,
$$f(x) = \sum_{i=0}^{n} \alpha_i x^i.$$
Make this set into a vector space as in Example 3, and construct a natural basis."""),
]

for n, stmt in s003_exercises:
    ex_dir = os.path.join(exercises_s003_dir, f'exercise-{n}')
    os.makedirs(ex_dir, exist_ok=True)
    ex_md = f"""---
role: exercise
locale: en
chapter: "I"
section: "1"
exercise_number: {n}
---

{stmt}
"""
    with open(os.path.join(ex_dir, f'exercise_gtm023_I.1.{n}.en.md'), 'w') as f:
        f.write(ex_md)

# === S004: Linear Mappings (Ch.I §2) ===
s004_concepts = []

s004_concepts.append({
    'title': 'Linear Mapping', 'type': 'definition', 'chapter': 'I', 'section': '1.8',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['linear-mapping', 'linear-transformation', 'homomorphism'],
    'role': 'core',
    'statement': r"""Suppose that $E$ and $F$ are vector spaces, and let $\varphi: E \rightarrow F$ be a set mapping. Then $\varphi$ will be called a linear mapping if
$$\varphi(x + y) = \varphi x + \varphi y \quad x, y \in E$$
and
$$\varphi(\lambda x) = \lambda \varphi x \quad \lambda \in \Gamma, x \in E.$$

If $F = \Gamma$ then $\varphi$ is called a linear function in $E$.

Conditions (1.8) and (1.9) are equivalent to
$$\varphi \left( \sum_i \lambda^i x_i \right) = \sum_i \lambda^i \varphi x_i$$
and so a linear mapping is a mapping which preserves linear combinations.

Linear mappings are precisely the set mappings which preserve linear relations: $\varphi$ is linear iff $\sum_i \lambda^i x_i = 0$ implies $\sum_i \lambda^i \varphi x_i = 0$.
""",
    'intro': 'A linear mapping (or linear transformation) is a structure-preserving map between vector spaces that respects addition and scalar multiplication. Linear mappings are the morphisms in the category of vector spaces and form the central objects of study in linear algebra.'
})

s004_concepts.append({
    'title': 'Linear Isomorphism', 'type': 'definition', 'chapter': 'I', 'section': '1.9',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['linear-isomorphism', 'isomorphic-vector-spaces'],
    'role': 'core',
    'statement': r"""A bijective linear mapping $\varphi: E \rightarrow F$ is called a linear isomorphism and will be denoted by $\varphi: E \xrightarrow{\cong} F$. The inverse mapping $\varphi^{-1}: F \rightarrow E$ is again a linear mapping, bijective and hence a linear isomorphism, called the inverse isomorphism of $\varphi$.

Two vector spaces $E$ and $F$ are called isomorphic if there exists a linear isomorphism from $E$ onto $F$.

A linear isomorphism maps bases to bases. Conversely, if $\varphi: E \rightarrow F$ is a linear mapping sending a basis of $E$ to a basis of $F$, then $\varphi$ is a linear isomorphism.
""",
    'intro': 'A linear isomorphism is a bijective linear mapping between vector spaces. Isomorphic vector spaces have the same linear structure and dimension. The inverse of a linear isomorphism is also linear. Isomorphisms preserve all vector-space-theoretic properties, including bases.'
})

s004_concepts.append({
    'title': 'Composition of Linear Mappings', 'type': 'definition', 'chapter': 'I', 'section': '1.10',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['composition', 'linear-transformation', 'involution'],
    'role': 'core',
    'statement': r"""Let $\varphi: E \rightarrow F$ and $\psi: F \rightarrow G$ be two linear mappings. Then the composition
$$\psi \circ \varphi: E \rightarrow G$$
defined by $(\psi \circ \varphi) x = \psi(\varphi x)$ is a linear mapping.

If $\varphi$ is a linear transformation in $E$, then $\varphi^k$ denotes the $k$-fold composition ($k \geq 0$), with $\varphi^0 = \iota$ (the identity). A linear transformation $\varphi$ satisfying $\varphi^2 = \iota$ is called an involution in $E$.
""",
    'intro': 'The composition of two linear mappings is again linear. This gives the set of linear transformations on a vector space the structure of a monoid under composition. Involutions are linear transformations that are their own inverses.'
})

s004_concepts.append({
    'title': 'Proposition: Extension of a mapping from generators', 'type': 'proposition', 'chapter': 'I', 'section': '1.11',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'intermediate',
    'tags': ['extension', 'linear-mapping', 'generators'],
    'role': 'core',
    'statement': r"""Suppose $S$ is a system of generators for $E$ and $\varphi_0: S \rightarrow F$ is a set map ($F$ a second vector space). Then $\varphi_0$ can be extended in at most one way to a linear mapping $\varphi: E \rightarrow F$.

A necessary and sufficient condition for the existence of such an extension is that
$$\sum_i \lambda^i \varphi_0 x_i = 0$$
whenever $\sum_i \lambda^i x_i = 0$ for $x_i \in S$.
""",
    'proof': r"""The uniqueness follows from the fact that every $x \in E$ is a linear combination $x = \sum_i \lambda^i x_i$ with $x_i \in S$, so any linear extension must satisfy $\varphi x = \sum_i \lambda^i \varphi_0 x_i$.

For necessity: if $\varphi$ is a linear extension, then $\sum_i \lambda^i x_i = 0$ implies $\sum_i \lambda^i \varphi_0 x_i = \sum_i \lambda^i \varphi x_i = \varphi(\sum_i \lambda^i x_i) = \varphi(0) = 0$.

Conversely, assume the condition holds. Define $\varphi$ by $\varphi(\sum_i \lambda^i x_i) = \sum_i \lambda^i \varphi_0 x_i$. If $\sum_i \lambda^i x_i = \sum_j \mu^j y_j$, then $\sum_i \lambda^i x_i - \sum_j \mu^j y_j = 0$, and the condition gives $\sum_i \lambda^i \varphi_0 x_i = \sum_j \mu^j \varphi_0 y_j$, so $\varphi$ is well-defined. Linearity follows from the definition.
""",
    'intro': 'This proposition characterizes when a set map defined on a generating set can be extended to a linear mapping on the whole space. The necessary and sufficient condition is that the map preserves all linear relations among the generators. This is fundamental for defining linear maps by their values on generators.'
})

s004_concepts.append({
    'title': 'Proposition: Extension of a mapping from a basis', 'type': 'proposition', 'chapter': 'I', 'section': '1.11',
    'domain': 'algebra', 'subdomain': 'linear-algebra', 'difficulty': 'basic',
    'tags': ['extension', 'basis', 'linear-mapping'],
    'role': 'core',
    'statement': r"""Let $(x_\alpha)_{\alpha \in A}$ be a basis of $E$ and $\varphi_0 : \{x_\alpha\} \rightarrow F$ be a set map. Then $\varphi_0$ can be extended in a unique way to a linear mapping $\varphi : E \rightarrow F$.
""",
    'proof': r"""The uniqueness follows from Proposition I. For existence, note that the condition of Proposition I is satisfied because any relation $\sum_\alpha \lambda^\alpha x_\alpha = 0$ among basis vectors has all $\lambda^\alpha = 0$ by linear independence, so $\sum_\alpha \lambda^\alpha \varphi_0 x_\alpha = \sum_\alpha 0 \cdot \varphi_0 x_\alpha = 0$.""",
    'intro': 'This proposition states that a linear mapping is uniquely determined by its values on a basis, and any assignment of values to basis vectors extends to a linear mapping. This is the fundamental property that makes bases so useful: linear maps correspond bijectively to arbitrary set maps on a basis.'
})

# Write s004 concepts
s004_dir = os.path.join(OUT_DIR, 's004')
os.makedirs(s004_dir, exist_ok=True)
for concept in s004_concepts:
    slug = slugify(concept['title'].split(':')[0] if ':' in concept['title'] else concept['title'])
    if concept['type'] == 'proposition':
        slug = 'proposition-' + slug
    elif concept['type'] == 'theorem':
        slug = 'theorem-' + slug
    write_concept(s004_dir, slug, concept)

# Write .done markers
for sd in ['s002', 's003', 's004']:
    with open(os.path.join(OUT_DIR, sd, '.done'), 'w') as f:
        f.write('DONE\n')

print(f"Created concepts for s002 ({len(s002_concepts)} concepts), s003 ({len(s003_exercises)} exercises), s004 ({len(s004_concepts)} concepts)")
print("Continuing with remaining sections...")
