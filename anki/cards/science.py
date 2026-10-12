# AQA Combined Science: Trilogy 8464 (Higher) — extra cards on top of the GCSE Plan app's topic cards.
# Each section: (deck key, plan week it is taught, spec tag, [(front, back), ...]). "(HT)" = Higher tier only.

def sec(deck, week, tag, pairs):
    return [(deck, week, tag, q, a) for q, a in pairs]

CARDS = []

CARDS += sec('BIO', 1, 'B1', [
    ('Function of the nucleus', 'Contains genetic material (DNA) that controls the cell’s activities'),
    ('Function of ribosomes', 'Protein synthesis'),
    ('Function of mitochondria', 'Site of aerobic respiration — releases energy'),
    ('Function of the cell membrane', 'Controls what enters and leaves the cell'),
    ('Three structures plant cells have that animal cells don’t', 'Cellulose cell wall, chloroplasts, permanent vacuole (cell sap)'),
    ('Prokaryotic vs eukaryotic cells', 'Prokaryotes (bacteria) have no nucleus: DNA is a single loop plus plasmids, and they are much smaller. Eukaryotes (plants, animals, fungi) have a nucleus.'),
    ('Magnification equation', 'magnification = size of image ÷ size of real object'),
    ('How many micrometres (µm) in 1 mm?', '1000 µm'),
    ('Why are electron microscopes better than light microscopes?', 'Higher magnification and higher resolution, so you can see sub-cellular structures such as ribosomes'),
    ('What is cell differentiation?', 'When a cell becomes specialised by gaining the sub-cellular structures it needs for its job'),
    ('Two adaptations of a sperm cell', 'Tail to swim; lots of mitochondria for energy (also enzymes in the head to get into the egg)'),
    ('Adaptation of a root hair cell', 'Long projection = large surface area for absorbing water and mineral ions'),
    ('What happens in the cell cycle before mitosis?', 'The cell grows, DNA replicates, and organelles such as mitochondria and ribosomes are copied'),
    ('Result of mitosis', 'Two genetically identical daughter cells'),
    ('Three sources of stem cells', 'Human embryos (any cell type), adult bone marrow (some blood cell types), plant meristems (any plant cell, for life)'),
    ('What is therapeutic cloning?', 'Making an embryo with the same genes as the patient, so its stem cells are not rejected'),
    ('Definition of diffusion', 'Net movement of particles from a higher to a lower concentration (passive — no energy needed)'),
    ('Definition of osmosis', 'Diffusion of water from a dilute solution to a concentrated solution through a partially permeable membrane'),
    ('Definition of active transport', 'Movement of substances from a more dilute to a more concentrated solution (against the gradient), using energy from respiration'),
    ('Two examples of active transport', 'Root hair cells absorbing mineral ions from soil; absorbing sugar from the gut into the blood'),
    ('Three factors affecting rate of diffusion', 'Concentration gradient, temperature, surface area of the membrane'),
    ('Why do large organisms need exchange surfaces and transport systems?', 'They have a small surface area to volume ratio, so diffusion alone is too slow'),
    ('Four features of an efficient exchange surface', 'Large surface area, thin membrane (short diffusion path), good blood supply, ventilation (animals)'),
])

CARDS += sec('BIO', 2, 'B2', [
    ('Levels of organisation from smallest', 'Cells → tissues → organs → organ systems → organism'),
    ('Lock and key model', 'The substrate fits the enzyme’s active site exactly, because the active site has a specific shape'),
    ('What does "denatured" mean?', 'High temperature or extreme pH changes the shape of the active site, so the substrate no longer fits'),
    ('Amylase (a carbohydrase) breaks down…', 'Starch → sugars. Made in salivary glands, pancreas, small intestine'),
    ('Protease breaks down…', 'Proteins → amino acids. Made in stomach, pancreas, small intestine'),
    ('Lipase breaks down…', 'Lipids → fatty acids + glycerol. Made in pancreas and small intestine'),
    ('Two jobs of bile', 'Neutralises stomach acid (alkaline) and emulsifies fats into droplets (bigger surface area for lipase). Made in the liver, stored in the gall bladder.'),
    ('Food test for starch', 'Iodine solution: orange-brown → blue-black'),
    ('Food test for reducing sugars', 'Benedict’s solution, heat in a water bath: blue → green/yellow/brick-red'),
    ('Food test for protein', 'Biuret reagent: blue → purple'),
    ('Food test for lipids', 'Sudan III: a red-stained oily layer forms'),
    ('What is a double circulatory system?', 'Blood passes through the heart twice per circuit: heart → lungs → heart → body'),
    ('Which side of the heart pumps blood to the lungs?', 'Right ventricle (to the lungs via the pulmonary artery). The left ventricle pumps to the body via the aorta.'),
    ('What controls the natural resting heart rate?', 'A group of cells in the right atrium acting as a pacemaker'),
    ('Arteries vs veins vs capillaries', 'Arteries: thick muscular, elastic walls for high pressure. Veins: thin walls, large lumen, valves. Capillaries: walls one cell thick for exchange.'),
    ('Four components of blood', 'Plasma, red blood cells, white blood cells, platelets'),
    ('Adaptations of red blood cells', 'Biconcave disc (large surface area), no nucleus (more room), contain haemoglobin to carry oxygen'),
    ('What is coronary heart disease?', 'Fatty material builds up in the coronary arteries, narrowing them and reducing oxygen supply to heart muscle'),
    ('Treatments for coronary heart disease', 'Stents (keep artery open), statins (lower cholesterol), heart transplant or artificial heart'),
    ('Benign vs malignant tumour', 'Benign: stays in one place, doesn’t invade. Malignant: invades tissue and spreads in the blood to form secondary tumours (cancer).'),
    ('Lifestyle risk factors and the disease they cause', 'Smoking → lung disease/cancer; obesity → type 2 diabetes; alcohol → liver disease; carcinogens and ionising radiation → cancer'),
    ('Xylem vs phloem', 'Xylem: hollow dead cells strengthened with lignin, carry water and minerals up. Phloem: living cells carry dissolved sugars up and down (translocation).'),
    ('What is transpiration?', 'Loss of water vapour from leaves through the stomata, which pulls water up the xylem'),
    ('Four factors that increase transpiration rate', 'Higher temperature, higher light intensity, more air flow, lower humidity'),
    ('Job of guard cells', 'Open and close the stomata to control gas exchange and water loss'),
    ('Main photosynthesising tissue in a leaf', 'Palisade mesophyll (lots of chloroplasts)'),
])

