interface SupportListProps {
  supporters: string[];
}

export function SupportList({ supporters }: SupportListProps) {
  if (supporters.length === 0) {
    return null;
  }

  return (
    <section className="bg-white py-16">
      <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
        <h2 className="text-center text-2xl font-bold text-gray-900 sm:text-3xl">
          Supporting Organizations
        </h2>
        <p className="mx-auto mt-3 max-w-2xl text-center text-gray-600">
          The following organizations have expressed their support for this emoji proposal.
        </p>
        <div className="mt-8 grid gap-3 sm:grid-cols-2">
          {supporters.map((supporter) => (
            <div
              key={supporter}
              className="flex items-center gap-3 rounded-xl border border-gray-100 bg-gray-50 px-5 py-4 shadow-sm"
            >
              <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-gradient-to-r from-[#3452ff] to-[#ff1053]">
                <svg
                  className="h-4 w-4 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M5 13l4 4L19 7"
                  />
                </svg>
              </div>
              <span className="text-sm font-medium text-gray-800">{supporter}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
