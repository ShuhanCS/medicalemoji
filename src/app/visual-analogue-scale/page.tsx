import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Visual Analogue Scale",
  description:
    "Emoji Based Visual Analogue Scale (EbVAS) - An open-source, free-to-use pain assessment tool using emoji.",
};

export default function VisualAnalogueScalePage() {
  const emojiFaces = [
    { emoji: "😁", label: "No Pain", value: 0, color: "#22c55e" },
    { emoji: "🙂", label: "Mild", value: 2, color: "#84cc16" },
    { emoji: "😐", label: "Moderate", value: 4, color: "#eab308" },
    { emoji: "🙁", label: "Uncomfortable", value: 6, color: "#f97316" },
    { emoji: "☹️", label: "Severe", value: 8, color: "#ef4444" },
    { emoji: "😭", label: "Worst Pain", value: 10, color: "#dc2626" },
  ];

  return (
    <>
      {/* Hero */}
      <section className="bg-[#ffcf6d]">
        <div className="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20 lg:px-8">
          <div className="mx-auto max-w-3xl text-center">
            <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl">
              Emoji Based Visual Analogue Scale
            </h1>
            <p className="mt-2 text-lg font-semibold text-gray-700">(EbVAS)</p>
            <p className="mt-4 text-lg text-gray-800">
              An open-source, free-to-use pain assessment tool powered by emoji. Designed for
              clinical use, research, and patient self-reporting.
            </p>
          </div>
        </div>
      </section>

      {/* Scale Display */}
      <section className="bg-white py-20">
        <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              The Scale
            </h2>
            <p className="mx-auto mt-4 max-w-2xl text-lg text-gray-600">
              Six emoji faces represent a spectrum from no pain to the worst possible pain,
              providing an intuitive and universally understood pain measurement tool.
            </p>
          </div>

          {/* Emoji Scale */}
          <div className="mt-12">
            {/* Gradient bar */}
            <div className="mx-auto mb-8 h-3 max-w-3xl rounded-full bg-gradient-to-r from-[#22c55e] via-[#eab308] to-[#dc2626]" />

            <div className="grid grid-cols-3 gap-4 sm:grid-cols-6 sm:gap-6">
              {emojiFaces.map((face) => (
                <div
                  key={face.value}
                  className="flex flex-col items-center rounded-2xl border border-gray-100 bg-white p-4 shadow-sm sm:p-6"
                >
                  <span className="text-5xl sm:text-6xl">{face.emoji}</span>
                  <span
                    className="mt-3 text-2xl font-bold"
                    style={{ color: face.color }}
                  >
                    {face.value}
                  </span>
                  <span className="mt-1 text-center text-xs font-medium text-gray-500 sm:text-sm">
                    {face.label}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="bg-gray-50 py-20">
        <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              How It Works
            </h2>
          </div>

          <div className="mt-12 grid gap-8 md:grid-cols-3">
            <div className="rounded-2xl border border-gray-100 bg-white p-8 shadow-sm">
              <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-[#3452ff]/10">
                <span className="text-xl font-bold text-[#3452ff]">1</span>
              </div>
              <h3 className="mt-4 text-lg font-semibold text-gray-900">Present the Scale</h3>
              <p className="mt-2 text-sm text-gray-600">
                Show the patient the six emoji faces arranged from the happiest (no pain) to the
                most distressed (worst pain imaginable).
              </p>
            </div>

            <div className="rounded-2xl border border-gray-100 bg-white p-8 shadow-sm">
              <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-[#ff1053]/10">
                <span className="text-xl font-bold text-[#ff1053]">2</span>
              </div>
              <h3 className="mt-4 text-lg font-semibold text-gray-900">Patient Selects</h3>
              <p className="mt-2 text-sm text-gray-600">
                The patient selects the emoji that best represents their current pain level. The
                universal nature of emoji transcends language barriers.
              </p>
            </div>

            <div className="rounded-2xl border border-gray-100 bg-white p-8 shadow-sm">
              <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-r from-[#3452ff]/10 to-[#ff1053]/10">
                <span className="text-xl font-bold text-gray-700">3</span>
              </div>
              <h3 className="mt-4 text-lg font-semibold text-gray-900">Record &amp; Track</h3>
              <p className="mt-2 text-sm text-gray-600">
                Record the corresponding numerical value (0-10) for clinical documentation. Track
                changes over time to measure treatment effectiveness.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Benefits */}
      <section className="bg-white py-20">
        <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              Why Use EbVAS?
            </h2>
          </div>

          <div className="mt-12 grid gap-6 sm:grid-cols-2">
            {[
              {
                title: "Universal Understanding",
                description: "Emoji are recognized worldwide, making the scale accessible regardless of language, literacy, or cultural background.",
              },
              {
                title: "Digital-Native",
                description: "Seamlessly integrates with telehealth platforms, patient portals, and mobile health apps for modern healthcare delivery.",
              },
              {
                title: "Open Source",
                description: "Free to use in clinical practice, research, and education. No licensing fees or restrictions.",
              },
              {
                title: "Validated Approach",
                description: "Based on the well-established Visual Analogue Scale methodology used in clinical settings for decades.",
              },
            ].map((benefit) => (
              <div
                key={benefit.title}
                className="flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 p-6"
              >
                <div className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-gradient-to-r from-[#3452ff] to-[#ff1053]">
                  <svg className="h-3.5 w-3.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <div>
                  <h3 className="font-semibold text-gray-900">{benefit.title}</h3>
                  <p className="mt-1 text-sm text-gray-600">{benefit.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="bg-gradient-to-r from-[#3452ff] to-[#ff1053] py-16">
        <div className="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-white sm:text-4xl">
            Start Using EbVAS Today
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-lg text-white/80">
            The Emoji Based Visual Analogue Scale is completely free and open source. Use it in
            your clinical practice, research, or health applications.
          </p>
          <div className="mt-8">
            <a
              href="mailto:info@medicalemoji.org"
              className="inline-flex min-h-[44px] items-center justify-center rounded-lg bg-white px-8 py-3 text-sm font-semibold text-gray-900 shadow-sm transition-all hover:bg-gray-50 hover:shadow-md"
            >
              Contact Us for More Information
            </a>
          </div>
        </div>
      </section>
    </>
  );
}
