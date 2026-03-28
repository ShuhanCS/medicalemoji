import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Campaign",
  description:
    "The Medical Emoji Campaign: 2022. Help us bring medical emoji to keyboards worldwide.",
};

export default function CampaignPage() {
  const goals = [
    {
      number: "01",
      title: "Society Consensus Letters",
      description:
        "Obtain consensus letters from major medical societies to include with our Unicode Technical Committee proposals. Society support demonstrates widespread professional backing and increases the likelihood of acceptance.",
      icon: (
        <svg className="h-8 w-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
        </svg>
      ),
    },
    {
      number: "02",
      title: "Online Engagement",
      description:
        'Demonstrate "expected usage level" to the Unicode Consortium through social media engagement, online petitions, and community support. High engagement proves that these emoji will be widely used once released.',
      icon: (
        <svg className="h-8 w-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z" />
        </svg>
      ),
    },
    {
      number: "03",
      title: "National Petition",
      description:
        "Secure a national petition from federal health entities to underscore the importance of medical emoji in public health communication and digital health literacy.",
      icon: (
        <svg className="h-8 w-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3 21v-4m0 0V5a2 2 0 012-2h6.5l1 1H21l-3 6 3 6h-8.5l-1-1H5a2 2 0 00-2 2zm9-13.5V9" />
        </svg>
      ),
    },
  ];

  return (
    <>
      {/* Hero */}
      <section className="bg-[#ffcf6d]">
        <div className="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20 lg:px-8">
          <div className="mx-auto max-w-3xl text-center">
            <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl">
              The Medical Emoji Campaign
            </h1>
            <p className="mt-2 text-xl font-semibold text-gray-700">2022</p>
            <p className="mt-4 text-lg text-gray-800">
              We&apos;re on a mission to bring medical emoji to every keyboard in the world. Here&apos;s
              how you can help.
            </p>
          </div>
        </div>
      </section>

      {/* Goals */}
      <section className="bg-white py-20">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              Our Three Goals
            </h2>
            <p className="mx-auto mt-4 max-w-2xl text-lg text-gray-600">
              Achieving these goals will significantly strengthen our proposals to the Unicode
              Consortium.
            </p>
          </div>

          <div className="mt-12 grid gap-8 md:grid-cols-3">
            {goals.map((goal) => (
              <div
                key={goal.number}
                className="rounded-2xl border border-gray-100 bg-white p-8 shadow-sm transition-all hover:-translate-y-1 hover:shadow-lg"
              >
                <div className="flex h-14 w-14 items-center justify-center rounded-xl bg-gradient-to-r from-[#3452ff] to-[#ff1053]">
                  {goal.icon}
                </div>
                <div className="mt-5">
                  <span className="text-xs font-semibold uppercase tracking-widest text-[#3452ff]">
                    Goal {goal.number}
                  </span>
                  <h3 className="mt-1 text-xl font-semibold text-gray-900">{goal.title}</h3>
                  <p className="mt-3 text-sm leading-relaxed text-gray-600">{goal.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Take Action */}
      <section className="bg-gray-50 py-20">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              Take Action
            </h2>
            <p className="mx-auto mt-4 max-w-2xl text-lg text-gray-600">
              Every signature, share, and show of support brings us closer to medical emoji on
              every device.
            </p>
          </div>

          <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {/* Typeform */}
            <a
              href="https://cidh.typeform.com/to/eskl6Wc8"
              target="_blank"
              rel="noopener noreferrer"
              className="group flex flex-col items-center rounded-2xl border border-gray-100 bg-white p-8 shadow-sm transition-all hover:-translate-y-1 hover:shadow-lg"
            >
              <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[#3452ff]/10">
                <svg className="h-7 w-7 text-[#3452ff]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
                </svg>
              </div>
              <h3 className="mt-4 text-lg font-semibold text-gray-900">Take Our Survey</h3>
              <p className="mt-2 text-center text-sm text-gray-600">
                Complete our brief survey to support medical emoji adoption.
              </p>
              <span className="mt-4 text-sm font-semibold text-[#3452ff] transition-colors group-hover:text-[#ff1053]">
                Open Survey &rarr;
              </span>
            </a>

            {/* Change.org */}
            <a
              href="https://chng.it/pnMtP7zZng"
              target="_blank"
              rel="noopener noreferrer"
              className="group flex flex-col items-center rounded-2xl border border-gray-100 bg-white p-8 shadow-sm transition-all hover:-translate-y-1 hover:shadow-lg"
            >
              <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[#ff1053]/10">
                <svg className="h-7 w-7 text-[#ff1053]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                </svg>
              </div>
              <h3 className="mt-4 text-lg font-semibold text-gray-900">Sign the Petition</h3>
              <p className="mt-2 text-center text-sm text-gray-600">
                Add your name to our Change.org petition for medical emoji.
              </p>
              <span className="mt-4 text-sm font-semibold text-[#ff1053] transition-colors group-hover:text-[#3452ff]">
                Sign Now &rarr;
              </span>
            </a>

            {/* Social Media Toolkit */}
            <a
              href="/resources"
              className="group flex flex-col items-center rounded-2xl border border-gray-100 bg-white p-8 shadow-sm transition-all hover:-translate-y-1 hover:shadow-lg sm:col-span-2 lg:col-span-1"
            >
              <div className="flex h-14 w-14 items-center justify-center rounded-full bg-gradient-to-r from-[#3452ff]/10 to-[#ff1053]/10">
                <svg className="h-7 w-7 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
                </svg>
              </div>
              <h3 className="mt-4 text-lg font-semibold text-gray-900">Social Media Toolkit</h3>
              <p className="mt-2 text-center text-sm text-gray-600">
                Download shareable graphics and templates to spread the word.
              </p>
              <span className="mt-4 text-sm font-semibold text-gray-700 transition-colors group-hover:text-[#3452ff]">
                Get Toolkit &rarr;
              </span>
            </a>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="bg-gradient-to-r from-[#3452ff] to-[#ff1053] py-16">
        <div className="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-white sm:text-4xl">
            Together, We Can Change the Keyboard
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-lg text-white/80">
            Medical emoji will improve health communication for billions of people. Join the
            campaign today.
          </p>
          <div className="mt-8 flex flex-col items-center justify-center gap-4 sm:flex-row">
            <a
              href="https://chng.it/pnMtP7zZng"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex min-h-[44px] items-center justify-center rounded-lg bg-white px-8 py-3 text-sm font-semibold text-gray-900 shadow-sm transition-all hover:bg-gray-50 hover:shadow-md"
            >
              Sign the Petition
            </a>
            <a
              href="mailto:info@medicalemoji.org"
              className="inline-flex min-h-[44px] items-center justify-center rounded-lg border-2 border-white px-8 py-3 text-sm font-semibold text-white transition-all hover:bg-white/10"
            >
              Contact Us
            </a>
          </div>
        </div>
      </section>
    </>
  );
}