CARDS += sec('BIO', 3, 'B3', [
    ('Four types of pathogen', 'Bacteria, viruses, protists, fungi'),
    ('How do bacteria make you ill?', 'They reproduce rapidly and may produce toxins that damage tissues'),
    ('How do viruses make you ill?', 'They live and reproduce inside cells, causing cell damage'),
    ('Measles', 'Virus. Fever and red skin rash. Spread by droplets (sneezes/coughs). Prevented by vaccination.'),
    ('HIV', 'Virus. Flu-like illness at first; attacks immune cells and can lead to AIDS. Spread by sexual contact and body fluids. Controlled by antiretroviral drugs.'),
    ('Tobacco mosaic virus (TMV)', 'Plant virus. Mosaic pattern on leaves, less chlorophyll, so less photosynthesis and growth.'),
    ('Salmonella', 'Bacteria. Food poisoning: fever, cramps, vomiting, diarrhoea (from toxins). UK poultry are vaccinated.'),
    ('Gonorrhoea', 'Bacterial STD. Thick yellow/green discharge, pain when urinating. Treated with antibiotics (many strains resistant to penicillin); prevented by condoms.'),
    ('Rose black spot', 'Fungus. Purple/black spots on leaves, which fall early, so less photosynthesis. Treated with fungicides and removing affected leaves.'),
    ('Malaria', 'Protist, spread by mosquitoes (vectors). Recurrent fevers. Prevented by nets, insecticide, stopping mosquitoes breeding.'),
    ('Non-specific defences of the human body', 'Skin, nose hairs and mucus, cilia and mucus in the trachea/bronchi, stomach acid'),
    ('Three ways white blood cells defend you', 'Phagocytosis (engulfing pathogens), producing antibodies, producing antitoxins'),
    ('How does a vaccine work?', 'A dead or inactive pathogen is injected; white blood cells make antibodies; memory cells allow a fast response if the real pathogen infects you'),
    ('What is herd immunity?', 'If most people are vaccinated, the pathogen is less likely to spread, protecting those who aren’t'),
    ('Why can’t antibiotics treat viral infections?', 'Antibiotics kill bacteria; viruses live inside cells, so drugs that kill them would damage body tissue'),
    ('Origins of three drugs', 'Digitalis from foxgloves; aspirin from willow; penicillin from Penicillium mould (discovered by Alexander Fleming)'),
    ('Pre-clinical drug testing checks…', 'Toxicity, efficacy and dose, using cells, tissues and live animals'),
    ('Clinical trial stages', 'Low doses on healthy volunteers (safety), then patients to find the optimum dose'),
    ('What is a double-blind trial?', 'Neither the patients nor the doctors know who has the drug and who has the placebo, to avoid bias'),
])

CARDS += sec('BIO', 4, 'B4', [
    ('Word equation for photosynthesis', 'carbon dioxide + water → glucose + oxygen (using light energy)'),
    ('Balanced symbol equation for photosynthesis', '6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂'),
    ('Is photosynthesis exothermic or endothermic?', 'Endothermic — energy is transferred from the environment (light) to the chloroplasts'),
    ('Four limiting factors of photosynthesis', 'Temperature, light intensity, carbon dioxide concentration, amount of chlorophyll'),
    ('Inverse square law for light (HT)', 'Light intensity ∝ 1 / distance² — doubling the distance quarters the intensity'),
    ('Five uses of glucose in plants', 'Respiration; starch for storage; cellulose for cell walls; fats/oils for storage; amino acids (with nitrate ions) for proteins'),
    ('Word equation for aerobic respiration', 'glucose + oxygen → carbon dioxide + water (releases energy)'),
    ('Anaerobic respiration in muscles', 'glucose → lactic acid'),
    ('Anaerobic respiration in plants and yeast', 'glucose → ethanol + carbon dioxide (fermentation — used for bread and alcoholic drinks)'),
    ('Why does aerobic respiration release more energy than anaerobic?', 'Glucose is completely oxidised in aerobic respiration'),
    ('What is oxygen debt? (HT)', 'The amount of extra oxygen needed after exercise to react with the lactic acid and remove it from cells'),
    ('What happens to lactic acid after exercise? (HT)', 'Blood carries it to the liver, where it is converted back into glucose'),
    ('Three body responses to exercise', 'Heart rate, breathing rate and breath volume all increase'),
    ('Definition of metabolism', 'The sum of all the reactions in a cell or the body'),
])

