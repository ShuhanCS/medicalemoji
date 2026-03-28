import Image from "next/image";
import type { Metadata } from "next";
import { teamMembers } from "@/data/team";
import { XIcon } from "@/components/icons";

export const metadata: Metadata = {
  title: "Team",
  description: "Meet the team behind the Medical Emoji project.",
};

export default function TeamPage() {
  return (
    <>
      {/* Hero */}
      <section className="bg-[#ffcf6d]">
        <div className="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20 lg:px-8">
          <div className="mx-auto max-w-3xl text-center">
            <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl">
              Our Team
            </h1>
            <p className="mt-4 text-lg text-gray-800">
              A dedicated group of physicians, researchers, and advocates working to bring medical
              emoji to the world.
            </p>
          </div>
        </div>
      </section>

      {/* Team Grid */}
      <section className="bg-white py-20">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
            {teamMembers.map((member) => (
              <div
                key={member.name}
                className="group flex flex-col items-center rounded-2xl border border-gray-100 bg-white p-8 shadow-sm transition-all hover:-translate-y-1 hover:shadow-lg"
              >
                {/* Avatar */}
                <div className="relative h-32 w-32 overflow-hidden rounded-full bg-gradient-to-br from-[#3452ff]/10 to-[#ff1053]/10">
                  {member.image ? (
                    <Image
                      src={member.image}
                      alt={member.name}
                      fill
                      className="object-cover"
                      sizes="128px"
                    />
                  ) : (
                    <div className="flex h-full w-full items-center justify-center">
                      <span className="text-3xl font-bold text-gray-400">
                        {member.name
                          .split(" ")
                          .map((n) => n[0])
                          .join("")}
                      </span>
                    </div>
                  )}
                </div>

                {/* Info */}
                <h3 className="mt-5 text-lg font-semibold text-gray-900">
                  {member.name}, {member.title}
                </h3>
                <a
                  href={member.twitter}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="mt-2 inline-flex items-center gap-1.5 text-sm text-[#3452ff] transition-colors hover:text-[#ff1053]"
                >
                  <XIcon />
                  {member.twitterHandle}
                </a>
              </div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
