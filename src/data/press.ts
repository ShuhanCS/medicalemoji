export interface PressMention {
  outlet: string;
  title: string;
  url: string;
  logo: string;
}

export const pressMentions: PressMention[] = [
  {
    outlet: "The Verge",
    title: "The Verge covered the medical emoji campaign",
    url: "https://www.theverge.com/",
    logo: "/images/misc/the-verge-logo.svg",
  },
  {
    outlet: "JAMA",
    title: "Published in the Journal of the American Medical Association",
    url: "https://jamanetwork.com/",
    logo: "/images/misc/jama-logo.svg",
  },
  {
    outlet: "Boston Globe",
    title: "Boston Globe feature on medical emoji",
    url: "https://www.bostonglobe.com/",
    logo: "/images/misc/boston-globe-logo.svg",
  },
  {
    outlet: "NBC Boston",
    title: "NBC Boston segment on medical emoji initiative",
    url: "https://www.nbcboston.com/",
    logo: "/images/misc/nbc-boston-logo.svg",
  },
  {
    outlet: "Healio",
    title: "Healio coverage of the medical emoji project",
    url: "https://www.healio.com/",
    logo: "/images/misc/healio-logo.svg",
  },
  {
    outlet: "Harvard Medical School",
    title: "Harvard Medical School recognition",
    url: "https://hms.harvard.edu/",
    logo: "/images/misc/hms-logo.svg",
  },
  {
    outlet: "Hepatology",
    title: "Hepatology journal endorsement",
    url: "https://aasldpubs.onlinelibrary.wiley.com/journal/15273350",
    logo: "/images/misc/hepatology-logo.svg",
  },
];