CARDS += sec('BIO', 6, 'B5', [
    ('Definition of homeostasis', 'Regulating internal conditions to keep them optimal for cell function and enzyme action'),
    ('Three parts of an automatic control system', 'Receptors, coordination centres (brain, spinal cord, pancreas), effectors (muscles or glands)'),
    ('Path of a reflex arc', 'Stimulus → receptor → sensory neurone → relay neurone → motor neurone → effector → response'),
    ('What happens at a synapse?', 'A chemical diffuses across the gap to set off an electrical impulse in the next neurone'),
    ('Why are reflexes fast?', 'They are automatic and don’t involve the conscious part of the brain'),
    ('Which gland is the "master gland"?', 'Pituitary gland — its hormones act on other glands'),
    ('Blood glucose too high — response', 'Pancreas releases insulin; glucose moves into cells; liver and muscle store it as glycogen'),
    ('Blood glucose too low — response (HT)', 'Pancreas releases glucagon, which makes the liver convert glycogen back into glucose'),
    ('Type 1 vs type 2 diabetes', 'Type 1: pancreas makes too little insulin → insulin injections. Type 2: cells stop responding to insulin → diet and exercise. Obesity is a risk factor for type 2.'),
    ('Role of FSH', 'Causes an egg to mature in the ovary (made by the pituitary)'),
    ('Role of LH', 'Stimulates release of the egg (ovulation)'),
    ('Role of oestrogen and progesterone', 'Oestrogen: builds up the uterus lining. Progesterone: maintains the lining.'),
    ('Hormonal contraceptives', 'Oral pill (oestrogen + progesterone inhibit FSH), implant, injection, patch (slow progesterone release)'),
    ('Non-hormonal contraceptives', 'Condoms, diaphragm, spermicide, copper IUD, abstaining around ovulation, surgical sterilisation'),
    ('How IVF works (HT)', 'FSH and LH to mature several eggs → eggs collected and fertilised in a lab → embryos inserted into the uterus'),
    ('Effects of adrenaline', 'Increases heart rate, boosting oxygen and glucose delivery to the brain and muscles (fight or flight)'),
    ('Role of thyroxine (HT)', 'Stimulates the basal metabolic rate; controlled by negative feedback'),
])

CARDS += sec('BIO', 7, 'B6', [
    ('Sexual vs asexual reproduction', 'Sexual: fusion of gametes, variety in offspring. Asexual: one parent, mitosis only, genetically identical clones.'),
    ('What does meiosis produce?', 'Four genetically different gametes, each with half the number of chromosomes'),
    ('What is DNA?', 'A polymer of two strands in a double helix, found in chromosomes'),
    ('What is a gene?', 'A small section of DNA that codes for a particular sequence of amino acids, to make a specific protein'),
    ('What is the genome?', 'The entire genetic material of an organism'),
    ('Homozygous vs heterozygous', 'Homozygous: two identical alleles. Heterozygous: two different alleles.'),
    ('Genotype vs phenotype', 'Genotype: the alleles present. Phenotype: the characteristic that shows.'),
    ('Cystic fibrosis is caused by…', 'A recessive allele (you need two copies). It is a disorder of cell membranes.'),
    ('Polydactyly is caused by…', 'A dominant allele — extra fingers or toes'),
    ('Sex chromosomes', 'XX = female, XY = male'),
    ('Three causes of variation', 'Genetic, environmental, or a combination of both'),
    ('Steps of natural selection', 'Variation exists → individuals best suited survive and reproduce → they pass on their alleles → over many generations the species changes'),
    ('Steps of selective breeding', 'Choose parents with the desired characteristic → breed them → choose the best offspring → repeat over many generations'),
    ('Risk of selective breeding', 'Inbreeding — more inherited disease and less resistance to new diseases'),
    ('What is genetic engineering?', 'Cutting a gene out of one organism and inserting it (via a plasmid or virus vector) into another — e.g. bacteria that make human insulin, GM crops'),
    ('Evidence for evolution', 'Fossils and antibiotic-resistant bacteria'),
    ('How fossils form', 'Parts that didn’t decay; minerals replacing parts as they decay; or preserved traces such as footprints'),
    ('How antibiotic resistance spreads', 'A mutation makes a bacterium resistant; it survives the antibiotic and reproduces, so the resistant strain spreads (e.g. MRSA)'),
    ('Three ways to slow antibiotic resistance', 'Don’t prescribe antibiotics for viral infections; finish the full course; restrict their use in farming'),
    ('Linnaeus’ classification order', 'Kingdom, phylum, class, order, family, genus, species'),
    ('Woese’s three domains', 'Archaea, Bacteria, Eukaryota'),
    ('Four causes of extinction', 'New predators, new diseases, more successful competitors, changes to the environment (e.g. climate)'),
])

