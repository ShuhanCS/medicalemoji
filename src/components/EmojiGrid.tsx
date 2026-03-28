import Link from "next/link";
import Image from "next/image";
import { emojiCandidates } from "@/data/emoji";

export function EmojiGrid() {
  return (
    <section className="bg-white py-20" id="candidates">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Our Candidates
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-lg text-gray-600">
            These are the medical emoji we are proposing to the Unicode Consortium for inclusion in the emoji standard.
          </p>
        </div>

        <div className="mt-12 grid grid-cols-2 gap-4 sm:grid-cols-3 sm:gap-6 md:grid-cols-4 lg:grid-cols-5 lg:gap-8">
          {emojiCandidates.map((emoji) => (
            <Link
              key={emoji.slug}
              href={`/emoji/${emoji.slug}`}
              className="group flex flex-col items-center rounded-2xl border border-gray-100 bg-white p-4 shadow-sm transition-all hover:-translate-y-1 hover:shadow-lg sm:p-6"
            >
              <div className="relative flex h-20 w-20 items-center justify-center sm:h-24 sm:w-24">
                <Image
                  src={emoji.image}
                  alt={emoji.name}
                  width={96}
                  height={96}
                  className="h-full w-full object-contain transition-transform group-hover:scale-110"
                />
              </div>
              <h3 className="mt-3 text-center text-sm font-semibold text-gray-900 sm:text-base">
                {emoji.name}
              </h3>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}
