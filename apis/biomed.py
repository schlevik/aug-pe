import random



def get_prompt(prompt, ds_name):
    if ds_name == 'psytar':
        return get_psytar_prompt(prompt)
    elif ds_name == 'hallmarks_of_cancer':
        return get_hoc_prompt(prompt)
    elif ds_name == 'mimic':
        return get_mimic_prompt(prompt)
    raise NotImplementedError()

def get_psytar_prompt(prompt):
    labels = prompt.split("|")
    styles = """Chronic patient
New parent
Senior reviewer
Allergy sufferer
Prescription user
Healthcare professional
Migraine patient
Fitness enthusiast
Mental health patient
Insomnia sufferer""".splitlines()

    label_map = {
        "ADR": "Adverse Drug Reaction",
        "DI": "Drug Indications",
        "EF": "Drug Effectiveness",
        "INF": "Drug Ineffeciveness",
        "Others": "Others",
        "SSI": "Sign/Symptoms/Illness",
        "WD": "Withdrowal Symptoms"
    }
    style = random.choice(styles)
    return f"Suppose you're a {style}. Write a one-sentence medication review that mentions the following adverse drug reactions: {', '.join(label_map.get(l, 'No reactions.') for l in labels)}"



def get_hoc_prompt(prompt):
    labels = prompt.split("|")
    styles = """Cell Biologist
Immunologist
Molecular Geneticist
Metabolic Scientist
Vascular Biologist
Evolutionary Biologist
Systems Biologist
Epigeneticist
Tissue Engineer
Biochemist""".splitlines()

    label_map = [
        "activating invasion and metastasis",
        "avoiding immune destruction",
        "cellular energetics",
        "enabling replicative immortality",
        "evading growth suppressors",
        "genomic instability and mutation",
        "inducing angiogenesis",
        "resisting cell death",
        "sustaining proliferative signaling",
        "tumor promoting inflammation"
    ]
    label_map = {l:l for l in label_map}
    style = random.choice(styles)
    return f"Suppose you're a {style} writing a scientific paper about hallmarks of cancer. Write one sentence from your papers' abstract, that mentions the following hallmark(s): {', '.join(label_map.get(l, 'No hallmark.') for l in labels)}"


def get_mimic_prompt(prompt):
    labels = prompt.split("|")
    styles = """Critical Care Physician
Respiratory Therapist
Clinical Pharmacist
Infectious Disease Specialist
ICU Nurse
Nephrologist
Clinical Dietitian
Physical Therapist
Social Worker
Palliative Care Specialist""".splitlines()

    label_map = [ 
            ((1, 139), "Infectious And Parasitic Diseases"),
            ((140, 239), "Neoplasms"),
            ((240, 279), "Endocrine, Nutritional And Metabolic Diseases, And Immunity Disorders"),
            ((280, 289), "Diseases Of The Blood And Blood-Forming Organs"),
            ((290, 319), "Mental Disorders"),
            ((320, 389), "Diseases Of The Nervous System And Sense Organs"),
            ((390, 459), "Diseases Of The Circulatory System"),
            ((460, 519), "Diseases Of The Respiratory System"),
            ((520, 579), "Diseases Of The Digestive System"),
            ((580, 629), "Diseases Of The Genitourinary System"),
            ((630, 679), "Complications Of Pregnancy, Childbirth, And The Puerperium"),
            ((680, 709), "Diseases Of The Skin And Subcutaneous Tissue"),
            ((710, 739), "Diseases Of The Musculoskeletal System And Connective Tissue"),
            ((740, 759), "Congenital Anomalies"),
            ((760, 779), "Certain Conditions Originating In The Perinatal Period"),
            ((780, 799), "Symptoms, Signs, And Ill-Defined Conditions"),
            ((800, 999), "Injury And Poisoning")
        ]
    label_map = {l:l for _, l in label_map}
    style = random.choice(styles)
    return f"Suppose you're a {style} writing a brief hospital history section as part of a discharge summary of a patient admitted to ICU. Mentions the following disesases: {', '.join(label_map.get(l, 'None.') for l in labels)}"


ALL_MIMIC_TONES = [
    "Chronological Narrative: Sequential storytelling with full sentences",
"Problem-Based: Listed by medical issues",
"Bullet-Point Style: Short points with dates",
"System-Based: Organized by organ systems",
"Heavy Abbreviation Style: Maximum use of medical acronyms",
"Intervention-Focused: Listed by medical procedures",
"Milestone-Based: Major events and timepoints",
"Table Format: Data arranged in grid",
"Assessment/Plan Style: Summary with ongoing tasks",
"Outcome-Oriented: Problems with their resolutions"
]