CARDS += sec('BIO', 9, 'B7', [
    ('Definition of an ecosystem', 'The interaction of a community of living organisms with the non-living parts of their environment'),
    ('Abiotic factors', 'Light intensity, temperature, moisture, soil pH and minerals, wind, CO₂ (plants), O₂ (aquatic animals)'),
    ('Biotic factors', 'Food availability, new predators, new pathogens, competition between species'),
    ('What is interdependence?', 'Species depend on each other for food, shelter, pollination and seed dispersal, so removing one affects others'),
    ('Predator–prey graph pattern', 'The prey population peaks first; the predator population rises and falls a little later'),
    ('What are producers?', 'Photosynthetic organisms (plants and algae) at the start of every food chain'),
    ('How to estimate a population with quadrats', 'Mean number per quadrat × (total area ÷ area of one quadrat)'),
    ('What is a transect used for?', 'Measuring how the distribution of a species changes across an area'),
    ('Processes that release CO₂ in the carbon cycle', 'Respiration, combustion, decomposition by microorganisms'),
    ('Process that removes CO₂ from the air', 'Photosynthesis'),
    ('Role of decomposers', 'Bacteria and fungi break down dead matter, returning CO₂ to the air and mineral ions to the soil'),
    ('Definition of biodiversity', 'The variety of all the different species of organisms on Earth or in an ecosystem'),
    ('Human causes of lost biodiversity', 'Pollution of water, air and land; deforestation; destroying peat bogs; global warming'),
    ('Biological consequences of global warming', 'Loss of habitats, changes in species distribution and migration patterns, reduced biodiversity'),
    ('Ways to protect biodiversity', 'Breeding programmes, protecting habitats, replanting hedgerows, reducing deforestation and CO₂ emissions, recycling'),
])

CARDS += sec('CHEM', 1, 'C1', [
    ('Radius of an atom', 'About 0.1 nm (1 × 10⁻¹⁰ m). The nucleus is about 1/10 000 of that.'),
    ('Relative mass and charge of proton, neutron, electron', 'Proton: mass 1, charge +1. Neutron: mass 1, charge 0. Electron: very small mass, charge −1.'),
    ('Atomic number vs mass number', 'Atomic number = protons. Mass number = protons + neutrons.'),
    ('What are isotopes?', 'Atoms of the same element with the same number of protons but a different number of neutrons'),
    ('Five ways to separate mixtures', 'Filtration, crystallisation, simple distillation, fractional distillation, chromatography'),
    ('Order of atomic models', 'Dalton’s solid spheres → Thomson’s plum pudding → Rutherford’s nuclear model → Bohr’s electron shells → Chadwick discovers the neutron'),
    ('What did the alpha-scattering experiment show?', 'Most particles passed straight through (mostly empty space); a few bounced back (a small, dense, positive nucleus)'),
    ('Electron arrangement of the first 20 elements', 'Shells fill 2, 8, 8, 2 — e.g. sodium is 2,8,1'),
    ('What does the group number tell you?', 'The number of electrons in the outer shell'),
    ('How did Mendeleev improve the periodic table?', 'He left gaps for undiscovered elements and predicted their properties, and swapped some orders to match properties'),
    ('Group 1 metal + water', 'metal hydroxide + hydrogen (e.g. 2Na + 2H₂O → 2NaOH + H₂)'),
    ('Why does Group 1 reactivity increase down the group?', 'The outer electron is further from the nucleus, so it is lost more easily'),
    ('Group 7 trends down the group', 'Reactivity decreases; melting and boiling points increase; the molecules are diatomic (Cl₂)'),
    ('Halogen displacement rule', 'A more reactive halogen displaces a less reactive one from a solution of its salt'),
    ('Why are Group 0 gases unreactive?', 'They have a full outer shell (stable arrangement)'),
])

CARDS += sec('CHEM', 2, 'C2', [
    ('What is ionic bonding?', 'Metal atoms transfer electrons to non-metal atoms, forming oppositely charged ions held by strong electrostatic forces'),
    ('Properties of ionic compounds', 'High melting and boiling points; conduct electricity when melted or dissolved (ions free to move)'),
    ('What is covalent bonding?', 'Non-metal atoms share pairs of electrons'),
    ('Why do simple molecules have low boiling points?', 'Only weak intermolecular forces need to be overcome, not the covalent bonds'),
    ('Diamond structure and properties', 'Each carbon forms 4 bonds: very hard, very high melting point, doesn’t conduct'),
    ('Graphite structure and properties', 'Each carbon forms 3 bonds in layers that slide (soft); delocalised electrons let it conduct'),
    ('Graphene', 'A single layer of graphite: strong, conducts electricity, useful in electronics'),
    ('Fullerenes and nanotubes', 'Hollow carbon molecules, e.g. buckminsterfullerene C₆₀. Nanotubes have a high length-to-diameter ratio and reinforce materials.'),
    ('What is metallic bonding?', 'A lattice of positive metal ions in a sea of delocalised electrons'),
    ('Why are metals malleable?', 'Layers of atoms can slide over each other'),
    ('Why are alloys harder than pure metals?', 'Different-sized atoms distort the layers so they can’t slide easily'),
    ('Why are polymers solid at room temperature?', 'Very long molecules with relatively strong intermolecular forces'),
    ('State symbols', '(s) solid, (l) liquid, (g) gas, (aq) dissolved in water'),
])

CARDS += sec('CHEM', 3, 'C3', [
    ('Law of conservation of mass', 'No atoms are lost or made in a reaction, so the mass of products = mass of reactants'),
    ('Why might mass seem to change in a reaction?', 'A gas escapes from (or enters) an open container'),
    ('How to calculate relative formula mass (Mr)', 'Add up the relative atomic masses (Ar) of all atoms in the formula — e.g. CO₂ = 12 + 16 + 16 = 44'),
    ('Avogadro constant (HT)', '6.02 × 10²³ particles per mole'),
    ('Moles from mass (HT)', 'moles = mass (g) ÷ Mr'),
    ('Concentration in g/dm³', 'mass of solute (g) ÷ volume (dm³)'),
    ('1 dm³ in cm³', '1000 cm³'),
    ('What is a limiting reactant? (HT)', 'The reactant that is completely used up, which limits how much product forms'),
    ('How to balance an equation from masses (HT)', 'Convert each mass to moles, divide by the smallest number to get the ratio'),
])

