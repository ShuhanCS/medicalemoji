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
    url: "https://www.theverge.com/2021/9/13/22665002/doctors-medical-emoji-organs-health",
    logo: "/images/misc/the-verge-logo.svg",
  },
  {
    outlet: "JAMA",
    title: "Published in the Journal of the American Medical Association",
    url: "https://jamanetwork.com/journals/jama/article-abstract/2783847",
    logo: "/images/misc/jama-logo.svg",
  },
  {
    outlet: "Boston Globe",
    title: "Boston Globe feature on medical emoji",
    url: "https://www.bostonglobe.com/2020/02/04/metro/this-mass-general-doctor-helped-get-two-new-medical-emojis-approved/",
    logo: "/images/misc/boston-globe-logo.svg",
  },
  {
    outlet: "WCVB Boston",
    title: "Boston doctor helps create two medical emoji",
    url: "https://www.wcvb.com/article/boston-doctor-helps-create-two-emojis-set-for-release-this-year/30812530",
    logo: "/images/misc/nbc-boston-logo.svg",
  },
  {
    outlet: "Healio",
    title: "Healio coverage of the medical emoji project",
    url: "https://www.healio.com/news/primary-care/20211015/medical-emoji-may-broaden-health-care-communication",
    logo: "/images/misc/healio-logo.svg",
  },
  {
    outlet: "Harvard Medical School",
    title: "Harvard Medical School recognition",
    url: "https://hms.harvard.edu/news/emoji-power",
    logo: "/images/misc/hms-logo.svg",
  },
  {
    outlet: "Hepatology",
    title: "Hepatology journal letter of support",
    url: "https://aasldpubs.onlinelibrary.wiley.com/journal/15273350",
    logo: "/images/misc/hepatology-logo.svg",
  },
];
