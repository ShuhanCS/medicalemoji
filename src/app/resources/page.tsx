import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Resources",
  description:
    "Download resources for the Medical Emoji campaign including one pagers and social media toolkits.",
};

export default function ResourcesPage() {
  const resources = [
    {
      title: "One Pager",
      description:
        "A comprehensive one-page overview of the Medical Emoji project, our goals, and how to support us. Perfect for sharing with colleagues, medical societies, and institutional leadership.",
      type: "PDF",
      icon: (
        <svg className="h-8 w-8 text-[#3452ff]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
        </svg>
      ),
      href: "/documents/medical-emoji-one-pager.pdf",
    },
    {
      title: "Social Media Toolkit",
      description:
        "Ready-to-use graphics, hashtags, and suggested posts for Twitter, Instagram, Facebook, and LinkedIn. Help spread the word about medical emoji to your network.",
      type: "Toolkit",
      icon: (
        <svg className="h-8 w-8 text-[#ff1053]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
        </svg>
      ),
      href: "/documents/social-media-toolkit.pdf",
    },
  ];

  return (
    <>
      {/* Hero */}
      <section className="bg-[#ffcf6d]">
        <div className="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20 lg:px-8">
          <div className="mx-auto max-w-3xl text-center">
            <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl">
              Resources
            </h1>
            <p className="mt-4 text-lg text-gray-800">
              Download materials to learn more about and promote the Medical Emoji campaign.
            </p>
          </div>
        </div>
      </section>

      {/* Resources List */}
      <section className="bg-white py-20">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
          <div className="grid gap-8 md:grid-cols-2">
            {resources.map((resource) => (
              <a
                key={resource.title}
                href={resource.href}
                target="_blank"
                rel="noopener noreferrer"
                className="group flex flex-col rounded-2xl border border-gray-100 bg-white p-8 shadow-sm transition-all hover:-translate-y-1 hover:shadow-lg"
              >
                <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-gray-50">
                  {resource.icon}
                </div>
                <div className="mt-5 flex-1">
                  <div className="flex items-center gap-2">
                    <h3 className="text-xl font-semibold text-gray-900">{resource.title}</h3>
                    <span className="rounded-full bg-gray-100 px-2.5 py-0.5 text-xs font-medium text-gray-600">
                      {resource.type}
                    </span>
                  </div>
                  <p className="mt-3 text-sm leading-relaxed text-gray-600">
                    {resource.description}
                  </p>
                </div>
                <div className="mt-6 flex items-center gap-2 text-sm font-semibold text-[#3452ff] transition-colors group-hover:text-[#ff1053]">
                  Download
                  <svg className="h-4 w-4 transition-transform group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                  </svg>
                </div>
              </a>
            ))}
          </div>
        </div>
      </section>

      {/* Additional Info */}
      <section className="bg-gray-50 py-16">
        <div className="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
          <h2 className="text-2xl font-bold text-gray-900 sm:text-3xl">
            Need Something Else?
          </h2>
          <p className="mx-auto mt-4 max-w-xl text-gray-600">
            If you need additional materials, press assets, or have questions about using our
            resources, please reach out.
          </p>
          <div className="mt-6">
            <a
              href="mailto:info@medicalemoji.org"
              className="inline-flex min-h-[44px] items-center justify-center rounded-lg bg-gradient-to-r from-[#3452ff] to-[#ff1053] px-8 py-3 text-sm font-semibold text-white shadow-sm transition-all hover:opacity-90 hover:shadow-md"
            >
              Contact Us
            </a>
          </div>
        </div>
      </section>
    </>
  );
}