CARDS += sec('CHEM', 4, 'C4', [
    ('Reactivity series (most to least)', 'Potassium, sodium, lithium, calcium, magnesium, (carbon), zinc, iron, (hydrogen), copper'),
    ('Oxidation and reduction (oxygen)', 'Oxidation = gain of oxygen. Reduction = loss of oxygen.'),
    ('Oxidation and reduction (electrons, HT)', 'OIL RIG: oxidation is loss, reduction is gain of electrons'),
    ('How are metals less reactive than carbon extracted?', 'Reduction with carbon (e.g. iron oxide in a blast furnace)'),
    ('Acid + metal →', 'salt + hydrogen'),
    ('Acid + alkali →', 'salt + water (neutralisation)'),
    ('Acid + metal carbonate →', 'salt + water + carbon dioxide'),
    ('Salts from each acid', 'Hydrochloric → chlorides; sulfuric → sulfates; nitric → nitrates'),
    ('Ionic equation for neutralisation', 'H⁺(aq) + OH⁻(aq) → H₂O(l)'),
    ('Strong vs weak acids (HT)', 'Strong acids fully ionise in water (HCl, HNO₃, H₂SO₄); weak acids only partially ionise (ethanoic, citric, carbonic)'),
    ('pH change for a 10× rise in H⁺ concentration (HT)', 'pH falls by 1'),
    ('In electrolysis, where do ions go?', 'Positive ions → cathode (negative electrode). Negative ions → anode (positive electrode).'),
    ('Why is aluminium oxide dissolved in cryolite?', 'To lower the melting point, saving energy'),
    ('Why must carbon anodes be replaced in aluminium extraction?', 'Oxygen made at the anode reacts with the carbon to form CO₂, so they wear away'),
    ('Aqueous electrolysis: what forms at the cathode?', 'Hydrogen, if the metal is more reactive than hydrogen; otherwise the metal'),
    ('Aqueous electrolysis: what forms at the anode?', 'Oxygen, unless halide ions are present (then the halogen)'),
    ('Products of electrolysing brine (NaCl solution)', 'Hydrogen at the cathode, chlorine at the anode, sodium hydroxide left in solution'),
    ('Half equation at the cathode for H⁺ (HT)', '2H⁺ + 2e⁻ → H₂'),
    ('Half equation at the anode for Cl⁻ (HT)', '2Cl⁻ → Cl₂ + 2e⁻'),
])

CARDS += sec('CHEM', 5, 'C5', [
    ('Exothermic reaction', 'Transfers energy to the surroundings, so the temperature rises — e.g. combustion, neutralisation; used in hand warmers'),
    ('Endothermic reaction', 'Takes in energy from the surroundings, so the temperature falls — e.g. thermal decomposition; used in sports injury packs'),
    ('What is activation energy?', 'The minimum energy particles need to react'),
    ('Bond breaking vs bond making (HT)', 'Breaking bonds takes in energy (endothermic); making bonds releases energy (exothermic)'),
    ('Energy change from bond energies (HT)', 'Energy in to break bonds − energy out from making bonds. Negative = exothermic.'),
])

CARDS += sec('CHEM', 6, 'C6', [
    ('Mean rate of reaction', 'quantity of reactant used (or product formed) ÷ time'),
    ('Four factors affecting rate', 'Concentration (or gas pressure), surface area, temperature, catalysts'),
    ('Collision theory', 'Reactions happen when particles collide with at least the activation energy. More frequent successful collisions = faster rate.'),
    ('Why does higher temperature increase rate?', 'Particles move faster, so collide more often AND more collisions have enough energy'),
    ('What does a catalyst do?', 'Speeds up a reaction without being used up, by providing a pathway with lower activation energy'),
    ('Three ways to measure rate', 'Volume of gas (gas syringe), loss of mass, time for a solution to go cloudy (disappearing cross)'),
    ('Rate at a point on a graph (HT)', 'Draw a tangent and calculate its gradient'),
    ('What is dynamic equilibrium?', 'In a closed system, the forward and backward reactions happen at the same rate'),
    ('Reversible reaction example', 'Hydrated copper sulfate (blue) ⇌ anhydrous copper sulfate (white) + water'),
    ('Raising temperature at equilibrium (HT)', 'Equilibrium shifts in the endothermic direction'),
    ('Raising pressure at equilibrium (HT)', 'Equilibrium shifts towards the side with fewer gas molecules'),
    ('Adding more reactant at equilibrium (HT)', 'More product forms until equilibrium is reached again'),
])

CARDS += sec('CHEM', 7, 'C7', [
    ('What is crude oil?', 'A finite resource: the remains of ancient plankton buried in mud; a mixture of mostly alkane hydrocarbons'),
    ('General formula of alkanes', 'CₙH₂ₙ₊₂'),
    ('First four alkanes', 'Methane CH₄, ethane C₂H₆, propane C₃H₈, butane C₄H₁₀'),
    ('How fractional distillation works', 'Oil is heated and evaporated; vapours rise up a column that is hotter at the bottom and condense at their boiling points'),
    ('Main fractions of crude oil', 'Refinery gases (LPG), petrol, kerosene, diesel oil, fuel oil, bitumen'),
    ('Trends as hydrocarbon chains get longer', 'Higher boiling point, more viscous, less flammable'),
    ('Complete combustion of a hydrocarbon', 'hydrocarbon + oxygen → carbon dioxide + water'),
    ('What is cracking?', 'Breaking long-chain hydrocarbons into shorter, more useful ones and alkenes (catalytic or steam cracking)'),
    ('Test for alkenes', 'Bromine water turns from orange to colourless'),
])

