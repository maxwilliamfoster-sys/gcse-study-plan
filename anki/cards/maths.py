# Edexcel 1MA1 Higher — extra cards: formulae NOT on the 2027 sheet, rules and methods.

def sec(deck, week, tag, pairs):
    return [(deck, week, tag, q, a) for q, a in pairs]

CARDS = []

CARDS += sec('MATHS_LEARN', 1, 'number', [
    ('a⁰ =', '1'),
    ('a⁻ⁿ =', '1 / aⁿ'),
    ('a^(m/n) =', '(ⁿ√a)ᵐ — root first, then power'),
    ('Standard form rule', 'A × 10ⁿ where 1 ≤ A < 10'),
    ('Error interval for a number rounded to the nearest 10, e.g. 70', '65 ≤ x < 75'),
    ('Truncating vs rounding', 'Truncating chops off digits without rounding: 3.78 truncated to 1 d.p. is 3.7'),
    ('Lower bound of a − b', 'Lower bound of a − upper bound of b'),
    ('Method: recurring decimal → fraction', 'Let x = the decimal; multiply by 10ⁿ so the repeating part lines up; subtract; solve for x'),
    ('How to find the HCF from prime factors', 'Multiply the prime factors common to both (lowest powers)'),
])

CARDS += sec('MATHS_LEARN', 2, 'algebra', [
    ('Difference of two squares', 'a² − b² = (a + b)(a − b)'),
    ('Identity sign ≡ means', 'True for every value of x'),
    ('Even number / odd number in proofs', 'Even: 2n. Odd: 2n + 1. Consecutive: n, n + 1.'),
    ('Method: factorise ax² + bx + c', 'Find two numbers that multiply to ac and add to b; split the middle term; factorise in pairs'),
])

CARDS += sec('MATHS_LEARN', 3, 'algebra', [
    ('Completing the square: x² + bx + c', '(x + b/2)² − (b/2)² + c'),
    ('Discriminant b² − 4ac tells you…', '> 0: two roots; = 0: one repeated root; < 0: no real roots'),
    ('Solving x² > 9', 'x < −3 or x > 3 (sketch the curve: it’s above the axis outside the roots)'),
    ('Solving x² < 9', '−3 < x < 3'),
    ('Inequality sign flips when…', 'You multiply or divide both sides by a negative number'),
])

CARDS += sec('MATHS_LEARN', 4, 'graphs', [
    ('Gradient of a line through two points', '(y₂ − y₁) ÷ (x₂ − x₁) — change in y over change in x'),
    ('In y = mx + c, m and c are…', 'm = gradient, c = y-intercept'),
    ('Gradients of perpendicular lines', 'Multiply to −1 (negative reciprocal: 2 → −½)'),
    ('Midpoint of (x₁, y₁) and (x₂, y₂)', '((x₁ + x₂)/2, (y₁ + y₂)/2)'),
    ('Equation of a circle centre the origin', 'x² + y² = r²'),
    ('Tangent to a circle at a point', 'Perpendicular to the radius: find the radius gradient, take the negative reciprocal, use y = mx + c through the point'),
    ('y = f(x) + a', 'Translation up by a'),
    ('y = f(x + a)', 'Translation LEFT by a (by vector (−a, 0))'),
    ('y = −f(x)', 'Reflection in the x-axis'),
    ('y = f(−x)', 'Reflection in the y-axis'),
    ('Shape of y = 1/x', 'Reciprocal graph: two curves in opposite quadrants, never touching the axes'),
    ('Shape of y = kˣ (k > 1)', 'Exponential growth: passes through (0, 1), always positive'),
    ('Area under a velocity–time graph', 'Distance travelled (estimate curves with trapeziums)'),
    ('Gradient of a velocity–time graph', 'Acceleration (for a curve, draw a tangent)'),
    ('fg(x) means…', 'Do g first, then f'),
    ('How to find an inverse function f⁻¹(x)', 'Write y = f(x), swap x and y, rearrange to make y the subject'),
])

CARDS += sec('MATHS_LEARN', 5, 'ratio', [
    ('Speed formula (not given)', 'speed = distance ÷ time'),
    ('Density formula (not given)', 'density = mass ÷ volume'),
    ('Pressure formula (not given)', 'pressure = force ÷ area'),
    ('Convert m/s to km/h', '× 3.6'),
    ('1 m² in cm²', '10 000 cm²'),
    ('1 m³ in cm³', '1 000 000 cm³'),
    ('1 litre in cm³', '1000 cm³'),
    ('y is directly proportional to x', 'y = kx — find k from the given pair'),
    ('y is inversely proportional to x', 'y = k / x'),
    ('Percentage change', '(change ÷ original) × 100'),
    ('Simple interest', 'Same interest each year: P × rate × years'),
])

