export interface FeaturedEndorsement {
  organization: string;
  abbreviation: string;
  signatory: string;
  signatoryTitle: string;
  date: string;
  href: string;
  /** Short pull-quote drawn from the letter. */
  quote: string;
  /** Emoji concepts the letter explicitly names, as site slugs. */
  concepts: string[];
}

/**
 * Project-wide letter of support: a single national, multi-specialty society
 * supporting the entire Medical Emoji effort at once, naming all ten concepts.
 */
export const featuredEndorsement: FeaturedEndorsement = {
  organization: "American College of Emergency Physicians",
  abbreviation: "ACEP",
  signatory: "Michael Fraser, PhD, MS, CAE",
  signatoryTitle: "Executive Director",
  date: "June 5, 2026",
  href: "https://medicalemoji.org/documents/ACEP-Medical-Emoji-Support-Letter-2026.pdf",
  quote:
    "Standardized medical emoji can provide simple visual anchors for common clinical concepts… a familiar, globally available communication layer for patient education, discharge instructions, public health messaging, medical education, and informal patient-provider communication.",
  concepts: [
    "liver",
    "kidney",
    "stomach",
    "intestine",
    "wbc",
    "ekg",
    "spine",
    "blood-bag",
    "pill-pack",
    "weight-scale",
  ],
};