CARDS += sec('CHEM', 8, 'C8', [
    ('Pure substance in chemistry', 'A single element or compound — it melts and boils at a specific temperature'),
    ('What is a formulation?', 'A mixture designed as a useful product, e.g. paint, fuel, medicine, alloy'),
    ('Rf value', 'distance moved by substance ÷ distance moved by solvent'),
    ('Chromatography: how do you know a substance is pure?', 'It produces a single spot in all solvents'),
    ('Test for hydrogen', 'Lit splint gives a squeaky pop'),
    ('Test for oxygen', 'Relights a glowing splint'),
    ('Test for carbon dioxide', 'Limewater turns milky (cloudy)'),
    ('Test for chlorine', 'Bleaches damp litmus paper white'),
])

CARDS += sec('CHEM', 9, 'C9', [
    ('Earth’s early atmosphere', 'Mostly carbon dioxide, little or no oxygen, released by volcanoes; water vapour condensed to form the oceans'),
    ('How did oxygen levels rise?', 'Algae and plants photosynthesised'),
    ('How did CO₂ levels fall?', 'Absorbed by algae and plants, dissolved in oceans, locked into sedimentary rocks and fossil fuels'),
    ('Composition of today’s atmosphere', 'About 80% nitrogen, 20% oxygen, small amounts of CO₂, water vapour and noble gases'),
    ('Three greenhouse gases', 'Carbon dioxide, methane, water vapour'),
    ('How the greenhouse effect works', 'Greenhouse gases absorb infrared radiation emitted from the Earth’s surface, keeping it warm'),
    ('Human sources of extra CO₂ and methane', 'CO₂: burning fossil fuels, deforestation. Methane: cattle farming, landfill.'),
    ('Problems caused by carbon monoxide', 'Toxic: it stops blood carrying oxygen'),
    ('Problems caused by sulfur dioxide and nitrogen oxides', 'Acid rain and respiratory problems'),
    ('Problems caused by particulates', 'Global dimming and lung damage'),
    ('What is a carbon footprint?', 'Total greenhouse gas emitted over the life of a product, service or event'),
])

CARDS += sec('CHEM', 9, 'C10', [
    ('What is potable water?', 'Water safe to drink: low levels of dissolved salts and microbes (not pure)'),
    ('How UK fresh water is made potable', 'Filtered (wire mesh, sand beds), then sterilised with chlorine, ozone or UV light'),
    ('Two methods of desalination', 'Distillation and reverse osmosis — both need lots of energy'),
    ('Stages of waste water treatment', 'Screening and grit removal → sedimentation (sludge + effluent) → anaerobic digestion of sludge, aerobic treatment of effluent'),
    ('Four stages of a life cycle assessment', 'Extracting/processing raw materials; manufacturing and packaging; use; disposal'),
    ('Phytomining (HT)', 'Plants absorb metal compounds from low-grade ore; they are burned and the metal extracted from the ash'),
    ('Bioleaching (HT)', 'Bacteria produce leachate solutions containing metal compounds'),
])

CARDS += sec('PHYS', 1, 'P1', [
    ('Eight energy stores', 'Kinetic, gravitational potential, elastic potential, thermal, chemical, magnetic, electrostatic, nuclear'),
    ('Definition of specific heat capacity', 'Energy needed to raise the temperature of 1 kg of a substance by 1 °C'),
    ('Definition of power', 'The rate of energy transfer (or work done). 1 watt = 1 joule per second.'),
    ('Two ways to reduce unwanted energy transfers', 'Lubrication (less friction) and thermal insulation (thicker walls, low thermal conductivity)'),
    ('Renewable energy resources', 'Bio-fuel, wind, hydro-electricity, geothermal, tides, sun, water waves'),
    ('Non-renewable energy resources', 'Coal, oil, gas, nuclear fuel'),
])

CARDS += sec('PHYS', 2, 'P2', [
    ('Definition of current', 'The rate of flow of electrical charge (measured in amperes, A)'),
    ('Series circuit rules', 'Same current everywhere; potential difference is shared; total resistance = R₁ + R₂'),
    ('Parallel circuit rules', 'Same pd across each branch; currents add up; total resistance is less than the smallest resistor'),
    ('Ohmic conductor', 'Current is directly proportional to pd at constant temperature'),
    ('Filament lamp I–V behaviour', 'Resistance increases as temperature increases'),
    ('Diode', 'Current flows in one direction only (very high resistance in reverse)'),
    ('LDR', 'Resistance decreases as light intensity increases'),
    ('Thermistor', 'Resistance decreases as temperature increases'),
    ('UK mains supply', 'Alternating current, 230 V, 50 Hz'),
    ('Wire colours in a UK plug', 'Live: brown. Neutral: blue. Earth: green and yellow.'),
    ('Why is the live wire dangerous even when switched off?', 'It is still at 230 V; touching it makes a path to earth, so current flows through you'),
    ('Why does the National Grid use step-up transformers?', 'Higher pd means lower current, so less energy is lost heating the cables'),
])