CARDS += sec('MATHS_LEARN', 6, 'geometry', [
    ('Sum of interior angles of an n-sided polygon', '(n − 2) × 180°'),
    ('Sum of exterior angles of any polygon', '360°'),
    ('Bearings rules', 'Measured from north, clockwise, written as 3 figures (e.g. 045°)'),
    ('Circle theorem: angle at the centre', 'Twice the angle at the circumference from the same arc'),
    ('Circle theorem: angle in a semicircle', '90°'),
    ('Circle theorem: angles in the same segment', 'Are equal'),
    ('Circle theorem: cyclic quadrilateral', 'Opposite angles add up to 180°'),
    ('Circle theorem: tangent and radius', 'Meet at 90°'),
    ('Circle theorem: two tangents from one point', 'Are equal in length'),
    ('Circle theorem: alternate segment', 'The angle between a tangent and a chord equals the angle in the alternate segment'),
    ('Circle theorem: perpendicular from the centre to a chord', 'Bisects the chord'),
    ('Four congruence conditions', 'SSS, SAS, ASA, RHS'),
    ('Similar shapes: area and volume scale factors', 'Length k → area k² → volume k³'),
])

CARDS += sec('MATHS_LEARN', 7, 'trig', [
    ('sin 30°, cos 30°, tan 30°', '1/2, √3/2, √3/3 (= 1/√3)'),
    ('sin 45°, cos 45°, tan 45°', '√2/2, √2/2, 1'),
    ('sin 60°, cos 60°, tan 60°', '√3/2, 1/2, √3'),
    ('sin 0°, cos 0°, tan 0°', '0, 1, 0'),
    ('sin 90°, cos 90°', '1, 0 (tan 90° is undefined)'),
    ('When do you use the sine rule?', 'When you know a side and its opposite angle (a matching pair)'),
    ('When do you use the cosine rule?', 'When you know all three sides, or two sides and the angle between them'),
    ('Pythagoras in 3D (space diagonal of a cuboid)', 'd² = a² + b² + c²'),
    ('Period of y = sin x and y = cos x', '360° (tan x has period 180°)'),
])

CARDS += sec('MATHS_LEARN', 8, 'mensuration', [
    ('Area of a triangle (not the trig one)', '½ × base × perpendicular height'),
    ('Area of a parallelogram', 'base × perpendicular height'),
    ('Area and circumference of a circle', 'A = πr², C = πd = 2πr'),
    ('Arc length (not given)', '(θ / 360) × πd'),
    ('Sector area (not given)', '(θ / 360) × πr²'),
    ('Volume of a cylinder', 'πr²h'),
    ('Volume of a frustum', 'Volume of the whole cone − volume of the small cone removed'),
    ('Vector proof: showing points are on a straight line', 'Show one vector is a multiple of the other AND they share a point'),
    ('Vectors: parallel means…', 'One vector is a scalar multiple of the other'),
])

CARDS += sec('MATHS_LEARN', 9, 'stats', [
    ('Independent events: P(A and B)', 'P(A) × P(B)'),
    ('Mutually exclusive events: P(A or B)', 'P(A) + P(B)'),
    ('Venn notation A ∩ B, A ∪ B, A′, ξ', 'Intersection (both), union (either), complement (not A), universal set'),
    ('Frequency density', 'frequency ÷ class width'),
    ('Interquartile range', 'Upper quartile − lower quartile'),
    ('Estimate the mean from grouped data', 'Σ(midpoint × frequency) ÷ total frequency'),
    ('Comparing two distributions', 'Compare an average (median/mean) AND a spread (IQR/range), in context'),
    ('Expected frequency', 'probability × number of trials'),
    ('Relative frequency', 'number of times it happened ÷ number of trials'),
    ('Product rule for counting', 'If there are m ways for one choice and n for another, there are m × n ways in total'),
])

CARDS += sec('MATHS_LEARN', 10, 'algebra', [
    ('Quadratic sequence nth term method', 'Halve the second difference to get the n² coefficient; subtract that an² from the sequence; find the linear nth term of what’s left'),
    ('Iteration: what does xₙ₊₁ = … mean?', 'Put xₙ in to get the next value; repeat (use ANS on the calculator)'),
    ('Show an equation has a root between 1 and 2', 'Substitute both values; show there is a change of sign'),
    ('Geometric sequence', 'Multiply by the same ratio each time (e.g. 3, 6, 12, 24)'),
])
