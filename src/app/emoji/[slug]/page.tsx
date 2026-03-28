import { notFound } from "next/navigation";
import Image from "next/image";
import type { Metadata } from "next";
import { emojiCandidates, getEmojiBySlug, getAllEmojiSlugs } from "@/data/emoji";
import { SupportList } from "@/components/SupportList";
import { ContactForm } from "@/components/ContactForm";
import Link from "next/link";

export async function generateStaticParams() {
  return getAllEmojiSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const emoji = getEmojiBySlug(slug);
  if (!emoji) return {};

  return {
    title: `${emoji.name} Emoji`,
    description: emoji.shortDescription,
  };
}

export default async function EmojiPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const emoji = getEmojiBySlug(slug);

  if (!emoji) {
    notFound();
  }

  // Find prev/next for navigation
  const currentIndex = emojiCandidates.findIndex((e) => e.slug === slug);
  const prev = currentIndex > 0 ? emojiCandidates[currentIndex - 1] : null;
  const next = currentIndex < emojiCandidates.length - 1 ? emojiCandidates[currentIndex + 1] : null;

  return (
    <>
      {/* Hero Section */}
      <section className="bg-[#ffcf6d]">
        <div className="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20 lg:px-8">
          <div className="flex flex-col items-center gap-8 md:flex-row md:gap-12 lg:gap-16">
            {/* Emoji Image */}
            <div className="flex shrink-0 items-center justify-center">
              <div className="relative h-48 w-48 sm:h-56 sm:w-56 lg:h-64 lg:w-64">
                <Image
                  src={emoji.image}
                  alt={emoji.name}
                  fill
                  className="object-contain drop-shadow-lg"
                  sizes="(max-width: 640px) 192px, (max-width: 1024px) 224px, 256px"
                />
              </div>
            </div>

            {/* Content */}
            <div className="flex-1 text-center md:text-left">
              <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl">
                {emoji.name} Emoji
              </h1>
              <p className="mt-4 text-lg leading-relaxed text-gray-800">
                {emoji.shortDescription}
              </p>
              <ul className="mt-6 space-y-3">
                {emoji.stats.map((stat, index) => (
                  <li key={index} className="flex items-start gap-3 text-gray-800">
                    <span className="mt-1 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-gray-900/10">
                      <svg className="h-3 w-3 text-gray-900" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M5 13l4 4L19 7" />
                      </svg>
                    </span>
                    <span className="text-sm sm:text-base">{stat}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Supporters */}
      <SupportList supporters={emoji.supporters} />

      {/* CTA / Contact */}
      <section className="bg-gradient-to-r from-[#3452ff] to-[#ff1053] py-16">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h2 className="text-2xl font-bold text-white sm:text-3xl">
              Support the {emoji.name} Emoji
            </h2>
            <p className="mx-auto mt-3 max-w-xl text-white/80">
              Help us bring the {emoji.name.toLowerCase()} emoji to keyboards worldwide. Contact us to lend your support.
            </p>
          </div>
          <div className="mt-8">
            <ContactForm variant="gradient" />
          </div>
        </div>
      </section>

      {/* Navigation between emoji */}
      <section className="border-t border-gray-100 bg-white py-8">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
          {prev ? (
            <Link
              href={`/emoji/${prev.slug}`}
              className="flex items-center gap-2 rounded-lg px-4 py-2 text-sm font-medium text-gray-600 transition-colors hover:bg-gray-50 hover:text-gray-900"
            >
              <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
              {prev.name}
            </Link>
          ) : (
            <div />
          )}
          <Link
            href="/#candidates"
            className="text-sm font-medium text-gray-500 transition-colors hover:text-gray-700"
          >
            All Emoji
          </Link>
          {next ? (
            <Link
              href={`/emoji/${next.slug}`}
              className="flex items-center gap-2 rounded-lg px-4 py-2 text-sm font-medium text-gray-600 transition-colors hover:bg-gray-50 hover:text-gray-900"
            >
              {next.name}
              <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </Link>
          ) : (
            <div />
          )}
        </div>
      </section>
    </>
  );
}
