import Link from "next/link";
import Image from "next/image";
import { XIcon } from "@/components/icons";

export function Footer() {
  return (
    <footer className="bg-[#313233] text-[#CCCCCC]">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="grid gap-8 md:grid-cols-3">
          {/* Brand */}
          <div>
            <Link href="/" className="flex items-center gap-2">
              <Image
                src="/images/misc/cropped-anatomical-heart.png"
                alt="Medical Emoji"
                width={32}
                height={32}
                className="h-8 w-8 brightness-0 invert"
              />
              <span className="text-lg font-bold text-white">Medical Emoji</span>
            </Link>
            <p className="mt-3 text-sm leading-relaxed text-[#a3a3a3]">
              Emoji for the Medical Community. Advocating for better representation of medicine and health in the Unicode emoji standard.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="mb-3 text-sm font-semibold uppercase tracking-wider text-white">
              Quick Links
            </h3>
            <ul className="space-y-2">
              <li>
                <Link href="/visual-analogue-scale" className="text-sm text-[#CCCCCC] transition-colors hover:text-white">
                  Visual Analogue Scale
                </Link>
              </li>
              <li>
                <Link href="/campaign" className="text-sm text-[#CCCCCC] transition-colors hover:text-white">
                  Campaign
                </Link>
              </li>
              <li>
                <Link href="/team" className="text-sm text-[#CCCCCC] transition-colors hover:text-white">
                  Team
                </Link>
              </li>
              <li>
                <Link href="/resources" className="text-sm text-[#CCCCCC] transition-colors hover:text-white">
                  Resources
                </Link>
              </li>
            </ul>
          </div>

          {/* Contact & Social */}
          <div>
            <h3 className="mb-3 text-sm font-semibold uppercase tracking-wider text-white">
              Connect
            </h3>
            <ul className="space-y-2">
              <li>
                <a
                  href="mailto:info@medicalemoji.org"
                  className="text-sm text-[#CCCCCC] transition-colors hover:text-white"
                >
                  info@medicalemoji.org
                </a>
              </li>
              <li>
                <a
                  href="https://twitter.com/medicalemoji"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 text-sm text-[#CCCCCC] transition-colors hover:text-white"
                >
                  <XIcon />
                  @medicalemoji
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-10 border-t border-gray-600 pt-6">
          <p className="text-center text-xs text-[#a3a3a3]">
            &copy; {new Date().getFullYear()} Medical Emoji. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
