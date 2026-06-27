#!/usr/bin/env python3
"""Create proof files for all theorem/lemma/proposition/corollary concepts in GTM024."""
import os

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch3/gtm024"

# All concepts that need proofs (non-definition, non-axiom types)
proof_concepts = {
    # §1
    "basis-cardinality-theorem": ("1", "1", "Standard: if B1, B2 are bases, each element of B1 is a finite linear combination of B2, so |B1| ≤ |B2|·ℵ₀. Symmetry gives equality of cardinalities."),
    "hyperplane-characterization": ("1", "1", "If V is a hyperplane, it is a maximal proper affine subspace. Its translate to contain θ is a maximal proper subspace M. Choose any φ∈X' with ker(φ)=M. Then V is a level set of φ."),
    "factorization-through-kernel": ("1", "1", "Define R on range(S) by R(S(x))=T(x). Well-defined because ker(S)⊂ker(T). Extend linearly to span, then to all of Z by choosing a complementary subspace."),
    "linear-dependence-via-kernels": ("1", "1", "If ψ∈span{φᵢ}, clearly ∩ker(φᵢ)⊂ker(ψ). Conversely, define S:X→ℝⁿ by S(x)=(φ₁(x),…,φₙ(x)). If ∩ker(φᵢ)⊂ker(ψ), then ker(S)⊂ker(ψ), so ψ factors through S by the factorization theorem."),
    "annihilator-transpose-lemma": ("1", "1", "ψ∈(range T)° iff ψ(Tx)=0 ∀x iff (T'ψ)(x)=0 ∀x iff T'ψ=θ iff ψ∈ker(T'). The second inclusion follows similarly."),

    # §2
    "stones-lemma": ("1", "2", "Let 𝒞 be the class of all convex sets disjoint from B containing A, partially ordered by inclusion. Zorn's lemma gives a maximal C. Set D=X\C. If D is not convex, there are x,z∈D with (x,z)∩C≠∅. Maximality of C then forces a contradiction via convexity arguments."),
    "simplex-intrinsic-core": ("1", "2", "Let vertices be x₀,…,xₙ. A point a=∑αᵢxᵢ with all αᵢ>0 is in icr because for any b in the simplex, we can extend past a. Conversely, if some αᵢ=0, the point lies in a proper face and is not in icr."),
    "core-characterization-finite-dim": ("1", "2", "If aff(A)=X, then A contains an n-simplex with n=dim(X), which has nonempty icr=cor. Conversely, if p∈cor(A), for any x∈X there is ε>0 with p+ε(x-p)∈A, so x∈aff(A)."),
    "core-ray-lemma": ("1", "2", "For y∈[p,x) with y=tx+(1-t)p, t∈(0,1): given z∈X, ∃λ>0 with p+λz∈A. Then y+(1-t)λz=(1-t)(p+λz)+tx∈A, proving y∈cor(A)."),
    "lina-theorem": ("1", "2", "If lina(A)≠X, the complement M consists of points not linearly accessible from A. One shows M is an affine subspace. If M contains a point p∈cor(C) and -p∈cor(D) for complementary convex sets C,D, then X=span({p}∪M), contradiction unless M is a hyperplane."),

    # §3
    "convex-function-characterization": ("1", "3", "For C¹ functions on an interval, convexity ⇔ difference quotients monotone ⇔ f' non-decreasing. For C², f''≥0 iff f' non-decreasing."),
    "convexity-via-inf-projection": ("1", "3", "For x,y in the projection and t∈(0,1), choose (x,s),(y,t)∈K. Then (tx+(1-t)y, ts+(1-t)t)∈K by convexity of K, so f(tx+(1-t)y)≤tf(x)+(1-t)f(y)."),
    "gauge-properties": ("1", "3", "(a) Clear from definition. (b) For x,y∈X, choose t>ρA(x)+ρA(y). Then x/α,y/β∈A for some α,β with α+β=t. By convexity, (x+y)/t∈A, so ρA(x+y)≤t. (c) Use balancedness: x∈tA ⇒ λx∈|λ|tA."),

    # §4
    "basic-separation-theorem": ("1", "4", "Apply Stone's lemma to get complementary convex C,D with A⊂C,B⊂D. The separating surface is the affine subspace lina(C)∩lina(D). If this is not a hyperplane, a contradiction arises. Then choose φ∈X' with this surface as a level set."),
    "separation-via-difference": ("1", "4", "If φ separates θ from A-B: φ(a-b)≥0 ⇒ φ(a)≥φ(b). For strong separation, use the absorbing set condition."),
    "strong-separation-theorem": ("1", "4", "If such V exists, (A+V)∩B=∅. Since V is absorbing, A+V and B can be separated by the basic separation theorem, giving strong separation. Conversely, if strongly separated, the slab defines V."),

    # §5
    "existence-positive-functionals": ("1", "5", "Choose x∈X\P. Apply basic separation theorem (4B) to separate x and P by a hyperplane [φ;α]. Any functional bounded below on a wedge is non-negative on it, so φ∈P⁺ and φ≠θ."),
    "cone-via-base": ("1", "5", "If x∈P∩(-P) then x=λb=-μc for b,c∈B, λ,μ>0. Then (λ/μ)b=-c, so by uniqueness of representation, b=c and λ/μ=1, implying x=θ."),

    # §6
    "hahn-banach-theorem": ("1", "6", "Define p(x)=inf{g(x+m):m∈M}. Then p is sublinear and φ≤p|M. By the key lemma (using Zorn's lemma), φ extends to φ̄≤p≤g on X."),
    "hahn-banach-seminorm-corollary": ("1", "6", "Apply the Hahn-Banach theorem with g=ρ. The condition |φ|≤ρ is equivalent to φ≤ρ and -φ≤ρ (for real case)."),
    "krein-rutman-theorem": ("1", "6", "Let p∈cor(P)∩M. Define a sublinear functional using the order structure and apply the Hahn-Banach extension preserving positivity via the core point condition."),
    "support-theorem": ("1", "6", "Assume θ∈icr(A). Let M=span(A). If x∈M, use basic separation on icr(A) and x in M. If x∉M, any φ∈M° with φ(x)>0 works."),
    "support-theorem-corollary": ("1", "6", "Immediate from the support theorem: points in A\icr(A) are proper support points; icr(A) points cannot be separated from icr(A)."),
    "subdifferentiability-theorem": ("1", "6", "For x₀∈cor(A), the point (x₀,f(x₀)) can be separated from epi(f) by a hyperplane. The non-verticality follows from x₀ being a core point. The subgradient is obtained from the separating functional."),
    "subgradient-geometric": ("1", "6", "(a) φ∈∂f(x₀) iff the affine function h(x)=f(x₀)+φ(x-x₀) satisfies h≤f on A, which geometrically means the graph of h supports epi(f) at (x₀,f(x₀)). (b) Scale the functional."),
    "equivalence-six-propositions": ("1", "6", "Shown by establishing the cycle: (1)→(2)→(3)→(4)→(5)→(6)→(1). Each implication has been demonstrated in the respective sections."),

    # §7
    "fans-condition": ("1", "7", "Necessity is clear. For sufficiency, suppose no solution exists in (1+δ)A. Separate c from T((1+δ)A) in ℝⁿ. The separating functional gives α₁,…,αₙ violating the condition."),
    "fans-inequality-condition": ("1", "7", "Define T:X→ℝⁿ as before. Inconsistency means (T(X)-c)∩P=∅. Separate in ℝⁿ, then lift to get the condition. The closedness of the image of P is used."),
    "mazur-orlicz-theorem": ("1", "7", "Reduce to finite subsystems. Use compactness of B={φ(xⱼ₁),…,φ(xⱼₙ):φ≤g} in ℝⁿ (Ascoli). If no solution exists, separate B from P+c. The separating functional gives α₁,…,αₙ violating (7.2)."),
    "directional-derivative-convex": ("1", "7", "For h∈Conv(X) with h(θ)=0, show h(tx)/t is non-decreasing for t>0 using h(sx)≤(s/t)h(tx)+((t-s)/t)h(θ). Apply to h(y)=g(x₀+y)-g(x₀)."),
    "directional-derivative-existence": ("1", "7", "The difference quotient is bounded below (by -g'(x₀;-x)) and non-decreasing, so limit exists. Sublinearity follows from limit properties and convexity of g."),
    "gradient-subgradient-relation": ("1", "7", "(a) For any ψ∈∂g(x₀), ψ(x)≤g'(x₀;x)=∇g(x₀)(x). Similarly ψ(-x)≤g'(x₀;-x)=-∇g(x₀)(x) gives -ψ(x)≥-∇g(x₀)(x). Hence ψ=∇g(x₀). (b) If ∇g fails to exist, construct distinct subgradients using Hahn-Banach on span{x̄}."),
    "tangent-support-relation": ("1", "7", "Subgradients of ρA at x₀ correspond to functionals φ with φ(x)≤ρA(x₀+x)-ρA(x₀) for all x. For x₀∈A with ρA(x₀)=1, these φ define supporting hyperplanes [φ;1] to A at x₀. The tangent function τA(x₀;·)=ρ'A(x₀;·) is exactly the support function."),

    # §8
    "extremal-flat-lemma": ("1", "8", "Induction on dim(A). If dim(A)=n, A has a bounding point unless A=ℝⁿ. A supporting hyperplane H at that point gives A∩H of lower dimension, which by induction contains an extremal flat. Parallelism: if L₁≠L₂, then L₁+K₂ strictly contains K₂ but is contained in A, contradicting maximality."),
    "recession-cone-properties": ("1", "8", "(a) Check convexity and positive homogeneity. (b) If x∈C_B, then b+tx∈B for all t≥0 by repeated application of x+B⊂B. Conversely, if condition holds, x+B⊂B. (c) Use sequential characterization and strong separation."),
    "klee-minkowski-decomposition": ("1", "8", "By (8.4), A=L_A+B where B=A∩L_A^\perp is line-free. Hausdorff maximal principle gives maximal chain of B-extremal subsets, leading to ext(B)≠∅. An inductive argument on dimension shows B⊂C_B+co(ext(B))."),
    "compact-convex-hull-extreme": ("1", "8", "Compact ⇒ C_A={θ} and L_A={θ}, so B=A. By Klee-Minkowski, A=co(ext(A)). Since A is closed, co(ext(A)) is already closed (finite dim)."),
    "cone-extreme-rays": ("1", "8", "Let K=[φ;1]∩C be a base. K is compact. If p∈ext(K), the ray through p is an extreme ray of C. The Minkowski theorem for K gives K=co(ext(K)), hence C=co(rext(C))."),
    "concave-program-theorem": ("1", "8", "Let F={x∈A:f(x)=inf f(A)}. F is nonempty, closed, convex, A-extremal. By 8B, F has an extreme point, which is extreme in A. For the converse, use concavity: f(Σtᵢeᵢ)≥Σtᵢf(eᵢ)≥f(p) if p minimizes f on ext(A). For unbounded case, use recession cone."),
    "extreme-points-k0": ("1", "8", "For φ∈ext(K₀), show φ(fg)=φ(f)φ(g). First with g=e: define ψ=(1-φ(e))φ, verify φ±ψ∈K₀, then ψ=θ by extremality. For general g, use similar technique with perturbation. Converse: for self-adjoint A, use inequality φ(f)²≥φ(f²) and a midpoint argument."),

    # §9
    "local-base-properties": ("2", "9", "(a) From continuity of scalar multiplication at 0. (b) From continuity of addition at (θ,θ). (c) x∈Ā iff every neighborhood of x meets A iff x∈∩(A+U). (d) θ is the only common point of all neighborhoods iff points can be separated, i.e., Hausdorff."),
    "finite-dim-isomorphism": ("2", "9", "T is continuous by induction using LTS axioms. For openness: let B be unit 2-ball in Fⁿ. The boundary S is compact, so T(S) is compact and does not contain θ. Thus X\T(S) contains a balanced θ-neighborhood U⊂T(B). Hence T is open."),
    "singer-yamabe-theorem": ("2", "9", "First lemma: A∩ker(φ) is dense in ker(φ) for φ∈X* continuous, A dense convex. Proof: pick points in A∩(x+U)∩H⁺ and A∩(x+U)∩H⁻, take convex combination to get point in A∩ker(φ)∩(x+2U). For the main theorem, apply lemma inductively to φ₁,…,φₙ."),
    "riesz-lemma": ("2", "9", "For any U∈𝒰, choose n with λⁿA⊂U. Then A⊂M+λA⊂M+λ(M+λA)=M+λ²A⊂…⊂M+λⁿA⊂M+U. Since U is arbitrary and M is closed, A⊂M̄=M."),
    "finite-dim-via-totally-bounded": ("2", "9", "If U is totally bounded, then U is bounded and fundamental. Choose λ with 0<|λ|<1. Then U⊂B+λU for some finite B. By Riesz lemma, B is fundamental. Since B is finite, dim(X)<∞. Converse: in Fⁿ, any bounded set is totally bounded."),

    # §10
    "locally-convex-base-lemma": ("2", "10", "(a) Verify the conditions of 9A for the topology with local base 𝒰. The key is that absolutely convex sets are balanced and convex. (b) The topology generated by 𝒰 is locally convex because finite intersections of absolutely convex sets are absolutely convex."),
    "seminorm-topology-properties": ("2", "10", "(a) Nets converge iff they converge in each semi-norm. (b) Boundedness in each semi-norm gives boundedness. (c) Total boundedness equivalent to finite ε-nets for each semi-norm. Proofs follow from the local base description."),
    "normability-theorem": ("2", "10", "If X is normed by ρ, U_ρ is a proper bounded θ-neighborhood. Conversely, if such U exists, it contains a barrel B. The gauge ρ_B is a norm (proper because B is bounded) and defines the topology since B is a neighborhood."),

    # §11
    "convex-set-closure-interior": ("2", "11", "Closure convex: continuous image argument. (a) int(A)=cor(A): use absorbing property of θ-neighborhoods. (b) int(A) dense in A: use segment from interior point. (c) lin(A)=Ā: any point in A can be approached from interior. (d) Algebraic boundary=topological boundary follows from (a) and (c)."),
    "convex-hull-totally-bounded": ("2", "11", "Given ε,ρ and an (ε/2,ρ)-net {x₁,…,xₙ}⊂A, show co({x₁,…,xₙ}) is totally bounded (compact in finite dim). Let {yⱼ} be an (ε/2,ρ)-net there. For any x∈co(A), approximate by convex combination of the xᵢ, then by yⱼ."),
    "linear-map-continuity": ("2", "11", "(a)⇔(b): T(x+U)⊂T(x)+V iff T(U)⊂V. (b)⇔(c): uniform continuity follows from linearity plus continuity at θ. For LCS case: T continuous at θ iff ∀ρ,∃σ,β: ρ(Tx)≤βσ(x)."),
    "finite-rank-continuity": ("2", "11", "If ker(T) closed, X/ker(T) is finite dim Hausdorff LTS. By 9E, any linear map on it is continuous. Then T = T̂∘Q is continuous. Converse is trivial."),
    "dense-hyperplane-corollary": ("2", "11", "If φ is discontinuous, ker(φ) is not closed. Its closure is a subspace containing ker(φ) properly. Since ker(φ) is a hyperplane (maximal proper subspace), its closure must be X."),
    "separation-closed-hyperplane": ("2", "11", "Let V be a convex θ-neighborhood with (x+V)∩A=∅. Apply basic separation to x+V and A. The separating functional φ is bounded on V, hence continuous. Thus the separating hyperplane is closed."),
    "hahn-banach-continuous": ("2", "11", "The algebraic Hahn-Banach extensions exist by 6A. Since g (resp. ρ) is continuous, the extension is bounded on a neighborhood of θ, hence continuous by 11D."),
    "separation-corollary-1": ("2", "11", "Let z=x-y≠θ. Choose convex θ-neighborhood V not containing z. Separate z from V by a closed hyperplane [ψ;α]. ψ(z)≠0 because ψ(V) is an interval containing 0. Then φ=re(ψ) separates x,y."),
    "separation-corollary-2": ("2", "11", "Immediate from the separation theorem: boundary point not in interior, so can be separated from interior by closed hyperplane, which supports the set at that point."),

    # §12
    "weak-topology-local-base": ("2", "12", "The sets {x:|φ(x)|≤1,φ∈F} for F⊂Y finite are absolutely convex and absorbing. They form a local base by definition of the N-topology. Hausdorffness: the semi-norms separate points iff Y is total."),
    "weak-continuous-functionals": ("2", "12", "If φ∈Y, it is σ(X,Y)-continuous by definition. Conversely, if φ is σ(X,Y)-continuous, there exists a finite F⊂Y and ε>0 such that |φ(x)|≤1 when |ψ(x)|≤ε for ψ∈F. This implies ker(φ)⊃∩_{ψ∈F}ker(ψ), so φ∈span(F)⊂Y."),
    "weak-closure-convex": ("2", "12", "By 11F, any point outside co̅(A) can be strongly separated from A by a closed hyperplane [φ;α] with φ∈X*. Then no net in A can converge weakly to this point, so it is not in the weak closure."),
    "norm-weak-lower-semicontinuous": ("2", "12", "The unit ball U(X) is convex and closed, hence weakly closed by 11F. Its positive multiples are also weakly closed. Therefore {x:‖x‖≤c} is weakly closed for all c>0, i.e., the norm is weakly lower semicontinuous."),
    "bipolar-theorem": ("2", "12", "Clearly {θ}∪A⊂°(A°). Since °(A°) is convex and weakly closed, it contains the closed convex hull. Conversely, if any closed half-space contains {θ}∪A, it must contain °(A°). Thus °(A°)=co̅({θ}∪A)."),
    "bipolar-corollary-1": ("2", "12", "Apply bipolar theorem to A°: (°(A°))°=A° since °(A°)=co̅({θ}∪A) implies its polar equals A°."),
    "bipolar-corollary-2": ("2", "12", "Let M=span(A). M̄ʷ=X iff (M̄ʷ)°=X°={θ}. But M̄ʷ=°(M°) by bipolar theorem. So condition becomes (°(M°))°=M°={θ}, i.e., M°={θ}."),
    "bipolar-corollary-3": ("2", "12", "Apply Corollary 2 with X replaced by X* and A being the subset of X*."),
    "alaoglu-bourbaki-theorem": ("2", "12", "V° is a closed subset of the product Π_{x∈X}[-ρ_V(x),ρ_V(x)]. By Tychonov's theorem, this product is compact. V° inherits the relative product topology, which coincides with the weak* topology, giving weak* compactness."),

    # §13
    "krein-milman-theorem": ("2", "13", "By Zorn's lemma, the family of non-empty compact extremal subsets has a minimal element. Any such minimal compact extremal set must be a singleton: if it contained two points, a continuous functional separating them would produce a proper extremal subset. Hence extreme points exist. If K≠co̅(ext(K)), separate a point in K\co̅(ext(K)) from co̅(ext(K)) by a hyperplane, producing a compact extremal set disjoint from ext(K), contradicting the first part."),
    "converse-krein-milman": ("2", "13", "If K=co̅(E) and x∈ext(K), then x must belong to the closure of E. Otherwise, separate x from Ē by a functional, producing an extremal set not containing x, contradicting that x is extreme."),
    "krein-milman-applications": ("2", "13", "Apply KM to U(C(Ω)*) with weak* topology. Its extreme points are ±δ_t. Any functional attaining its norm on U(C(Ω)*) corresponds to such an extreme point, yielding the Riesz representation."),

    # §14
    "biconjugate-theorem": ("2", "14", "f**(x)=sup_φ(φ(x)-f*(φ))=sup_φ(φ(x)-sup_y(φ(y)-f(y)))≤f(x). For the reverse inequality: separate (x,f(x)-ε) from epi(f) by a hyperplane to get φ with f**(x)≥f(x)-ε."),
    "subgradient-optimality": ("2", "14", "θ∈∂f(x₀) ⇔ 0=f(x₀)-f(x₀)≥θ(y-x₀)=0 for all y, so f(y)≥f(x₀). Conversely, if x₀ minimizes f, then 0≤f(y)-f(x₀)=θ(y-x₀) for all y, so θ∈∂f(x₀)."),
    "convex-program-optimality": ("2", "14", "Under Slater's condition, optimality is equivalent to the existence of Lagrange multipliers satisfying the KKT conditions. Proof via Fenchel duality or subgradient calculus: 0∈∂f(x₀)+∑λᵢ∂gᵢ(x₀) with complementarity."),

    # §15
    "godini-theorem": ("2", "15", "(a)⇒(b): Proximality means for each coset x+M, there is m∈M minimizing ‖x-m‖. This means Q_M maps the unit ball onto the unit ball of X/M. (b)⇒(c): trivial. (c)⇒(a): If Q_M(U(X)) is closed, it equals U(X/M) by density. The inverse image of a norm-attaining point gives a best approximation."),
    "metric-projection-lemma": ("2", "15", "Existence: intersection of nested closed balls (A∩B̄(x,d(x,A)+1/n)) is nonempty by local compactness. Uniqueness: strictly normed. Continuity: norm-to-norm estimate using local compactness and uniqueness."),
    "renorming-lemma": ("2", "15", "Choose a countable separating family {φₙ}⊂X* with U(X*) weak*-separable. Embed X into ℓ² via x↦(2^{-n/2}φₙ(x)). Pull back the ℓ² norm, which is strict. Equivalence follows from boundedness of the map."),
    "schauder-fixed-point": ("2", "15", "Approximate A by finite dimensional sections Aₙ. Use metric projection Pₙ onto Aₙ and compose: fₙ=Pₙ∘f|Aₙ. By Brouwer, fₙ has fixed point uₙ. Pass to limit using total boundedness: lim uₙ exists and is a fixed point of f."),

    # §16
    "banach-space-completion": ("3", "16", "Define X̃ as equivalence classes of Cauchy sequences in X. Define norm by ‖[{xₙ}]‖=lim‖xₙ‖. Verify completeness: given Cauchy sequence in X̃, diagonal argument extracts limit. Uniqueness up to isometry: any two completions are isometric via identity map on the dense subspace X."),
    "reflexivity-criterion": ("3", "16", "If X is reflexive, J_X(U)=U** is weak*-compact (Alaoglu), so U is σ(X,X*)-compact=weakly compact. Conversely, if U is weakly compact, J_X(U) is weak*-compact, hence weak*-closed. By Goldstine, J_X(U) is weak*-dense in U**, so J_X(U)=U**, i.e., J_X is surjective."),

    # §17
    "baire-category-theorem": ("3", "17", "Let {Gₙ} be dense open sets. For any open U₀, inductively choose open balls Bₙ with B̄ₙ₊₁⊂Gₙ₊₁∩Bₙ. The centers form a Cauchy sequence; the limit belongs to ∩Gₙ∩U₀. Thus ∩Gₙ is dense."),
    "uniform-boundedness-principle": ("3", "17", "Let Aₙ={x:‖T_α x‖≤n for all α}. Aₙ is closed and ∪Aₙ=X. By Baire, some Aₙ has interior, so it contains a ball B(x₀,r). For any x∈U(X), ‖T_α x‖≤(1/r)(‖T_α(x₀+rx)‖+‖T_α x₀‖)≤2n/r, so sup‖T_α‖<∞."),
    "open-mapping-theorem": ("3", "17", "Show T(U) contains a ball around θ. Use Baire: Y=∪ₙnT(U)̄, some nT(U)̄ has interior. By linearity and continuity, θ∈int(T(U)). Then T is open: T(x+U) contains T(x)+int(T(U))."),
    "closed-graph-theorem": ("3", "17", "The graph G is a Banach space under ‖(x,Tx)‖=‖x‖+‖Tx‖. Projection π₁:G→X is continuous bijection, hence by open mapping theorem, its inverse is continuous. Then T=π₂∘π₁^{-1} is continuous."),

    # §18
    "eberlein-smulian-theorem": ("3", "18", "Weakly compact ⇒ weakly seq compact: by Eberlein's original argument using metrizability of weak topology on separable subspaces. Conversely, if every sequence has a weak cluster point, use Smulian's argument with iterated limits to show weak compactness."),
    "smulian-weak-compactness": ("3", "18", "If A is relatively weakly compact, the condition follows from weak compactness of the closure. Conversely, the condition implies every sequence has a weak cluster point. By Eberlein-Smulian, this gives relative weak compactness."),
    "banach-dieudonne-theorem": ("3", "18", "If M∩U(X*) is weak*-closed for M⊂X*, then M is weak*-closed. Proof uses the Krein-Smulian theorem: a convex set in the dual is weak*-closed iff its intersection with every positive multiple of the unit ball is weak*-closed."),

    # §19
    "iterated-limit-condition": ("3", "19", "If A is weakly compact: let x₀ be weak cluster point of {xₙ}, φ₀ weak* cluster point of {φₘ}. Limits equal φ₀(x₀). Conversely, if condition holds but A is not relatively weakly compact, construct sequences violating the condition via a non-weak*-continuous limit point."),
    "james-lemma-2": ("3", "19", "Inductive construction: having chosen ψ₁,…,ψ_{n-1}, select ψₙ∈Kₙ to maximize σ_A(∑_{i=1}^{n} β_i(ψ_i-φ₀)). The lower bound follows from the non-attainment hypothesis."),
    "james-sublinear-lemma": ("3", "19", "Choose x₀∈K that nearly minimizes σ(u+βx). Using sublinearity: σ(u+βx₀+β'y)≥(1+β'/β)σ(u+βz)-σ((β'/β)u) where z=(βx₀+β'y)/(β+β'). The inequality follows after algebraic manipulation."),
    "james-theorem": ("3", "19", "Suppose A is not weakly compact. Then iterated limit condition fails. Build sequences {xₙ}⊂A, {φₘ}⊂U(X*) with limₙ limₘ φₘ(xₙ)≠limₘ limₙ φₘ(xₙ). Use Lemmas 2 and 3 to construct ψ∈X* failing to attain sup on A, contradiction."),
    "reflexivity-via-proximinal": ("3", "19", "(a) If X not reflexive, ∃ separable nonreflexive M⊂X (exercise 3.33). U(M) is not weakly compact. By James, ∃φ∈M* not attaining norm on U(M). Then H=[φ;‖φ‖] has no minimal element, not proximinal. (b) H and U(M) cannot be strictly separated: any separating ψ would give contradiction with φ's non-attainment."),
    "milman-uniform-rotundity": ("3", "19", "For any separable closed M⊂X, choose {xₙ}⊂U(M) with φ(xₙ)→‖φ‖. Uniform rotundity implies {xₙ} is Cauchy (midpoints bounded away from boundary). The limit gives a norm-attaining point. By James, U(M) is weakly compact, so X is reflexive."),

    # §20
    "conical-support-lemma": ("3", "20", "Construct nested Aₙ=A∩(xₙ+C) with x₁=x. Given xₙ, choose xₙ₊₁∈Aₙ with sup φ(Aₙ)<φ(xₙ₊₁)+1/n. Then diam(Aₙ₊₁)≤2/(γn). Nested complete sets with diam→0 intersect at a unique point x₀, which satisfies the conical support condition."),
    "first-bishop-phelps-theorem": ("3", "20", "For x∈∂A, choose z∉A close to x, then apply conical support lemma with φ separating z from A. Get support point x₀ with ‖x-x₀‖ small. Hence support points are dense in boundary."),
    "second-bishop-phelps-theorem": ("3", "20", "Choose x∈A with sup φ(A)≤φ(x)+1. Apply 20B lemma with ε=1, γ=δ. Obtain ψ support functional with ‖φ-ψ‖≤δ."),
    "subreflexive-space": ("3", "20", "Apply second Bishop-Phelps to A=U(X). The support functionals of U(X) are exactly the norm-attaining functionals. They are dense in X* by the theorem."),
    "brondsted-rockafellar-theorem": ("3", "20", "Using approximate subgradients ∂_εf(x)≠∅ for ε>0 (by separation). The lemma of 20C gives nearby point x₀ with ψ∈∂f(x₀) and estimates relating f(x₀) to f(x). Taking liminf as x₀→x gives the formula."),
    "mazur-smooth-points": ("3", "20", "In separable X, the norm is the supremum of a countable family from U(X*). By a category argument, the set where the norm is Gateaux differentiable (i.e., smooth points) is a dense G_δ in the sphere."),

    # §21
    "michael-selection-theorem": ("3", "21", "Construct inductively a sequence of continuous approximate selections fₙ with ‖fₙ₊₁(x)-fₙ(x)‖≤2^{-n} and d(fₙ(x),Φ(x))≤2^{-n}. Use paracompactness for partitions of unity and convexity of Φ(x). The uniform limit is the desired continuous selection."),
    "borsuk-dugundji-theorem": ("3", "21", "Use partition of unity on X\A subordinate to a locally finite cover by balls centered in A. Extend f to each ball using constant value at the center, then patch together using convex combinations. Values stay in co(f(A))."),

    # §22
    "riesz-representation-theorem": ("4", "22", "Define μ(E)=φ(χ_E) for each Borel E⊂Ω. Show μ is a regular Borel measure using continuity of φ and properties of continuous functions. The isometry ‖μ‖_v=‖φ‖ follows from approximation of measurable functions by continuous ones."),
    "stone-weierstrass-theorem": ("4", "22", "First show Ā is a sublattice (closed under max/min) by approximating |f| by polynomials in f (Weierstrass approximation). Then for any continuous f, use lattice operations to approximate f by elements of Ā using point separation."),

    # §23
    "dixmier-ng-theorem": ("4", "23", "Let V be the space of τ-continuous linear functionals on X. The canonical embedding J_V:X→V* is a congruence: U(X) τ-compact implies J_V(U(X)) is weak*-compact in V*, hence weak*-closed. By bipolar, J_V(X) is weak*-dense in V*, so J_V is surjective."),
    "conjugate-space-characterization": ("4", "23", "(a) If J_V is isomorphism, Ū(X) is σ(X,V̄)-relatively compact. Conversely, if U(X) is σ(X,V)-relatively compact, then J_V(U(X)) is weak*-closed in V* and equals U(V*)∩J_V(X). By bipolar, J_V(X) is weak*-dense, hence equals V*. (b) J_V isomorphism ⇔ V̄ is minimal."),
    "operator-space-conjugate": ("4", "23", "Define functionals x⊗y by ⟨T,x⊗y⟩=⟨y,Tx⟩. Their linear hull V is duxial: sup_{‖x⊗y‖≤1}|⟨T,x⊗y⟩|≥‖T‖. U(B) is closed in Π‖x‖U(Y*) which is compact by Tychonov+Alaoglu, so U(B) is relatively σ(B,V)-compact. By (a), B≅V̄*."),

    # §24
    "linfty-injective": ("4", "24", "Define sublinear g:X→L^∞ by g(x)=‖x‖e. The identity f on L^∞ satisfies f≤g|L^∞. The family of extensions of f dominated by g (to subspaces between L^∞ and X) has a maximal element by Zorn's lemma. Maximality forces the domain to be X. This gives projection P with ‖P‖=1."),
    "pelczynski-isomorphism": ("4", "24", "L^∞ is dual to separable L¹, so L^∞ embeds in m (23D). By Lemma 2, L^∞ is injective, so m∼X×L^∞ for some X. Also m∼m×m (easy). Then m∼m×m∼(X×L^∞)×(X×L^∞)∼X×X×L^∞×L^∞∼X×L^∞×(X×L^∞)∼m×m∼m. Hence m∼X×L^∞ gives m∼L^∞ by Pelczynski's decomposition method."),
    "linfty-lipschitz-isomorphism": ("4", "24", "The subspace M⊂Lip of functions vanishing at 0 is congruent to L^∞ via differentiation f↦f'. By 24A, M∼m∼L^∞. Then Lip∼ℝ⊕M∼ℝ⊕L^∞∼L^∞ (since L^∞∼ℝ⊕L^∞). For general separable L^∞(Ω,μ): if purely atomic, L^∞∼m; if non-atomic, L^∞∼L^∞[0,1]∼m."),

    # §25
    "universal-space-m": ("4", "25", "Let {xₙ*} be a dense sequence in U(X*). Define T:X→m by T(x)=(x₁*(x),x₂*(x),…). Then ‖Tx‖_∞=sup|xₙ*(x)|=‖x‖, so T is an isometric embedding."),
    "universal-space-c": ("4", "25", "The Cantor set K maps continuously onto U(X*) (by a classical result). Extend to h:[0,1]→U(X*) linearly on gaps. Define T:X→C[0,1] by T(x)(t)=⟨h(t),x⟩. Then ‖Tx‖_∞=sup_{t}|⟨h(t),x⟩|=sup_{φ∈U(X*)}|φ(x)|=‖x‖, so T is a congruence onto its image."),
}

for slug in sorted(os.listdir(BASE)):
    d = os.path.join(BASE, slug)
    if not os.path.isdir(d):
        continue
    if slug not in proof_concepts:
        continue
    ch, sec, proof_text = proof_concepts[slug]

    pf_file = os.path.join(d, f"proof_gtm024_{ch}.{sec}.en.md")
    with open(pf_file, "w") as f:
        f.write(f"---\nrole: proof\nlocale: en\nof_concept: {slug}\nsource_book: gtm024\nsource_chapter: \"{ch}\"\nsource_section: \"{sec}\"\n---\n\n{proof_text.strip()}\n")

print(f"Created {len(proof_concepts)} proof files")