CARDS += sec('PHYS', 4, 'P3', [
    ('Is a change of state physical or chemical?', 'Physical — reversible, and mass is conserved'),
    ('What is internal energy?', 'The total kinetic and potential energy of all the particles in a system'),
    ('Definition of specific latent heat', 'Energy needed to change the state of 1 kg of a substance with no change in temperature'),
    ('Latent heat of fusion vs vaporisation', 'Fusion: solid ↔ liquid. Vaporisation: liquid ↔ gas.'),
    ('What do the flat parts of a heating curve show?', 'A change of state — energy breaks bonds instead of raising temperature'),
    ('Why does gas pressure rise with temperature (fixed volume)?', 'Particles move faster, so they hit the walls more often and with more force'),
])

CARDS += sec('PHYS', 5, 'P4', [
    ('Alpha radiation', 'Helium nucleus (2 protons + 2 neutrons). Stopped by paper or a few cm of air. Most ionising.'),
    ('Beta radiation', 'A fast electron from the nucleus. Stopped by a few mm of aluminium.'),
    ('Gamma radiation', 'Electromagnetic wave. Reduced by thick lead or concrete. Least ionising.'),
    ('Definition of half-life', 'Time for the number of unstable nuclei in a sample (or the count rate) to halve'),
    ('Unit of activity', 'Becquerel (Bq) — decays per second'),
    ('Effect of alpha decay on the nucleus', 'Mass number falls by 4, atomic number falls by 2'),
    ('Effect of beta decay on the nucleus', 'A neutron becomes a proton: atomic number rises by 1, mass number unchanged'),
    ('Irradiation vs contamination', 'Irradiation: exposed to radiation, doesn’t become radioactive. Contamination: radioactive atoms get onto or into an object.'),
    ('Is radioactive decay predictable?', 'No — it is random'),
])

CARDS += sec('PHYS', 6, 'P5', [
    ('Scalar vs vector', 'Scalar: magnitude only (speed, distance, mass). Vector: magnitude and direction (velocity, displacement, force).'),
    ('Hooke’s law', 'The extension of a spring is directly proportional to the force applied, up to the limit of proportionality'),
    ('Gradient of a distance–time graph', 'Speed'),
    ('Velocity–time graph: gradient and area', 'Gradient = acceleration. Area under the line = distance travelled.'),
    ('Typical speeds', 'Walking ~1.5 m/s, running ~3 m/s, cycling ~6 m/s, sound in air ~330 m/s'),
    ('Newton’s first law', 'If the resultant force is zero, a stationary object stays still and a moving one keeps the same velocity'),
    ('Newton’s second law (in words)', 'Acceleration is directly proportional to the resultant force and inversely proportional to the mass'),
    ('Newton’s third law', 'When two objects interact, they exert equal and opposite forces on each other'),
    ('What is terminal velocity?', 'Top speed reached when drag equals weight, so the resultant force is zero'),
])

CARDS += sec('PHYS', 7, 'P5', [
    ('Stopping distance =', 'Thinking distance + braking distance'),
    ('Factors affecting thinking distance', 'Speed and reaction time (tiredness, drugs, alcohol, distractions)'),
    ('Factors affecting braking distance', 'Speed, wet or icy roads, worn brakes or tyres'),
    ('Typical reaction time', '0.2–0.9 s'),
    ('Conservation of momentum (HT)', 'In a closed system, total momentum before = total momentum after'),
    ('Why are large decelerations dangerous?', 'Large forces act on the people inside; brakes may overheat or the vehicle may skid'),
])

CARDS += sec('PHYS', 8, 'P6', [
    ('Transverse vs longitudinal waves', 'Transverse: oscillations perpendicular to energy transfer (light, water ripples). Longitudinal: parallel, with compressions and rarefactions (sound).'),
    ('EM spectrum in order of increasing frequency', 'Radio, microwave, infrared, visible, ultraviolet, X-ray, gamma'),
    ('Speed of all EM waves in a vacuum', '3 × 10⁸ m/s'),
    ('Uses of radio waves and microwaves', 'Radio: TV and radio. Microwaves: satellite communications, cooking.'),
    ('Uses of infrared and visible light', 'IR: heaters, cooking, infrared cameras. Visible: fibre-optic communications.'),
    ('Uses of UV, X-rays and gamma', 'UV: energy-efficient lamps, sun tanning. X-rays and gamma: medical imaging and treatment.'),
    ('Dangers of UV, X-rays and gamma', 'UV: skin ageing and skin cancer. X-rays and gamma: ionising, can mutate genes and cause cancer.'),
    ('Why does refraction happen?', 'The wave changes speed when it crosses into a different medium, so it changes direction'),
])

CARDS += sec('PHYS', 9, 'P7', [
    ('Rules of magnetic poles', 'Like poles repel, unlike poles attract'),
    ('Permanent vs induced magnet', 'An induced magnet only becomes magnetic in a magnetic field, always attracts, and loses most magnetism when removed'),
    ('Direction of magnetic field lines', 'From north to south — strongest at the poles'),
    ('Why does a compass point north?', 'The Earth’s core produces a magnetic field'),
    ('Field around a current-carrying wire', 'Circular. Stronger with more current; weaker further from the wire.'),
    ('How to make a solenoid stronger', 'Add an iron core (electromagnet), more turns, more current'),
    ('Fleming’s left-hand rule (HT)', 'Thumb = motion (force), first finger = field, second finger = current'),
])

