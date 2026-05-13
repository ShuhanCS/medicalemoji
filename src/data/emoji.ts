export interface Supporter {
  name: string;
  href?: string;
  linkLabel?: string;
}

export interface EmojiCandidate {
  slug: string;
  name: string;
  image: string;
  altImage?: string;
  shortDescription: string;
  stats: string[];
  supporters: Supporter[];
  color: string;
}

export const emojiCandidates: EmojiCandidate[] = [
  {
    slug: "kidney",
    name: "Kidney",
    image: "/images/emoji/kidneysnew2.png",
    shortDescription: "Chronic kidney disease affects approximately 10% of the global population.",
    stats: [
      "Chronic kidney disease affects approximately 10% of the global population.",
      "As of 2019, chronic kidney disease resulted in 1.3 million deaths worldwide.",
      "Kidney disease is among the leading causes of death globally and continues to rise.",
    ],
    supporters: [
      {
        name: "American Association of Kidney Patients (AAKP)",
        href: "https://medicalemoji.org/documents/AAKP-Kidney-Emoji-Letter-1.7.22.pdf",
      },
      {
        name: "American Society of Nephrology (ASN)",
        href: "https://medicalemoji.org/documents/kidney-support-letters/ASN_Long-2.pdf",
      },
      {
        name: "American Society of Diagnostic and Interventional Nephrology (ASDIN)",
        href: "https://medicalemoji.org/documents/kidney-support-letters/ASDIN.pdf",
      },
      {
        name: "Canadian Society of Nephrology",
        href: "https://medicalemoji.org/documents/Kidney_Emoji_Letter-1.pdf",
      },
      {
        name: "Glomerular Disease Consortium",
        href: "https://medicalemoji.org/documents/kidney-support-letters/Glomcon.pdf",
      },
      {
        name: "International Society of Nephrology (ISN)",
        href: "https://medicalemoji.org/documents/kidney-support-letters/ISN.pdf",
      },
      {
        name: "Kidney Disease: Improving Global Outcomes (KDIGO)",
        href: "https://medicalemoji.org/documents/The-Unicode-Consortium_Signed.pdf",
      },
      {
        name: "National Kidney Foundation (NKF)",
        href: "https://medicalemoji.org/documents/kidney-support-letters/NKF-1.pdf",
      },
      {
        name: "NephJC",
        href: "https://medicalemoji.org/documents/NephJC_KidneyEmoji.pdf",
      },
      {
        name: "Renal Physicians Association",
        href: "https://medicalemoji.org/documents/kidney-support-letters/RPA.pdf",
      },
      {
        name: "Kidney Foundation of Western New York",
        href: "https://medicalemoji.org/documents/Kidney-Foundation-of-WNY-kidney-emoji-letter.pdf",
      },
      {
        name: "Women Nephrology India",
        href: "https://medicalemoji.org/documents/Kidney-Emoji-WIN-Letter-Head-V4B-converted.docx",
        linkLabel: "View document",
      },
    ],
    color: "#c0392b",
  },
  {
    slug: "liver",
    name: "Liver",
    image: "/images/emoji/5-liver.png",
    shortDescription: "Liver disease accounts for approximately 2 million deaths per year worldwide.",
    stats: [
      "Liver disease accounts for approximately 2 million deaths per year worldwide.",
      "Liver disease is the 11th most common cause of death globally.",
      "Approximately 25% of Americans have non-alcoholic fatty liver disease (NAFLD).",
    ],
    supporters: [
      {
        name: "American Gastroenterological Association (AGA)",
        href: "https://medicalemoji.org/documents/AGA-FINAL-Emoji-Letter_Signed.pdf",
      },
      {
        name: "American Society for Gastrointestinal Endoscopy (ASGE)",
        href: "https://medicalemoji.org/documents/GI-Emojis_Letter-to-Consortium_Final_Signed.docx-1.pdf",
      },
      {
        name: "Hepatology (Journal)",
        href: "https://aasldpubs.onlinelibrary.wiley.com/doi/abs/10.1002/hep.32261",
        linkLabel: "View article",
      },
    ],
    color: "#8e44ad",
  },
  {
    slug: "stomach",
    name: "Stomach",
    image: "/images/emoji/3-stomach.png",
    shortDescription: "GERD costs approximately $18 billion in direct costs and $75 billion in indirect costs.",
    stats: [
      "Gastroesophageal reflux disease (GERD) costs approximately $18 billion in direct costs annually.",
      "Indirect costs of GERD are estimated at approximately $75 billion.",
      "GERD is one of the most common gastrointestinal disorders worldwide.",
    ],
    supporters: [
      {
        name: "American Gastroenterological Association (AGA)",
        href: "https://medicalemoji.org/documents/AGA-FINAL-Emoji-Letter_Signed.pdf",
      },
      {
        name: "American Society for Gastrointestinal Endoscopy (ASGE)",
        href: "https://medicalemoji.org/documents/GI-Emojis_Letter-to-Consortium_Final_Signed.docx-1.pdf",
      },
    ],
    color: "#e67e22",
  },
  {
    slug: "spine",
    name: "Spine",
    image: "/images/emoji/4-bottom_spine.png",
    altImage: "/images/emoji/whole_spine2-1.png",
    shortDescription: "Low back pain affects 10-30% of the US population and is the #1 cause of years lived with disability.",
    stats: [
      "Low back pain affects approximately 10-30% of the US population.",
      "Low back pain is the #1 cause of years lived with disability worldwide.",
      "Spinal conditions are among the most common reasons for physician visits.",
    ],
    supporters: [
      {
        name: "The Spine Journal",
        href: "https://www.thespinejournalonline.com/article/S1529-9430(22)00070-5/fulltext",
        linkLabel: "View article",
      },
    ],
    color: "#2980b9",
  },
  {
    slug: "intestine",
    name: "Intestine",
    image: "/images/emoji/1-intestines.png",
    shortDescription: "Colorectal cancer is the 3rd most commonly diagnosed cancer and the 2nd most common cause of cancer death.",
    stats: [
      "Colorectal cancer is the 3rd most commonly diagnosed cancer worldwide.",
      "Colorectal cancer is the 2nd most common cause of cancer death.",
      "Approximately 300,000 appendectomies are performed each year in the United States.",
    ],
    supporters: [
      {
        name: "American Gastroenterological Association (AGA)",
        href: "https://medicalemoji.org/documents/AGA-FINAL-Emoji-Letter_Signed.pdf",
      },
      {
        name: "American Society for Gastrointestinal Endoscopy (ASGE)",
        href: "https://medicalemoji.org/documents/GI-Emojis_Letter-to-Consortium_Final_Signed.docx-1.pdf",
      },
    ],
    color: "#27ae60",
  },
  {
    slug: "ekg",
    name: "EKG",
    image: "/images/emoji/13-ecg-1.png",
    shortDescription: "One person dies every 36 seconds from cardiovascular disease in the United States.",
    stats: [
      "One person dies every 36 seconds from cardiovascular disease in the United States (CDC).",
      "Heart disease is the leading cause of death for men, women, and people of most racial and ethnic groups.",
      "About 659,000 people in the United States die from heart disease each year.",
    ],
    supporters: [],
    color: "#e74c3c",
  },
  {
    slug: "wbc",
    name: "White Blood Cell",
    image: "/images/emoji/14-white-blood-cell-1.png",
    shortDescription: "15.5 million primary care visits for infectious diseases in 2016. Pandemics have shaped human history from the Black Plague to COVID-19.",
    stats: [
      "15.5 million primary care visits for infectious diseases occurred in 2016.",
      "Pandemics have shaped human history from the Black Plague to COVID-19.",
      "The immune system and white blood cells are the body's primary defense against infection.",
    ],
    supporters: [],
    color: "#3498db",
  },
  {
    slug: "blood-bag",
    name: "Blood Bag",
    image: "/images/emoji/8-blood-bagcolor.png",
    shortDescription: "Every 2 seconds, someone in the U.S. needs blood. Blood donation depends entirely on volunteers.",
    stats: [
      "Every 2 seconds, someone in the United States needs blood.",
      "Blood donation depends entirely on the generosity of volunteers.",
      "Blood transfusions save millions of lives each year worldwide.",
    ],
    supporters: [],
    color: "#c0392b",
  },
  {
    slug: "pill-pack",
    name: "Pill Pack",
    image: "/images/emoji/7-pill-pack.png",
    shortDescription: "Approximately 50,000 opioid overdose deaths in the U.S. in 2019, with $78.5 billion in expenses.",
    stats: [
      "Approximately 50,000 opioid overdose deaths occurred in the United States in 2019.",
      "The opioid crisis costs an estimated $78.5 billion in healthcare expenses, lost productivity, and criminal justice involvement.",
      "Fewer than 20% of people with opioid use disorder (OUD) seek treatment.",
    ],
    supporters: [],
    color: "#16a085",
  },
  {
    slug: "weight-scale",
    name: "Weight Scale",
    image: "/images/emoji/11-scales.png",
    shortDescription: "Over 2 billion people worldwide live with obesity. 95 million Americans need lifestyle modifications.",
    stats: [
      "Over 2 billion people worldwide live with obesity or are overweight.",
      "95 million Americans need lifestyle modifications to address weight-related health issues.",
      "Obesity is a major risk factor for heart disease, diabetes, and many cancers.",
    ],
    supporters: [],
    color: "#f39c12",
  },
];

export function getEmojiBySlug(slug: string): EmojiCandidate | undefined {
  return emojiCandidates.find((e) => e.slug === slug);
}

export function getAllEmojiSlugs(): string[] {
  return emojiCandidates.map((e) => e.slug);
}
