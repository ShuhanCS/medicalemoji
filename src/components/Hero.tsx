import Link from "next/link";

export function Hero() {
  return (
    <section className="relative overflow-hidden bg-[#ffcf6d]">
      <div className="absolute inset-0 opacity-10">
        <div className="absolute -right-20 -top-20 h-96 w-96 rounded-full bg-white/30" />
        <div className="absolute -bottom-32 -left-20 h-80 w-80 rounded-full bg-white/20" />
      </div>
      <div className="relative mx-auto max-w-7xl px-4 py-20 sm:px-6 sm:py-28 lg:px-8 lg:py-36">
        <div className="mx-auto max-w-3xl text-center">
          <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl lg:text-6xl">
            Emoji For the Medical Community
          </h1>
          <p className="mt-6 text-lg leading-relaxed text-gray-800 sm:text-xl">
            There are over 3,600 emoji in the Unicode standard, but very few represent medicine and healthcare.
            We&apos;re changing that by proposing new medical emoji to better serve clinicians, patients, and researchers worldwide.
          </p>
          <div className="mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row">
            <Link
              href="/visual-analogue-scale"
              className="inline-flex min-h-[44px] items-center justify-center rounded-lg bg-white px-8 py-3 text-sm font-semibold text-gray-900 shadow-sm transition-all hover:bg-gray-50 hover:shadow-md"
            >
              Visual Scale
            </Link>
            <Link
              href="/campaign"
              className="inline-flex min-h-[44px] items-center justify-center rounded-lg bg-gradient-to-r from-[#3452ff] to-[#ff1053] px-8 py-3 text-sm font-semibold text-white shadow-sm transition-all hover:opacity-90 hover:shadow-md"
            >
              Campaign
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}
