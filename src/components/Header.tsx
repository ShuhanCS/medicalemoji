"use client";

import Link from "next/link";
import Image from "next/image";
import { useState } from "react";
import { Menu, X, ChevronDown } from "lucide-react";
import { emojiCandidates } from "@/data/emoji";

export function Header() {
  const [mobileOpen, setMobileOpen] = useState(false);
  const [emojiDropdownOpen, setEmojiDropdownOpen] = useState(false);

  return (
    <header className="sticky top-0 z-50 w-full border-b border-gray-100 bg-white/95 backdrop-blur supports-[backdrop-filter]:bg-white/80">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-2">
          <Image
            src="/images/misc/cropped-anatomical-heart.png"
            alt="Medical Emoji"
            width={36}
            height={36}
            className="h-9 w-9"
          />
          <span className="text-lg font-bold text-gray-900">Medical Emoji</span>
        </Link>

        {/* Desktop Navigation */}
        <nav className="hidden items-center gap-1 md:flex">
          <Link
            href="/visual-analogue-scale"
            className="rounded-lg px-3 py-2 text-sm font-medium text-gray-700 transition-colors hover:bg-gray-100 hover:text-gray-900"
          >
            Visual Analogue Scale
          </Link>

          {/* Emoji Dropdown */}
          <div
            className="relative"
            onMouseEnter={() => setEmojiDropdownOpen(true)}
            onMouseLeave={() => setEmojiDropdownOpen(false)}
          >
            <button className="flex items-center gap-1 rounded-lg px-3 py-2 text-sm font-medium text-gray-700 transition-colors hover:bg-gray-100 hover:text-gray-900">
              The Emoji
              <ChevronDown className="h-4 w-4" />
            </button>
            {emojiDropdownOpen && (
              <div className="absolute left-0 top-full z-50 mt-1 w-56 rounded-xl border border-gray-100 bg-white py-2 shadow-lg">
                {emojiCandidates.map((emoji) => (
                  <Link
                    key={emoji.slug}
                    href={`/emoji/${emoji.slug}`}
                    className="block px-4 py-2 text-sm text-gray-700 transition-colors hover:bg-gray-50 hover:text-gray-900"
                    onClick={() => setEmojiDropdownOpen(false)}
                  >
                    {emoji.name}
                  </Link>
                ))}
              </div>
            )}
          </div>

          <Link
            href="/resources"
            className="rounded-lg px-3 py-2 text-sm font-medium text-gray-700 transition-colors hover:bg-gray-100 hover:text-gray-900"
          >
            Resources
          </Link>
          <Link
            href="/team"
            className="rounded-lg px-3 py-2 text-sm font-medium text-gray-700 transition-colors hover:bg-gray-100 hover:text-gray-900"
          >
            Team
          </Link>
          <Link
            href="/campaign"
            className="ml-2 rounded-lg bg-gradient-to-r from-[#3452ff] to-[#ff1053] px-4 py-2 text-sm font-semibold text-white transition-opacity hover:opacity-90"
          >
            Campaign
          </Link>
        </nav>

        {/* Mobile Menu Button */}
        <button
          className="rounded-lg p-2 text-gray-700 md:hidden"
          onClick={() => setMobileOpen(!mobileOpen)}
          aria-label="Toggle menu"
        >
          {mobileOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
        </button>
      </div>

      {/* Mobile Navigation */}
      {mobileOpen && (
        <div className="border-t border-gray-100 bg-white md:hidden">
          <nav className="mx-auto max-w-7xl space-y-1 px-4 py-4">
            <Link
              href="/visual-analogue-scale"
              className="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50"
              onClick={() => setMobileOpen(false)}
            >
              Visual Analogue Scale
            </Link>
            <div>
              <button
                className="flex w-full items-center justify-between rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50"
                onClick={() => setEmojiDropdownOpen(!emojiDropdownOpen)}
              >
                The Emoji
                <ChevronDown className={`h-4 w-4 transition-transform ${emojiDropdownOpen ? "rotate-180" : ""}`} />
              </button>
              {emojiDropdownOpen && (
                <div className="ml-4 space-y-1 py-1">
                  {emojiCandidates.map((emoji) => (
                    <Link
                      key={emoji.slug}
                      href={`/emoji/${emoji.slug}`}
                      className="block rounded-lg px-3 py-2 text-sm text-gray-600 hover:bg-gray-50 hover:text-gray-900"
                      onClick={() => {
                        setMobileOpen(false);
                        setEmojiDropdownOpen(false);
                      }}
                    >
                      {emoji.name}
                    </Link>
                  ))}
                </div>
              )}
            </div>
            <Link
              href="/resources"
              className="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50"
              onClick={() => setMobileOpen(false)}
            >
              Resources
            </Link>
            <Link
              href="/team"
              className="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50"
              onClick={() => setMobileOpen(false)}
            >
              Team
            </Link>
            <Link
              href="/campaign"
              className="mt-2 block rounded-lg bg-gradient-to-r from-[#3452ff] to-[#ff1053] px-4 py-2.5 text-center text-sm font-semibold text-white"
              onClick={() => setMobileOpen(false)}
            >
              Campaign
            </Link>
          </nav>
        </div>
      )}
    </header>
  );
}
