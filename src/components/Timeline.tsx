export function Timeline() {
  const events = [
    {
      year: "2018",
      title: "The Beginning",
      description:
        "Dr. Shuhan He begins researching the lack of medical representation in the Unicode emoji standard.",
    },
    {
      year: "2019",
      title: "First Proposals",
      description:
        "Shuhan He, MD and Jenny 8 Lee team up with Emojination to submit the anatomical heart and lungs emoji proposals to Unicode.",
    },
    {
      year: "2021",
      title: "Emoji Approved",
      description:
        "The anatomical heart and lungs emoji are officially accepted into Unicode 14.0 and begin appearing on devices worldwide.",
    },
    {
      year: "2021-Now",
      title: "Expanding the Set",
      description:
        "The Medical Emoji team expands with new members and begins proposing additional medical emoji including kidney, liver, spine, and more.",
    },
  ];

  return (
    <section className="bg-gray-50 py-20" id="timeline">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Our Journey
          </h2>
        </div>

        {/* Desktop horizontal timeline */}
        <div className="mt-12 hidden md:block">
          <div className="relative">
            {/* Line */}
            <div className="absolute left-0 right-0 top-6 h-0.5 bg-gradient-to-r from-[#3452ff] to-[#ff1053]" />

            <div className="grid grid-cols-4 gap-8">
              {events.map((event, index) => (
                <div key={index} className="relative pt-12">
                  {/* Dot */}
                  <div className="absolute left-1/2 top-3.5 h-5 w-5 -translate-x-1/2 rounded-full border-4 border-white bg-gradient-to-r from-[#3452ff] to-[#ff1053] shadow-md" />
                  <div className="text-center">
                    <span className="text-2xl font-bold text-[#3452ff]">{event.year}</span>
                    <h3 className="mt-2 text-lg font-semibold text-gray-900">{event.title}</h3>
                    <p className="mt-2 text-sm leading-relaxed text-gray-600">{event.description}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Mobile vertical timeline */}
        <div className="mt-12 md:hidden">
          <div className="relative space-y-8 pl-8">
            {/* Vertical line */}
            <div className="absolute bottom-0 left-2.5 top-0 w-0.5 bg-gradient-to-b from-[#3452ff] to-[#ff1053]" />

            {events.map((event, index) => (
              <div key={index} className="relative">
                {/* Dot */}
                <div className="absolute -left-5.5 top-1 h-5 w-5 rounded-full border-4 border-white bg-gradient-to-r from-[#3452ff] to-[#ff1053] shadow-md" />
                <span className="text-xl font-bold text-[#3452ff]">{event.year}</span>
                <h3 className="mt-1 text-base font-semibold text-gray-900">{event.title}</h3>
                <p className="mt-1 text-sm leading-relaxed text-gray-600">{event.description}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