CARDS += sec('RP', 5, 'RP', [
    ('RP Microscopy: key steps', 'Thin specimen on a slide with stain, lowest-power objective first, focus with coarse then fine focus, draw with a scale bar'),
    ('RP Osmosis: method', 'Potato cylinders of equal size in different sugar/salt concentrations; measure mass before and after; calculate % change in mass'),
    ('RP Osmosis: why use % change in mass?', 'The cylinders may have different starting masses'),
    ('RP Food tests: four reagents', 'Iodine (starch), Benedict’s (sugars), Biuret (protein), Sudan III (lipids)'),
    ('RP Enzymes: method', 'Amylase + starch at different pH buffers in a water bath; test drops with iodine every 30 s; time until it stays orange'),
    ('RP Photosynthesis: method', 'Pondweed at different distances from a lamp; count bubbles or measure gas volume per minute'),
    ('RP Photosynthesis: control variables', 'Temperature, CO₂ concentration, same pondweed'),
    ('RP Making salts: method', 'Add excess insoluble copper oxide to warm sulfuric acid, filter off the excess, evaporate then crystallise'),
    ('RP Electrolysis: method', 'Inert carbon electrodes in an aqueous solution; identify the products at each electrode with gas tests'),
    ('RP Temperature changes: method', 'React solutions in a polystyrene cup with a lid; record the highest temperature reached'),
    ('RP Specific heat capacity: method', 'Heat an insulated metal block with a heater and joulemeter; record the temperature rise; use the specific heat capacity equation from the sheet'),
    ('RP Resistance of a wire: method', 'Measure pd and current for different lengths of wire; work out resistance; plot resistance against length'),
    ('RP I–V characteristics: method', 'Vary the pd across a resistor, lamp and diode with a variable resistor; record current; reverse for negative values'),
    ('RP Density of an irregular object', 'Mass on a balance; volume by displacement in a eureka can; then use the density equation'),
])

CARDS += sec('RP', 10, 'RP', [
    ('RP Reaction time: method', 'Drop a ruler between someone’s finger and thumb; record the distance caught; use a conversion table'),
    ('RP Quadrats: method', 'Random sampling with coordinates from a random number generator; count organisms per quadrat; calculate the mean'),
    ('RP Rates of reaction: two methods', 'Sodium thiosulfate + HCl, time for the cross to disappear (cloudiness); or magnesium + HCl, measure gas volume'),
    ('RP Chromatography: why draw the start line in pencil?', 'Pencil won’t dissolve in the solvent and run'),
    ('RP Chromatography: why keep the start line above the solvent?', 'So the samples don’t dissolve into the solvent'),
    ('RP Water purification: method', 'Test pH, evaporate to find the mass of dissolved solids, distil the water'),
    ('RP Force and extension: method', 'Add masses to a spring and measure the extension each time with a ruler at eye level'),
    ('RP Acceleration: method', 'Trolley pulled by hanging masses; measure acceleration with light gates; vary force (keeping total mass constant) or mass'),
    ('RP Waves: ripple tank', 'Measure wavelength (ruler over several waves) and frequency (count waves in 10 s), then use the wave speed equation'),
    ('RP Waves: string', 'Vibration generator; adjust frequency to get a stationary wave; measure half-wavelengths with a metre rule'),
    ('RP Infrared radiation: method', 'Leslie cube filled with hot water; measure IR from each surface with a detector at the same distance'),
    ('Which surface emits the most IR?', 'Matt black (shiny silver emits the least)'),
])

CARDS += sec('PHYS', 3, 'units', [
    ('Unit of current', 'ampere (A)'),
    ('Unit of work done', 'joule (J)'),
    ('Unit of weight', 'newton (N)'),
    ('Unit of gravitational field strength', 'N/kg (g = 9.8 N/kg on Earth — given in the question)'),
    ('Unit of wavelength', 'metre (m)'),
    ('Unit of period', 'second (s)'),
    ('Unit of gas pressure', 'pascal (Pa)'),
    ('Unit of activity (radioactivity)', 'becquerel (Bq)'),
    ('Prefixes: G, M, k', 'G = ×10⁹, M = ×10⁶, k = ×10³'),
    ('Prefixes: m, µ, n', 'm = ×10⁻³, µ = ×10⁻⁶, n = ×10⁻⁹'),
    ('The equation sheet gives you…', 'Every physics equation — but NOT units, symbols’ meanings in context, or how to rearrange. Practise choosing and rearranging.'),
])

CARDS += sec('CHEM', 2, 'formulae', [
    ('Charge on ions from groups 1, 2, 3, 6, 7', 'Group 1: +1, group 2: +2, group 3: +3, group 6: −2, group 7: −1'),
    ('Formula of the hydroxide ion', 'OH⁻'),
    ('Formula of the sulfate ion', 'SO₄²⁻'),
    ('Formula of the nitrate ion', 'NO₃⁻'),
    ('Formula of the carbonate ion', 'CO₃²⁻'),
    ('Formula of the ammonium ion', 'NH₄⁺'),
    ('Formulae of hydrochloric, sulfuric and nitric acid', 'HCl, H₂SO₄, HNO₃'),
    ('Formulae of sodium hydroxide and calcium hydroxide', 'NaOH, Ca(OH)₂'),
    ('Formulae of water, carbon dioxide, methane, ammonia', 'H₂O, CO₂, CH₄, NH₃'),
    ('Which elements are diatomic?', 'H₂, N₂, O₂, F₂, Cl₂, Br₂, I₂'),
    ('Formula of sodium chloride, magnesium oxide, calcium carbonate', 'NaCl, MgO, CaCO₃'),
    ('Formula of copper sulfate and sodium carbonate', 'CuSO₄, Na₂CO₃'),
    ('What the periodic table gives you in the exam', 'Symbols, atomic numbers and relative atomic masses — not ion charges, formulae or electron arrangements'),
])
