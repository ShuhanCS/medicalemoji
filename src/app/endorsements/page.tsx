import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { Check, ExternalLink, FileText } from "lucide-react";
import { emojiCandidates, getEmojiBySlug } from "@/data/emoji";
import { featuredEndorsement } from "@/data/endorsements";

export const metadata: Metadata = {
  title: "Endorsements",
  description:
    "Medical societies and professional organizations supporting the Medical Emoji Project, led by the American College of Emergency Physicians' project-wide endorsement.",
};

const ACEP_NAME = "American College of Emergency Physicians (ACEP)";

export default function EndorsementsPage() {
  const conceptEmoji = featuredEndorsement.concepts
    .map((slug) => getEmojiBySlug(slug))
    .filter((emoji): emoji is NonNullable<typeof emoji> => Boolean(emoji));

  // Per-emoji society letters, excluding ACEP (featured separately above).
  const byEmoji = emojiCandidates
    .map((emoji) => ({
      emoji,
      supporters: emoji.supporters.filter((s) => s.name !== ACEP_NAME),
    }))
    .filter((entry) => entry.supporters.length > 0);

  return (
    <>
      {/* Hero */}
      <section className="bg-[#ffcf6d]">
        <div className="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20 lg:px-8">
          <div className="mx-auto max-w-3xl text-center">
            <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl">
              Endorsements
            </h1>
            <p className="mt-4 text-lg text-gray-800">
              Medical societies, patient organizations, and professional bodies stand behind the
              call for better medical representation in the Unicode emoji standard.
            </p>
          </div>
        </div>
      </section>

      {/* Featured: ACEP project-wide endorsement */}
      <section className="bg-white py-16 sm:py-20">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
          <div className="overflow-hidden rounded-3xl border border-gray-100 shadow-sm">
            <div className="bg-gradient-to-r from-[#3452ff] to-[#ff1053] px-8 py-6 text-white">
              <p className="text-xs font-semibold uppercase tracking-wider text-white/80">
                Project-wide endorsement
              </p>
              <h2 className="mt-1 text-2xl font-bold sm:text-3xl">
                {featuredEndorsement.organization}
              </h2>
              <p className="mt-1 text-sm text-white/80">
                A national, multi-specialty society backing every current medical emoji concept.
              </p>
            </div>

            <div className="px-8 py-8">
              <blockquote className="border-l-4 border-[#3452ff] pl-5 text-lg leading-relaxed text-gray-700">
                &ldquo;{featuredEndorsement.quote}&rdquo;
              </blockquote>
              <div className="mt-5 text-sm text-gray-600">
                <p className="font-semibold text-gray-900">{featuredEndorsement.signatory}</p>
                <p>
                  {featuredEndorsement.signatoryTitle}, {featuredEndorsement.organization}
                </p>
                <p className="mt-1 text-gray-500">{featuredEndorsement.date}</p>
              </div>

              {/* Concepts named in the letter */}
              <div className="mt-8">
                <p className="text-xs font-semibold uppercase tracking-wider text-gray-500">
                  Concepts named in the letter
                </p>
                <div className="mt-3 flex flex-wrap gap-2">
                  {conceptEmoji.map((emoji) => (
                    <Link
                      key={emoji.slug}
                      href={`/emoji/${emoji.slug}`}
                      className="inline-flex items-center gap-2 rounded-full border border-gray-200 bg-gray-50 py-1.5 pl-1.5 pr-3 text-sm font-medium text-gray-800 transition-colors hover:border-[#3452ff]/30 hover:bg-white"
                    >
                      <Image
                        src={emoji.image}
                        alt=""
                        width={24}
                        height={24}
                        className="h-6 w-6 object-contain"
                      />
                      {emoji.name}
                    </Link>
                  ))}
                </div>
              </div>

              <a
                href={featuredEndorsement.href}
                target="_blank"
                rel="noreferrer"
                className="mt-8 inline-flex min-h-[44px] items-center gap-2 rounded-lg bg-gradient-to-r from-[#3452ff] to-[#ff1053] px-6 py-3 text-sm font-semibold text-white shadow-sm transition-all hover:opacity-90 hover:shadow-md"
              >
                <FileText className="h-4 w-4" aria-hidden="true" />
                Read the ACEP letter (PDF)
                <ExternalLink className="h-4 w-4" aria-hidden="true" />
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Supporting organizations by emoji */}
      <section className="bg-gray-50 py-16 sm:py-20">
        <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h2 className="text-2xl font-bold text-gray-900 sm:text-3xl">
              Supporting Organizations by Emoji
            </h2>
            <p className="mx-auto mt-3 max-w-2xl text-gray-600">
              Specialty societies and patient groups that have written in support of specific
              medical emoji concepts.
            </p>
          </div>

          <div className="mt-12 space-y-10">
            {byEmoji.map(({ emoji, supporters }) => (
              <div key={emoji.slug}>
                <div className="flex items-center gap-3">
                  <Image
                    src={emoji.image}
                    alt=""
                    width={36}
                    height={36}
                    className="h-9 w-9 object-contain"
                  />
                  <Link
                    href={`/emoji/${emoji.slug}`}
                    className="text-lg font-semibold text-gray-900 transition-colors hover:text-[#3452ff]"
                  >
                    {emoji.name}
                  </Link>
                </div>
                <div className="mt-4 grid gap-3 sm:grid-cols-2">
                  {supporters.map((supporter) => {
                    const content = (
                      <>
                        <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-gradient-to-r from-[#3452ff] to-[#ff1053]">
                          <Check className="h-4 w-4 text-white" aria-hidden="true" />
                        </div>
                        <span className="min-w-0 flex-1 text-sm font-medium text-gray-800">
                          {supporter.name}
                        </span>
                        {supporter.href ? (
                          <span className="flex shrink-0 items-center gap-1 text-xs font-semibold text-[#3452ff]">
                            <FileText className="h-3.5 w-3.5" aria-hidden="true" />
                            {supporter.linkLabel ?? "View letter"}
                            {supporter.href.startsWith("http") ? (
                              <ExternalLink className="h-3.5 w-3.5" aria-hidden="true" />
                            ) : null}
                          </span>
                        ) : null}
                      </>
                    );

                    return supporter.href ? (
                      <a
                        key={supporter.name}
                        href={supporter.href}
                        target="_blank"
                        rel="noreferrer"
                        className="flex items-center gap-3 rounded-lg border border-gray-100 bg-white px-5 py-4 shadow-sm transition-colors hover:border-[#3452ff]/30"
                      >
                        {content}
                      </a>
                    ) : (
                      <div
                        key={supporter.name}
                        className="flex items-center gap-3 rounded-lg border border-gray-100 bg-white px-5 py-4 shadow-sm"
                      >
                        {content}
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="bg-white py-16">
        <div className="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
          <h2 className="text-2xl font-bold text-gray-900 sm:text-3xl">
            Does your organization want to add its support?
          </h2>
          <p className="mx-auto mt-4 max-w-xl text-gray-600">
            Society support letters help demonstrate the clinical and public-health value of medical
            emoji. If your organization would like to endorse the project, we&apos;d love to hear
            from you.
          </p>
          <div className="mt-6">
            <a
              href="mailto:info@medicalemoji.org"
              className="inline-flex min-h-[44px] items-center justify-center rounded-lg bg-gradient-to-r from-[#3452ff] to-[#ff1053] px-8 py-3 text-sm font-semibold text-white shadow-sm transition-all hover:opacity-90 hover:shadow-md"
            >
              Get in Touch
            </a>
          </div>
        </div>
      </section>
    </>
  );
}
